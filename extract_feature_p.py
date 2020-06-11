from PIL import Image
import os
import imagehash
import multiprocessing as mp


def image_feature(filename):
    return imagehash.phash(Image.open(filename))


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
