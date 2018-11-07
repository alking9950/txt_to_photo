from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
import sqlite3
from bidi.algorithm import get_display

def photo(texts):
    im = Image.new('RGB',(500,500))
    fnt = ImageFont.truetype('Droid.ttf', 20)
    reshaped_text = arabic_reshaper.reshape(texts.strip())
    bidi_text = get_display(reshaped_text)
    txt = Image.new('RGBA', im.size, (255, 255, 255,0))
    d = ImageDraw.Draw(txt)
    size = d.textsize(bidi_text , font=fnt, spacing=4 )
    sor = Image.new('RGBA', (size[0],size[1]+10), (255, 255, 255,0))
    txt = Image.new('RGBA', sor.size, (255, 255, 255,0))
    d = ImageDraw.Draw(txt)
    d.multiline_text((0,0), bidi_text, font=fnt, fill=(52, 73, 94),align="center",spacing=3)
    out = Image.alpha_composite(sor, txt).convert('RGB')
    return out
    
