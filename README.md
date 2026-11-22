# Safeway Roofing & Chimneys

Static website for safewayroofing.ie. No build step is needed to host it: the HTML in this repo is ready to serve.

- `build.py` regenerates every page, `sitemap.xml` and `robots.txt`. Edit copy there, then run `python3 build.py`.
- `assets/style.css` holds the design.
- Forms are delivered by Web3Forms (access key in `build.py`, WEB3FORMS_KEY). `assets/site.js` holds form sending and tracking. Add the Google Ads ID and conversion labels in the settings block at the top.
- `lp/` holds the Google Ads landing pages (not indexed by search engines).
