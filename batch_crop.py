import cv2
import os
import sys

src_dir = sys.argv[1]
dest_dir = sys.argv[2]

for img_name in os.listdir(src_dir):

    img = cv2.imread(f"{src_dir}/{img_name}")

    img_w = img.shape[1]
    w_crop_factor = 0.15
    img = img[:, int(img_w * w_crop_factor):int(img_w - img_w * w_crop_factor)]

    img_h = img.shape[0]
    h_crop_factor_top = 0.1
    h_crop_factor_bottom = 0.07
    img = img[int(img_h * h_crop_factor_top):int(img_h * (1 - h_crop_factor_bottom)), :]

    cv2.imwrite(f"{dest_dir}/{img_name}", img)
