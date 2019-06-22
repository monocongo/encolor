import cv2
import numpy as np


class Encolorizer():

    def __init__(self,
                 prototxt_path: str,
                 model_path: str,
                 points_path: str):

        # load the serialized colorizer model and cluster center points from disk
        self.network = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
        self.cluster_center_points = np.load(points_path)

        # add the cluster centers as 1x1 convolutions to the model
        class8 = self.network.getLayerId("class8_ab")
        conv8 = self.network.getLayerId("conv8_313_rh")
        self.cluster_center_points = self.cluster_center_points.transpose().reshape(2, 313, 1, 1)
        self.network.getLayer(class8).blobs = [self.cluster_center_points.astype("float32")]
        self.network.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    def colorize(self,
                 image: np.ndarray) -> np.ndarray:

        # load the input image from disk, scale the pixel intensities to the
        # range [0, 1], and then convert the image from the BGR to Lab color space
        scaled = image.astype("float32") / 255.0
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

        # resize the Lab image to 224x224 (the dimensions that
        # the colorization network accepts), split the channels,
        # extract the 'L' channel, and then perform mean centering
        resized_lab = cv2.resize(lab, (224, 224))
        l_channel = cv2.split(resized_lab)[0]
        l_channel -= 50

        # pass the 'L' channel through the network which
        # will predict the 'a' and 'b' channel values
        'print("[INFO] colorizing image...")'
        self.network.setInput(cv2.dnn.blobFromImage(l_channel))
        ab_channels = self.network.forward()[0, :, :, :].transpose((1, 2, 0))

        # resize the predicted 'ab' volume to the same dimensions as the input image
        ab_channels = cv2.resize(ab_channels, (image.shape[1], image.shape[0]))

        # grab the 'L' channel from the *original* input image
        # (not the resized one) and concatenate the original
        # 'L' channel with the predicted 'ab' channels
        l_channel = cv2.split(lab)[0]
        colorized = np.concatenate((l_channel[:, :, np.newaxis], ab_channels), axis=2)

        # convert the output image from the Lab color space to RGB, then
        # clip any values that fall outside the range [0, 1]
        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
        colorized = np.clip(colorized, 0, 1)

        # the current colorized image is represented as a floating point
        # data type in the range [0, 1] -- convert it to an unsigned
        # 8-bit integer representation in the range [0, 255]
        colorized = (255 * colorized).astype("uint8")

        return colorized
