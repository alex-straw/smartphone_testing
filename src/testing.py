import numpy as np
import cv2
import os

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
    phone = 1

    image = get_phone_image(phone,current_path)
    template = get_template(phone,current_path)

if __name__ == "__main__":
    main()