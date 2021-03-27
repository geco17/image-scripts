from PIL import Image
import os


# create thumbnails for all images in directory (not recursive)
def thumbnails(src_dir, dest_dir, max_size):
    files = os.listdir(src_dir)
    for name in files:
        f = os.path.join(src_dir, name)
        if os.path.isfile(f):
            thumbnail(f, dest_dir, max_size)
        else:
            print(f'[skip] directory: {f}')


# create a thumbnail for the given image in the destination directory
def thumbnail(src_file, dest_dir, max_size):
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


# helper method to get thumbnail argument size
def __dest_thumbnail_file(src_file, dest_dir):
    pieces = os.path.splitext(os.path.basename(src_file))
    no_ext = pieces[0]
    ext = pieces[1]
    dest_file = f'{dest_dir}{os.path.sep}{no_ext}-thumbnail{ext}'
    return dest_file