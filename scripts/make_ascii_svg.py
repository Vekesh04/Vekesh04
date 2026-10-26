"""Regenerate from a local photo: python scripts/make_ascii_svg.py /path/photo.png.
The original photograph is deliberately not committed. Requires Pillow.
"""
import sys
from pathlib import Path
from html import escape
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
ROOT=Path(__file__).resolve().parents[1]
im=Image.open(sys.argv[1]).convert('L')
# Crop the face and shoulders to keep the portrait legible at README size.
w,h=im.size; im=im.crop((int(w*.20),int(h*.15),int(w*.77),int(h*.74)))
im=ImageOps.autocontrast(im,cutoff=2); im=ImageEnhance.Contrast(im).enhance(1.35)
im=im.resize((68,65))
ramp=' .:-=+*#%@'
out=['<svg xmlns="http://www.w3.org/2000/svg" width="370" height="440" viewBox="0 0 370 440" role="img"><title>ASCII portrait of Vekesh Makani</title><rect width="370" height="440" rx="16" fill="#0d1117"/><text x="20" y="25" fill="#8b949e" font-size="11" font-family="monospace">$ render --portrait vekesh</text>']
for y in range(65):
    line=''.join(ramp[round((255-im.getpixel((x,y)))/255*(len(ramp)-1))] for x in range(68))
    out.append(f'<clipPath id="r{y}"><rect x="15" y="{39+y*5.8}" width="340" height="7"><animate attributeName="width" from="0" to="340" dur=".15s" begin="{y*.035}s" fill="freeze"/></rect></clipPath><text xml:space="preserve" x="15" y="{45+y*5.8}" clip-path="url(#r{y})" fill="#d1d5db" font-family="monospace" font-size="8" textLength="340" lengthAdjust="spacingAndGlyphs">{escape(line)}</text>')
out.append('</svg>'); (ROOT/'avi-ascii.svg').write_text(''.join(out))
