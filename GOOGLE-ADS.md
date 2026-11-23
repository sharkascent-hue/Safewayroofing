# Google Ads setup sheet: Safeway Roofing & Chimneys

Everything below is already live on the website. Copy it into Google Ads.
Replace `https://safewayroofing.ie/` with the Vercel address if the domain is not pointed at the new site yet.

## 1. Landing pages (Final URLs)

Built for ads: no menu, quote form at the top, call and WhatsApp buttons, no intro animation.
Hidden from Google search on purpose, which does not affect ads.

| Ad group / keywords | Final URL |
|---|---|
| Roofers Dublin (general) | https://safewayroofing.ie/lp/roofers-dublin/ |
| Roof repairs Dublin | https://safewayroofing.ie/lp/roof-repairs-dublin/ |
| Emergency roof repairs / roof leaking | https://safewayroofing.ie/lp/emergency-roof-repairs/ |
| Chimney repairs | https://safewayroofing.ie/lp/chimney-repairs-dublin/ |
| Flat roofs | https://safewayroofing.ie/lp/flat-roofs-dublin/ |
| Gutters, fascia & soffits | https://safewayroofing.ie/lp/gutters-fascia-soffits/ |
| New roof / re-roofing | https://safewayroofing.ie/lp/new-roof-dublin/ |
| Roof cleaning / moss removal | https://safewayroofing.ie/lp/roof-cleaning/ |
| Drone roof inspection | https://safewayroofing.ie/lp/drone-roof-inspection/ |
| Roofers Kildare | https://safewayroofing.ie/lp/roofers-kildare/ |
| Roofers Wicklow | https://safewayroofing.ie/lp/roofers-wicklow/ |

Leave **auto-tagging ON** (Google Ads > Admin > Account settings). The site saves the ad click ID and sends it with every enquiry email.

## 2. Sitelinks (link text max 25 characters, each description line max 35)

| Sitelink text | Description line 1 | Description line 2 | URL |
|---|---|---|---|
| Request a Quote | Clear, upfront pricing | No obligation, fast reply | https://safewayroofing.ie/contact-us/ |
| Roof Repairs | Leaks, slates and tiles fixed | Fully insured local team | https://safewayroofing.ie/our-services/roof-repairs/ |
| Chimney Repairs | Brickwork, flashing, leaks | Repointing and lead work | https://safewayroofing.ie/our-services/chimney-repairs/ |
| Gutters & Fascia | UPVC gutters, fascia, soffits | Black or white, neat finish | https://safewayroofing.ie/our-services/upvc-gutter-installation/ |
| Drone Roof Inspections | HD photos of your roof | Safe, no ladders needed | https://safewayroofing.ie/our-services/drone-roof-inspections/ |
| Our Recent Work | Photos of real Safeway jobs | Re-roofs, repairs, chimneys | https://safewayroofing.ie/our-work/ |
| Customer Reviews | What our customers say | Homeowners across Dublin | https://safewayroofing.ie/reviews/ |
| Areas We Cover | Dublin, Kildare & Wicklow | Check your town online | https://safewayroofing.ie/areas-we-cover/ |

## 3. Callouts (max 25 characters each)

- 10 Year Written Guarantee
- Fully Insured Team
- 24/7 Emergency Line
- Clear Upfront Quotes
- Drone Roof Inspections
- Dublin, Kildare & Wicklow
- VAT Registered Business
- CRO Registered (only if the company is registered with the CRO)

## 4. Structured snippet

Header: **Services**. Values: Roof Repairs, New Roofs, Flat Roofs, Chimney Repairs, UPVC Gutters, Fascia & Soffits, Roof Cleaning, Dry Verge & Ridge

## 5. Call asset

Phone: **087 485 8556** (Ireland). Turn on call reporting so calls from ads count as conversions.

## 6. Location asset

Link the Google Business Profile for Safeway Roofing & Chimneys, 51 Bracken Road, Dublin D18 CV48.

## 7. Conversion tracking (one step left)

The tracking code is already in the website and switches itself on when the IDs are added.
In Google Ads > Goals > Conversions, create these three website conversions ("Use Google tag", "Set up manually"):

| Conversion | Category | Counts when |
|---|---|---|
| Quote form sent | Submit lead form | Someone sends a quote form (thank-you page loads) |
| Call click | Contact | Someone taps the phone number on the site |
| WhatsApp click | Contact | Someone taps a WhatsApp button |

Then send the web developer:
- the **Conversion ID** (looks like `AW-123456789`), and
- the **Conversion label** for each of the three (looks like `AbC-D_efG-h12_34-567`).

They go into the settings block at the top of `assets/site.js` (`googleAdsId`, `convForm`, `convCall`, `convWhatsApp`).
Once added, the cookie banner appears automatically (Google Consent Mode v2, needed for ads in Ireland/EU).
Optional: a GA4 Measurement ID (`G-XXXXXXXXXX`) can go in `ga4Id` the same way.

## Checked and ready

- No intro animation for ad clicks or Google's ad checking robot, on any page
- Every landing page has a quote form, call button, WhatsApp button, privacy policy link and business details
- Enquiry emails include the page and the ad click ID
- Privacy policy covers forms, cookies and ad measurement
- Mobile-friendly; pages load fast (about 0.4–0.9 MB each)
