import argparse

import wget


# ------------------------------------------------------------------------------
def main(destination_dir: str) -> int:

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
