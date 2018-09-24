# -*- coding: utf-8 -*-
import vk_api
import settings


def main():

    vk_session = vk_api.VkApi(settings.login, settings.password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_cover(  # Подставьте свои данные
        photo=settings.cover_path,
        group_id=settings.group_id,
        crop_x=0,
        crop_y=0,
        crop_x2=1590,
        crop_y2=400
    )


if __name__ == '__main__':
    main()