import argparse

import cv2

from encolor.encolorize import Encolorizer


# ------------------------------------------------------------------------------
def colorize_video(video_path: str,
                   prototxt_path: str,
                   model_path: str,
                   points_path: str) -> int:

    encolorizer = Encolorizer(prototxt_path, model_path, points_path)

    print("[INFO] opening video file...")
    vs = cv2.VideoCapture(video_path)

    # loop over frames from the video stream
    while True:

        # grab the next frame and handle if we are reading from either
        # VideoCapture or VideoStream
        frame = vs.read()
        frame = frame[1]

        # if we are viewing a video and we did not grab a frame then we
        # have reached the end of the video
        if frame is None:
            break

        colorized = encolorizer.colorize(frame)

        # show the colorized frames
        cv2.imshow("Colorized", colorized)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # release the video file pointer
    vs.release()

    # close any open windows
    cv2.destroyAllWindows()

    return 0


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    # USAGE
    # python colorize_video.py --video ~/data/video/train_station_bw.mp4 \
    #     --prototxt model/colorization_deploy_v2.prototxt \
    #     --model model/colorization_release_v2.caffemodel \
    #     --points model/pts_in_hull.npy

    # construct the argument parser and parse the arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-i",
                             "--video",
                             type=str,
                             required=True,
                             help="path to input black and white video MP4")
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
    args_parser.add_argument("-w",
                             "--width",
                             type=int,
                             default=500,
                             help="input width dimension of frame")
    args = vars(args_parser.parse_args())

    colorize_video(args["video"], args["prototxt"], args["model"], args["points"])
