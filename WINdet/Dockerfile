#Dockerfile

FROM python:3.11.3

WORKDIR /ASHIcode

COPY ./private /ASHIcode/private
COPY ./main.py /ASHIcode/main.py
COPY ./yolov8m_windet.pt /ASHIcode/yolov8m_windet.pt

RUN apt update
RUN apt install -y libgl1-mesa-dev
RUN pip install torch torchvision ultralytics dill



CMD ["python","main.py"]