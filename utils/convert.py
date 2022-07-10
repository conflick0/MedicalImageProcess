import os
from utils import io


def dcm2img(dcm_dir, img_dir, save_img_type='jpg'):
    """
    Convert dcm to img.
    param: dcm_dir: dcm dir
    param: img_dir: img dir
    param: save_img_type: save img type,
        {'jpg', 'bmp'}, default is 'jpg'
    """
    os.makedirs(img_dir, exist_ok=True)
    imgs = io.read_dcms(dcm_dir)
    io.write_imgs(imgs, img_dir, save_img_type)


def nrrd2img(nrrd_path, img_dir, save_img_type='jpg'):
    """
    Convert nrrd to img.
    param: nrrd_dir: nrrd dir
    param: img_dir: img dir
    param: save_img_type: save img type,
        {'jpg', 'bmp'}, default is 'jpg'
    """
    os.makedirs(img_dir, exist_ok=True)
    imgs = io.read_nrrd(nrrd_path)
    io.write_imgs(imgs, img_dir, save_img_type)


def img2nrrd(img_dir, nrrd_path, header=None, is_flip=True):
    """
    Convert img to nrrd.
    param: img_dir: img dir
    param: nrrd_path: nrrd path
    param: header: header of nrrd, default is None
    """
    imgs = io.read_imgs(img_dir)
    io.write_nrrd(imgs, nrrd_path, header, is_flip)


def ptn2img(ptn_path, img_dir, ptn_shape, save_img_type='jpg'):
    """
    Convert ptn to img.
    param: ptn_dir: ptn dir
    param: img_dir: img dir
    param: ptn_shape: shape of ptn, ex. (512, 512, 267)
    param: save_img_type: save img type,
        {'jpg', 'bmp'}, default is 'jpg'
    """
    os.makedirs(img_dir, exist_ok=True)
    imgs = io.read_ptn(ptn_path, ptn_shape)
    io.write_imgs(imgs, img_dir, save_img_type)


def img2ptn(img_dir, ptn_path):
    """
    Convert img to ptn.
    param: img_dir: img dir
    param: ptn_path: ptn path
    param: ptn_shape: shape of ptn, ex. (512, 512, 267)
    """
    imgs = io.read_imgs(img_dir)
    io.write_ptn(imgs, ptn_path)


def ptn2nrrd(ptn_path, nrrd_path, ptn_shape, header=None, is_flip=True):
    """
    Convert ptn to nrrd.
    param: ptn_dir: ptn dir
    param: nrrd_path: nrrd path
    param: ptn_shape: shape of ptn, ex. (512, 512, 267)
    param: header: header of nrrd, default is None
    """
    imgs = io.read_ptn(ptn_path, ptn_shape)
    io.write_nrrd(imgs, nrrd_path, header, is_flip)


def nrrd2ptn(nrrd_path, ptn_path):
    """
    Convert ptn to nrrd.
    param: nrrd_path: nrrd path
    param: ptn_dir: ptn dir
    """
    imgs = io.read_nrrd(nrrd_path)
    io.write_ptn(imgs, ptn_path)
