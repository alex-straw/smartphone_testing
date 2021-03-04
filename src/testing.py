import numpy as np
import cv2
import os
import matplotlib.pyplot as plt


class phone:
    def __init__(self,number,thresh_lower,thresh_upper,actual_battery_centre):
        self.number = number
        self.thresh_lower = thresh_lower
        self.thres_upper = thresh_upper
        self.actual_battery_centre = actual_battery_centre

phone_1 = phone(1, 45, 105,[754,1168])
phone_2 = phone(2, 70, 102,[939,1042])
phone_3 = phone(3, 100, 150,[663,1278])
phone_4 = phone(4, 20, 255,[1174,1607])

def get_phone_image(phone,current_path):
    image_path = current_path + '/photographs/phone_' + str(phone) + '.jpg'
    image = cv2.imread(image_path, 0)
    return(image)

def get_template(phone,current_path):
    image_path = current_path + '/photographs/phone_' + str(phone) + '_template.jpg'
    image = cv2.imread(image_path, 0)
    return(image)

def scale_image(image,scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return(image)

def plot_all(image,current_phone,final_plot_scale):
    windowhandle = "Finding battery for phone " + str(current_phone.number)

    hori = np.concatenate((image,image), axis = 1)
    hori = scale_image(hori,final_plot_scale)

    cv2.imshow(windowhandle,hori)
    cv2.waitKey(10000)

def main():
    current_path = os.path.dirname(__file__)
    current_phone = phone_2
    final_plot_scale = 20

    image = get_phone_image(current_phone.number,current_path)
    template = get_template(current_phone.number,current_path)
    actual_battery_centre = current_phone.actual_battery_centre

    plot_all(image,current_phone,final_plot_scale)

if __name__ == "__main__":
    main()