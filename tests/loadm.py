import millow
from PIL import Image

with open("res.mlol", "rb") as f:
    img = millow.toimg(f.read())

img.save("ret.png")