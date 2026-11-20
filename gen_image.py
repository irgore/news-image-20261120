#!/usr/bin/env python3
"""Newspaper front page generator - Nov 20, 2026"""
import os, json, hashlib
from PIL import Image, ImageDraw, ImageFont

OUT = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)

W, H = 600, 750  # newspaper aspect, resized to 1024 later
img = Image.new("RGB", (W, H), "#f5f0e8")
draw = ImageDraw.Draw(img)

# Try fonts
try:
    mast_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 32)
    head_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 16)
    sub_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 11)
    small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
except:
    mast_font = ImageFont.load_default()
    head_font = sub_font = small_font = mast_font

# Layout
MARGIN = 18
BOX_W = (W - MARGIN * 3) // 2
COL_W = BOX_W - 10

y = MARGIN

# ---- MASTHEAD ----
draw.text(((W - draw.textlength("THE CHRONICLE", font=mast_font)) // 2, y),
          "THE CHRONICLE", fill="#111", font=mast_font)
y += 36
draw.line([MARGIN, y, W - MARGIN, y], fill="#111", width=2)
y += 3
draw.line([MARGIN, y, W - MARGIN, y], fill="#111", width=1)
y += 8
# Date + edition
dt = "FRIDAY, NOVEMBER 20, 2026"
ed = "LATE EDITION · $2.50"
draw.text((MARGIN, y), dt, fill="#333", font=small_font)
draw.text((W - MARGIN - draw.textlength(ed, font=small_font), y), ed, fill="#333", font=small_font)
y += 20
draw.line([MARGIN, y, W - MARGIN, y], fill="#111", width=1)
y += 14

# ---- LEFT COLUMN: LEAD STORY ----
lx, rx = MARGIN, MARGIN + BOX_W + MARGIN

# Lead headline
lead = "ANTHROPIC IPO CLOSES AT $1.27T"
draw.text((lx, y), lead, fill="#111", font=head_font)
y += 20
lead2 = "Shares Surge 17% on First Day, Valuing AI Lab Above Meta"
draw.text((lx, y), lead2, fill="#111", font=sub_font)
y += 16

# Lead body
lead_body = (
    "NEW YORK — Anthropic shares closed at $524.68 on their first day of trading "
    "Friday, giving the AI research company a market capitalization of $1.27 trillion — "
    "above Meta Platforms and second only to Google among AI-focused public companies.\n\n"
    "The initial public offering, priced at $448 per share, raised $34.2 billion, "
    "making it the largest tech IPO since Saudi Aramco. CEO Dario Amodei rang the "
    "opening bell at the New York Stock Exchange alongside members of Congress who "
    "pushed for the company's 'public benefit' governance model.\n\n"
    "The debut fueled a broader AI rally, though the Nasdaq composite fell 0.3% "
    "by close as investors rotated out of legacy chipmakers. 'This marks the moment "
    "AI moved from venture capital to public markets,' said Goldman Sachs analyst "
    "Maya Chen. 'The question now is execution at scale.'"
)
# Draw lead with word wrap
words = lead_body.split()
cx, cy = lx, y
line = ""
for w in words:
    test = line + (" " if line else "") + w
    if w == "\n\n":
        draw.text((cx, cy), line, fill="#222", font=small_font)
        cy += 12; line = ""
    elif draw.textlength(test, font=small_font) > COL_W:
        draw.text((cx, cy), line, fill="#222", font=small_font)
        cy += 12; line = w
    else:
        line = test
if line:
    draw.text((cx, cy), line, fill="#222", font=small_font)
    cy += 12

# Dashed line separator
for i in range(lx, lx + COL_W, 6):
    draw.line([i, cy + 4, i + 3, cy + 4], fill="#999", width=1)
cy += 12

# Second story
story2 = "TRUMP NAMES KIRSTEN DAVIES CYBER CHIEF"
draw.text((lx, cy), story2, fill="#111", font=head_font)
cy += 18
s2body = (
    "WASHINGTON — President-elect Donald Trump named Kirsten Davies, "
    "former CISO of Unilever and Estée Lauder, as national cyber director "
    "Friday, signaling a corporate-security approach to federal cyber defense. "
    "Davies would succeed Harry Coker. The pick drew bipartisan praise from "
    "the Senate Intelligence Committee."
)
words2 = s2body.split()
line2 = ""
for w in words2:
    test2 = line2 + (" " if line2 else "") + w
    if draw.textlength(test2, font=small_font) > COL_W:
        draw.text((lx, cy), line2, fill="#222", font=small_font)
        cy += 12; line2 = w
    else:
        line2 = test2
if line2:
    draw.text((lx, cy), line2, fill="#222", font=small_font)
    cy += 12

# ---- RIGHT COLUMN ----
ry = MARGIN + 101  # start aligned with lead headline

# Story 3
s3head = "ICJ Rules Myanmar Committed Genocide Against Rohingya"
draw.text((rx, ry), s3head, fill="#111", font=head_font)
ry += 18
s3body = (
    "THE HAGUE — The International Court of Justice ruled Friday that "
    "Myanmar committed genocide against the Rohingya minority, a landmark "
    "verdict that opens the door to reparations and criminal prosecutions. "
    "Rohingya refugees in Cox's Bazar erupted in tears and prayer as news "
    "of the ruling spread. 'Justice, at last,' said community leader "
    "Mohammed Islam, whose family was among the 740,000 forced to flee "
    "the 2017 military crackdown. Myanmar's junta rejected the ruling."
)
words3 = s3body.split()
line3 = ""
for w in words3:
    test3 = line3 + (" " if line3 else "") + w
    if draw.textlength(test3, font=small_font) > COL_W:
        draw.text((rx, ry), line3, fill="#222", font=small_font)
        ry += 12; line3 = w
    else:
        line3 = test3
if line3:
    draw.text((rx, ry), line3, fill="#222", font=small_font)
    ry += 12

# Dashed line
for i in range(rx, rx + COL_W, 6):
    draw.line([i, ry + 4, i + 3, ry + 4], fill="#999", width=1)
ry += 14

# Story 4
s4head = "Houthi Strike Hits Riyadh Skyscraper at Saudi Wealth Fund HQ"
draw.text((rx, ry), s4head, fill="#111", font=head_font)
ry += 18
s4body = (
    "RIYADH — A Houthi ballistic missile struck the upper floors of "
    "Riyadh's tallest skyscraper, which houses the headquarters of Saudi "
    "Arabia's Public Investment Fund, officials said Friday. At least "
    "four people were injured. The attack, claimed by Yemen's Houthi "
    "militia, marks the most audacious strike on the Saudi capital since "
    "the conflict began. Oil prices jumped 2.8% on the news."
)
words4 = s4body.split()
line4 = ""
for w in words4:
    test4 = line4 + (" " if line4 else "") + w
    if draw.textlength(test4, font=small_font) > COL_W:
        draw.text((rx, ry), line4, fill="#222", font=small_font)
        ry += 12; line4 = w
    else:
        line4 = test4
if line4:
    draw.text((rx, ry), line4, fill="#222", font=small_font)
    ry += 12

# Bottom bar
bottom_y = H - 30
draw.line([MARGIN, bottom_y, W - MARGIN, bottom_y], fill="#111", width=1)
footer = "WWW.THECHRONICLE.COM · ALL THE NEWS THAT'S FIT TO PRINT · EST. 1851"
draw.text(((W - draw.textlength(footer, font=small_font)) // 2, bottom_y + 5),
          footer, fill="#333", font=small_font)

# ---- BOTTOM STORIES ----
by = bottom_y - 90
# 4 small stories in 4 columns
small_cols = 4
scw = (W - MARGIN * (small_cols + 1)) // small_cols
stories = [
    ("GTA VI Launch Booms", "Content economy surges as blockbuster game drives creator revenue, streaming records."),
    ("Crimean Bridge Strikes", "Ukraine strains Russian logistics with precision strikes on key supply route."),
    ("Apple's AI Agent Rival", "Tech giant developing own agent to challenge OpenAI and Anthropic dominance."),
    ("Fiona the Hippo Dies", "Beloved Cincinnati Zoo hippo passes 11 days after swallowing visitor's hat."),
]

for i, (shead, sbody) in enumerate(stories):
    sx = MARGIN + i * (scw + MARGIN)
    draw.text((sx, by), shead, fill="#111", font=sub_font)
    sy = by + 16
    ws = sbody.split()
    ln = ""
    for w in ws:
        t = ln + (" " if ln else "") + w
        if draw.textlength(t, font=small_font) > scw:
            draw.text((sx, sy), ln, fill="#333", font=small_font)
            sy += 11; ln = w
        else:
            ln = t
    if ln:
        draw.text((sx, sy), ln, fill="#333", font=small_font)

# Resize to 1024
final = img.resize((1024, 1024), Image.LANCZOS)
out_path = os.path.join(OUT, "entry.png")
final.save(out_path, "PNG", optimize=True)

# Verify
with open(out_path, "rb") as f:
    h = hashlib.sha256(f.read()).hexdigest()
size = os.path.getsize(out_path)
print(f"OK size={size} hash={h} path={out_path}")