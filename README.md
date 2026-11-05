# vchen007.github.io

Victor Chen's portfolio site: <https://vchen007.github.io>. Built with Jekyll on GitHub Pages, starting from the [AcademicPages](https://github.com/academicpages/academicpages.github.io) template (a fork of [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/), MIT licensed; see `LICENSE`).

## Where things live

| What | Where |
| --- | --- |
| Home page (intro, featured projects, skills, experience) | `_pages/about.md` |
| Skills shown on the home page | `_data/skills.yml` |
| Top navigation | `_data/navigation.yml` |
| Name, bio, social links, site description | `_config.yml` |
| Projects (one file each; file name sets the order, `portfolio-0` is first) | `_portfolio/` |
| Résumé PDF (linked from the nav, `/cv/` and `/resume`) | `files/Resume Victor Chen.pdf` |
| Colours, dark mode and page components | `_sass/_theme.scss` |
| Images, link-preview cards (`images/og/`) | `images/` |

## Adding a project

Create `_portfolio/portfolio-N.md` with front matter like this, then write the walkthrough below it:

```yaml
---
title: "Project title"
excerpt: "One sentence for the project card, search results and link previews."
kicker: "Tableau dashboard"        # small label above the title on the card
collection: portfolio
featured: true                     # also show it on the home page
teaser: my-chart.png               # card image in /images/ (or a full URL)
teaser_fit: contain                # optional: show the whole image instead of cropping
og_image: og/portfolio-N.png       # link-preview image (generate it, see below)
tools: [Python, SQL]
summary:                           # the "At a glance" box at the top of the page
  question: "..."                  # or goal: "..."
  data: "..."
  approach: "..."
  result: "..."
links:                             # optional buttons in the box
  - label: "Open in Tableau Public"
    url: "https://..."
---
```

Then regenerate the link-preview cards: `node _scripts/make-social-images.js` (needs Playwright: `npm i -D playwright && npx playwright install chromium`).

## Updating the first-down EPA project

`_scripts/first_down_epa.py` downloads nflverse play-by-play and rebuilds the data behind `/portfolio/first-down-epa/`:

```bash
pip install pandas pyarrow
python3 _scripts/first_down_epa.py --seasons 2016-2026
```

Update the dates and numbers in `_portfolio/portfolio-0.md` if they change.

## Running locally

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000>.

## Checks

`.github/workflows/site-check.yml` builds the site and checks internal links, images and scripts on every push and pull request, and links to other sites every Monday. To run the same check locally after a build: `bundle exec htmlproofer ./_site --disable-external --swap-urls '^https\://vchen007\.github\.io:'`.
