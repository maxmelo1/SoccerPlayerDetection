# SoccerPlayerDetection
Demo for testing mmdetection and YOLO v8 in the roboflow "Soccer Player Detection Computer Vision Project" tutorial dataset


## Dataset

The dataset is available at [Roboflow](https://universe.roboflow.com/prestona/soccer-player-detection-pk7eg). The data consists in images containing screenshots of soccer games streaming. The classes are the soccer players, goal keepers, referee/staff and the ball. The dataset was splitted in 429 training images, 124 validation images and 62 test images.

## Models

Models evaluated: YOLO v8m and RTMDet.

## Results

| Model   | Set | Epochs | MAP-50 |
|---------|-----|--------|--------|
| RTMDet  | Val |   300  | 0.726  |
| YOLO v8 | Val |   300  | 0.962  |