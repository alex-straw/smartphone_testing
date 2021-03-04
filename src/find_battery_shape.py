import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def draw_crosshair(image,battery_centre):
    cv2.drawMarker(image,battery_centre, color=(255),markerType=cv2.MARKER_CROSS,markerSize=200,thickness=10)
    return(image)

def remove_background(image):
    ret, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    background_removed = cv2.bitwise_or(thresh,image)
    return(background_removed)


def find_shape(image,thresh_low,thresh_high,epsilon,cnt_area):

    ret, thresh = cv2.threshold(image, thresh_low, 255, cv2.THRESH_BINARY_INV)
    ret2, thresh2 = cv2.threshold(image, thresh_high, 255, cv2.THRESH_BINARY)

    """ Combine image matrices from the two threshold operations : OR """

    combination_thresh = cv2.bitwise_or(thresh, thresh2)

    """ NOT flips 0s to 1s in the black & white image """

    inverse_thresh = cv2.bitwise_not(combination_thresh)

    # Find the contours
    contours, _ = cv2.findContours(inverse_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # For each contour approximate the curve and
    # detect the shapes.
    for cnt in contours:
        if cv2.contourArea(cnt) > cnt_area:
            epsilon = epsilon * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            cv2.drawContours(image, [approx], 0, (255, 100, 0), 20)

            if len(approx) == 4:
                centre_x = (approx[0][0][0] + approx[1][0][0] + approx[2][0][0] + approx[3][0][0]) / 4
                centre_y = (approx[0][0][1] + approx[1][0][1] + approx[2][0][1] + approx[3][0][1]) / 4

                battery_centre = (int(centre_x), int(centre_y))

                label = ("BATTERY CENTRE X: " + str(battery_centre[0]) + " Y:" + str(battery_centre[1]))
                image = cv2.putText(image, label, (250, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, color = (0, 0, 255),thickness=8)
                image = draw_crosshair(image, battery_centre)
        else:
            pass

    return(image,battery_centre)

if __name__ == '__main__':
    # find_battery_features.py executed as script
    find_shape()