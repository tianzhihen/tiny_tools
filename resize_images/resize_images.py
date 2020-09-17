import os
import cv2
import argparse
from tqdm import tqdm


def resize_images(input_dir, output_path, img_width, img_height):
    image_names = os.listdir(input_dir)
    for idx, img_name in enumerate(tqdm(image_names)):
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_width, img_height))
        cv2.imwrite(os.path.join(output_path, img_name), img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str, help='your image input dir path')
    parser.add_argument('output_path', type=str, help='your image output dir path')
    parser.add_argument('target_width', type=int, help='target image width')
    parser.add_argument('target_height', type=int, help='target image height')
    args = parser.parse_args()

    resize_images(args.input_path, args.output_path, args.target_width, args.target_height)
