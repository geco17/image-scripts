# Image util

Some useful functions for image manipulation.

Examples

Import the util

```python
import imgoptimizr.imageutil.utils as u
```
And then

1. Create webp images in the destination directory for all images in the source directory.
```python
u.webps(r'src\directory', r'dest\directory')
```

2. Create thumbnail images in the destination directory for all images in the source directory, where all thumbnails have the size specified.
```python
u.thumbnails_exact(r'src\directory', r'dest\directory', (250, 150))
```

3. Create thumbnail images in the destination directory with max size specified.
```python
u.thumbnails_exact(r'src\directory', r'dest\directory', (250, 150))
```

Basic GUI available, work in progress. See class `ThumbnailExactManyGui`.