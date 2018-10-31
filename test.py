import pickle
import cv2 as cv
import classes as cls
import matplotlib.pyplot as plt


def load(datafile):
    try:
        with open(datafile, 'rb') as f:
            data = pickle.load(f)
    except IOError as err:
        raise ValueError('Arquivo não encontrado, você possui o arquivo ' +
                         'treinamento (save/train.pkl)')
    return data


def open_img(imgpath):
    img = cv.imread(imgpath)
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def show_imgs(imgs):
    for idx, img in enumerate(imgs):
        fig = plt.figure(f'Match #{idx+1}: {img[0] * 100:.2f}% de match')
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(open_img(img[1]))
    plt.show()


def search_term(term):
    if term not in cls.class2id:
        raise ValueError(f'Palavra-chave {term} não existe entre as possíveis')

    data = load('save/train.pkl')
    cls_idx = cls.class2id[term]

    data = [(v[cls_idx], k) for k, v in data.items()]
    top5 = sorted(data, key=lambda x: x[0], reverse=True)[:5]
    show_imgs(top5)
