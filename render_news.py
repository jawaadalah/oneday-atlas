#!/usr/bin/env python3
"""Render Tuesday 24 November 2026 world-news collage, 1024x1024 PNG.
Original work for make.fun news-image-20261124. Stories sourced from
public news digests of 24 Nov 2026 (Just Security Early Edition, The
Global Eye, Horizon, IQMIA). No copied artwork; all text drawn here."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (10, 25, 49); ORANGE = (255, 122, 0); PAPER = (250, 247, 240)
INK = (18, 18, 18); GREY = (90, 90, 90); RED = (178, 34, 34)
REGION_COLORS = {
    "MIDDLE EAST": (178, 34, 34), "EUROPE": (25, 80, 160),
    "ASIA": (0, 128, 96), "AFRICA": (150, 90, 10),
    "AMERICAS": (90, 40, 140), "TECH": (10, 90, 140), "WORLD": (70, 70, 70),
}
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FBO = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, width):
    words = text.split(); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 96], fill=NAVY)
d.text((24, 14), "THE WORLD IN ONE DAY", font=font(FB, 40), fill=(255, 255, 255))
d.text((24, 62), "Tuesday 24 November 2026  \u00b7  27 stories, 7 regions, one day",
       font=font(FR, 19), fill=(255, 200, 140))
d.rectangle([0, 96, W, 100], fill=ORANGE)

LEAD = ("US\u2013IRAN STANDOFF DEEPENS",
        "Washington meets Qatar as Tehran vows to fight the naval blockade",
        "MIDDLE EAST")
# Lead block
y = 112
d.text((24, y), LEAD[0], font=font(FBO, 34), fill=INK)
y += 46
for ln in wrap(d, LEAD[1], font(FR, 19), 976):
    d.text((24, y), ln, font=font(FR, 19), fill=GREY); y += 26
y += 8
d.line([24, y, 1000, y], fill=(200, 200, 200), width=2)
y += 12

STORIES = [
 ("MIDDLE EAST", "Gaza strikes kill Hamas security chief", "Israeli airstrikes kill Naeem Abu Nahel and six others, including two police officers."),
 ("EUROPE", "Zaporizhzhia hit overnight", "Russian attack kills 2 and wounds 40, four of them children, in an apartment block."),
 ("EUROPE", "Germany gets Ukraine's Delta system", "Berlin first to access Kyiv's battlefield network; more interceptor missiles agreed."),
 ("MIDDLE EAST", "Iraq takes over Kurdish oilfields", "PM orders ministry to run fields in Diyala, Kirkuk, Salahuddin and Nineveh."),
 ("AFRICA", "Fighting traps Ebola teams in DRC", "Heavy combat near a hospital in Ituri forces responders to take cover for a day."),
 ("EUROPE", "Seven states seek EU curbs on Russians", "Letter to von der Leyen backs limits on tourist and sports travel."),
 ("MIDDLE EAST", "UN urges probe of Benghazi port attacks", "UNSMIL calls for an independent investigation after Sunday's strikes."),
 ("EUROPE", "NATO: we will defend space", "Rutte warns after reports Russia is preparing a nuclear-armed satellite."),
 ("ASIA", "Russian jets enter Korean zone", "Seoul says several Russian aircraft flew inside its air defence zone."),
 ("ASIA", "Seoul pays to catch AI cheats", "South Korea offers up to $375,000 for tips on AI cheating in the college exam."),
 ("TECH", "US blacklists Singapore cloud firm", "Commerce acts against Megaspeed International after months of pressure."),
 ("TECH", "UN chief: rein in AI within a year", "Guterres urges states to build a multilateral framework for AI risks."),
 ("TECH", "States sue SpaceX over Grok images", "Oregon and Virginia allege Grok generated child abuse imagery."),
 ("AMERICAS", "Huang back as Nvidia CEO", "Jensen Huang reinstated under two weeks after resigning."),
 ("AMERICAS", "Pentagon rebukes Canada", "US accuses Ottawa of falling short in defending North America."),
 ("AMERICAS", "Trump speeds up death sentences", "President says he will order DOJ to expedite federal executions."),
 ("WORLD", "COP31 ends without a pact", "Climate summit closes divided; failure exposes a split world."),
 ("ASIA", "14 nations back Rohingya ruling", "UK, Spain, Canada, Australia and ten more recognise the ICJ genocide verdict."),
 ("ASIA", "Quake shakes Nepal border", "A 5.6-magnitude earthquake strikes near the Chinese border."),
 ("AMERICAS", "Cuba's hospitals failing, WHO warns", "WHO chief visits a health system in deep deterioration."),
 ("AMERICAS", "Mexico to try 'El Chapo Isidro'", "Trial goes ahead despite a US extradition request."),
 ("ASIA", "China opens station to Pakistan", "Pakistani astronaut Zeeshan Ali joins the Shenzhou-24 mission to Tiangong."),
 ("MIDDLE EAST", "Yemen: dozens dead in Saudi strikes", "Houthis report heavy casualties from airstrikes."),
 ("MIDDLE EAST", "Iran lashes singer 74 times", "Parastoo Ahmadi punished; Tehran sets seven conditions for talks."),
 ("AFRICA", "Somalia, Uganda step up offensive", "Allies intensify operations against al-Shabaab as withdrawal begins."),
 ("AMERICAS", "Measles claims a ninth life", "Pennsylvania outbreak reaches 46 counties."),
 ("EUROPE", "Russia warns Estonia over border", "Moscow says Estonian moves are 'on verge of triggering open war'."),
 ("EUROPE", "Zelensky: admit Ukraine to NATO", "President presses the case at the NATO assembly in Berlin."),
]

# Grid: 3 cols x 9 rows-ish; cards computed to fit remaining height
top = y
cols, gap = 3, 16
cw = (W - 48 - gap * (cols - 1)) // cols
rows = 9
ch = (H - top - 64) // rows  # leave footer strip
idx = 0
for r in range(rows):
    for c in range(cols):
        if idx >= len(STORIES): break
        region, head, body = STORIES[idx]; idx += 1
        x = 24 + c * (cw + gap); yy = top + r * ch
        col = REGION_COLORS[region]
        d.rectangle([x, yy + 2, x + 5, yy + ch - 12], fill=col)
        d.text((x + 12, yy + 2), region, font=font(FB, 11), fill=col)
        hy = yy + 18
        for ln in wrap(d, head, font(FB, 15), cw - 14)[:2]:
            d.text((x + 12, hy), ln, font=font(FB, 15), fill=INK); hy += 19
        for ln in wrap(d, body, font(FR, 12), cw - 14)[:2]:
            d.text((x + 12, hy), ln, font=font(FR, 12), fill=GREY); hy += 16
    if idx >= len(STORIES): break

# Footer
fy = H - 52
d.rectangle([0, fy, W, H], fill=NAVY)
d.text((24, fy + 8), "Also 24 Nov: Arm extends CEO Rene Haas to 2033  \u00b7  NATO jets sent to Poland  \u00b7  700,000+ Russian soldiers killed, new analysis",
       font=font(FR, 14), fill=(255, 255, 255))
d.text((24, fy + 30), "Sources: Just Security, The Global Eye, Horizon, IQMIA \u2014 24 November 2026",
       font=font(FR, 12), fill=(180, 190, 205))

img.save("/home/hatch/workspace/makefun-evolving/work/news24/entry.png", optimize=True)
import os
print("bytes:", os.path.getsize("/home/hatch/workspace/makefun-evolving/work/news24/entry.png"))
print("stories:", idx)
