#!/usr/bin/env python3
"""Static site generator for Safeway Roofing & Chimneys.
Run `python3 build.py` from this folder to regenerate every HTML page, sitemap.xml and robots.txt.
Edit copy in the data blocks below, styles in assets/style.css, behaviour/tracking in assets/site.js."""
import json, os, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://safewayroofing.ie/"
NAME = "Safeway Roofing & Chimneys"
PHONE, TEL, WA = "087 485 8556", "+353874858556", "353874858556"
EMAIL = "safewayroofing.chimneys@gmail.com"
ADDR = "51 Bracken Road, Dublin, D18 CV48"
FB = "https://www.facebook.com/profile.php?id=61596233412199"
IG = "https://www.instagram.com/safewayroofing.chimneys"
V = "1"
e = html.escape

ICON = {
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
 "x": '<path d="M18 6 6 18M6 6l12 12"/>',
 "down": '<path d="m6 9 6 6 6-6"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "tool": '<path d="M14.7 6.3a4 4 0 0 0 5 5L21 13l-8 8-3-3 8-8-1.3-1.3zM10 14l-6 6M5 3l4 4-2 2-4-4z"/>',
 "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h6"/>',
 "home": '<path d="m3 11 9-8 9 8"/><path d="M5 10v10h14V10"/>',
 "cam": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
 "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.2L5.8 21 7 14.200 2 9.300l6.900-1z"/>',
}
FILL = {
 "wa": '<path d="M12 2a10 10 0 0 0-8.600 15.100L2 22l5-1.300A10 10 0 1 0 12 2zm5.800 14.200c-.2.700-1.400 1.300-2 1.400-.5.100-1.200.100-1.900-.100-.400-.100-1-.300-1.700-.600-3-1.300-4.900-4.300-5-4.500-.200-.200-1.200-1.600-1.200-3 0-1.500.800-2.200 1-2.500.300-.300.600-.300.800-.300h.600c.200 0 .400 0 .700.500l.900 2.200c.100.200.100.400 0 .600l-.300.500-.500.500c-.200.200-.300.300-.100.600.200.300.800 1.300 1.700 2.100 1.100 1 2.100 1.300 2.400 1.500.300.100.500.100.700-.100l.900-1.100c.200-.300.400-.200.700-.100l2.100 1c.300.200.500.200.600.400.100.100.100.700-.200 1.400z"/>',
 "fb": '<path d="M22 12a10 10 0 1 0-11.600 9.900v-7H7.900V12h2.500V9.800c0-2.500 1.500-3.900 3.800-3.900 1.100 0 2.200.2 2.200.2v2.500h-1.200c-1.200 0-1.600.8-1.600 1.600V12h2.800l-.4 2.900h-2.400v7A10 10 0 0 0 22 12z"/>',
 "ig": '<path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.200a3.200 3.200 0 1 1 0-6.400 3.200 3.200 0 0 1 0 6.400zM17.300 5.500a1.200 1.200 0 1 0 0 2.400 1.200 1.200 0 0 0 0-2.400zM21.900 7.900c-.1-1.600-.4-3-1.600-4.200S17.700 2.200 16.100 2.100C14.500 2 9.500 2 7.900 2.100 6.300 2.200 4.900 2.500 3.700 3.700S2.200 6.300 2.100 7.900C2 9.500 2 14.500 2.100 16.100c.1 1.600.4 3 1.600 4.200s2.600 1.500 4.200 1.600c1.600.1 6.600.1 8.200 0 1.600-.1 3-.4 4.200-1.600s1.500-2.600 1.600-4.200c.1-1.600.1-6.600 0-8.200zm-2.100 10a3.300 3.300 0 0 1-1.900 1.900c-1.300.5-4.400.4-5.900.4s-4.600.1-5.900-.4a3.300 3.300 0 0 1-1.900-1.900c-.5-1.300-.4-4.400-.4-5.900s-.1-4.600.4-5.900a3.300 3.300 0 0 1 1.900-1.900c1.300-.5 4.400-.4 5.900-.4s4.600-.1 5.900.4a3.300 3.300 0 0 1 1.900 1.900c.5 1.300.4 4.400.4 5.900s.1 4.600-.4 5.900z"/>',
}
def ic(n):
    if n in FILL: return f'<svg class="i f" viewBox="0 0 24 24" aria-hidden="true">{FILL[n]}</svg>'
    return f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true">{ICON[n]}</svg>'

WHY = ["Skilled, fully insured tradespeople", "Quick response and reliable timekeeping", "Local knowledge and honest workmanship",
       "Quality materials built to last", "Clear quotes with upfront pricing"]
WHY_P = "We offer insured roofing, guttering and chimney services across Dublin, Kildare and Wicklow, with skilled workmanship that protects your home and keeps it looking good."

REVIEWS = [
 ("Pat and his team were excellent. Fixed our leaking roof the same week we called. Fair price and very tidy work.", "Matilda Mull"),
 ("Quick turnaround and a solid job. The roof hasn’t leaked once since they worked on it.", "Grace Freeman"),
 ("We’ve used Safeway Roofing & Chimneys twice now, and both times the service was excellent. Always on time and no hassle.", "Charles Sanderson"),
 ("They repaired our valley and replaced broken slates. Everything looks perfect now. Five stars.", "Dylan Stevens"),
]

AREAS = {
 "South Dublin": ["Rathmines","Rathgar","Terenure","Templeogue","Crumlin","Walkinstown","Kimmage","Dundrum","Churchtown","Stillorgan","Blackrock","Ballsbridge","Donnybrook","Booterstown","Tallaght","Clondalkin","Lucan","Ballyfermot","Sandyford","Killiney","Dalkey","Shankill"],
 "North Dublin": ["Phibsborough","Drumcondra","Santry","Whitehall","Ballymun","Glasnevin","Finglas","Coolock","Raheny","Clontarf","Donaghmede","Swords","Malahide","Portmarnock","Howth","Baldoyle","Beaumont","Artane","Killester","Darndale"],
 "Kildare": ["Naas","Newbridge","Kildare Town","Athy","Celbridge","Maynooth","Leixlip","Clane","Kilcullen","Sallins","Kill","Straffan","Monasterevin","Rathangan","Prosperous"],
 "Wicklow": ["Bray","Greystones","Wicklow Town","Arklow","Ashford","Newtownmountkennedy","Kilcoole","Delgany","Blessington","Baltinglass","Rathdrum","Roundwood","Shillelagh"],
}
COUNTIES = {
 "dublin": ("Dublin", ["South Dublin", "North Dublin"], "work-roofers-laying-underlay",
   "From Clontarf and Swords on the northside to Dundrum, Tallaght and Dalkey on the southside, our insured crew looks after roofs, gutters and chimneys right across Dublin city and county. We are based in Sandyford, Dublin 18, so help is never far away."),
 "kildare": ("Kildare", ["Kildare"], "work-white-fascia-soffit-gutter-house",
   "Safeway Roofing & Chimneys works throughout County Kildare, from Maynooth, Leixlip and Celbridge to Naas, Newbridge and Athy. Whether it is a slipped slate, a leaking flat roof or a full re-roof, you get a clear quote and tidy, careful work."),
 "wicklow": ("Wicklow", ["Wicklow"], "work-gable-chimney-fascia-gutter",
   "Homes in County Wicklow take plenty of wind and rain. We repair and replace roofs, guttering, fascia and chimneys from Bray and Greystones down to Arklow, and inland to Blessington and Baltinglass, with every completed project backed by our written guarantee."),
}

# --- gallery: file -> (caption, category) ---
WORK = [
 ("work-roofers-laying-underlay","Crew laying new underlay on a tiled roof","roof"),
 ("work-roof-relay-before-after-01","Roof relay, before and after","ba"),
 ("work-white-fascia-soffit-gutter-house","New white fascia, soffit and guttering","line"),
 ("work-chimney-stack-lead-flashing-01","Chimney stack with new lead flashing","chim"),
 ("work-underlay-battens-new-roof","New underlay and battens ready for tiles","roof"),
 ("work-black-fascia-gutter-downpipes-house","Black fascia, gutters and downpipes","line"),
 ("work-garden-room-flat-roof-felt","Garden room flat roof in torch-on felt","flat"),
 ("work-roof-relay-before-after-02","Old felt replaced with breathable membrane","ba"),
 ("work-black-fascia-soffit-corner","Black fascia and soffit corner detail","line"),
 ("work-roofer-fitting-underlay","Fitting underlay on a re-roof","roof"),
 ("work-ridge-tiles-red-mortar","Ridge tiles re-bedded in red mortar","roof"),
 ("work-chimney-lead-flashing-slate-roof","Lead flashing where chimney meets slate","chim"),
 ("work-roof-relay-before-after-03","Roof section stripped and relaid","ba"),
 ("work-black-dry-verge-roof-edge-02","Black dry verge along the roof edge","line"),
 ("work-breathable-membrane-battens-tiles","Breathable membrane, battens and tiles","roof"),
 ("work-gable-chimney-fascia-gutter","Gable, chimney, fascia and gutter finished","line"),
 ("work-roof-relay-before-after-04","Before and after: new membrane and battens","ba"),
 ("work-underlay-patch-roof-repair","Roof repair with new underlay patch","roof"),
 ("work-black-fascia-soffit-gutter-render","Black roofline against fresh render","line"),
 ("work-chimney-stack-lead-flashing-02","Brick chimney with stepped lead flashing","chim"),
 ("work-terracotta-ridge-hip-tiles","Terracotta ridge and hip tiles","roof"),
 ("work-black-downpipe-fascia-gable","Black downpipe and fascia on a gable","line"),
 ("work-hip-end-tiles-mortar-flashing","Hip end re-bedded and flashed","roof"),
 ("work-black-fascia-gable-dry-verge","Gable with black fascia and dry verge","line"),
 ("work-reroof-blue-membrane-tiles","Re-roof in progress with new membrane","roof"),
 ("work-slate-roof-lead-flashing-mortar-verge","Slate roof with new lead flashing","chim"),
 ("work-black-fascia-soffit-tile-edge","Black fascia and soffit under the tile edge","line"),
 ("work-underlay-battens-terracotta-roof","Underlay and battens on a terracotta roof","roof"),
 ("work-damaged-flat-roof-lead-flashing-cables","Damaged flat roof found on inspection","flat"),
 ("work-white-fascia-gutter-brick-house-ladder","White fascia and gutter on a brick house","line"),
 ("work-roof-strip-out-chimney-insulation","Roof stripped back around the chimney","roof"),
 ("work-black-fascia-ridge-gable-chimney","Black fascia, ridge and gable","line"),
 ("work-eurovent-underlay-lead-flashing","New underlay with lead flashing","roof"),
 ("work-dormer-cheek-stripped-lead","Dormer cheek stripped for new lead","flat"),
 ("work-house-fascia-gutters-ladder","Fascia and gutters being replaced","line"),
 ("work-terracotta-tile-roof-valley","Terracotta tile roof valley","roof"),
 ("work-roof-eaves-underlay-fascia-closeup","Eaves detail: underlay over new fascia","line"),
 ("work-hip-roof-underlay-lead-valley","Hip roof underlay and lead valley","roof"),
 ("work-black-dry-verge-roof-edge-01","Dry verge fitted along the roof edge","line"),
 ("work-underlay-lead-flashing-measuring","Measuring up for lead flashing","roof"),
 ("work-black-fascia-gable-ladder","Black fascia on a gable end","line"),
 ("work-roof-battens-membrane-stacked-tiles","Tiles stacked ready on new battens","roof"),
 ("work-terracotta-roof-underlay-battens","Terracotta roof with new underlay","roof"),
 ("work-breathable-membrane-new-battens","Breathable membrane and new battens","roof"),
 ("work-roofer-fitting-underlay-hip-roof","Underlay going on a hip roof","roof"),
 ("work-underlay-new-roof-tiles","New underlay beside existing tiles","roof"),
 ("work-roof-strip-battens-debris","Old roof stripped back to battens","roof"),
 ("work-roof-stripped-battens-gutter-view","Stripped roof seen from the gutter line","roof"),
 ("work-old-felt-stripped-roof-ladder","Old felt exposed during strip-out","roof"),
 ("work-house-scaffold-tower-ladders","Safe access set up before work starts","roof"),
 ("work-scaffold-tower-ladder-house-rear","Scaffold tower at the rear of a house","roof"),
 ("work-gable-fascia-replacement-ladders","Gable fascia replacement under way","line"),
]
CAP = {f: c for f, c, _ in WORK}
CATS = [("all","All work"),("roof","Roofing"),("line","Fascia, soffits & gutters"),("chim","Chimneys & lead"),("flat","Flat roofs"),("ba","Before & after")]

def S(slug, name, short, img, h1, meta, intro, proc, steps, faqs, gal, nav=None):
    return dict(slug=slug, name=name, short=short, img=img, h1=h1, meta=meta, intro=intro, proc=proc, steps=steps, faqs=faqs, gal=gal, nav=nav or name)

SERVICES = [
 S("new-roof-installation","New Roof Installation","New roofs built to last, using durable materials that keep the weather out.","svc-new-roof",
   "New Roof Installation Across Dublin, Kildare & Wicklow",
   "New roofs and re-roofs in Dublin, Kildare and Wicklow. Slate, tile and flat roofs fitted by a fully insured team, with a 10 year written guarantee.",
   ["A new roof is one of the biggest investments you can make in your home. <strong>Safeway Roofing & Chimneys</strong> fits long-lasting, weatherproof roofs using quality materials chosen to handle Irish conditions in <strong>Dublin, Kildare and Wicklow</strong>.",
    "Whether you are replacing an old roof or covering a new extension, our crew works safely and carefully from start to finish. We install pitched and flat roofs, slate and tile finishes, and UPVC fascia and soffits to complete the job."],
   "Our 3-Step Installation Process",
   [("Quote & Survey","We look over your property and give you a clear quote with no obligation."),("Careful Installation","Our experienced crew fits your new roof safely and efficiently."),("Final Check","We check every detail so your new roof meets our standards and yours.")],
   [("How much does a new roof cost?","The price depends on the roof’s size, materials and style. Get in touch for a clear quote based on your home."),
    ("Do you fit both pitched and flat roofs?","Yes. We install pitched and flat roofs, with slate and tile finishes, and can fit UPVC fascia and soffits to complete the job."),
    ("Is the work guaranteed?","Yes. Every completed project comes with a 10 year written guarantee, and all our work is fully insured.")],
   ["work-underlay-battens-new-roof","work-breathable-membrane-battens-tiles","work-roofer-fitting-underlay","work-roof-relay-before-after-01"], nav="New Roofs"),
 S("roof-repairs","Roof Repairs","Prompt fixes for leaks, storm damage and worn or slipped tiles.","work-underlay-patch-roof-repair",
   "Roof Repairs in Dublin, Kildare & Wicklow",
   "Roof repairs across Dublin, Kildare and Wicklow. Leaks, slipped slates, broken tiles, flashing and storm damage fixed by a fully insured team. 24/7 emergency line.",
   ["A roof in good shape keeps leaks, damp and structural problems away from your home. <strong>Safeway Roofing & Chimneys</strong> carries out prompt, careful roof repairs across <strong>Dublin, Kildare and Wicklow</strong>, whether the roof is pitched, flat, slate, tile or UPVC.",
    "We deal with leaks, cracked or slipped tiles, damaged flashing, storm damage and more, using quality materials and proven methods so each repair lasts. Homeowners throughout Dublin, Kildare and Wicklow rely on us for repairs that protect their property."],
   "Our 3-Step Repair Process",
   [("Quote & Inspection","We inspect your roof to find the damage and give you a clear repair quote with no obligation."),("Skilled Repairs","Our experienced crew fixes leaks, replaces broken tiles and restores your roof safely and efficiently."),("Final Check","We inspect the finished repair carefully so it meets our standards and keeps your home protected.")],
   [("How can I tell if my roof needs repairing?","Watch for missing or cracked tiles, damp patches or stains inside, sagging sections and damaged flashing. A regular inspection helps catch problems early."),
    ("Can you repair every type of roof?","Yes. We repair pitched, flat, slate, tile and UPVC roofing across Dublin, Kildare and Wicklow."),
    ("How long will a repair take?","Small repairs are often finished in a day. Larger jobs can take two to three days depending on the damage."),
    ("Is your repair work insured?","Yes. All work is fully insured and carried out by trained professionals.")],
   ["work-hip-end-tiles-mortar-flashing","work-roof-relay-before-after-02","work-reroof-blue-membrane-tiles","work-terracotta-tile-roof-valley"]),
 S("flat-roofs","Flat Roofs","Hard-wearing flat roofing that stays watertight and safe for the long term.","svc-flat-roofs",
   "Flat Roofing in Dublin, Kildare & Wicklow",
   "Flat roof installation and repair in Dublin, Kildare and Wicklow. Felt, fibreglass and single-ply rubber systems fitted by a fully insured team.",
   ["Flat roofs need the right expertise to stay watertight, drain properly and last. <strong>Safeway Roofing & Chimneys</strong> installs, repairs and maintains flat roofs on homes and commercial buildings across <strong>Dublin, Kildare and Wicklow</strong>.",
    "From a brand-new flat roof to a repair or routine upkeep, we work carefully and tidily. We use quality felt, fibreglass and single-ply membrane systems that guard your property against leaks and water damage for years."],
   "Our 3-Step Process",
   [("Quote & Inspection","We inspect your flat roof and give you a detailed quote with no obligation."),("Skilled Installation","Our experienced crew installs or repairs your flat roof with quality materials and sound techniques."),("Final Check","We make sure your flat roof is secure and watertight and meets our high standards.")],
   [("How long does a flat roof last?","A well-installed flat roof can last 15 to 30 years depending on the materials and how well it is looked after. We use durable membranes for lasting protection."),
    ("Are flat roofs prone to leaks?","Not when they are installed and maintained properly. Correct waterproofing, good drainage and quality materials keep water out."),
    ("Does a flat roof need regular maintenance?","Yes. An annual check for debris, blocked outlets or small damage helps extend its life and avoids costly repairs."),
    ("Which flat roof systems do you fit?","We fit felt, fibreglass and single-ply rubber membrane roofs, and recommend the best option for your property and budget.")],
   ["work-garden-room-flat-roof-felt","work-damaged-flat-roof-lead-flashing-cables","work-dormer-cheek-stripped-lead"]),
 S("upvc-gutter-installation","UPVC Gutter Installation","Neat UPVC guttering fitted to carry rainwater away and protect your walls.","svc-gutters",
   "UPVC Guttering in Dublin, Kildare & Wicklow",
   "UPVC gutter installation, replacement and repair in Dublin, Kildare and Wicklow. Leaking or sagging gutters sorted by a fully insured local team.",
   ["Good guttering protects your home from water damage, damp and flooding. <strong>Safeway Roofing & Chimneys</strong> fits <strong>UPVC guttering</strong> across Dublin, Kildare and Wicklow, set up securely so rainwater is carried cleanly away from your property.",
    "We replace old or damaged gutters and fit new UPVC systems for homes and businesses alike. Quality materials and careful fitting give you a long-lasting system that needs little upkeep."],
   "Our 3-Step Process",
   [("Survey & Quote","We look over your existing guttering and give you a clear, no-obligation quote for replacement or new fitting."),("Skilled Fitting","Our crew fits your UPVC gutters with correct alignment, secure fixings and good water flow."),("Final Check","We check the finished system carefully so it works properly, is secure and looks neat.")],
   [("Why choose UPVC gutters?","UPVC is durable, weatherproof, low maintenance and does not corrode, so it protects your home for years."),
    ("How long does fitting take?","Most gutter jobs are finished in one to two days, depending on the size of the property."),
    ("Do you work across Dublin, Kildare and Wicklow?","Yes. We fit UPVC guttering for homeowners and businesses across all three counties."),
    ("Can you fix leaks or blockages in existing gutters?","Yes. As well as new installs we repair leaks, replace damaged sections and get your gutters running properly again.")],
   ["work-white-fascia-gutter-brick-house-ladder","work-black-fascia-gutter-downpipes-house","work-house-fascia-gutters-ladder","work-black-downpipe-fascia-gable"], nav="UPVC Gutters"),
 S("upvc-fascia-soffits","UPVC Fascia & Soffits","Clean-looking UPVC fascias and soffits that tidy up and protect your roofline.","svc-fascia-soffits",
   "UPVC Fascia & Soffits in Dublin, Kildare & Wicklow",
   "UPVC fascia and soffit replacement in Dublin, Kildare and Wicklow. Low-maintenance roofline in black or white, fitted by a fully insured team.",
   ["Well-fitted fascia and soffits keep water, pests and weather out while giving your home a neat, finished look. <strong>Safeway Roofing & Chimneys</strong> supplies and fits UPVC fascia and soffits across <strong>Dublin, Kildare and Wicklow</strong>, with precise, durable and weatherproof results.",
    "We replace tired or damaged boards and fit brand-new UPVC systems on homes and commercial buildings. Quality materials mean a long-lasting, low-maintenance finish that keeps your roof edges strong and tidy."],
   "Our 3-Step Process",
   [("Quote & Inspection","We check your existing fascia and soffits and give you a no-obligation quote for replacement or new fitting."),("Skilled Fitting","Our crew fits or replaces your UPVC fascia and soffits with careful alignment, sealing and a durable finish."),("Final Check","We check every board to make sure it is secure, weatherproof and neatly finished.")],
   [("Why replace old fascia and soffits?","Worn or damaged boards let in water and pests and can harm the roof structure. New UPVC gives lasting protection."),
    ("How long does fitting take?","Most jobs take one to two days, depending on the size of the property and the amount of work."),
    ("Is UPVC low maintenance?","Yes. UPVC is durable and weatherproof and needs far less upkeep than timber."),
    ("Do you cover Dublin, Kildare and Wicklow?","Yes. We fit UPVC fascia and soffits across all three counties.")],
   ["work-black-fascia-soffit-corner","work-black-fascia-soffit-gutter-render","work-white-fascia-soffit-gutter-house","work-black-fascia-soffit-tile-edge"]),
 S("chimney-repairs","Chimney Repairs","Careful chimney repairs and upkeep to keep your stack sound and safe.","svc-chimney-repairs",
   "Chimney Repairs in Dublin, Kildare & Wicklow",
   "Chimney repairs in Dublin, Kildare and Wicklow. Cracked brickwork, leaking flashing, repointing and rebuilds by a fully insured team with a written guarantee.",
   ["A sound chimney keeps your home safe and working properly. <strong>Safeway Roofing & Chimneys</strong> repairs damaged, leaking or tired chimneys so they are secure, weatherproof and protect your property.",
    "We deal with cracks, structural damage, flashing problems and leaks, and finish every repair to a standard that is safe and built to last."],
   "Our 3-Step Process",
   [("Quote & Inspection","We inspect your chimney, pinpoint the problems and give you a clear quote with no obligation."),("Skilled Repairs","Our crew repairs cracks, damaged brickwork, flashing and leaks using quality materials and sound techniques."),("Final Check","We make sure your chimney is sound, watertight and safe for the years ahead.")],
   [("How can I tell if my chimney needs repair?","Look for cracked bricks, crumbling mortar, leaks, damaged flashing or unusual smoke behaviour. Regular checks catch problems early."),
    ("Will chimney repairs stop leaks and water damage?","Yes. Properly sealed flashing, brickwork and mortar keep water out and protect your home."),
    ("How long does a chimney repair take?","Smaller repairs can often be finished in a day, while bigger structural work may take a few days. We keep disruption to a minimum."),
    ("Is your chimney work insured?","Yes. Safeway Roofing & Chimneys is fully insured and every job is carried out by skilled professionals.")],
   ["work-chimney-stack-lead-flashing-01","work-chimney-stack-lead-flashing-02","work-chimney-lead-flashing-slate-roof","work-gable-chimney-fascia-gutter"]),
 S("ridge-tile-repointing","Ridge Tile Repointing","Ridge tile repointing that secures your ridge and stops leaks.","svc-ridge-tiles",
   "Ridge Tile Repointing in Dublin, Kildare & Wicklow",
   "Ridge tile repointing and re-bedding in Dublin, Kildare and Wicklow. Loose or leaking ridge and hip tiles secured by a fully insured team.",
   ["The ridge is the most exposed line on your roof. When the mortar under the ridge tiles cracks or falls away, tiles work loose and rain finds a way in. <strong>Safeway Roofing & Chimneys</strong> repoints and re-beds ridge and hip tiles across <strong>Dublin, Kildare and Wicklow</strong>.",
    "We lift what is loose, clear out the failed mortar and bed the tiles back down properly, so the ridge is secure, weatherproof and neat against the rest of the roof."],
   "Our 3-Step Process",
   [("Quote & Inspection","We check the ridge, hips and verges, show you what has failed and give you a clear quote with no obligation."),("Repoint & Re-bed","Loose tiles are lifted, old mortar is cleared and the ridge is bedded and pointed again for a firm hold."),("Final Check","We check every tile is solid and the line is tidy before we leave.")],
   [("How do I know my ridge tiles need repointing?","Gaps or cracks in the mortar along the top of the roof, bits of mortar in the gutter, or a ridge tile that has shifted are the usual signs."),
    ("Can loose ridge tiles cause leaks?","Yes. Once the mortar fails, wind-driven rain can get under the ridge, and loose tiles can come away in a storm."),
    ("Is there an alternative to mortar?","Yes. A dry ridge system fixes the tiles mechanically without mortar. See our Elite Dry Verge/Ridge page or ask us which suits your roof.")],
   ["work-ridge-tiles-red-mortar","work-terracotta-ridge-hip-tiles","work-hip-end-tiles-mortar-flashing"]),
 S("elite-dry-verge-ridge","Elite Dry Verge/Ridge","A low-maintenance dry system for verges and ridges that gives a neat, secure finish.","svc-dry-verge",
   "Elite Dry Verge & Ridge in Dublin, Kildare & Wicklow",
   "Dry verge and dry ridge systems fitted in Dublin, Kildare and Wicklow. A mortar-free, low-maintenance roof edge from a fully insured team.",
   ["Give the edges of your roof lasting protection with an <strong>Elite Dry Verge & Ridge</strong> system fitted by <strong>Safeway Roofing & Chimneys</strong>. It keeps water out, cuts down on maintenance and improves the look of your property.",
    "For a new roof or to replace an ageing verge or ridge, we use quality materials and careful fitting to leave a clean, low-maintenance finish that holds up for years."],
   "Our 3-Step Process",
   [("Quote & Inspection","We inspect your roof edges and give you a clear quote with no obligation."),("Precise Fitting","Our skilled crew fits the dry verge and ridge system accurately for a durable, tidy finish."),("Final Check","We check that your roof edges are secure, neat and meet building standards.")],
   [("What is an Elite Dry Verge & Ridge system?","It is a quality roof edge system that guards against water ingress and wind damage, needs little upkeep and leaves a clean, professional finish."),
    ("How long does a dry verge and ridge system last?","Professionally fitted, it can last 25 to 40 years with minimal maintenance, protecting your roof for the long term."),
    ("Can it be fitted to an existing roof?","Yes. We can fit or replace dry verge and ridge systems on new and existing roofs with little disruption."),
    ("Why choose dry verge over traditional mortar?","Dry verge systems need no maintenance, last longer and resist water damage and wind uplift better than mortar, making them a cost-effective long-term choice.")],
   ["work-black-dry-verge-roof-edge-01","work-black-dry-verge-roof-edge-02","work-black-fascia-gable-dry-verge","work-black-fascia-ridge-gable-chimney"], nav="Dry Verge & Ridge"),
 S("roof-cleaning","Roof Cleaning","Gentle roof washing that removes moss and grime and helps your roof last longer.","svc-roof-cleaning",
   "Roof Cleaning in Dublin, Kildare & Wicklow",
   "Roof cleaning and moss removal in Dublin, Kildare and Wicklow. Safe methods for tile, slate and flat roofs from a fully insured team.",
   ["A clean roof protects your home and keeps it looking its best. <strong>Safeway Roofing & Chimneys</strong> provides roof cleaning across <strong>Dublin, Kildare and Wicklow</strong>, clearing moss, algae, dirt and debris to bring your roof back to good health. Regular cleaning helps prevent water damage, blocked gutters and early wear, so your home stays weatherproof all year.",
    "Our crew works on tile, slate, flat and UPVC roofs, using safe, effective methods that extend the life of your roof and lift its appearance."],
   "Our 3-Step Process",
   [("Quote & Inspection","We check your roof for moss, algae, staining and any structural concerns before we begin."),("Safe, Careful Cleaning","Our crew removes dirt, moss and build-up using safe methods that protect your tiles and surfaces."),("Final Rinse & Check","We wash the roof down and check it is clean and clear of debris before we finish.")],
   [("How often should I have my roof cleaned?","Most roofs in Dublin, Kildare and Wicklow benefit from cleaning every two to three years, depending on moss growth and weather."),
    ("Will cleaning damage my tiles?","No. We use safe, professional methods designed to protect slate, tile and flat roofs."),
    ("Do you remove all the moss and algae?","Yes. We clear moss, algae, lichen and debris, leaving the roof clean and helping slow regrowth."),
    ("Can roof cleaning help stop leaks?","It can. Clearing moss and build-up improves water flow and cuts the risk of trapped moisture that leads to leaks.")],
   ["work-house-scaffold-tower-ladders","work-scaffold-tower-ladder-house-rear","work-terracotta-tile-roof-valley"]),
 S("brick-cleaning-repointing","Brick Cleaning & Repointing","Brick cleaning and repointing to bring your brickwork back to life.","svc-brick-cleaning",
   "Brick Cleaning & Repointing in Dublin, Kildare & Wicklow",
   "Brick cleaning and repointing in Dublin, Kildare and Wicklow. Tired, stained or crumbling brickwork and chimney stacks restored by a fully insured team.",
   ["Brickwork that is stained or losing its mortar looks tired and lets damp into the wall. <strong>Safeway Roofing & Chimneys</strong> cleans and repoints brickwork on house fronts, gables and chimney stacks across <strong>Dublin, Kildare and Wicklow</strong>.",
    "We rake out failed joints, repoint with a mortar that suits the brick and clean the face of the wall carefully, so the brick keeps its character and the joints keep the weather out."],
   "Our 3-Step Process",
   [("Quote & Inspection","We look at the condition of the brick and the joints and give you a clear quote with no obligation."),("Clean & Repoint","Loose mortar is raked out, joints are repointed and the brick face is cleaned with care."),("Final Check","We check the joints are full and even and leave the area clean and tidy.")],
   [("When does brickwork need repointing?","When the mortar is cracked, crumbling or has receded behind the face of the brick. Left alone, water gets into the wall."),
    ("Do you repoint chimney stacks?","Yes. Chimneys take the worst of the weather, and repointing is often done alongside flashing or flaunching repairs."),
    ("Will cleaning damage old brick?","We choose a method to suit the brick and take care to protect its face. We will talk you through the approach before we start.")],
   ["work-white-fascia-gutter-brick-house-ladder","work-chimney-stack-lead-flashing-02","work-chimney-stack-lead-flashing-01"]),
 S("painting-decorating","Painting & Decorating","Inside and out painting that refreshes your home.","svc-painting",
   "Painting & Decorating in Dublin, Kildare & Wicklow",
   "Interior and exterior painting and decorating in Dublin, Kildare and Wicklow. A clean, lasting finish from a fully insured local team.",
   ["A fresh coat of paint protects your walls and changes how the whole house looks. Alongside our roofing work, <strong>Safeway Roofing & Chimneys</strong> takes on interior and exterior painting and decorating across <strong>Dublin, Kildare and Wicklow</strong>.",
    "Good preparation is what makes paint last. We wash down, fill and prime before any colour goes on, and we protect paths, windows and planting while we work. It is a natural job to pair with new fascia, soffits and gutters while access is already up."],
   "Our 3-Step Process",
   [("Quote & Visit","We look at the surfaces, agree colours and finishes and give you a clear quote with no obligation."),("Prepare & Paint","Surfaces are cleaned, repaired and primed, then painted for an even, lasting finish."),("Final Check","We walk the job with you and leave everything clean and tidy.")],
   [("Do you paint both inside and outside?","Yes. We take on interior and exterior painting and decorating."),
    ("Can painting be done with roofline work?","Yes. Many customers have the exterior painted at the same time as new fascia, soffits or gutters, which makes good use of the access."),
    ("Do you prepare the walls first?","Always. Washing down, filling and priming come before painting so the finish lasts.")],
   ["work-white-fascia-soffit-gutter-house","work-black-fascia-soffit-gutter-render","work-gable-chimney-fascia-gutter"]),
 S("drone-roof-inspections","Drone Roof Inspections","HD photos and video of your roof, with no ladders and nothing missed.","svc-drone-inspection",
   "Drone Roof Inspections in Dublin, Kildare & Wicklow",
   "Drone roof inspections in Dublin, Kildare and Wicklow. HD photos and video, safe ladder-free surveys and clear advice from a fully insured roofing team.",
   ["Some roof problems cannot be seen from the ground, and some roofs are awkward to reach safely. <strong>Safeway Roofing & Chimneys</strong> uses a drone to inspect roofs, chimneys and gutters across <strong>Dublin, Kildare and Wicklow</strong>, so you can see the condition of your roof for yourself.",
    "You get HD photos and video of slates, tiles, ridges, valleys, flashing and chimney stacks, followed by straight advice on what needs attention now and what can wait."],
   "Our 3-Step Process",
   [("Book a Visit","Call or send the form and we will arrange a time that suits you."),("Drone Survey","We fly the roof and capture clear photos and video of every elevation, with no ladders on your walls."),("Report & Advice","We go through what we found and give you a clear quote for any work that is needed.")],
   [("Why use a drone to inspect a roof?","It is safe and quick, it reaches places that are hard to see from a ladder and it gives you clear pictures of the actual problem."),
    ("What can a drone inspection find?","Slipped or cracked slates and tiles, failed ridge mortar, damaged flashing and lead, blocked valleys and gutters, and chimney defects."),
    ("Will I see the photos?","Yes. We show you the photos and video and explain what they mean before recommending any work.")],
   ["work-terracotta-ridge-hip-tiles","work-terracotta-tile-roof-valley","work-roof-stripped-battens-gutter-view"]),
]
SVC = {s["slug"]: s for s in SERVICES}
MORE = ["Asphalt Roofs","Chimney Repairs","Felt Roofs","Fibreglass Roof","Flat Roofs","Garage Roofs","Guttering & Downpipes","Lead Roofs","Lead Work","Leaking Roofs – All Types","New Roofs & Re-Roofs","Soffits, Fascias & Cladding","Valleys & Gullies","Pitched Roofs","Pointing","Porch Roofs","Roof Flashing","Roof Lights","Roof Repairs","Roof Window Repairs","Roof Window Installs","Roofing Carpentry","Roof Inspections & Reports","Roof Insulation","Shed Roofs","Single Ply Rubber Roof","Slate & Tiled Roofs"]
HOME_FAQ = [
 ("How much does a new roof cost?","The price depends on the roof’s size, materials and style. Get in touch for a clear quote based on your home."),
 ("Can you handle emergency roof or gutter repairs?","Yes. We respond quickly to urgent roof, gutter and chimney problems across Dublin, Kildare and Wicklow, and make the area safe and weather-tight."),
 ("Do you offer quotes and inspections?","Yes. We will look at your roof, gutters or chimney and give you a clear quote. Get in touch to arrange a visit."),
 ("Is your work insured and guaranteed?","Yes. Our work is fully insured, and every completed project comes with a 10 year written guarantee."),
]

# ------------------------------------------------------------------ components
def img(r, f, alt, sm=True, cls="", lazy=True, w=None, h=None):
    src = f"{r}assets/img/{f}{'-sm' if sm else ''}.webp"
    return f'<img src="{src}" alt="{e(alt)}"{" loading=\"lazy\" decoding=\"async\"" if lazy else " fetchpriority=\"high\""}{f" class=\"{cls}\"" if cls else ""}>'

def form(r, fid, title="Get your quote", sub="Tell us about the job and we will come back to you with a clear quote.", service="", message=True, h="h2"):
    opts = "".join(f'<option{" selected" if s["name"]==service else ""}>{e(s["name"])}</option>' for s in SERVICES)
    emer = f'<option{" selected" if service=="Emergency repair" else ""}>Emergency repair</option>'
    msg = '<div class="fld full"><label for="{0}-m">How can we help? (optional)</label><textarea id="{0}-m" name="message" placeholder="e.g. water coming in around the chimney"></textarea></div>'.format(fid) if message else ""
    return f'''<form class="fcard" id="{fid}" data-quote="{fid}" novalidate>
<{h}>{e(title)}</{h}><p class="fsub">{e(sub)}</p>
<div class="fmsg" role="alert" aria-live="polite"></div>
<div class="fgrid">
<div class="fld"><label for="{fid}-n">Name</label><input id="{fid}-n" name="name" autocomplete="name" placeholder="Your name" required></div>
<div class="fld"><label for="{fid}-p">Phone</label><input id="{fid}-p" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="Phone number" required></div>
<div class="fld"><label for="{fid}-a">Area</label><input id="{fid}-a" name="area" autocomplete="address-level2" placeholder="e.g. Dundrum"></div>
<div class="fld"><label for="{fid}-s">Service</label><select id="{fid}-s" name="service"><option value="">Choose a service</option>{emer}{opts}<option>Other</option></select></div>
{msg}
</div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-red btn-block" type="submit" style="margin-top:14px">Get my quote {ic("arrow")}</button>
<div class="for">or talk to us now</div>
<div class="alt"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")} {PHONE}</a><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{ic("wa")} WhatsApp</a></div>
<p class="fnote">No obligation. See our <a href="{r}privacy-policy/">privacy policy</a>.</p>
</form>'''

def ticks(items, cls=""):
    return f'<ul class="ticks {cls}">' + "".join(f"<li>{ic('check')}<span>{e(i)}</span></li>" for i in items) + "</ul>"

def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details{' open' if i==0 else ''}><summary>{e(q)}</summary><p>{e(a)}</p></details>" for i,(q,a) in enumerate(faqs)) + "</div>"

def reviews_html(n=4, cols="g4"):
    out = f'<div class="grid {cols}">'
    for t, who in REVIEWS[:n]:
        out += f'<figure class="rev rv" style="margin:0"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{e(t)}”</blockquote><figcaption><cite><i>{who[0]}</i><span>{e(who)}<small>Safeway customer</small></span></cite></figcaption></figure>'
    return out + "</div>"

def gallery(r, files, cls="", numbered=False, cats=False):
    d = dict((f,c) for f,_,c in WORK)
    out = f'<div class="gal {cls}">'
    for i, f in enumerate(files):
        cap = CAP.get(f, "")
        wide = " wide" if numbered and i in (0, 5) else ""
        num = f"<b>{i+1:02d}</b>" if numbered else ""
        out += f'<button type="button" class="gi{wide}" data-c="{d.get(f,"")}" data-full="{r}assets/img/{f}.webp" data-cap="{e(cap)}" aria-label="View photo: {e(cap)}">{img(r,f,cap)}<span class="cap">{num}{e(cap)}</span></button>'
    return out + "</div>"

LB = '<div class="lb" id="lb" role="dialog" aria-label="Photo viewer"><button class="x" aria-label="Close">✕</button><button class="p" aria-label="Previous">‹</button><img alt=""><button class="nx" aria-label="Next">›</button><p></p></div>'

def steps_html(steps):
    return '<div class="grid g3">' + "".join(f'<div class="card step rv"><span class="n">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(p)}</p></div>' for i,(t,p) in enumerate(steps)) + "</div>"

def cta_band(r, h="Ready for a quote?", p="Contact Safeway Roofing & Chimneys for roofing, guttering or chimney work anywhere in Dublin, Kildare and Wicklow. Our insured team offers quick, dependable service suited to your home."):
    return f'''<section class="cta-band"><div class="wrap"><div><h2>{h}</h2><p>{p}</p></div>
<div class="btn-row" style="margin:0"><a class="btn btn-red" href="{r}contact-us/#quote">Get your quote {ic("arrow")}</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")} Call {PHONE}</a></div></div></section>'''

def scards(r, items, numbered=True):
    out = '<div class="grid g4">'
    for i, s in enumerate(items):
        out += f'''<a class="scard rv" href="{r}our-services/{s["slug"]}/">{img(r,s["img"],s["name"])}{f'<span class="num">{i+1:02d}</span>' if numbered else ''}
<div class="sc-b"><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="go">View details {ic("arrow")}</span></div></a>'''
    return out + "</div>"

NAV = [("Home",""),("About","about-us/"),("Services","our-services/"),("Our Work","our-work/"),("Areas","areas-we-cover/"),("Reviews","reviews/"),("Contact","contact-us/")]

def header(r, path, lp=False):
    top = f'''<div class="topbar"><div class="wrap"><span><i class="pulse"></i>10 year written guarantee<span class="hide-m"> with every completed project</span></span>
<span class="tb-r"><span>24/7 emergency<span class="hide-m"> line</span></span><a class="hide-m" href="tel:{TEL}">{ic("phone")} {PHONE}</a><a class="hide-m" href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ic("fb")}</a><a class="hide-m" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ic("ig")}</a></span></div></div>'''
    brand = f'<a class="brand" href="{r}" aria-label="{e(NAME)} home"><img src="{r}assets/img/logo.webp" width="66" height="66" alt="{e(NAME)} logo"><span>Safeway<small>Roofing &amp; Chimneys</small></span></a>'
    if lp:
        return top + f'''<header class="hdr"><div class="wrap">{brand}<div class="hdr-cta"><a class="hdr-phone" href="tel:{TEL}">{ic("phone")} {PHONE}</a><a class="btn btn-red hide-m" href="#quote">Get your quote</a></div></div></header>'''
    def cur(p):
        return ' aria-current="page"' if (p == path or (p and path.startswith(p))) and not (p == "" and path) else ""
    li = ""
    for n, p in NAV:
        if n == "Services":
            dd = "".join(f'<li><a href="{r}our-services/{s["slug"]}/">{e(s["nav"])}</a></li>' for s in SERVICES)
            li += f'<li><a href="{r}{p}"{cur(p)}>{n} {ic("down")}</a><ul class="drop two">{dd}</ul></li>'
        elif n == "Areas":
            dd = "".join(f'<li><a href="{r}areas-we-cover/{k}/">Roofers in {v[0]}</a></li>' for k, v in COUNTIES.items())
            li += f'<li><a href="{r}{p}"{cur(p)}>{n} {ic("down")}</a><ul class="drop">{dd}<li><a href="{r}areas-we-cover/">All areas we cover</a></li></ul></li>'
        else:
            li += f'<li><a href="{r}{p}"{cur(p)}>{n}</a></li>'
    m = ""
    for i, (n, p) in enumerate(NAV):
        if n == "Services":
            sub = "".join(f'<a href="{r}our-services/{s["slug"]}/">{e(s["nav"])}</a>' for s in SERVICES)
            m += f'<details><summary>{n} <i>{i+1:02d} +</i></summary><div><a href="{r}{p}">All services</a>{sub}</div></details>'
        else:
            m += f'<a class="m1" href="{r}{p}">{n} <i>{i+1:02d}</i></a>'
    return top + f'''<header class="hdr"><div class="wrap">{brand}
<nav aria-label="Main"><ul class="nav">{li}</ul></nav>
<div class="hdr-cta"><a class="hdr-phone" href="tel:{TEL}" aria-label="Call {PHONE}">{ic("phone")} <span>{PHONE}</span></a><a class="btn btn-red hide-m" href="{r}contact-us/#quote">Get your quote</a>
<button class="burger" data-menu="open" aria-label="Open menu">{ic("menu")}</button></div></div></header>
<div class="mnav" id="mnav"><div class="mnav-top">{brand}<button class="burger" style="display:inline-flex" data-menu="close" aria-label="Close menu">{ic("x")}</button></div>
{m}<div class="btn-row"><a class="btn btn-red" href="{r}contact-us/#quote">Get your quote</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")} Call {PHONE}</a><a class="btn btn-wa" href="https://wa.me/{WA}">{ic("wa")} WhatsApp us</a></div></div>'''

def footer(r, lp=False):
    credit = '<a class="credit" href="https://almlabmarketing.com" target="_blank" rel="noopener">Website by <img src="https://almlabmarketing.com/almlab-credit.png" alt="AlmLab" loading="lazy"></a>'
    bot = f'<div class="f-bot"><span>© <span id="yr">2026</span> {e(NAME)}. All rights reserved. · VAT registered business · <a href="{r}privacy-policy/">Privacy policy</a></span>{credit}</div>'
    extras = f'''<a class="wa-fab" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp us">{ic("wa")}</a>
<div class="mbar"><a class="c" href="tel:{TEL}">{ic("phone")} Call</a><a class="w" href="https://wa.me/{WA}">{ic("wa")} WhatsApp</a><a class="q" href="{'#quote' if lp else r+'contact-us/#quote'}">Quote</a></div>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookies"><p>We use Google cookies to measure visits and how our ads perform. You can accept or decline. <a href="{r}privacy-policy/">Privacy policy</a></p><div class="btn-row" style="margin-top:12px"><button class="btn btn-ghost" data-consent="no">Decline</button><button class="btn btn-red" data-consent="yes">Accept</button></div></div>
{LB}<script src="{r}assets/site.js?v={V}" defer></script>'''
    if lp:
        return f'<footer class="ftr" style="padding-top:0"><div class="wrap">{bot.replace("margin-top:50px","")}</div></footer>' .replace('class="f-bot"','class="f-bot" style="margin-top:0;border-top:0"') + extras
    sv = "".join(f'<li><a href="{r}our-services/{s["slug"]}/">{e(s["nav"])}</a></li>' for s in SERVICES[:8])
    return f'''<footer class="ftr"><div class="wrap"><div class="cols">
<div class="f-brand"><img src="{r}assets/img/logo.webp" width="110" height="110" alt="{e(NAME)}" loading="lazy"><p>{e(NAME)} is your local choice for roofing, guttering and chimney work in Dublin, Kildare and Wicklow.</p>
<div class="soc"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ic("fb")}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ic("ig")}</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic("wa")}</a></div></div>
<div><h4>Services</h4><ul>{sv}<li><a href="{r}our-services/">All services</a></li></ul></div>
<div><h4>Explore</h4><ul><li><a href="{r}about-us/">About us</a></li><li><a href="{r}our-work/">Our work</a></li><li><a href="{r}reviews/">Reviews</a></li><li><a href="{r}areas-we-cover/">Areas we cover</a></li><li><a href="{r}areas-we-cover/dublin/">Roofers in Dublin</a></li><li><a href="{r}areas-we-cover/kildare/">Roofers in Kildare</a></li><li><a href="{r}areas-we-cover/wicklow/">Roofers in Wicklow</a></li><li><a href="{r}contact-us/">Contact us</a></li></ul></div>
<div><h4>Contact</h4><ul><li><a href="tel:{TEL}"><strong style="color:#fff;font-size:1.2rem">{PHONE}</strong></a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{ADDR}</li><li>24/7 emergency line</li></ul></div>
</div>{bot}</div></footer>''' + extras

PAGES = []  # (path, indexable)

def page(path, title, desc, body, lp=False, faqs=None, crumbs=None, index=True, body_attr="", ogimg="og.jpg"):
    depth = path.count("/")
    r = "../" * depth
    canon = DOMAIN + path
    ld = [{"@context":"https://schema.org","@type":"RoofingContractor","name":NAME,"url":DOMAIN,"telephone":TEL,"email":EMAIL,
           "image":DOMAIN+"assets/img/og.jpg","logo":DOMAIN+"assets/img/logo-512.png",
           "address":{"@type":"PostalAddress","streetAddress":"51 Bracken Road","addressLocality":"Dublin","postalCode":"D18 CV48","addressCountry":"IE"},
           "areaServed":["Dublin","Kildare","Wicklow"],"sameAs":[FB,IG]}]
    if faqs:
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]})
    if crumbs:
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":DOMAIN+p} for i,(n,p) in enumerate([("Home","")]+crumbs)]})
    doc = f'''<!doctype html>
<html lang="en-IE" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
{'<meta name="robots" content="noindex,follow">' if not index else ''}
<meta name="theme-color" content="#0d0d0f">
<meta property="og:type" content="website"><meta property="og:site_name" content="{e(NAME)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}assets/img/{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{r}assets/img/favicon-48.png"><link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,600;0,700;1,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css?v={V}">
<script>document.documentElement.className+=' js'</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body{' class="lp"' if lp else ''}{body_attr}>
<a class="skip" href="#main">Skip to content</a>
{header(r, path, lp)}
<main id="main">
{body(r)}
</main>
{footer(r, lp)}
</body>
</html>
'''
    out = os.path.join(HERE, path, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    PAGES.append((path, index))

def inner_hero(r, bg, eyebrow, h1, sub, crumbs, btns=True):
    cr = f'<a href="{r}">Home</a>' + "".join(f' <span>/</span> ' + (f'<a href="{r}{p}">{e(n)}</a>' if i < len(crumbs)-1 else f'<span>{e(n)}</span>') for i,(n,p) in enumerate(crumbs))
    b = f'<div class="btn-row"><a class="btn btn-red" href="#quote">Get your quote {ic("arrow")}</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")} {PHONE}</a></div>' if btns else ""
    return f'''<section class="hero inner"><img class="hero-bg" src="{r}assets/img/{bg}.webp" alt="" fetchpriority="high"><div class="hero-stripe"></div>
<div class="wrap"><div><nav class="crumbs" aria-label="Breadcrumb">{cr}</nav><span class="eyebrow">{e(eyebrow)}</span><h1>{h1}</h1><p class="sub">{sub}</p>{b}</div></div></section>'''

def why_block(r, pic="safeway-van", alt="Safeway Roofing & Chimneys van"):
    return f'''<section class="sec soft"><div class="wrap split flip"><div class="media rv">{img(r,pic,alt)}<div class="badge-f"><b>10 Year</b><span>Written guarantee</span></div></div>
<div class="rv"><span class="eyebrow">Why choose us</span><h2>Why choose <span class="red">Safeway</span> Roofing &amp; Chimneys</h2><p class="lead">{WHY_P}</p>{ticks(WHY,"light one")}
<div class="btn-row"><a class="btn btn-red" href="#quote">Get your quote {ic("arrow")}</a></div></div></div></section>'''

def quote_block(r, fid="quote", service="", h="Request a quote", p="Call, email or send the form and we will give you a clear quote suited to your property."):
    return f'''<section class="sec dark" id="quote-sec"><div class="wrap split"><div class="rv"><span class="eyebrow">Get in touch</span><h2>{h}</h2><p class="lead">{p}</p>
<ul class="contact-list" style="margin-top:26px"><li><span class="ic">{ic("phone")}</span><div><b>Phone, 24/7 emergency line</b><a href="tel:{TEL}">{PHONE}</a></div></li>
<li><span class="ic">{ic("mail")}</span><div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li><span class="ic">{ic("pin")}</span><div><b>Location</b><span style="color:#fff;font-weight:600">{ADDR}</span></div></li></ul></div>
<div class="rv">{form(r, fid, service=service)}</div></div></section>'''

# ------------------------------------------------------------------ pages
def home(r):
    areas_json = json.dumps(AREAS, ensure_ascii=False)
    mq = "".join(f"<span>{e(s['nav'])}</span>" for s in SERVICES) + "<span>Dublin · Kildare · Wicklow</span>"
    homegal = [f for f,_,_ in WORK[:10]]
    acols = "".join(f'<div class="acol rv"><h3>{ic("pin")} {k}</h3><ul class="chips">' + "".join(f"<li>{a}</li>" for a in v[:12]) + f'<li>+ more</li></ul></div>' for k, v in AREAS.items())
    return f'''<section class="hero"><img class="hero-bg" src="{r}assets/img/work-roofers-laying-underlay.webp" alt="" fetchpriority="high"><div class="hero-stripe"></div>
<div class="wrap"><div>
<span class="pill"><span class="stars">★★★★★</span> Trusted by homeowners in Dublin, Kildare &amp; Wicklow</span><br>
<span class="eyebrow">Roofing · Guttering · Chimneys</span>
<h1>Dependable roofing, guttering &amp; chimney care <span class="red">you can trust.</span></h1>
<p class="sub">{e(NAME)} looks after roofs, gutters and chimneys for homeowners across Dublin, Kildare and Wicklow. Expect prompt, tidy, fairly priced work from a fully insured team that keeps your home dry and secure.</p>
{ticks(["Fully insured team","10 year written guarantee","24/7 emergency line","Clear, upfront quotes"])}
<div class="btn-row"><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")} 24/7 Emergency: {PHONE}</a><a class="btn btn-ghost" href="{r}our-work/">View our work</a></div>
</div>
<div id="quote">{form(r,"hero-quote",title="Get your quote",sub="Tell us what is wrong and where you are. We will come back to you with a clear quote.",message=False)}</div>
</div></section>
<div class="mq" aria-hidden="true"><div class="mq-t">{mq}{mq}</div></div>

<section class="sec"><div class="wrap split"><div class="rv"><span class="eyebrow">Meet Safeway</span><h2>Roofing &amp; guttering help right when your home <span class="red">needs it.</span></h2>
<p class="lead">{e(NAME)} is a local roofing and chimney specialist covering Dublin, Kildare and Wicklow, with expertise in roofs, gutters and chimney repairs.</p>
<p>Our insured, experienced team handles new roofs, repairs, flat roofing, UPVC fascia and soffits, guttering and chimney work, always aiming for sturdy, weatherproof results that look great. Beyond the roof itself, we also take on ridge tile repointing, brick cleaning and repointing, and interior and exterior painting and decorating.</p>
<div class="grid g2" style="margin-top:26px"><div class="card"><div class="ic">{ic("shield")}</div><h3>Skilled &amp; insured</h3><p>Our insured, experienced crew delivers high-standard roofing, guttering and chimney work.</p></div>
<div class="card"><div class="ic">{ic("clock")}</div><h3>Quick to respond</h3><p>From sudden leaks to planned upgrades, we arrive on time and finish the job properly.</p></div></div>
<div class="btn-row"><a class="btn btn-line" href="{r}about-us/">More about us {ic("arrow")}</a></div></div>
<div class="media rv">{img(r,"safeway-van","Safeway Roofing & Chimneys van",sm=False)}<div class="badge-f"><b>10 Year</b><span>Written guarantee</span></div></div></div></section>

<section class="sec dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Our services</span><h2>Roofing, guttering &amp; chimney services for your home.</h2></div>
<a class="btn btn-ghost" href="{r}our-services/">View all services {ic("arrow")}</a></div>{scards(r, SERVICES[:8])}</div></section>

<section class="sec"><div class="wrap split"><div class="media rv">{img(r,"svc-drone-inspection","Drone inspecting a tiled roof",sm=False)}</div>
<div class="rv"><span class="eyebrow">Drone roof inspections</span><h2>See your roof <span class="red">before</span> we quote.</h2>
<p class="lead">We can send a drone up to check the whole roof, so you see exactly what needs doing, with no ladders and nothing missed.</p>
{ticks(["HD photos and video of your roof","Safe, ladder-free inspections","Accurate and detailed reports","Fast results with expert advice"],"light")}
<div class="btn-row"><a class="btn btn-red" href="{r}our-services/drone-roof-inspections/">Book your drone inspection {ic("arrow")}</a></div></div></div></section>

<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Recent work</span><h2>Recent Safeway projects.</h2></div><a class="btn btn-line" href="{r}our-work/">View our work {ic("arrow")}</a></div>
{gallery(r, homegal, numbered=True)}<p class="fnote" style="margin-top:16px">Tap a photo to see it full size.</p></div></section>

<section class="sec"><div class="wrap"><div class="sec-head center"><span class="eyebrow">How it works</span><h2>Three simple steps to a sound roof.</h2></div>
{steps_html([("Request your quote","Call, email or send the online form and we’ll give you a clear quote suited to your property."),("We assess the job","A member of our team looks over your roof, gutters or chimney and recommends the most sensible fix."),("Work done properly","We finish on schedule using quality materials, leaving your home secure, weatherproof and looking good.")])}</div></section>

<section class="sec soft"><div class="wrap split flip"><div class="media tall rv">{img(r,"work-white-fascia-soffit-gutter-house","New fascia, soffit and guttering fitted by Safeway",sm=False)}</div>
<div class="rv"><span class="eyebrow">Why Safeway</span><h2>Why Safeway Roofing &amp; Chimneys.</h2><p class="lead">{e(NAME)} covers roofing, guttering and chimney jobs throughout Dublin, Kildare and Wicklow. Our skilled, insured crew delivers dependable results that protect your home and improve its appearance.</p>
{ticks(["Qualified, fully insured tradespeople","Prompt response and punctual service","Quality materials for lasting results","Clear, upfront quotes with clear pricing","10 year written guarantee with every completed project","VAT registered business"],"light one")}
<div class="trust" style="margin-top:26px"><img src="{r}assets/img/guild-master-craftsmen.webp" alt="National Guild of Master Craftsmen" loading="lazy"><span style="font-weight:600;max-width:24ch">National Guild of Master Craftsmen</span></div>
<div class="btn-row"><a class="btn btn-red" href="{r}contact-us/#quote">Get your quote {ic("arrow")}</a></div></div></div></section>

<section class="sec dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Customer reviews</span><h2>What our customers say.</h2></div><a class="btn btn-ghost" href="{r}reviews/">Read more reviews {ic("arrow")}</a></div>{reviews_html()}</div></section>

<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Areas we cover</span><h2>Dublin, Kildare &amp; Wicklow.</h2></div>
<div><p style="margin:0;font-weight:600">Do we cover your area?</p><form class="acheck" data-area style="margin-top:8px"><input name="q" aria-label="Your town or area" placeholder="Type your town, e.g. Naas"><button class="btn btn-red" type="submit">Check</button></form><p class="acheck-out" aria-live="polite"></p></div></div>
<div class="acols">{acols}</div><div class="btn-row"><a class="btn btn-line" href="{r}areas-we-cover/">See every area we cover {ic("arrow")}</a></div>
<script type="application/json" id="area-data">{areas_json}</script></div></section>

<section class="sec soft"><div class="wrap"><div class="sec-head center"><span class="eyebrow">FAQ</span><h2>Frequently asked questions.</h2></div>{faq_html(HOME_FAQ)}</div></section>
{cta_band(r)}'''

def about(r):
    return inner_hero(r,"safeway-van","About us","Dependable roofing, guttering &amp; chimney specialists.","Looking after roofs, gutters and chimneys for homeowners across Dublin, Kildare and Wicklow.",[("About Us","about-us/")]) + f'''
<section class="sec"><div class="wrap split"><div class="rv"><span class="eyebrow">Who we are</span><h2>Tidy, careful work on <span class="red">every job.</span></h2>
<p class="lead">{e(NAME)} looks after roofs, gutters and chimneys for homeowners in Dublin, Kildare and Wicklow.</p>
<p>Our insured crew takes pride in tidy, careful work on every job, from new roofs and repairs to flat roofing, UPVC gutters, fascia and soffits, and chimney work.</p>
<p>We also handle ridge tile repointing, brick cleaning and repointing, and painting and decorating inside and out.</p>
<p>Every quote is clear and upfront, so you know exactly where you stand before we start.</p>
<div class="btn-row"><a class="btn btn-red" href="#quote">Get your quote {ic("arrow")}</a><a class="btn btn-line" href="{r}our-work/">See our work</a></div></div>
<div class="media rv">{img(r,"safeway-van","Safeway Roofing & Chimneys van",sm=False)}<div class="badge-f"><b>10 Year</b><span>Written guarantee</span></div></div></div></section>
<section class="sec dark"><div class="wrap split flip"><div class="media rv">{img(r,"work-roofers-laying-underlay","Safeway crew laying roof underlay",sm=False)}</div>
<div class="rv"><span class="eyebrow">Our aim</span><h2>Keep your home dry, safe and well looked after.</h2>
<p class="lead">Our aim at {e(NAME)} is simple: keep your home dry, safe and well looked after.</p>
<p>We build every job to last, paying close attention to safety, detail and a clean finish. Good materials and careful workmanship mean results that stand up to Irish weather.</p>
<p>We want to be the first call homeowners across Dublin, Kildare and Wicklow make when their roof, guttering or chimney needs attention.</p></div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head center"><span class="eyebrow">How it works</span><h2>From first call to finished job.</h2></div>
{steps_html([("Request a quote","Call, email or use our online form and we will arrange a clear quote to suit your property."),("Careful inspection","We inspect your roof, gutters or chimney properly, then talk you through the best option and a clear price."),("Prompt, tidy work","The job is finished on schedule with quality materials, leaving your home secure, weatherproof and looking its best.")])}</div></section>
{why_block(r,"work-gable-chimney-fascia-gutter","Finished gable, chimney and roofline")}
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Customer reviews</span><h2>What our customers say.</h2></div></div>{reviews_html()}</div></section>
{quote_block(r)}'''

def services_index(r):
    return inner_hero(r,"work-underlay-battens-new-roof","Our services","Roofing, guttering &amp; chimney services for your home.","Everything from a slipped slate to a full new roof, carried out by one fully insured team across Dublin, Kildare and Wicklow.",[("Our Services","our-services/")]) + f'''
<section class="sec"><div class="wrap">{scards(r, SERVICES)}</div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">More of what we do</span><h2>If it is on your roof, we can help.</h2></div></div>
<ul class="list2">{"".join(f"<li>{e(m)}</li>" for m in MORE)}</ul></div></section>
{quote_block(r)}'''

def service_page(s):
    def body(r):
        others = [x for x in SERVICES if x["slug"] != s["slug"]]
        i = SERVICES.index(s); rel = [SERVICES[(i+k) % len(SERVICES)] for k in (1,2,3,4)]
        return inner_hero(r, s["img"], s["name"], s["h1"].replace("&","&amp;"), e(s["short"]) + " Fully insured, with a 10 year written guarantee on every completed project.", [("Our Services","our-services/"),(s["name"],"")]) + f'''
<section class="sec"><div class="wrap split"><div class="rv"><span class="eyebrow">{e(s["name"])}</span><h2>{e(s["nav"])} done <span class="red">properly.</span></h2>
{"".join(f'<p{" class=lead" if k==0 else ""}>{p}</p>' for k,p in enumerate(s["intro"]))}
<div class="btn-row"><a class="btn btn-red" href="#quote">Get your quote {ic("arrow")}</a><a class="btn btn-line" href="tel:{TEL}">{ic("phone")} {PHONE}</a></div></div>
<div class="media rv">{img(r,s["img"],s["name"]+" by Safeway Roofing & Chimneys",sm=False)}</div></div></section>
<section class="sec dark"><div class="wrap"><div class="sec-head center"><span class="eyebrow">How it works</span><h2>{e(s["proc"])}</h2></div>{steps_html(s["steps"])}</div></section>
{why_block(r)}
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Recent work</span><h2>Recent Safeway projects.</h2></div><a class="btn btn-line" href="{r}our-work/">See all projects {ic("arrow")}</a></div>
{gallery(r, s["gal"], cls="g3c" if len(s["gal"])==3 else "")}</div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Common questions</span><h2>{e(s["nav"])}: your questions answered.</h2></div>{faq_html(s["faqs"])}</div></section>
{quote_block(r, service=s["name"], h="Request a quote")}
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">More services</span><h2>Other ways we can help.</h2></div><a class="btn btn-line" href="{r}our-services/">All services {ic("arrow")}</a></div>{scards(r, rel, numbered=False)}</div></section>'''
    return body

def work(r):
    f = "".join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if k=="all" else "false"}">{e(n)}</button>' for k,n in CATS)
    return inner_hero(r,"work-breathable-membrane-battens-tiles","Our work","Recent Safeway projects.","Real jobs from around Dublin, Kildare and Wicklow: re-roofs, repairs, chimneys, flat roofs and new roofline.",[("Our Work","our-work/")],btns=False) + f'''
<section class="sec"><div class="wrap"><div class="filters" role="group" aria-label="Filter photos">{f}</div>{gallery(r,[x for x,_,_ in WORK])}
<p class="fnote" style="margin-top:16px">Tap a photo to see it full size.</p></div></section>
{cta_band(r,"Want your roof to look like this?","Send us a few photos or tell us what is wrong and we will come back with a clear quote.")}'''

def areas(r):
    cols = "".join(f'<div class="acol rv"><h3>{ic("pin")} {k}</h3><ul class="chips">' + "".join(f"<li>{a}</li>" for a in v) + '</ul></div>' for k, v in AREAS.items())
    cards = "".join(f'<a class="scard rv" style="aspect-ratio:4/3" href="{r}areas-we-cover/{k}/">{img(r,v[2],"Roofers in "+v[0])}<div class="sc-b"><h3>Roofers in {v[0]}</h3><span class="go">View area {ic("arrow")}</span></div></a>' for k,v in COUNTIES.items())
    return inner_hero(r,"work-house-scaffold-tower-ladders","Areas we cover","Roofing, guttering &amp; chimney work across Dublin, Kildare &amp; Wicklow.","Based in Dublin 18 and on the road every day across all three counties.",[("Areas We Cover","areas-we-cover/")]) + f'''
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Do we cover you?</span><h2>Check your area.</h2></div>
<div><form class="acheck" data-area><input name="q" aria-label="Your town or area" placeholder="Type your town, e.g. Greystones"><button class="btn btn-red" type="submit">Check</button></form><p class="acheck-out" aria-live="polite"></p></div></div>
<div class="acols">{cols}</div><script type="application/json" id="area-data">{json.dumps(AREAS, ensure_ascii=False)}</script>
<p style="margin-top:24px;color:var(--muted)">Not on the list? We may still cover you. Ring <a href="tel:{TEL}"><strong>{PHONE}</strong></a> and ask.</p></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">By county</span><h2>Find your local roofers.</h2></div></div><div class="grid g3">{cards}</div></div></section>
{quote_block(r)}'''

def county_page(key):
    name, groups, pic, text = COUNTIES[key]
    def body(r):
        cols = "".join(f'<div class="acol rv"><h3>{ic("pin")} {g}</h3><ul class="chips">' + "".join(f"<li>{a}</li>" for a in AREAS[g]) + '</ul></div>' for g in groups)
        return inner_hero(r,pic,f"Areas we cover · {name}",f"Roofers in {name}: roofing, guttering &amp; chimney repairs.",f"Fully insured, with a 10 year written guarantee on every completed project and a 24/7 emergency line.",[("Areas We Cover","areas-we-cover/"),(name,"")]) + f'''
<section class="sec"><div class="wrap split"><div class="rv"><span class="eyebrow">Local to {name}</span><h2>Your roofing team in <span class="red">{name}.</span></h2><p class="lead">{text}</p>
{ticks(WHY,"light one")}<div class="btn-row"><a class="btn btn-red" href="#quote">Get your quote {ic("arrow")}</a><a class="btn btn-line" href="tel:{TEL}">{ic("phone")} {PHONE}</a></div></div>
<div class="media rv">{img(r,pic,"Safeway Roofing & Chimneys at work in "+name,sm=False)}<div class="badge-f"><b>10 Year</b><span>Written guarantee</span></div></div></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Towns we cover</span><h2>Where we work in {name}.</h2></div></div><div class="acols" style="grid-template-columns:repeat({len(groups)},1fr)">{cols}</div></div></section>
<section class="sec dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Our services in {name}</span><h2>What we can do for your home.</h2></div><a class="btn btn-ghost" href="{r}our-services/">All services {ic("arrow")}</a></div>{scards(r, SERVICES[:8])}</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Customer reviews</span><h2>What our customers say.</h2></div></div>{reviews_html()}</div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head center"><span class="eyebrow">FAQ</span><h2>Common questions.</h2></div>{faq_html(HOME_FAQ)}</div></section>
{quote_block(r, h=f"Request a quote in {name}")}'''
    return body

def reviews(r):
    return inner_hero(r,"work-white-fascia-soffit-gutter-house","Reviews","What our customers say.","Homeowners across Dublin, Kildare and Wicklow on the work we have done for them.",[("Reviews","reviews/")],btns=False) + f'''
<section class="sec"><div class="wrap">{reviews_html(4,"g2")}
<div class="card" style="margin-top:26px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap"><div><h3>Had work done by Safeway?</h3><p>We would love to hear how it went. Leave us a review or message us on Facebook or Instagram.</p></div>
<div class="btn-row" style="margin:0"><a class="btn btn-line" href="{FB}" target="_blank" rel="noopener">{ic("fb")} Facebook</a><a class="btn btn-line" href="{IG}" target="_blank" rel="noopener">{ic("ig")} Instagram</a></div></div></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">The work behind the words</span><h2>See the jobs for yourself.</h2></div><a class="btn btn-line" href="{r}our-work/">View our work {ic("arrow")}</a></div>{gallery(r,[x for x,_,_ in WORK[:8]])}</div></section>
{quote_block(r)}'''

CONTACT_FAQ = [
 ("How much will a new roof cost?","The price depends on the size of your roof, the materials you choose and how complex the job is. Get in touch and we will arrange a clear quote for your home."),
 ("Can you attend urgent roof or gutter problems?","Yes. We respond quickly to leaks, damaged gutters and chimney problems across Dublin, Kildare and Wicklow, and make the area safe and weather-tight."),
 ("Do you offer quotes and inspections?","Yes. We will look at your roof, gutters or chimney and give you a clear quote. Get in touch to arrange a visit."),
 ("Are you insured and do you stand behind your work?","Yes. Safeway Roofing & Chimneys is fully insured and every job is completed to a high standard that we are happy to stand behind."),
]
def contact(r):
    return inner_hero(r,"safeway-van","Contact us","Get in touch.","Call, WhatsApp, email or send the form. For urgent leaks, ring our 24/7 emergency line.",[("Contact Us","contact-us/")],btns=False) + f'''
<section class="sec" id="quote-sec"><div class="wrap split" style="align-items:start"><div class="rv"><span class="eyebrow">Contact details</span><h2>Talk to <span class="red">Safeway.</span></h2>
<ul class="contact-list" style="margin-top:20px"><li><span class="ic">{ic("phone")}</span><div><b>Phone number · 24/7 emergency</b><a href="tel:{TEL}">{PHONE}</a></div></li>
<li><span class="ic">{ic("wa")}</span><div><b>WhatsApp</b><a href="https://wa.me/{WA}" target="_blank" rel="noopener">Send us a photo of the job</a></div></li>
<li><span class="ic">{ic("mail")}</span><div><b>Email address</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li><span class="ic">{ic("pin")}</span><div><b>Location</b><span style="font-weight:700;font-size:1.1rem">{ADDR}</span></div></li></ul>
<iframe class="map" title="Map showing Safeway Roofing & Chimneys, 51 Bracken Road, Dublin 18" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=51+Bracken+Road,+Sandyford,+Dublin+D18+CV48&output=embed"></iframe></div>
<div class="rv" id="quote">{form(r,"contact-quote")}</div></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Common questions</span><h2>Before you get in touch.</h2></div>{faq_html(CONTACT_FAQ)}</div></section>'''

def privacy(r):
    return inner_hero(r,"work-black-fascia-gable-dry-verge","Legal","Privacy policy.","What information we collect through this website, how we use it and the choices you have.",[("Privacy Policy","privacy-policy/")],btns=False) + f'''
<section class="sec"><div class="wrap prose">
<h2>1. Who we are</h2><p>{e(NAME)} (“we”, “us”, “our”) provides roofing, guttering, chimney and related exterior services across Dublin, Kildare, Wicklow and surrounding areas. We are the data controller for personal information collected through this website.</p>
<p><strong>Contact:</strong> {e(NAME)}, {ADDR}. Phone: <a href="tel:{TEL}">{PHONE}</a>. Email: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>2. Information we collect</h2><ul><li><strong>Details you give us:</strong> your name, phone number, area and a description of the work you need, when you use our quote form, call, email or message us.</li>
<li><strong>Project information:</strong> photos, measurements, inspection notes and job details created while providing a quote or service.</li>
<li><strong>Technical data:</strong> the page you sent a form from and, if you arrived from an advert, the advert reference (for example a Google click ID). With your consent, cookies also record device and usage information.</li></ul>
<h2>3. How we use your information</h2><ul><li>To reply to your enquiry and prepare a quote</li><li>To schedule, carry out and manage work you have booked, including emergency call-outs</li><li>To issue invoices and guarantees and keep accounting records</li><li>To contact you about your project, including follow-up and aftercare</li><li>To understand which pages and adverts lead to enquiries, where you have consented</li><li>To meet our legal, tax and insurance obligations</li></ul>
<p>We do not sell your personal data, and we do not use it for unrelated marketing without your consent.</p>
<h2>4. Legal basis for processing</h2><p>Under data protection law (including the GDPR) we rely on: <strong>contract</strong> (to provide a quote or carry out work you request), <strong>legitimate interests</strong> (to run and secure our business and respond to enquiries), <strong>legal obligation</strong> (accounting, tax and insurance records) and <strong>consent</strong> (for optional cookies). Where we rely on consent, you can withdraw it at any time.</p>
<h2>5. Quote forms</h2><p>Details you submit through our forms are sent to us by email through a form delivery provider (FormSubmit) so we can respond. We use them only to deal with your request and to follow up on it.</p>
<h2>6. WhatsApp and phone contact</h2><p>If you contact us by phone or WhatsApp, we keep the details you share (such as your number and messages) only to respond and manage your enquiry or project. WhatsApp is operated by a third party and is subject to its own privacy policy.</p>
<h2>7. Cookies and advertising</h2><p>This website does not need cookies to work. If you accept the cookie notice, Google cookies are used to measure visits and to tell us when an advert led to an enquiry. If you decline, those cookies are not set. You can change your mind by clearing this site’s data in your browser. Fonts are loaded from Google Fonts and the map on our contact page is provided by Google Maps; both are subject to Google’s privacy policy.</p>
<h2>8. Sharing your information</h2><p>We only share personal data with trusted providers who help us run our business, for example website hosting, email and form services, accountants and insurers, and where we are required to by law. Some providers may process data outside the European Economic Area; where this happens we take reasonable steps to make sure appropriate safeguards are in place.</p>
<h2>9. Data retention</h2><p>We keep personal data only for as long as needed for the purposes above. Enquiry details are kept for as long as needed to deal with your request and for a reasonable period afterwards. Job, invoice and guarantee records are kept for the periods required by tax, accounting and warranty rules.</p>
<h2>10. Your rights</h2><p>You have the right to access the personal data we hold about you, have inaccurate data corrected, have your data deleted, restrict or object to our processing, receive your data in a portable format and withdraw consent at any time. To exercise any of these rights, contact us using the details above. We will respond within one month. You can also complain to the Data Protection Commission (dataprotection.ie).</p>
<h2>11. Security</h2><p>We take reasonable technical and organisational steps to protect your personal data. No method of transmission over the internet is completely secure, so we cannot guarantee absolute security.</p>
<h2>12. Children</h2><p>Our website and services are directed at adults. We do not knowingly collect personal data from anyone under 16.</p>
<h2>13. Changes to this policy</h2><p>We may update this policy from time to time. The latest version will always be on this page.</p><p><em>Last updated: November 2026</em></p>
</div></section>'''

def thanks(r):
    return f'''<section class="hero inner"><img class="hero-bg" src="{r}assets/img/safeway-van.webp" alt=""><div class="hero-stripe"></div><div class="wrap"><div>
<span class="eyebrow">Quote request sent</span><h1>Thanks, we have <span class="red">your details.</span></h1>
<p class="sub">We will be in touch shortly about your quote. If water is coming in right now, do not wait: ring our 24/7 emergency line.</p>
<div class="btn-row"><a class="btn btn-red" href="tel:{TEL}">{ic("phone")} Call {PHONE}</a><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{ic("wa")} Send photos on WhatsApp</a><a class="btn btn-ghost" href="{r}our-work/">See our recent work</a></div></div></div></section>'''

# --- Google Ads landing pages ---
def LP(slug, kw, h1, sub, service, bg, bullets, cards, gal, faqs, title, desc):
    return dict(slug=slug, kw=kw, h1=h1, sub=sub, service=service, bg=bg, bullets=bullets, cards=cards, gal=gal, faqs=faqs, title=title, desc=desc)
G = "10 year written guarantee"
LPS = [
 LP("roof-repairs-dublin","Roof repairs Dublin","Roof repairs in Dublin, <span class='red'>done properly.</span>","Leaks, slipped slates, broken tiles, flashing and storm damage fixed by a fully insured local team. Clear quote before any work starts.","Roof Repairs","work-underlay-patch-roof-repair",
    ["Fully insured team",G,"Clear, upfront quotes","24/7 emergency line"],
    [("tool","Leaks found and fixed","We inspect the roof to find where the water is getting in, then repair that, not just the stain."),("doc","Clear quote first","You get a clear repair quote with no obligation before anything starts."),("shield","Repairs that last","Quality materials and proven methods, backed by our written guarantee.")],
    SVC["roof-repairs"]["gal"], SVC["roof-repairs"]["faqs"],
    "Roof Repairs Dublin | Fully Insured, 10 Year Guarantee | Safeway Roofing","Roof repairs in Dublin from a fully insured local team. Leaks, slates, tiles and flashing fixed. Request your quote or call 087 485 8556."),
 LP("emergency-roof-repairs","Emergency roof repairs","Emergency roof repairs. <span class='red'>Call us 24/7.</span>","Water coming in or storm damage? Ring now. We respond quickly across Dublin, Kildare and Wicklow and make the area safe and weather-tight.","Emergency repair","work-roof-strip-out-chimney-insulation",
    ["24/7 emergency line","Quick response","Fully insured team","Dublin, Kildare & Wicklow"],
    [("clock","Quick to respond","From sudden leaks to storm damage, we arrive on time and get the roof weather-tight."),("tool","Proper repair to follow","Once your home is safe we quote clearly for the lasting repair."),("shield","Insured and guaranteed","Fully insured, with a 10 year written guarantee on every completed project.")],
    ["work-underlay-patch-roof-repair","work-hip-end-tiles-mortar-flashing","work-roof-relay-before-after-02","work-chimney-stack-lead-flashing-01"], [HOME_FAQ[1]]+SVC["roof-repairs"]["faqs"][:2],
    "Emergency Roof Repairs Dublin | 24/7 Line | Safeway Roofing","Emergency roof repairs across Dublin, Kildare and Wicklow. Leaks and storm damage made safe fast by a fully insured team. Call 087 485 8556."),
 LP("chimney-repairs-dublin","Chimney repairs Dublin","Chimney repairs in Dublin you can <span class='red'>rely on.</span>","Cracked brickwork, crumbling mortar, leaking flashing and unsafe stacks repaired by a fully insured team.","Chimney Repairs","svc-chimney-repairs",
    ["Fully insured team",G,"Lead flashing & repointing","Clear, upfront quotes"],
    [("home","Sound and safe","We repair cracks, damaged brickwork and structural problems so the stack is secure."),("tool","Leaks stopped","Properly sealed flashing, brickwork and mortar keep water out."),("doc","Clear quote first","We inspect, pinpoint the problems and quote with no obligation.")],
    SVC["chimney-repairs"]["gal"], SVC["chimney-repairs"]["faqs"],
    "Chimney Repairs Dublin | Fully Insured | Safeway Roofing & Chimneys","Chimney repairs in Dublin: brickwork, repointing, lead flashing and leaks. Fully insured with a 10 year written guarantee. Call 087 485 8556."),
 LP("flat-roofs-dublin","Flat roofing Dublin","Flat roofs in Dublin that stay <span class='red'>watertight.</span>","New flat roofs and repairs in felt, fibreglass and single-ply rubber for extensions, garages, dormers and garden rooms.","Flat Roofs","svc-flat-roofs",
    ["Felt, fibreglass & rubber",G,"Fully insured team","Clear, upfront quotes"],
    [("home","Extensions to garden rooms","Flat roofs installed, repaired and maintained on homes and commercial buildings."),("tool","The right system","We recommend the best option for your property and budget."),("shield","Built to last","Correct waterproofing, good drainage and quality materials keep water out.")],
    SVC["flat-roofs"]["gal"], SVC["flat-roofs"]["faqs"],
    "Flat Roofing Dublin | Repairs & New Flat Roofs | Safeway Roofing","Flat roof repairs and new flat roofs in Dublin. Felt, fibreglass and rubber systems from a fully insured team. Call 087 485 8556."),
 LP("gutters-fascia-soffits","Gutters, fascia & soffits","New gutters, fascia &amp; soffits, <span class='red'>neatly fitted.</span>","Leaking, sagging or rotten roofline replaced with low-maintenance UPVC in black or white, across Dublin, Kildare and Wicklow.","UPVC Gutter Installation","svc-gutters",
    ["Black or white UPVC",G,"Fully insured team","Most jobs done in 1 to 2 days"],
    [("home","Protects your walls","Rainwater is carried cleanly away from your property."),("tool","Repairs or full replacement","We fix leaks, replace damaged sections or fit a complete new system."),("shield","Low maintenance","UPVC is durable, weatherproof and does not corrode.")],
    ["work-white-fascia-soffit-gutter-house","work-black-fascia-gutter-downpipes-house","work-black-fascia-soffit-corner","work-white-fascia-gutter-brick-house-ladder"], SVC["upvc-gutter-installation"]["faqs"][:2]+SVC["upvc-fascia-soffits"]["faqs"][:2],
    "Gutters, Fascia & Soffits Dublin | UPVC Fitted | Safeway Roofing","UPVC gutters, fascia and soffits supplied and fitted in Dublin, Kildare and Wicklow by a fully insured team. Call 087 485 8556."),
 LP("new-roof-dublin","New roofs & re-roofing","A new roof, <span class='red'>built to last.</span>","Full re-roofs and new roofs in slate and tile, with breathable membrane, new battens and UPVC roofline to finish.","New Roof Installation","svc-new-roof",
    [G,"Fully insured team","Slate, tile & flat roofs","Clear, upfront quotes"],
    [("doc","Survey and clear quote","We look over your property and give you a clear quote with no obligation."),("home","Careful installation","Our experienced crew fits your new roof safely and efficiently."),("shield","Guaranteed in writing","Every completed project comes with a 10 year written guarantee.")],
    SVC["new-roof-installation"]["gal"], SVC["new-roof-installation"]["faqs"],
    "New Roofs & Re-Roofing Dublin | 10 Year Guarantee | Safeway Roofing","New roofs and re-roofs in Dublin, Kildare and Wicklow. Slate, tile and flat roofs from a fully insured team. Call 087 485 8556."),
 LP("roof-cleaning","Roof cleaning","Roof cleaning &amp; <span class='red'>moss removal.</span>","Moss, algae and grime cleared safely from tile, slate and flat roofs across Dublin, Kildare and Wicklow.","Roof Cleaning","svc-roof-cleaning",
    ["Safe methods for your tiles","Fully insured team","Gutters left clear","Clear, upfront quotes"],
    [("home","Looks like new","Clearing moss and staining lifts the look of the whole house."),("tool","Protects the roof","Regular cleaning helps prevent water damage, blocked gutters and early wear."),("shield","Done safely","Safe, professional methods designed to protect slate, tile and flat roofs.")],
    SVC["roof-cleaning"]["gal"]+["work-ridge-tiles-red-mortar"], SVC["roof-cleaning"]["faqs"],
    "Roof Cleaning & Moss Removal Dublin | Safeway Roofing","Roof cleaning and moss removal in Dublin, Kildare and Wicklow from a fully insured team. Request your quote or call 087 485 8556."),
 LP("roofers-kildare","Roofers Kildare","Roofers in Kildare for repairs, gutters &amp; <span class='red'>chimneys.</span>","From Maynooth, Leixlip and Celbridge to Naas, Newbridge and Athy. Fully insured, with a clear quote before any work starts.","","work-white-fascia-soffit-gutter-house",
    ["Fully insured team",G,"24/7 emergency line","Clear, upfront quotes"],
    [("tool","Repairs to full re-roofs","Leaks, slates, tiles, flat roofs and complete new roofs."),("home","Roofline and chimneys","UPVC gutters, fascia and soffits, plus chimney repairs and lead work."),("shield","Guaranteed in writing","Every completed project comes with a 10 year written guarantee.")],
    ["work-roofers-laying-underlay","work-white-fascia-soffit-gutter-house","work-chimney-stack-lead-flashing-01","work-roof-relay-before-after-01"], HOME_FAQ,
    "Roofers Kildare | Roof Repairs, Gutters & Chimneys | Safeway Roofing","Roofers covering Naas, Newbridge, Maynooth, Celbridge and all of Kildare. Fully insured with a 10 year written guarantee. Call 087 485 8556."),
 LP("roofers-wicklow","Roofers Wicklow","Roofers in Wicklow for repairs, gutters &amp; <span class='red'>chimneys.</span>","From Bray and Greystones to Wicklow Town, Arklow and Blessington. Fully insured, with a clear quote before any work starts.","","work-gable-chimney-fascia-gutter",
    ["Fully insured team",G,"24/7 emergency line","Clear, upfront quotes"],
    [("tool","Repairs to full re-roofs","Leaks, slates, tiles, flat roofs and complete new roofs."),("home","Roofline and chimneys","UPVC gutters, fascia and soffits, plus chimney repairs and lead work."),("shield","Guaranteed in writing","Every completed project comes with a 10 year written guarantee.")],
    ["work-gable-chimney-fascia-gutter","work-underlay-battens-new-roof","work-chimney-lead-flashing-slate-roof","work-roof-relay-before-after-03"], HOME_FAQ,
    "Roofers Wicklow | Roof Repairs, Gutters & Chimneys | Safeway Roofing","Roofers covering Bray, Greystones, Wicklow Town, Arklow and all of Wicklow. Fully insured with a 10 year written guarantee. Call 087 485 8556."),
]
def lp_page(L):
    def body(r):
        cards = "".join(f'<div class="card rv"><div class="ic">{ic(i)}</div><h3>{e(t)}</h3><p>{e(p)}</p></div>' for i,t,p in L["cards"])
        strip = "".join(f"<li>{ic('check')} {e(b)}</li>" for b in L["bullets"])
        return f'''<section class="hero"><img class="hero-bg" src="{r}assets/img/{L["bg"]}.webp" alt="" fetchpriority="high"><div class="hero-stripe"></div>
<div class="wrap"><div><span class="pill"><span class="stars">★★★★★</span> Trusted by homeowners in Dublin, Kildare &amp; Wicklow</span><br>
<span class="eyebrow">{e(L["kw"])}</span><h1>{L["h1"]}</h1><p class="sub">{e(L["sub"])}</p>{ticks(L["bullets"])}
<div class="btn-row"><a class="btn btn-red" href="tel:{TEL}">{ic("phone")} Call {PHONE}</a><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{ic("wa")} WhatsApp a photo</a></div></div>
<div id="quote">{form(r,"lp-"+L["slug"],title="Get your quote",sub="Fill this in and we will come back to you with a clear, no-obligation quote.",service=L["service"],message=False,h="h2")}</div></div></section>
<div class="lp-strip"><div class="wrap"><ul>{strip}</ul></div></div>
<section class="sec"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Why homeowners call Safeway</span><h2>Prompt, tidy, fairly priced work.</h2></div><div class="grid g3">{cards}</div></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Recent work</span><h2>Recent Safeway projects.</h2></div></div>{gallery(r, L["gal"], cls="g3c" if len(L["gal"])==3 else "")}</div></section>
<section class="sec dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Customer reviews</span><h2>What our customers say.</h2></div></div>{reviews_html()}</div></section>
<section class="sec"><div class="wrap"><div class="sec-head center"><span class="eyebrow">How it works</span><h2>Three simple steps.</h2></div>
{steps_html([("Request your quote","Call, WhatsApp or send the form and tell us what is wrong."),("We assess the job","We look over your roof, gutters or chimney and recommend the most sensible fix, with a clear price."),("Work done properly","We finish on schedule using quality materials, leaving your home secure and weatherproof.")])}</div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Common questions</span><h2>Good to know.</h2></div>{faq_html(L["faqs"])}</div></section>
{cta_band(r).replace(r+"contact-us/#quote","#quote")}'''
    return body

# ------------------------------------------------------------------ build
page("", "Roofing, Guttering & Chimney Repairs Dublin | Safeway Roofing & Chimneys",
     "Safeway Roofing & Chimneys: roof repairs, new roofs, flat roofs, gutters, fascia and chimney repairs across Dublin, Kildare and Wicklow. Fully insured. 10 year written guarantee. Call 087 485 8556.",
     home, faqs=HOME_FAQ)
page("about-us/", "About Us | Safeway Roofing & Chimneys, Dublin", "Meet Safeway Roofing & Chimneys: a fully insured local team looking after roofs, gutters and chimneys across Dublin, Kildare and Wicklow.", about, crumbs=[("About Us","about-us/")])
page("our-services/", "Roofing, Guttering & Chimney Services | Safeway Roofing & Chimneys", "New roofs, roof repairs, flat roofs, UPVC gutters, fascia and soffits, chimney repairs, roof cleaning and more across Dublin, Kildare and Wicklow.", services_index, crumbs=[("Our Services","our-services/")])
for s in SERVICES:
    p = f"our-services/{s['slug']}/"
    page(p, f"{s['name']} Dublin, Kildare & Wicklow | Safeway Roofing", s["meta"], service_page(s), faqs=s["faqs"], crumbs=[("Our Services","our-services/"),(s["name"],p)])
page("our-work/", "Our Work | Recent Roofing Projects | Safeway Roofing & Chimneys", "Photos of recent Safeway Roofing & Chimneys projects: re-roofs, roof repairs, chimneys, flat roofs, fascia, soffits and gutters.", work, crumbs=[("Our Work","our-work/")])
page("areas-we-cover/", "Areas We Cover | Dublin, Kildare & Wicklow | Safeway Roofing", "Safeway Roofing & Chimneys covers North and South Dublin, Kildare and Wicklow. Check your town and request a quote.", areas, crumbs=[("Areas We Cover","areas-we-cover/")])
for k, v in COUNTIES.items():
    p = f"areas-we-cover/{k}/"
    page(p, f"Roofers {v[0]} | Roof Repairs, Gutters & Chimneys | Safeway Roofing", f"Roofers in {v[0]}: roof repairs, new roofs, flat roofs, gutters, fascia and chimney repairs. Fully insured with a 10 year written guarantee. Call 087 485 8556.", county_page(k), faqs=HOME_FAQ, crumbs=[("Areas We Cover","areas-we-cover/"),(v[0],p)])
page("reviews/", "Reviews | Safeway Roofing & Chimneys", "What homeowners across Dublin, Kildare and Wicklow say about Safeway Roofing & Chimneys.", reviews, crumbs=[("Reviews","reviews/")])
page("contact-us/", "Contact Us | Get Your Quote | Safeway Roofing & Chimneys", "Contact Safeway Roofing & Chimneys on 087 485 8556 or request a quote online. 24/7 emergency line for Dublin, Kildare and Wicklow.", contact, faqs=CONTACT_FAQ, crumbs=[("Contact Us","contact-us/")])
page("privacy-policy/", "Privacy Policy | Safeway Roofing & Chimneys", "How Safeway Roofing & Chimneys collects, uses and protects your personal information.", privacy, crumbs=[("Privacy Policy","privacy-policy/")])
page("thank-you/", "Thank You | Safeway Roofing & Chimneys", "Your quote request has been sent to Safeway Roofing & Chimneys.", thanks, index=False, body_attr=" data-thanks")
for L in LPS:
    page(f"lp/{L['slug']}/", L["title"], L["desc"], lp_page(L), lp=True, faqs=L["faqs"], index=False)

today = datetime.date.today().isoformat()
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{DOMAIN}{p}</loc><lastmod>{today}</lastmod></url>\n" for p, idx in PAGES if idx) + "</urlset>\n"
open(os.path.join(HERE, "sitemap.xml"), "w").write(sm)
open(os.path.join(HERE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}sitemap.xml\n")
print(f"built {len(PAGES)} pages")
