import argparse
import os
import shutil

import wget


# ------------------------------------------------------------------------------
def main(destination_dir: str) -> int:
    """
    Download colorization model files provided by Richard Zhang et al.
    See https://richzhang.github.io/colorization/

    :param destination_dir: destination directory location for downloaded files
    :return: 0 if all goes as expected
    """

    # make sure directory exists, otherwise create it
    if not os.path.isdir(destination_dir):
        if os.path.exists(destination_dir):
            message = f"{destination_dir} already exists but is not a directory"
            raise ValueError(message)
        else:
            os.mkdir(destination_dir)

    # download model files from relevant URLs
    urls = [
        "https://github.com/richzhang/colorization/blob/master/colorization/resources/pts_in_hull.npy?raw=true",
        "https://raw.githubusercontent.com/richzhang/colorization/master/colorization/models/colorization_deploy_v2.prototxt",
        "http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel"
    ]
    for url in urls:
        filename = wget.download(url)
        shutil.move(filename, os.sep.join((destination_dir, filename)))

    # successful completion
    return 0


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    # USAGE
    # python download_model_files.py --dest ../model

    # construct the argument parser and parse the arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-d",
                             "--dest",
                             type=str,
                             required=True,
                             help="destination directory for downloaded files")
    args = vars(args_parser.parse_args())

    main(args["dest"])
