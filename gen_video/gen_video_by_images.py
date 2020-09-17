import os
import cv2
import argparse
from tqdm import tqdm


def gen_video(input_dir, output_path, img_width, img_height, fps=20):
    image_names = os.listdir(input_dir)
    image_names.sort()

    if not img_width or not img_height:
        img_height, img_width, _ = cv2.imread(os.path.join(input_dir, image_names[-1])).shape
    video_writer = cv2.VideoWriter(output_path,
                                   cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (img_width, img_height))

    for idx, img_name in enumerate(tqdm(image_names)):
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_width, img_height))
        video_writer.write(img)
    video_writer.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str, help='your input dir path')
    parser.add_argument('output_path', type=str, help='your output video path')
    parser.add_argument('--img_width', type=int, default=None, help='image width')
    parser.add_argument('--img_height', type=int, default=None, help='your output video path')
    parser.add_argument('--fps', type=int, default=20, help='your output video path')
    args = parser.parse_args()

    gen_video(args.input_path, args.output_path, args.img_width, args.img_height, args.fps)
