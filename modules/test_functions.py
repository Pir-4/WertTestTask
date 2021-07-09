import io
from PIL import Image

def is_Image(inputStr):
    """"""
    #PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x000001B58E225A40>
    t = io.BytesIO(str.encode(inputStr))
    t.seek(0)
    return Image.open(t)