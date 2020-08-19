import os
import cv2
from tqdm import tqdm


def gen_video(input_dir, output_path):
    image_names = os.listdir(input_dir)
    image_names.sort()

    video_writer = cv2.VideoWriter(output_path,
                                   cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (1280, 720))

    for idx, img_name in enumerate(tqdm(image_names)):
        print("progress: {}".format(idx/len(image_names)))
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)
        video_writer.write(img)
    video_writer.release()

if __name__ == '__main__':
    input_path = "your input dir path"
    output_path = "your output video path"
    gen_video(input_path, output_path)
