import pathlib

from PIL import Image, ImageDraw, ImageFont
import settings
import datetime
import os


def date_on_cover(
        font='./fonts/28days.ttf',
        font_size=200,
        text=datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y")

):
    im = Image.open(settings.cover_path).convert('RGBA')
    txt = Image.new('RGBA', im.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype(font, font_size)
    draw = ImageDraw.Draw(im)
    draw.text(
        xy=(0, 0),
        text=text,
        fill=(255, 95, 51, 255),
        font=fnt
    )
    out = Image.alpha_composite(im, txt)
    save_path = os.getcwd() + "/cover/date_on_cover.png"
    out.save(save_path, 'PNG')
    return save_path
