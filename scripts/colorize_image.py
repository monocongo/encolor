import argparse

import cv2

from encolor.encolorize import Encolorizer


# ------------------------------------------------------------------------------
def colorize_image(image_path: str,
                   prototxt_path: str,
                   model_path: str,
                   points_path: str) -> int:

    encolorizer = Encolorizer(prototxt_path, model_path, points_path)
    image = cv2.imread(image_path)
    colorized = encolorizer.colorize(image)

    # show the original and output colorized images
    cv2.imshow("Original", image)
    cv2.imshow("Colorized", colorized)
    cv2.waitKey(0)

    return 0


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    # USAGE
    # python colorize_image.py --image images/robin_williams.jpg \
    #     --prototxt model/colorization_deploy_v2.prototxt \
    #     --model model/colorization_release_v2.caffemodel \
    #     --points model/pts_in_hull.npy

    # construct the argument parser and parse the arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-i",
                             "--image",
                             type=str,
                             required=True,
                             help="path to input black and white image")
    args_parser.add_argument("-p",
                             "--prototxt",
                             type=str,
                             required=True,
                             help="path to Caffe prototxt file")
    args_parser.add_argument("-m",
                             "--model",
                             type=str,
                             required=True,
                             help="path to Caffe pre-trained model")
    args_parser.add_argument("-c",
                             "--points",
                             type=str,
                             required=True,
                             help="path to cluster center points")
    args = vars(args_parser.parse_args())

    colorize_image(args["image"], args["prototxt"], args["model"], args["points"])
