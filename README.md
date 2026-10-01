# AI Object Detector

A simple real-time AI object detector built with Python, OpenCV, and Ultralytics YOLO11.

The app uses your webcam, detects objects in real time, and displays bounding boxes, labels, and confidence scores.

## Features

- Real-time webcam object detection
- YOLO11 Nano pretrained model
- Bounding boxes and class labels
- Confidence scores
- Simple setup
- Press `Q` to quit

## Requirements

- Python 3
- A webcam

## Installation

Clone the repository and move into the project folder:

```bash
git clone https://github.com/dyogocodes/ai-object-detector.git
cd ai-object-detector
```

Optional but recommended, create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The YOLO11 Nano model file, `yolo11n.pt`, is downloaded automatically the first time the program runs.

Press `Q` while the detector window is active to stop the program.

## How it works

1. OpenCV captures frames from your webcam.
2. YOLO11 analyzes each frame.
3. Detected objects are drawn onto the frame.
4. OpenCV displays the annotated video in real time.

## Tech Stack

- Python
- OpenCV
- Ultralytics YOLO11
