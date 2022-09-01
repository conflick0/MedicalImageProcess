import numpy as np
from utils import convert as cvt


def test_ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header, is_flip=True):
    cvt.ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header=header, is_flip=is_flip)


def test_nrrd2ptn():
    ptn_path = r'C:\Users\jack\Downloads\latest_segment_512_512_267.ptn'
    nrrd_path = r'C:\Users\jack\Downloads\latest_segment_512_512_267.nrrd'
    cvt.nrrd2ptn(nrrd_path, ptn_path)


if __name__ == '__main__':
    #  (left, right), (posterior, anterior), (inferior, superior)
    # 'right-anterior-inferior' 'left-posterior-superior'

    ptn_path = r'D:\home\school\ntut\dataset\chgh\source\Patient_108\case108.ptn'
    nrrd_path = r'C:\Users\jack\Downloads\GT_2.nrrd'

    ptn_shape = [512, 512, 267]

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

    is_flip = True

    print(f'load ptn from: {ptn_path}')
    print(f'convert ...')
    test_ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header, is_flip)
    print(f'done.')
    print(f'save nrrd to: {nrrd_path}')
