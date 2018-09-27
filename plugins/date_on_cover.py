from PIL import Image, ImageDraw, ImageFont
import settings
import datetime
import os
from plugins.resize_and_crop import *
import random

def date_on_cover(
        font='./fonts/28days.ttf',
        font_size=150,
        text=datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y")

):
    randome_file = './cover/'+getRandomFile(os.getcwd()+'/cover/')
    # im = Image.open(settings.cover_path).convert('RGBA')
    im = Image.open(randome_file).convert('RGBA')
    size = (1590, 400)
    im = resize_and_crop(im, size, crop_type='middle')
    txt = Image.new('RGBA', im.size, (0, 0, 0, 150))
    fnt = ImageFont.truetype(font, font_size)
    fnt_text = ImageFont.truetype('./font/Russo One.ttf', font_size)
    draw = ImageDraw.Draw(txt)

    # текст который направили в функцию
    margin_bottom = 0
    margin_left = 10

    width, height = draw.textsize(text, fnt)
    # выравнивание по правому краю
    # draw.multiline_text(((size[0] - width), margin_bottom), text, font=fnt, fill=(255, 95, 51, 255), )
    # выравнивание по левому краю
    draw.multiline_text(
        (margin_left, margin_bottom),
        text,
        font=fnt_text,
        fill=(255, 95, 51, 255),
    )
    margin_bottom += height

    # Текст под нижней линией - копирайт
    text = 'by СИСADМИН'
    temp_font = ImageFont.truetype(font, 50)
    text_width = draw.textsize(text, temp_font)
    margin_bottom = 50
    xy = size[0]-text_width[0], size[1]-margin_bottom
    draw.text(
        text=text,
        xy=xy,
        fill=(255, 95, 51, 255),
        font=ImageFont.truetype(font, 50)
    )
    # Линия снизу
    margin_bottom = size[1]-50
    draw.line(
        xy=[0, margin_bottom, size[0], margin_bottom],
        fill=(255, 95, 51, 255),
        width=5
    )

    out = Image.alpha_composite(im, txt)
    save_path = os.getcwd() + "/date_on_cover.png"
    out.save(save_path, 'PNG')
    return save_path

def draw_line(draw):
    pass

def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]
