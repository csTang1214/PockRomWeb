# PockRomWeb

Marketing website for **AICompanion** — a free, offline AI companion app for Android.

Plain static HTML/CSS/JS, no build step, hosted on GitHub Pages.

## Structure

```
index.html              Landing page (hero, features, screenshots, FAQ, CTA)
404.html                 Custom not-found page
robots.txt / sitemap.xml SEO crawling files
assets/css/style.css     All styles
assets/js/main.js        Mobile nav toggle
assets/img/              Icons, hero/OG images, screenshots (jpg + webp)
scripts/prep_images.py   One-off script used to generate assets/img/ from the app repo's source images
```

## Local preview

Any static file server works, e.g.:

```
npx serve .
```

## Deploying

Push to `main` and enable GitHub Pages (Settings → Pages → Deploy from branch → `main` / `/root`) for this repo. The site will be served at:

```
https://cstang1214.github.io/PockRomWeb/
```

If `index.html`'s canonical/OG URLs or `sitemap.xml`/`robots.txt` ever need to point somewhere else (e.g. a custom domain), update those three files together.

## Updating screenshots or copy

Source screenshots live in the repo root (`CharacterChat.jpg`, etc.) and are re-derived into `assets/img/screenshots/` (jpg + webp) by `scripts/prep_images.py`. Re-run it after swapping a source image:

```
python scripts/prep_images.py
```
