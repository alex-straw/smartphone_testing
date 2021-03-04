import numpy as np
import cv2
import os

class phone:
    def __init__(self,number,thresh_lower,thresh_upper):
        self.number = number
        self.thresh_lower = thresh_lower
        self.thres_upper = thresh_upper


phone_1 = phone(1, 45, 105)
phone_2 = phone(2, 70, 102)
phone_3 = phone(3, 100, 150)
phone_4 = phone(4, 20, 255)

def get_phone_image(phone,current_path):
    image_path = current_path + '/photographs/phone_' + str(phone) + '.jpg'
    image = cv2.imread(image_path, 0)
    return(image)

def get_template(phone,current_path):
    image_path = current_path + '/photographs/phone_' + str(phone) + '_template.jpg'
    image = cv2.imread(image_path, 0)
    return(image)

def main():
    current_path = os.path.dirname(__file__)
    current_phone = phone_1

    image = get_phone_image(current_phone.number,current_path)
    template = get_template(current_phone.number,current_path)

    cv2.imshow("hi",template)
    cv2.waitKey(1000)


if __name__ == "__main__":
    main()