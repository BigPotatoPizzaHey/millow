from PIL import Image
import struct
import zlib

def loadimg(img: Image.Image) -> bytes:
    width, height = img.size
    print(width, height)
    ret = struct.pack("ii", width, height)
    for x in range(width):
        for y in range(height):
            pixel = list(map(int.to_bytes, img.getpixel((x, y))))[:3]
            # transparency not supported
            assert len(pixel) == 3
            #print(pixel)
            ret += struct.pack("ccc", *pixel)
    return zlib.compress(ret)

def toimg(raw: bytes) -> Image.Image:
    uncompressed = zlib.decompress(raw)
    offset = 0
    width, height = struct.unpack_from("ii", uncompressed)
    ret = Image.new('RGB', (width, height), color="white")

    offset += 8
    for x in range(width):
        for y in range(height):
            pixel = struct.unpack_from("ccc", uncompressed, offset)
            pixel = tuple(map(int.from_bytes, pixel))
            offset += 3
            ret.putpixel((x, y), pixel)
            # print(pixel)
    return ret