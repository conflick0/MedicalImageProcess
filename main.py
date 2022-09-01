from utils import convert as cvt
import numpy as np

def test_dcm2img():
    dcm_dir = r'D:\home\school\ntut\dataset\corcta\corcta_dcm'
    img_dir = r'C:\Users\jack\Downloads\dcm_imgs'
    cvt.dcm2img(dcm_dir, img_dir, 'bmp')


def test_nrrd2img():
    nrrd_path = r'C:\Users\jack\Downloads\Segmentation.nrrd'
    nrrd_path1 = r'C:\Users\jack\Downloads\Segmentation1.nrrd'
    img_dir = r'C:\Users\jack\Downloads\nrrd_imgs'
    img_dir1 = r'C:\Users\jack\Downloads\nrrd_imgs1'
    cvt.nrrd2img(nrrd_path, img_dir, 'bmp')
    cvt.img2nrrd(img_dir, nrrd_path1)
    cvt.nrrd2img(nrrd_path1, img_dir1, 'bmp')


def test_ptn2img():
    ptn_path = r'C:\Users\cg\Downloads\segment_512_512_267.ptn'
    ptn_path1 = r'C:\Users\cg\Downloads\segment1_512_512_267.ptn'
    img_dir = r'C:\Users\cg\Downloads\ptn_imgs'
    img_dir1 = r'C:\Users\cg\Downloads\ptn_imgs1'
    cvt.ptn2img(ptn_path, img_dir, (512, 512, 267), 'bmp')
    cvt.img2ptn(img_dir, ptn_path1)
    cvt.ptn2img(ptn_path1, img_dir1, (512, 512, 267), 'bmp')


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
    # nrrd_path = r'D:\home\school\ntut\dataset\chgh\source\Patient_05\GT_2.nrrd'
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

    test_ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header, is_flip)

