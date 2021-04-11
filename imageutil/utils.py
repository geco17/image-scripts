import imghdr

from PIL import Image
import os
import filetype


# create webp for all images in directory (not recursive)
def webps(src_dir, dest_dir):
    files = os.listdir(src_dir)
    for name in files:
        f = os.path.join(src_dir, name)
        if __is_image(f) and not imghdr.what(f) == 'webp':
            webp(f, dest_dir)


# create a single webp image
def webp(file, dest_dir):
    im = Image.open(file)
    im = im.convert('RGB')
    dest_file = __dest_webp_file(file, dest_dir)
    im.save(dest_file)


# create thumbnails for all images in directory (not recursive)
def thumbnails(src_dir, dest_dir, max_size):
    files = os.listdir(src_dir)
    for name in files:
        f = os.path.join(src_dir, name)
        if __is_image(f):
            thumbnail(f, dest_dir, max_size)
        else:
            print(f'[skip] directory: {f}')


# create thumbnails for all images in directory (not recursive)
def thumbnails_exact(src_dir, dest_dir, requested_size):
    files = os.listdir(src_dir)
    for name in files:
        f = os.path.join(src_dir, name)
        if __is_image(f):
            thumbnail_exact(f, dest_dir, requested_size)
        else:
            print(f'[skip] directory: {f}')


def thumbnail_exact(src_file, dest_dir, requested_size):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    dest_file = __dest_thumbnail_file(src_file, dest_dir)
    print(f'dest file: {dest_file}')
    im = Image.open(src_file)
    orig_w, orig_h = im.size
    w, h = requested_size
    print(f'orig w {orig_w} orig h {orig_h} req width {w} req h {h}')
    if orig_w < w or orig_h < h:
        raise Exception(f'original dimensions {orig_w}x{orig_h} not valid for thumbnail dimensions {w}x{h}')
    requested_ratio = w / h
    actual_ratio = orig_w / orig_h
    print(f'actual ratio {actual_ratio} requested ratio {requested_ratio}')
    diff = requested_ratio / actual_ratio
    if diff == 1:
        print('aspect ratios equal')
        new_im = im
    else:
        if diff > 1:
            # the requested image will be wider than the image we have to work with
            # therefore we need to crop height-wise and then resize
            crop_h = orig_h / diff
            print(f'crop height from {orig_h} to {crop_h}')
            new_im = im.crop((0, 0, orig_w, crop_h))
        else:
            # the requested image will be narrower than the image we have to work with
            # therefore we need to crop width-wise and then resize
            crop_w = orig_w * diff
            print(f'crop width from {orig_w} to {crop_w}')
            new_im = im.crop((0, 0, crop_w, orig_h))
    new_im = new_im.resize((w, h))
    new_im.save(dest_file)


# create a thumbnail for the given image in the destination directory
def thumbnail(src_file, dest_dir, max_size):
    print(f'Thumbnail')
    print(f'Source file: {src_file}')
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    dest_file = __dest_thumbnail_file(src_file, dest_dir)
    print(f'dest file: {dest_file}')
    im = Image.open(src_file)
    orig_w, orig_h = im.size
    max_w, max_h = max_size
    if orig_w < max_w or orig_h < max_h:
        raise Exception(f'original dimensions {orig_w}x{orig_h} not valid for thumbnail dimensions {max_w}x{max_h}')
    im.thumbnail(max_size)
    im.save(dest_file)


# helper method to get thumbnail file name
def __dest_thumbnail_file(src_file, dest_dir):
    pieces = os.path.splitext(os.path.basename(src_file))
    no_ext = pieces[0]
    ext = pieces[1]
    dest_file = f'{dest_dir}{os.path.sep}{no_ext}-thumbnail{ext}'
    return dest_file


# helper method to get webp file name
def __dest_webp_file(src_file, dest_dir):
    pieces = os.path.splitext(os.path.basename(src_file))
    no_ext = pieces[0]
    dest_file = f'{dest_dir}{os.path.sep}{no_ext}.webp'
    return dest_file


def __is_image(file):
    return os.path.isfile(file) and filetype.is_image(file)
