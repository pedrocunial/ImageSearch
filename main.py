import argparse
import train

from keras.applications.mobilenetv2 import MobileNetV2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Buscador de Imagens')
    parser.add_argument('--build-index', '--train',
                        dest='train', action='store_true')
    parser.add_argument('--data', default='data/')
    parser.add_argument('--term', default=None)

    args = parser.parse_args()

    if not args.data.endswith('/'):
        dirname = args.data + '/'
    else:
        dirname = args.data

    model = MobileNetV2()

    if args.train:
        imgs = train.load_imgs(dirname)
        data = train.classify_dataset(imgs, model)
        train.save(train.sort_by_idx(data))
