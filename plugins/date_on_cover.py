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
    txt = Image.new('RGBA', im.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype(font, font_size)
    draw = ImageDraw.Draw(im)
    draw.text(
        xy=(0, 0),
        text=text,
        fill=(255, 95, 51, 255),
        font=fnt
    )
    draw.text(
        text='by СИСADМИН',
        xy=(720, 250),
        fill=(255, 95, 51, 255),
        font=fnt
    )
    out = Image.alpha_composite(im, txt)
    save_path = os.getcwd() + "/date_on_cover.png"
    out.save(save_path, 'PNG')
    return save_path

def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]
