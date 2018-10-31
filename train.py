import os
import pickle
import numpy as np

from keras.preprocessing.image import load_img
from keras.preprocessing import image
from keras.applications.mobilenetv2 import preprocess_input


IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png')
LEN_CLASSES = 1000


def mnetv2_input_from_image(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return preprocess_input(x)


def load_imgs(dirname, size=(224, 224)):
    imgs = {}
    for innerdir in os.listdir(dirname):
        fullpath = dirname + innerdir
        if os.path.isdir(fullpath) and '.' not in innerdir:
            for filename in os.listdir(fullpath):
                if filename.lower().endswith(IMG_EXTENSIONS):
                    try:
                        curr = load_img(fullpath + '/' + filename,
                                        target_size=size)
                        imgs[
                            fullpath + '/' + filename
                        ] = mnetv2_input_from_image(curr)
                    except OSError as err:
                        print(
                            f'Failed to open img {fullpath + "/" + filename}')
    return imgs


def classify_dataset(imgs, model):
    res = {}
    for path, img in imgs.items():
        pred = model.predict(img)
        res[path] = pred[0]
    return res


def sort_by_idx(data):
    res = [[]] * LEN_CLASSES
    for path, value in data.items():
        res[value[0]] = (path, value[1])

        print(value[1])
    return res
    return [sorted(r, key=lambda x: x[1], reverse=True)
            if r else [] for r in res]


def save(data):
    with open('save/train.pkl', 'wb') as f:
        pickle.dump(data, f)
