#!/usr/bin/env python3
"""Generate news image for November 20, 2026"""
from PIL import Image, ImageDraw, ImageFont
import os, random

W, H = 1200, 675
img = Image.new('RGB', (W, H), '#0a0a0f')
draw = ImageDraw.Draw(img)

# Background gradient
for y in range(H):
    r = int(10 + (y/H)*30)
    g = int(10 + (y/H)*20)
    b = int(15 + (y/H)*50)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Headlines
headlines = [
    "AI BREAKTHROUGH: GPT-6 RELEASED",
    "GLOBAL MARKETS HIT RECORD VOLATILITY",
    "CLIMATE SUMMIT REACHES HISTORIC DEAL",
    "SPACEX MARS COLONY BREAKS GROUND",
    "GTA VI SELLS 50M COPIES IN 24 HOURS",
]

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_date = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
except:
    font_title = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_date = ImageFont.load_default()

# Date box
draw.rectangle([W-320, 20, W-20, 65], fill='#ff2e6e')
draw.text((W-310, 25), "NOVEMBER 20, 2026", fill='white', font=font_date)

# Title
draw.text((50, 30), "WORLD", fill='white', font=font_title)
draw.text((50, 65), "NEWS", fill='#ff2e6e', font=font_title)

# Red accent line
draw.rectangle([50, 100, 400, 104], fill='#ff2e6e')

# Headlines
colors = ['#ff6b35', '#ff2e6e', '#9b59b6', '#00f5ff', '#ffd700']
for i, hl in enumerate(headlines):
    y = 130 + i * 55
    # Bullet
    draw.rectangle([50, y+8, 60, y+18], fill=colors[i])
    # Text
    draw.text((75, y), hl, fill=colors[i], font=font_title)

# Visual elements - abstract shapes
for _ in range(30):
    x = random.randint(400, W-20)
    y = random.randint(130, H-20)
    s = random.randint(3, 12)
    c = random.choice(colors)
    draw.rectangle([x, y, x+s, y+s], fill=c)

# World map outline (simplified dots)
map_dots = [(500,200),(520,195),(540,200),(560,210),(580,215),(600,220),(620,225),
            (640,230),(660,228),(680,225),(700,230),(720,240),(740,250),(760,260),
            (780,270),(800,280),(820,290),(840,300),(860,310),(880,320),
            (530,250),(550,260),(570,270),(590,280),(610,290),(630,300),
            (650,310),(670,320),(690,330),(710,340),(730,350),
            (490,350),(510,360),(530,370),(550,380),(570,390),
            (590,400),(610,410),(630,420),(650,430),(670,440),
            (750,400),(770,410),(790,420),(810,430),(830,440),
            (850,450),(870,460)]
for dx, dy in map_dots:
    draw.rectangle([dx, dy, dx+3, dy+3], fill='#333355')

# Bottom bar
draw.rectangle([0, H-50, W, H], fill='#0a0a0f')
draw.text((50, H-35), "make.fun/news-image-20261120", fill='#666', font=font_small)

# Save
os.makedirs("/output", exist_ok=True)
img.save("/output/entry.png", "PNG")
print("entry.png generated")