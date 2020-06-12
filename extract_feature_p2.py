from PIL import Image
import os
import numpy as np
from hashlib import md5
import multiprocessing as mp

def read_to_2d_array(filename, size=(10, 10), bit=5):
    img = Image.open(filename)
    img = img.convert('L')
    if size is not None:
        img = img.resize(size)
    data = np.array(img)
    if bit < 8:
        data = data // (2**(8-bit)) * (2**(8-bit))
    return data


def image_feature(filename):
    data = read_to_2d_array(filename)
    return md5(data).hexdigest()


def process_one_folder(folder):
    with open(folder + ".csv", 'w') as f:
        for file in os.listdir(folder):
            filename = os.path.join(folder, file)
            feat = image_feature(filename)
            f.write(f"{file},{feat}\n")


n = 10

# print(f"file,feature")

pool = mp.Pool(mp.cpu_count())
pool.map(process_one_folder, [f"download_{i}" for i in range(1, n + 1)])
pool.close()
