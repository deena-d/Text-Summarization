# Text Summarization and Image Classification Web App

This project is a web application that performs text summarization and image classification tasks.

## Features

- **Text Summarization**: Given an article or text input, the application summarizes the content using the Hugging Face Transformers library.
- **Image Classification** (commented out): The application can also classify images using the MobileNet model from Keras with pre-trained weights from ImageNet.
- **Web Interface**: Provides a user-friendly web interface for users to input text and receive summaries.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask web application by executing `python app.py`.
4. Open your web browser and navigate to `http://localhost:8000`.
5. Enter text in the input field and click the "Summarize" button to generate a summary.

## Requirements

- Python 3.x
- Flask
- TensorFlow
- Hugging Face Transformers
- Keras

## Author

DEENA D

## License

This project is licensed under the [MIT License](LICENSE).
