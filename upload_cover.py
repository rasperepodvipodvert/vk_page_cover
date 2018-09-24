# -*- coding: utf-8 -*-
import vk_api
import settings


def main():
    """ Пример загрузки фото """

    # login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(settings.login, settings.password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """
    vk = vk_session.get_api()
    groups = vk.groups.get(
        filter='editor',
        extended=1
    )
    # group_id = groups['items'][1]
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_cover(  # Подставьте свои данные
        photo='./cover/cover.jpg',
        group_id=settings.group_id,
        crop_x=0,
        crop_y=0,
        crop_x2=1590,
        crop_y2=400
    )
    print(photo)

if __name__ == '__main__':
    main()