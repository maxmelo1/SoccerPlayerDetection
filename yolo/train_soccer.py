from ultralytics import YOLO

#!cat pothole_v8.yaml



# Load the model.
model = YOLO('yolov8m.pt')

# Training.
results = model.train(
   data='soccer.yaml',
   imgsz=640,
   epochs=300,
   batch=16,
   name='soccer_yolov8m_v8_300e_16b',
   plots=True,
   patience=150,
)
