# -*- coding: utf-8 -*-
import vk_api

from plugins.date_on_cover import *  # подключаем плагины
from plugins.general import *


def main():
    vk_session = vk_api.VkApi(settings.login, settings.password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)
    vk = vk_session.get_api()
    info = get_group_info(vk, settings.group_id)
    text = ''+\
            'Заголовок: '+info['title'] + '\n' \
            'Краткий URL страницы: '+ info['address'] + '\n' \
            'Количество подписчиков: ' + str(get_groups_members(vk, settings.group_id))+'\n' \
            "---" + '\n' \
            'Курс BTC: '+ str(get_btc_cost('btc'))+' USD'+ '\n' \
            'Курс ETH: ' + str(get_btc_cost('eth')) + ' USD' + '\n'

    date_on_cover(text=text, font_size=50)
    # photo = upload.photo_cover(  # Подставьте свои данные
    #     photo=date_on_cover(),
    #     group_id=settings.group_id,
    #     crop_x=0,
    #     crop_y=0,
    #     crop_x2=1590,
    #     crop_y2=400
    # )
    # return photo

def get_groups_members(vk, group_id):
    members = vk.groups.getMembers(group_id=group_id)['count']
    return members


def get_group_info(vk, group_id):
    sett = vk.groups.getSettings(group_id=group_id)
    print(settings)
    return sett


if __name__ == '__main__':
    main()
