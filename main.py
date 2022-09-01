import numpy as np
from utils import convert as cvt


def test_ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header, is_flip=True):
    cvt.ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header=header, is_flip=is_flip)


if __name__ == '__main__':
    # file path
    ptn_path = r'D:\home\school\ntut\dataset\chgh\source\Patient_108\case108.ptn'
    nrrd_path = r'C:\Users\jack\Downloads\GT_2.nrrd'

    # file shape
    ptn_shape = [512, 512, 267]

    # file info
    header = {
        'space': 'left-posterior-superior',
        'space directions': [
            [0.3359375, 0, 0],
            [0, 0.3359375, 0],
            [0, 0, 0.5]
        ],
        'space origin': list(np.array(
            [45.83203125, 257.83203125, 246.8]
        ) * -1),
    }

    # is_flip: True / False
    is_flip = True

    # convert ptn2nrrd
    print(f'load ptn from: {ptn_path}')
    print(f'convert ...')
    test_ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header, is_flip)
    print(f'save nrrd to: {nrrd_path}')
    print(f'done')
