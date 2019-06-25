# encolor
Colorize black and white images and video.

This project provides colorization of black and white (greyscale) images based 
upon the work of [Richard Zhang et al.](https://richzhang.github.io/colorization/)

The initial step is to download the relevant deep learning model and associated 
configuration files by running the script `download_model_files.py`, providing a 
single argument to specify the destination directory for these files:
```
$ python scripts/download_model_files.py --dest /home/ubuntu/colorization
```
