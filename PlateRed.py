import cv2
import numpy as np
import os
import DetectChars
import DetectPlates
import PossiblePlate

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 255.0, 0.0)

showSteps = False

def main():
    
    blnKNNTrainingSuccesful = DetectChars.loadblnKNNDataAndTrainKSS()

    if blnKNNTrainingSuccesful != False:
        pass
    else:
        printf("Error404")
    return

    imgOriginalScene = cv2.imread("2.png")