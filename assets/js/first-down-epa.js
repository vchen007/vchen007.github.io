/* Interactive charts for /portfolio/first-down-epa/.
   Loads assets/data/first-down-epa.json (built by _scripts/first_down_epa.py),
   sums the cells that match the filters, and draws three SVG charts. */
(function () {
  'use strict';
  var root = document.getElementById('fd-explorer');
  if (!root) return;
  var NS = 'http://www.w3.org/2000/svg';
  var $ = function (id) { return document.getElementById(id); };
  var data, state = { from: null, to: null, script: 'neutral', zone: 'all', team: '' };

  function el(name, attrs, parent) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function text(parent, x, y, str, cls, anchor) {
    var t = el('text', { x: x, y: y, 'class': cls || 'tick', 'text-anchor': anchor || 'middle' }, parent);
    t.textContent = str;
    return t;
  }
  function fmtEpa(v) { return (v > 0 ? '+' : v < 0 ? '−' : '') + Math.abs(v).toFixed(2); }
  function fmtPct(v) { return Math.round(v * 100) + '%'; }
  function niceTicks(lo, hi, n) {
    var step = Math.pow(10, Math.floor(Math.log10((hi - lo) / n)));
    var err = (hi - lo) / n / step;
    step *= err >= 7.5 ? 10 : err >= 3.5 ? 5 : err >= 1.5 ? 2 : 1;
    var out = [];
    for (var v = Math.ceil(lo / step) * step; v <= hi + 1e-9; v += step) out.push(Math.round(v / step) * step);
    return out;
  }

  /* ---- aggregation ---------------------------------------------------- */
  function matches(r) {
    var s = data.seasons[r[0]];
    if (s < state.from || s > state.to) return false;
    if (state.script !== 'all' && data.dims.script[r[2]] !== state.script) return false;
    if (state.zone !== 'all' && data.dims.zone[r[3]] !== state.zone) return false;
    return true;
  }
  function blank() { return { pass: { n: 0, epa: 0, s: 0 }, run: { n: 0, epa: 0, s: 0 } }; }
  function add(acc, r) { var t = acc[data.dims.type[r[4]]]; t.n += r[5]; t.epa += r[6]; t.s += r[7]; }
  function stats(a) {
    var n = a.pass.n + a.run.n;
    return { n: n, passRate: n ? a.pass.n / n : NaN, pass: a.pass.n ? a.pass.epa / a.pass.n : NaN,
      run: a.run.n ? a.run.epa / a.run.n : NaN, all: n ? (a.pass.epa + a.run.epa) / n : NaN,
      passSucc: a.pass.n ? a.pass.s / a.pass.n : NaN, runSucc: a.run.n ? a.run.s / a.run.n : NaN };
  }
  function compute() {
    var bySeason = {}, byTeam = {}, byTeamSeason = {}, total = blank(), teamFilter = state.team;
    data.rows.forEach(function (r) {
      if (!matches(r)) return;
      var s = data.seasons[r[0]], t = data.teams[r[1]], key = s + '|' + t;
      add(total, r);
      add(bySeason[s] = bySeason[s] || blank(), r);
      add(byTeam[t] = byTeam[t] || blank(), r);
      add(byTeamSeason[key] = byTeamSeason[key] || blank(), r);
    });
    var seasons = data.seasons.filter(function (s) { return s >= state.from && s <= state.to; });
    var runWins = 0, teamSeasons = 0;
    Object.keys(byTeamSeason).forEach(function (k) {
      var st = stats(byTeamSeason[k]);
      if (isFinite(st.pass) && isFinite(st.run)) { teamSeasons++; if (st.run > st.pass) runWins++; }
    });
    return {
      total: stats(total), runWins: runWins, teamSeasons: teamSeasons,
      trend: seasons.map(function (s) { return { season: s, st: stats(bySeason[s] || blank()), team: teamFilter ? stats(byTeamSeason[s + '|' + teamFilter] || blank()) : null }; }),
      teams: Object.keys(byTeam).sort().map(function (t) { return { team: t, st: stats(byTeam[t]) }; })
    };
  }

  /* ---- tooltip -------------------------------------------------------- */
  function tooltip(host) {
    var tip = document.createElement('div');
    tip.className = 'fd-tip'; tip.hidden = true; host.appendChild(tip);
    return {
      show: function (title, rows, x, y) {
        while (tip.firstChild) tip.removeChild(tip.firstChild);
        var h = document.createElement('div'); h.className = 'fd-tip__title'; h.textContent = title; tip.appendChild(h);
        rows.forEach(function (row) {
          var d = document.createElement('div'); d.className = 'fd-tip__row';
          if (row.key) { var k = document.createElement('span'); k.className = 'fd-key fd-key--' + row.key; k.style.marginLeft = '0'; d.appendChild(k); }
          var v = document.createElement('strong'); v.textContent = row.value; d.appendChild(v);
          var l = document.createElement('span'); l.textContent = row.label; d.appendChild(l);
          tip.appendChild(d);
        });
        tip.hidden = false;
        var w = host.clientWidth, tw = tip.offsetWidth;
        tip.style.left = Math.max(0, Math.min(w - tw, x + 12)) + 'px';
        tip.style.top = Math.max(0, y - tip.offsetHeight - 10) + 'px';
      },
      hide: function () { tip.hidden = true; }
    };
  }

  /* ---- line charts ---------------------------------------------------- */
  function lineChart(host, points, series, opts) {
    while (host.firstChild) host.removeChild(host.firstChild);
    var W = Math.max(280, host.clientWidth || root.clientWidth || 640), H = opts.height, m = { t: 12, r: 64, b: 26, l: 44 };
    var svg = el('svg', { viewBox: '0 0 ' + W + ' ' + H, width: W, height: H }, host);
    var vals = [];
    points.forEach(function (p) { series.forEach(function (s) { var v = s.get(p); if (isFinite(v)) vals.push(v); }); });
    if (!vals.length) { text(svg, W / 2, H / 2, 'No plays match these filters'); return; }
    var lo = Math.min.apply(null, vals.concat(opts.includeZero ? [0] : [], opts.minDomain ? [opts.minDomain[0]] : [])), hi = Math.max.apply(null, vals.concat(opts.includeZero ? [0] : [], opts.minDomain ? [opts.minDomain[1]] : []));
    var pad = (hi - lo || 0.1) * 0.12; lo -= pad; hi += pad;
    var ticks = niceTicks(lo, hi, 4); lo = Math.min(lo, ticks[0]); hi = Math.max(hi, ticks[ticks.length - 1]);
    var x = function (i) { return points.length === 1 ? (m.l + W - m.r) / 2 : m.l + i * (W - m.l - m.r) / (points.length - 1); };
    var y = function (v) { return m.t + (hi - v) / (hi - lo) * (H - m.t - m.b); };
    var grid = el('g', { 'class': 'grid' }, svg);
    ticks.forEach(function (t) {
      el('line', { x1: m.l, x2: W - m.r, y1: y(t), y2: y(t), 'class': t === 0 ? 'zero' : '' }, grid);
      text(svg, m.l - 8, y(t) + 4, opts.fmt(t), 'tick', 'end');
    });
    var every = W < 480 ? 2 : 1;
    points.forEach(function (p, i) { if (i % every === 0 || i === points.length - 1) text(svg, x(i), H - 6, opts.xLabel(p)); });
    series.forEach(function (s) {
      var d = '', started = false;
      points.forEach(function (p, i) { var v = s.get(p); if (!isFinite(v)) { started = false; return; } d += (started ? 'L' : 'M') + x(i).toFixed(1) + ' ' + y(v).toFixed(1); started = true; });
      el('path', { d: d, 'class': 'line ' + s.cls + (s.dash ? '' : ''), 'stroke-dasharray': s.dash || 'none' }, svg);
      points.forEach(function (p, i) { var v = s.get(p); if (isFinite(v) && !s.dash) el('circle', { cx: x(i), cy: y(v), r: 4, 'class': 'pt ' + s.pt }, svg); });
      var last = points.length - 1, lv = s.get(points[last]);
      if (isFinite(lv) && s.label) text(svg, x(last) + 10, y(lv) + 4, s.label, 'direct', 'start');
    });
    /* crosshair + tooltip */
    var tip = tooltip(host), cross = el('line', { y1: m.t, y2: H - m.b, 'class': 'crosshair', visibility: 'hidden' }, svg);
    var hit = el('rect', { x: m.l - 10, y: 0, width: W - m.l - m.r + 20, height: H, fill: 'transparent', tabindex: 0, role: 'img', 'aria-label': 'Chart values: use the left and right arrow keys to read each season' }, svg);
    function at(i) {
      var p = points[i]; cross.setAttribute('x1', x(i)); cross.setAttribute('x2', x(i)); cross.setAttribute('visibility', 'visible');
      var rows = series.filter(function (s) { return isFinite(s.get(p)); }).map(function (s) { return { key: s.key, value: opts.fmt(s.get(p), true), label: s.tipLabel }; });
      var scale = host.clientWidth / W;
      tip.show(opts.title(p), rows, x(i) * scale, Math.min.apply(null, series.map(function (s) { var v = s.get(p); return isFinite(v) ? y(v) : H; })) * scale);
    }
    function nearest(evt) {
      var r = svg.getBoundingClientRect(), px = (evt.clientX - r.left) * W / r.width;
      var i = Math.round((px - m.l) / ((W - m.l - m.r) / Math.max(1, points.length - 1)));
      return Math.max(0, Math.min(points.length - 1, i));
    }
    var focusIdx = points.length - 1;
    hit.addEventListener('pointermove', function (e) { at(nearest(e)); });
    hit.addEventListener('pointerleave', function () { cross.setAttribute('visibility', 'hidden'); tip.hide(); });
    hit.addEventListener('focus', function () { at(focusIdx); });
    hit.addEventListener('blur', function () { cross.setAttribute('visibility', 'hidden'); tip.hide(); });
    hit.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { focusIdx = Math.max(0, Math.min(points.length - 1, focusIdx + (e.key === 'ArrowLeft' ? -1 : 1))); at(focusIdx); e.preventDefault(); }
    });
  }

  /* ---- scatter -------------------------------------------------------- */
  function scatter(host, teams, total) {
    while (host.firstChild) host.removeChild(host.firstChild);
    var W = Math.max(280, host.clientWidth || root.clientWidth || 640), H = Math.round(Math.min(420, Math.max(280, W * 0.62))), m = { t: 12, r: 16, b: 40, l: 66 };
    var svg = el('svg', { viewBox: '0 0 ' + W + ' ' + H, width: W, height: H }, host);
    var pts = teams.filter(function (t) { return t.st.n >= 20 && isFinite(t.st.all); });
    if (!pts.length) { text(svg, W / 2, H / 2, 'Not enough plays for these filters'); return; }
    var xs = pts.map(function (p) { return p.st.passRate; }), ys = pts.map(function (p) { return p.st.all; });
    var xlo = Math.min.apply(null, xs), xhi = Math.max.apply(null, xs), ylo = Math.min.apply(null, ys), yhi = Math.max.apply(null, ys);
    var xp = (xhi - xlo || .05) * .08, yp = (yhi - ylo || .05) * .1; xlo -= xp; xhi += xp; ylo -= yp; yhi += yp;
    var xt = niceTicks(xlo, xhi, 5), yt = niceTicks(ylo, yhi, 4);
    var x = function (v) { return m.l + (v - xlo) / (xhi - xlo) * (W - m.l - m.r); };
    var y = function (v) { return m.t + (yhi - v) / (yhi - ylo) * (H - m.t - m.b); };
    var grid = el('g', { 'class': 'grid' }, svg);
    yt.forEach(function (t) { if (t < ylo || t > yhi) return; el('line', { x1: m.l, x2: W - m.r, y1: y(t), y2: y(t), 'class': t === 0 ? 'zero' : '' }, grid); text(svg, m.l - 8, y(t) + 4, fmtEpa(t), 'tick', 'end'); });
    xt.forEach(function (t) { if (t < xlo || t > xhi) return; text(svg, x(t), H - m.b + 16, fmtPct(t)); });
    text(svg, (m.l + W - m.r) / 2, H - 4, 'First-down pass rate →', 'axis-title');
    var yl = text(svg, 14, (m.t + H - m.b) / 2, 'EPA per first-down play →', 'axis-title');
    yl.setAttribute('transform', 'rotate(-90 14 ' + (m.t + H - m.b) / 2 + ')');
    if (isFinite(total.passRate)) el('line', { x1: x(total.passRate), x2: x(total.passRate), y1: m.t, y2: H - m.b, 'class': 'avg' }, svg);
    if (isFinite(total.all)) el('line', { x1: m.l, x2: W - m.r, y1: y(total.all), y2: y(total.all), 'class': 'avg' }, svg);
    var tip = tooltip(host), scale = function () { return host.clientWidth / W; };
    var ordered = pts.slice().sort(function (a, b) { return (a.team === state.team) - (b.team === state.team); });
    ordered.forEach(function (p) {
      var hl = p.team === state.team, cx = x(p.st.passRate), cy = y(p.st.all);
      el('circle', { cx: cx, cy: cy, r: hl ? 7 : 5, 'class': 'dot' + (hl ? ' dot--hl' : '') }, svg);
      if (hl || W >= 560) text(svg, cx, cy - (hl ? 11 : 8), p.team, 'dot-label' + (hl ? ' dot-label--hl' : ''));
      var hit = el('circle', { cx: cx, cy: cy, r: 12, 'class': 'hit', tabindex: 0, role: 'button', 'aria-label': p.team + ': ' + fmtPct(p.st.passRate) + ' passes, ' + fmtEpa(p.st.all) + ' EPA per play' }, svg);
      var show = function () { tip.show(p.team, [
        { value: fmtPct(p.st.passRate), label: 'pass rate' },
        { key: 'pass', value: fmtEpa(p.st.pass), label: 'EPA per pass' },
        { key: 'run', value: fmtEpa(p.st.run), label: 'EPA per run' },
        { value: p.st.n.toLocaleString(), label: 'plays' }], cx * scale(), cy * scale()); };
      hit.addEventListener('pointerenter', show); hit.addEventListener('focus', show);
      hit.addEventListener('pointerleave', tip.hide); hit.addEventListener('blur', tip.hide);
      hit.addEventListener('click', function () { state.team = state.team === p.team ? '' : p.team; $('fd-team').value = state.team; render(); });
    });
  }

  /* ---- page ------------------------------------------------------------ */
  function seasonLabel(s) { return data.seasonNotes[String(s)] ? s + '*' : String(s); }
  function render() {
    var r = compute(), t = r.total;
    var tiles = { passRate: fmtPct(t.passRate), passEpa: fmtEpa(t.pass), runEpa: fmtEpa(t.run), runWins: r.runWins + ' of ' + r.teamSeasons };
    Array.prototype.forEach.call(document.querySelectorAll('[data-tile]'), function (n) { var v = tiles[n.getAttribute('data-tile')]; if (v && v.indexOf('NaN') < 0) n.textContent = v; });

    var team = state.team;
    var trendSeries = [
      { key: 'pass', cls: 'line--pass', pt: 'pt--pass', label: 'Passes', tipLabel: 'per pass, NFL', get: function (p) { return p.st.pass; } },
      { key: 'run', cls: 'line--run', pt: 'pt--run', label: 'Runs', tipLabel: 'per run, NFL', get: function (p) { return p.st.run; } }
    ];
    if (team) {
      trendSeries.push({ key: 'pass', cls: 'line--pass', dash: '5 4', tipLabel: 'per pass, ' + team, get: function (p) { return p.team && p.team.n ? p.team.pass : NaN; } });
      trendSeries.push({ key: 'run', cls: 'line--run', dash: '5 4', tipLabel: 'per run, ' + team, get: function (p) { return p.team && p.team.n ? p.team.run : NaN; } });
    }
    var common = { xLabel: function (p) { return seasonLabel(p.season); }, title: function (p) { return p.season + (data.seasonNotes[p.season] ? ' (' + data.seasonNotes[p.season] + ')' : ''); } };
    lineChart($('fd-trend'), r.trend, trendSeries, Object.assign({ height: 240, includeZero: true, fmt: function (v) { return fmtEpa(v); } }, common));
    var rateSeries = [{ key: 'pass', cls: 'line--pass', pt: 'pt--pass', label: 'NFL', tipLabel: 'passes, NFL', get: function (p) { return p.st.passRate; } }];
    if (team) rateSeries.push({ key: 'pass', cls: 'line--pass', dash: '5 4', label: team, tipLabel: 'passes, ' + team, get: function (p) { return p.team && p.team.n ? p.team.passRate : NaN; } });
    lineChart($('fd-rate'), r.trend, rateSeries, Object.assign({ height: 180, minDomain: [0.35, 0.65], fmt: function (v) { return fmtPct(v); } }, common));

    $('fd-scatter-sub').textContent = (state.from === state.to ? state.from : state.from + '–' + state.to) + ' combined · dashed lines are the NFL average · click a dot to highlight it';
    scatter($('fd-scatter'), r.teams, t);

    var note = '';
    if (team) {
      var ts = r.teams.filter(function (x) { return x.team === team; })[0];
      if (ts) note = team + ' in these plays: passed ' + fmtPct(ts.st.passRate) + ' of the time, ' + fmtEpa(ts.st.pass) + ' EPA per pass and ' + fmtEpa(ts.st.run) + ' per run (' + ts.st.n.toLocaleString() + ' plays). Dashed lines in the charts above are ' + team + '.';
    }
    $('fd-team-note').textContent = note;

    var tbl = $('fd-table'); while (tbl.firstChild) tbl.removeChild(tbl.firstChild);
    var head = tbl.createTHead().insertRow();
    ['Season', 'Plays', 'Pass rate', 'EPA/pass', 'EPA/run', 'Success, passes', 'Success, runs'].forEach(function (h) { var th = document.createElement('th'); th.textContent = h; head.appendChild(th); });
    var body = tbl.createTBody();
    r.trend.forEach(function (p) {
      var row = body.insertRow(), st = p.st;
      [seasonLabel(p.season), st.n.toLocaleString(), fmtPct(st.passRate), fmtEpa(st.pass), fmtEpa(st.run), fmtPct(st.passSucc), fmtPct(st.runSucc)].forEach(function (v) { row.insertCell().textContent = v; });
    });
  }

  function init(json) {
    data = json;
    var from = $('fd-from'), to = $('fd-to'), teamSel = $('fd-team');
    data.seasons.forEach(function (s) {
      [from, to].forEach(function (sel) { var o = document.createElement('option'); o.value = s; o.textContent = seasonLabel(s); sel.appendChild(o); });
    });
    data.teams.forEach(function (t) { var o = document.createElement('option'); o.value = t; o.textContent = t; teamSel.appendChild(o); });
    state.from = data.seasons[0]; state.to = data.seasons[data.seasons.length - 1];
    from.value = state.from; to.value = state.to;
    $('fd-controls').addEventListener('change', function (e) {
      state.from = +from.value; state.to = +to.value;
      if (state.from > state.to) { if (e.target === from) { state.to = state.from; to.value = state.to; } else { state.from = state.to; from.value = state.from; } }
      state.script = $('fd-script').value; state.zone = $('fd-zone').value; state.team = teamSel.value;
      render();
    });
    var resizeTimer, lastWidth = 0;
    function onResize() {
      if (root.clientWidth === lastWidth) return;
      lastWidth = root.clientWidth; clearTimeout(resizeTimer); resizeTimer = setTimeout(render, 100);
    }
    if (window.ResizeObserver) new ResizeObserver(onResize).observe(root); else window.addEventListener('resize', onResize);
    render();
  }

  var src = '/assets/data/first-down-epa.json';
  fetch(src).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(init).catch(function () {
    $('fd-team-note').textContent = 'The chart data could not be loaded. The team-by-season numbers are available as a CSV (link above).';
  });
})();
