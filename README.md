# Child Drawing Classifier API

## Overview

This repository provides a **Flask-based** API for deploying a pre-trained **YOLOv8n-cls** model with a top-1 accuracy of **95.99%**. The model is specifically designed to classify children's drawings into four psychological categories:

- **Anger and aggression**
- **Anxiety**
- **Happy**
- **Sad**

The API processes an uploaded drawing and returns percentage-based predictions for each category, offering detailed insights into the psychological state conveyed in the image. The application is deployed on Render, making it accessible for seamless integration with web or mobile apps. The primary objective is to enable parents to analyze their children's drawings and gain insights into their emotional and psychological well-being.

This repository builds on work done in a previous repository, where multiple models were trained and evaluated. The previous repository can be found [here](https://github.com/HebaHamdan2/Psychological-Classification-of-Children-Drawings).
Among them, the **YOLOv8n-cls** model was selected due to its high accuracy and efficiency, making it suitable for real-world applications. This API serves as a foundation for integrating the prediction capabilities into user-friendly platforms.

## Features

- **Image Upload**: Accepts image files in `png`, `jpg`, or `jpeg` formats.
- **YOLOv8 Model**: Utilizes a pre-trained YOLOv8 classification model for psychological category predictions.
- **Dynamic Resizing**: Resizes images to the required input size for YOLO.
- **REST API**: Supports POST requests for predictions.
- **CORS Enabled**: Allows cross-origin resource sharing for flexible integrations.
  
## Demo
You can try out the demo by accessing the deployed API endpoint directly in your browser or through Postman.

**Demo Link:** https://childdrawingclassifier-api.onrender.com/predict

## Installation and Setup

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- Flask
- Pre-trained YOLOv8 model file (`best.pt`)
- Render account (for deployment)

### Clone the Repository

```bash
$ git clone https://github.com/HebaHamdan2/ChildDrawingClassifier-API.git
$ cd ./ChildDrawingClassifier-API
```

### Set Up a Virtual Environment

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

### Install Dependencies

```bash
$ pip install -r requirements.txt
```

### Model Setup

Place your pre-trained YOLOv8 model (`best.pt`) in the specified directory:

```plaintext
./YOLOv8n-cls Model/runs/classify/train/weights/
```

Ensure the model path in the code is correctly set:

```python
MODEL_PATH = os.getenv("MODEL_PATH", "./YOLOv8n-cls Model/runs/classify/train/weights/best.pt")
```

### Run Locally

Create an uploads directory for temporary file storage:

```bash
$ mkdir uploads
```

Start the Flask server:

```bash
$ python app.py
```

The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### `POST /predict`

#### Request

- Form-data with a key `image` containing the file to be classified.
- Supported formats: `png`, `jpg`, `jpeg`.

#### Response

- **200 OK**: Returns classification probabilities for each category.
- **400 Bad Request**: Missing or invalid image file.
- **500 Internal Server Error**: Server-side issues during inference.

#### Example Response

```json
{
    "predictions": {
        "Anger and aggression": "0.00%",
        "Anxiety": "0.03%",
        "Happy": "0.98%",
        "Sad": "98.99%"
    }
}
```

## Deployment on Render

### Prerequisites

- A Render account

Ensure the following files are in the repository:

- `app.py`: Flask application
- `requirements.txt`: List of dependencies
- Pre-trained YOLO model (`best.pt`)

### Steps

1. Push your code to GitHub:

   ```bash
   $ git add .
   $ git commit -m "Initial commit"
   $ git push origin main
   ```

2. Log in to Render and create a new Web Service.
3. Connect the repository.
4. Set the Build Command:

   ```bash
   pip install -r requirements.txt
   ```

5. Set the Start Command:

   ```bash
   python app.py
   ```

6. Add an environment variable for the port:

   ```plaintext
   PORT = 5000
   ```

7. Deploy the service.

The API will be accessible at the Render-provided URL.

## Future Enhancements

This API is designed to serve as the backend for web and mobile applications aimed at helping parents analyze their children’s drawings and monitor their psychological health. Future developments will focus on:

- Building user-friendly web and mobile interfaces.
- Expanding the model's capabilities with more psychological categories.
- Integrating additional datasets to improve accuracy and robustness.

## Contributing

Contributions are welcome! Please feel free to create an issue or submit a pull request for enhancements or bug fixes.
