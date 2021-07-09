import io
from PIL import Image
import tempfile

def is_Image(inputStr):
    """"""
    #PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x000001B58E225A40>
    #t = io.BytesIO(str.encode(inputStr))
    #t.seek(0)
    #return Image.open(t)
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(str.encode(inputStr))
        temp.flush()
        im = Image.open(temp)
