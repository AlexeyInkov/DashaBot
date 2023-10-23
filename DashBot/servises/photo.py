import urllib.request


from rembg import remove
from PIL import Image

from config_data.config import BOT_TOKEN
from loader import bot
from servises.bot_states import UserInfoState


def change_image(photo_id: str, action_key: str) -> str:
    action = {
        "remove_background": remove_background,
        "change_to_baw": change_to_baw,
        "change_size": change_size,
        "photo_to_sticker": photo_to_sticker
    }
    file_info = bot.get_file(photo_id)
    urllib.request.urlretrieve(
        f'http://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}',
        file_info.file_path
    )
    with Image.open(file_info.file_path) as img:
        img = action[action_key](img)
        img.save(file_info.file_path, "PNG")
    return file_info.file_path


def remove_background(img: Image) -> Image:  # Удаляет фон
    return remove(img)


def change_to_baw(img: Image) -> Image:  # Делает ЧБ
    return img.convert('L')


def change_size(img: Image, maxi: int = 512) -> Image:  # Изменяем размер
    if max(img.height, img.width) > maxi:
        if img.height > img.width:
            size = (int(img.width / img.height * maxi), maxi)
        else:
            size = (maxi, int(img.height / img.width * maxi))
        img.thumbnail(size=size)
    return img


def photo_to_sticker(img: Image) -> Image:
    img = change_size(img, 400)
    img = remove_background(img)
    return img
