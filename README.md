# encolor
Colorize black and white images and video.

This project provides colorization of black and white (greyscale) images based 
upon the work of [Richard Zhang et al.](https://richzhang.github.io/colorization/)

The initial step is to download the relevant deep learning model and associated 
configuration files by running the script `download_model_files.py`, providing a 
single argument to specify the destination directory for these files:
```
$ export MODEL_DIR=/home/ubuntu/colorization
$ python scripts/download_model_files.py --dest $MODEL_DIR
```
We can now specify these files as configuration arguments to the scripts 
`colorize_image.py` and `colorize_video.py`:
```
$ python colorize_image.py --image /home/ubuntu/images/automobile.jpg --prototxt $MODEL_DIR/colorization_deploy_v2.prototxt --model $MODEL_DIR/colorization_release_v2.caffemodel --points $MODEL_DIR/pts_in_hull.npy
$ python colorize_video.py --video /home/ubuntu/video/city_park.mp4 --prototxt $MODEL_DIR/colorization_deploy_v2.prototxt --model $MODEL_DIR/colorization_release_v2.caffemodel --points $MODEL_DIR/pts_in_hull.npy
```

##### Citations:


@inproceedings{zhang2016colorful,
  title={Colorful Image Colorization},
  author={Zhang, Richard and Isola, Phillip and Efros, Alexei A},
  booktitle={ECCV},
  year={2016}
}

[pyimagesearch: Black and white image colorization with OpenCV and Deep Learning](https://www.pyimagesearch.com/2019/02/25/black-and-white-image-colorization-with-opencv-and-deep-learning/)
