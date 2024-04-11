from flask import Flask, render_template, request
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from transformers import pipeline

app = Flask(__name__)
image_model = MobileNet(weights='imagenet', include_top=True)  # Use MobileNet for faster inference
summarizer = pipeline('summarization')

@app.route('/', methods=['GET', 'POST'])
def predict_and_summarize():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # Text summarization
        article = request.form.get('article', '')  # Assuming the input textarea in index.html has name 'article'
        summarized_text = summarizer(article, max_length=300, min_length=10, do_sample=False)
        summary = summarized_text[0]['summary_text']

        # Image classification
        # Commenting out image classification as it's not used in the current route

        return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
