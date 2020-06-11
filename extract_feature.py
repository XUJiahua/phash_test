from PIL import Image
import os
import imagehash


def image_feature(filename):
    return imagehash.phash(Image.open(filename))


print(f"file,feature")
n = 10
for i in range(1, n + 1):
    folder = f"download_{i}"
    for file in os.listdir(folder):
        filename = os.path.join(folder, file)
        feat = image_feature(filename)
        print(f"{file},{feat}")
