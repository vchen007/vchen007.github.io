---
permalink: /
title: "Sports & Business Analytics"
excerpt: "Victor Chen is a sports and business analyst who builds dashboards, data pipelines and models with SQL, Python, R and Tableau."
author_profile: true
hide_title: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<section class="hero">
  <p class="hero__eyebrow">Sports &amp; business analytics</p>
  <h1 class="hero__title">Hi, I'm Victor Chen.</h1>
  <p class="hero__lead">I'm an analyst with an MS in Business Analytics from the Wisconsin School of Business (UW–Madison) and a Sports Business Analytics certification. I chart NBA and NFL games for For The Numbers (FTN), and I build dashboards, data pipelines and models with SQL, Python, R and Tableau. I'm looking for an analytics role on a data-driven team.</p>
  <div class="hero__actions">
    <a class="btn" href="{{ base_path }}/portfolio/">See my projects</a>
    <a class="btn btn--ghost" href="{{ base_path }}/files/Resume%20Victor%20Chen.pdf">Résumé (PDF)</a>
    <a class="btn btn--ghost" href="mailto:{{ site.author.email }}">Email me</a>
  </div>
</section>

<h2 class="section-title">Featured projects</h2>

<div class="project-grid">
{% for project in site.portfolio %}{% if project.featured %}
  {% include project-card.html project=project %}
{% endif %}{% endfor %}
</div>

<p class="section-more"><a href="{{ base_path }}/portfolio/">All {{ site.portfolio.size }} projects →</a></p>

<h2 class="section-title">Skills</h2>

<div class="skills-grid">
{% for skill in site.data.skills %}
  <div>
    <h3>{{ skill.group }}</h3>
    <ul class="chips">{% for item in skill.items %}<li><span class="chip">{{ item }}</span></li>{% endfor %}</ul>
  </div>
{% endfor %}
</div>

<h2 class="section-title">Experience</h2>

<ul class="timeline">
  <li>
    <span class="timeline__role">NBA/NFL Charter · For The Numbers (FTN)</span>
    <span class="timeline__meta">Remote · Oct 2024 – present</span>
    <span class="timeline__note">Chart every possession of NBA games (screens, defensive contests, rebound contests; 350+ plays a game) and NFL skill-position players for FTN's research team and proprietary metrics.</span>
  </li>
  <li>
    <span class="timeline__role">Analytics Consultant · AMCON Distributing (Wisconsin School of Business)</span>
    <span class="timeline__meta">Madison, WI · Jan – May 2024</span>
    <span class="timeline__note">Built a Power BI sales dashboard for account managers on a Python → MySQL pipeline that cleaned the sponsor's Excel files.</span>
  </li>
  <li>
    <span class="timeline__role">MS Business Analytics · University of Wisconsin–Madison</span>
    <span class="timeline__meta">Wisconsin School of Business · BS Business Administration, Chapman University</span>
  </li>
</ul>

<p class="section-more"><a href="{{ base_path }}/files/Resume%20Victor%20Chen.pdf">Full résumé, including earlier roles →</a></p>
