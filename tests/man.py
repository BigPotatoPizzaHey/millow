import millow
from PIL import Image

img = Image.open("OIP.webp")

with open("res.mlol", "wb") as f:
    f.write(millow.loadimg(img))
