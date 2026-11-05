---
title: "Does Passing on First Down Pay Off?"
permalink: /portfolio/first-down-epa/
excerpt: "An interactive look at 157,000 first-down plays from 2016 to 2026: passes gain about +0.10 expected points per play, runs lose about 0.10, yet teams still run more often than they pass."
kicker: "Interactive · NFL analytics"
collection: portfolio
featured: true
teaser: first-down-epa.png
og_image: og/portfolio-0.png
tools: [Python, pandas, nflverse, JavaScript, SVG]
summary:
  question: "Over a decade of NFL play-by-play, does a first-down pass or run gain more, and has play-calling caught up?"
  data: "Every regular-season first-down run and pass from 2016 through Week 8 of 2026 (157,728 plays), from nflverse play-by-play, which includes expected points added (EPA) for each play."
  approach: "A Python pipeline filters the plays, sorts each one by game situation and field position, and writes a compact data file. The charts below are drawn in plain JavaScript and SVG, so every filter recalculates in the browser."
  result: "In neutral game situations, first-down passes averaged +0.10 EPA per play and runs −0.10, a gap that shows up in every season. Teams still passed only 47% of the time, and runs beat passes in just 23 of 352 team-seasons."
links:
  - label: "Download the team data (CSV)"
    url: "/assets/data/first-down-epa-teams.csv"
  - label: "Pipeline code"
    url: "https://github.com/vchen007/vchen007.github.io/blob/master/_scripts/first_down_epa.py"
---

My [first-down dashboard](/portfolio/portfolio-6/) shows how often teams run or pass on first down, and the [2026 live version](/portfolio/portfolio-1/) tracks this season's run/pass split and EPA. This page steps back to ten-plus seasons and asks whether the choice pays off, and whether play-calling has changed because of it. I measure the payoff with **expected points added (EPA)**, which compares the expected points of the next play's down, distance and field position with those before the snap. A 5-yard run on 1st & 10 is worth a little; a 20-yard completion is worth a lot; a sack or interception costs points.

<div class="fd-tiles" id="fd-tiles" aria-live="polite">
  <div class="fd-tile"><span class="fd-tile__value" data-tile="passRate">47%</span><span class="fd-tile__label">of first-down plays were passes</span></div>
  <div class="fd-tile"><span class="fd-tile__value" data-tile="passEpa">+0.10</span><span class="fd-tile__label">EPA per pass</span></div>
  <div class="fd-tile"><span class="fd-tile__value" data-tile="runEpa">−0.10</span><span class="fd-tile__label">EPA per run</span></div>
  <div class="fd-tile"><span class="fd-tile__value" data-tile="runWins">23 of 352</span><span class="fd-tile__label">team-seasons where runs did better</span></div>
</div>

<div class="fd-explorer" id="fd-explorer">
  <form class="fd-controls" id="fd-controls" aria-label="Filters">
    <label>Seasons
      <span class="fd-range"><select id="fd-from" aria-label="First season"></select> to <select id="fd-to" aria-label="Last season"></select></span>
    </label>
    <label>Game situation
      <select id="fd-script">
        <option value="neutral" selected>Neutral (win prob. 20–80%)</option>
        <option value="all">All situations</option>
        <option value="ahead">Leading big (win prob. over 80%)</option>
        <option value="behind">Trailing big (win prob. under 20%)</option>
        <option value="late">Last two minutes of a half</option>
      </select>
    </label>
    <label>Field position
      <select id="fd-zone">
        <option value="all" selected>Anywhere</option>
        <option value="own">Own territory</option>
        <option value="opp">Opponent territory, outside the red zone</option>
        <option value="red">Red zone</option>
      </select>
    </label>
    <label>Highlight a team
      <select id="fd-team"><option value="">None</option></select>
    </label>
  </form>

  <figure class="fd-chart">
    <figcaption><strong>EPA per play on first down, by season</strong><span class="fd-legend"><span class="fd-key fd-key--pass"></span>Passes <span class="fd-key fd-key--run"></span>Runs</span></figcaption>
    <div class="fd-svg" id="fd-trend" role="group" aria-label="Line chart of EPA per play for first-down passes and runs by season"></div>
  </figure>

  <figure class="fd-chart">
    <figcaption><strong>Share of first-down plays that were passes</strong></figcaption>
    <div class="fd-svg" id="fd-rate" role="group" aria-label="Line chart of the first-down pass rate by season"></div>
  </figure>

  <figure class="fd-chart">
    <figcaption><strong>Teams: pass rate vs. EPA per first-down play</strong><span class="fd-sub" id="fd-scatter-sub"></span></figcaption>
    <div class="fd-svg" id="fd-scatter" role="group" aria-label="Scatter plot of each team's first-down pass rate against its EPA per first-down play"></div>
  </figure>

  <p class="fd-team-note" id="fd-team-note" aria-live="polite"></p>

  <details class="notebook-output">
    <summary>Show the numbers as a table</summary>
    <div class="fd-table-wrap"><table class="fd-table" id="fd-table"></table></div>
  </details>
  <noscript><p>The interactive charts need JavaScript. The <a href="/assets/data/first-down-epa-teams.csv">team-by-season data</a> is available as a CSV.</p></noscript>
</div>

## What the numbers say

- **Passing wins on average, every year.** In neutral situations, first-down passes gained about 0.2 more EPA per play than runs in every season from 2016 to 2026. The smallest gap was 2022 (+0.06 vs. −0.10) and the largest was 2017 (+0.10 vs. −0.14). Passes were also more often successful (positive EPA): 50% vs. 36%.
- **Play-calling barely moved.** Teams passed on 46–49% of neutral first downs in every one of those seasons, despite the gap.
- **The red zone narrows the gap.** Inside the 20, teams pass only 37% of the time. Passes still do better there (+0.08 EPA vs. −0.05 for runs), but the gap is about 0.12 instead of 0.2, and success rates are closer (46% vs. 40%).
- **Pass-heavy teams do a little better, but it isn't the whole story.** Across 352 team-seasons, a higher first-down pass rate goes with higher EPA per first-down play, but only loosely (correlation 0.27). Good quarterbacks both earn more passing and make it pay, so this is not proof that any team would improve by passing more.

## Method and caveats

- **Plays:** regular-season plays on first down where the offense ran or passed and EPA is available, excluding kneels and spikes. Sacks and scrambles count as passes, which works against passing, since sacks lose points. Plays wiped out by a penalty are included, as in most public EPA work.
- **Game situation:** "neutral" means the offense's win probability was between 20% and 80% and it was not the last two minutes of a half or overtime. That removes most of the plays where the score forces the call (running out the clock, or throwing to catch up).
- **What EPA leaves out:** a run's value isn't only its own result. Runs can set up play-action, rest a defense and shorten the game, and teams call them for those reasons. EPA measures each play on its own.
- **Teams:** relocated teams use today's abbreviation (OAK → LV, SD → LAC, STL → LA). 2026 covers games through Week 8 (data pulled November 5, 2026).
- **Source:** play-by-play and EPA from [nflverse](https://github.com/nflverse/nflverse-data), the same data the nfl_data_py library uses. The [pipeline script](https://github.com/vchen007/vchen007.github.io/blob/master/_scripts/first_down_epa.py) rebuilds the data file from scratch.

<link rel="stylesheet" href="/assets/css/first-down-epa.css">
<script src="/assets/js/first-down-epa.js" defer></script>
