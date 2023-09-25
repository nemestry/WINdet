# импортируем библиотеки
from ultralytics import YOLO

model=YOLO('yolov8m_windet.pt') # обученная модель

pre = model.predict(
    source="./private/images",
    show=True,
    imgsz=640,
    save=True,
    name="output",
    conf=0.5,
)
