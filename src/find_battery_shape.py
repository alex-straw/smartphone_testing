import numpy as np
import cv2
from matplotlib import pyplot as plt

def no_op(no_op):
    pass

def draw_crosshair(image,battery_centre):
    cv2.drawMarker(image,battery_centre, color=(255),markerType=cv2.MARKER_CROSS,markerSize=200,thickness=10)
    return(image)

""" MAIN EQUIVALENT """

def find_shape(image,thresh_low,thresh_high):

    # Convert to greyscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert to binary image by thresholding

    ret, thresh = cv2.threshold(image, thresh_low, 255, cv2.THRESH_BINARY_INV)
    ret2, thresh2 = cv2.threshold(image, thresh_high, 255, cv2.THRESH_BINARY)

    """ Combine image matrices from the two threshold operations : OR """

    combination_thresh = cv2.bitwise_or(thresh, thresh2)

    """ NOT flips 0s to 1s in the black & white image """

    inverse_thresh = cv2.bitwise_not(combination_thresh)

    contours = cv2.findContours(inverse_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]

    for cnt in contours:
        if cv2.contourArea(cnt) > 30000:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            cv2.drawContours(image, [approx], 0, (255, 100, 0), 3)

            x, y = approx[0][0]

            if len(approx) == 4:
                cv2.putText(image, "Battery", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

                centre_x = (approx[0][0][0] + approx[1][0][0] + approx[2][0][0] + approx[3][0][0]) / 4
                centre_y = (approx[0][0][1] + approx[1][0][1] + approx[2][0][1] + approx[3][0][1]) / 4

                battery_centre = (int(centre_x), int(centre_y))

                image = draw_crosshair(image, battery_centre)

                label = ("BATTERY CENTRE X: " + str(battery_centre[0]) + " Y:" + str(battery_centre[1]))
                image = cv2.putText(image, label, (25, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
            else:
                pass
    return(image,battery_centre)

if __name__ == '__main__':
    # find_battery_features.py executed as script
    # do something
    find_shape()


