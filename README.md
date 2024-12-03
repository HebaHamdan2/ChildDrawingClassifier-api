#  Overview

This repository contains a Flask-based web API for image classification using the **YOLOv8n-cls** model. The API can classify images, such as children's drawings, into psychological categories like **'Anger and aggression', 'Anxiety', 'Happy', and 'Sad'**, and return the percentage prediction for each category. It is designed to be deployed on platforms like **Render** and tested locally or via tools like **Postman**.

## Features

- **Real-time image classification**: Classifies children's drawings into four psychological categories.
- **Pre-trained YOLOv8n-cls model**: Utilizes a state-of-the-art deep learning model for accurate predictions.
- **Image Upload**: Accepts image files in PNG, JPG, or JPEG formats.
- **Dynamic Resizing**: Resizes images to the required input size for YOLO.
- **REST API**: Supports POST requests for predictions.
- **CORS Enabled**: Allows cross-origin resource sharing for flexibility.
- **Easy Deployment**: Deployed on Render for accessibility and scalability.
- **Cross-origin resource sharing (CORS)**: Ensures seamless integration with frontend applications.

## Demo

The API is currently live and can be tested via Postman or any HTTP client:

**API Endpoint**: [https://childdrawingclassifier-api.onrender.com/predict](https://childdrawingclassifier-api.onrender.com/predict)

## Technologies Used

- **Programming Language**: Python
- **Framework**: Flask
- **Deep Learning Library**: Ultralytics YOLO
- **Image Processing**: Pillow (PIL)
- **Deployment Platform**: Render
- **Web API Client**: Postman (for testing)

## Installation and Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- pip (Python package installer)
- Git
- Virtual environment (optional but recommended)
- A pre-trained YOLOv8 model file (`best.pt`)

### Clone the Repository

```bash
git clone https://github.com/yourusername/children-drawings-psychology-api.git
cd children-drawings-psychology-api
