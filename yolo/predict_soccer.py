from ultralytics import YOLO
import matplotlib.pyplot as plt

import argparse



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model_path', type=str, default='./runs/detect/soccer_yolov8m_v8_300e_16b/weights/best.pt')
    parser.add_argument('--image_path', type=str, default='./datasets/SoccerPlayerDetectionyolov8/test/images/798b45_3_7_png_jpg.rf.65da737c630bf725764deff92ce8ce5d.jpg', help='path to the image')
        
    args = parser.parse_args()

    model = YOLO(args.model_path)

    results = model(args.image_path) 

    for r in results:
        if r.boxes.conf[0] > 0.5:

            im_array = r.plot()[...,::-1]

            plt.imshow(im_array)
            plt.show()


if __name__ == "__main__":
    main()