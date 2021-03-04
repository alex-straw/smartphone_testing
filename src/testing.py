import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

import find_battery_template
import find_battery_features

class phone:
    def __init__(self,number,thresh_lower,thresh_upper,actual_battery_centre):
        self.number = number
        self.thresh_lower = thresh_lower
        self.thresh_upper = thresh_upper
        self.actual_battery_centre = actual_battery_centre

phone_1 = phone(1, 39, 66,[754,1168])
phone_2 = phone(2, 22, 56,[939,1042])
phone_3 = phone(3, 55, 102,[663,1278])
phone_4 = phone(4, 51, 153,[1174,1607])

def get_phone_image(phone,current_path):
    image_path = current_path + '/photographs/phone_' + str(phone) + '.jpg'
    image = cv2.imread(image_path, 0)
    return(image)

def get_template(phone,current_path):
    image_path = current_path + '/photographs/phone_' + str(phone) + '_template.jpg'
    image = cv2.imread(image_path, 0)
    return(image)

def calculate_average_error(true_centre,estimated_centre):

    def error(true_value,estimated_value):
        error_decimal = ( abs(true_value - estimated_value) / true_value )
        return(error_decimal)

    error_x = error(true_centre[0],estimated_centre[0])
    error_y = error(true_centre[1], estimated_centre[1])

    average_error = (error_x + error_y)/2

    return(average_error)


def scale_image(image,scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return(image)

def plot_images(image,windowhandle,final_plot_scale):

    image = scale_image(image, final_plot_scale)
    cv2.namedWindow(windowhandle)  # Create a named window
    cv2.moveWindow(windowhandle, 40, 30)  # Move it to (40,30)
    cv2.imshow(windowhandle, image)
    cv2.waitKey(10000)

def main():
    current_path = os.path.dirname(__file__)
    current_phone = phone_1
    final_plot_scale = 30
    thresh_l = current_phone.thresh_lower
    thresh_h = current_phone.thresh_upper
    window_handle = "phone " + str(current_phone.number)

    image = get_phone_image(current_phone.number,current_path)
    template = get_template(current_phone.number,current_path)

    """ TEMPLATE MATCH USING find_battery_template.py """

    located_image_template,template_centre = find_battery_template.find_template(image,template)
    located_image_features,features_centre = find_battery_features.find_features(image,thresh_l,thresh_h)


    error = calculate_average_error(current_phone.actual_battery_centre, features_centre)

    plot_images(located_image_features,window_handle,final_plot_scale)
    print(error*100)

if __name__ == "__main__":
    main()