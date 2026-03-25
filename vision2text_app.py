import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from PIL import Image

# Load model
model = load_model("best_model.h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load max length
with open("max_length.txt", "r") as f:
    max_length = int(f.read())

# Load CNN
base_model = VGG16(weights="vgg16_weights.h5")
cnn_model = Model(inputs=base_model.inputs, outputs=base_model.layers[-2].output)

# Functions
def index_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_caption(model, tokenizer, photo, max_length, top_k=2):
    photo = photo.reshape((1, 4096))
    in_text = 'startseq'

    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)

        yhat = model.predict([photo, sequence], verbose=0)

        yhat_probs = yhat[0]
        top_indices = np.argsort(yhat_probs)[-top_k:]
        yhat = np.random.choice(top_indices)

        word = index_to_word(yhat, tokenizer)

        if word is None:
            break

        in_text += ' ' + word

        if word == 'endseq':
            break

    return in_text

def clean_output(caption):
    words = caption.split()
    return ' '.join(words[1:-1])

def extract_feature(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    feature = cnn_model.predict(image, verbose=0)
    return feature[0]

# UI
st.title("🖼️ Vision2Text: AI Powered Image Caption Generator")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        feature = extract_feature(image)
        caption = generate_caption(model, tokenizer, feature, max_length)
        final_caption = clean_output(caption)

        st.success("Caption Generated!")
        st.write(final_caption)
        st.markdown("---")
        st.markdown("Built with ❤️ using Deep Learning")