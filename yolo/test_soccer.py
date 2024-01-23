from ultralytics import YOLO

model = YOLO('runs/detect/soccer_yolov8m_v8_300e_16b/weights/best.pt')

metrics = model.val(
    name='yolov8m_soccer_eval_val_640',
    split='val'
)  # no arguments needed, dataset and settings remembered

metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category

print(metrics.box.map50)
