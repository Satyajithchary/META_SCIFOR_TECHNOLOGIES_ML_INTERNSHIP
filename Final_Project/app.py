import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the model and tokenizer
model = tf.keras.models.load_model(recipe_generation_model.h5)
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

max_sequence_len = 100  # Set this to the value used during training

st.title('Recipe Generation App')

input_text = st.text_input('Enter the start of your recipe:')

if st.button('Generate Recipe'):
    if input_text:
        # Preprocess the input text
        token_list = tokenizer.texts_to_sequences([input_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')

        # Generate the recipe
        predicted = model.predict_classes(token_list, verbose=0)

        # Decode the prediction to text
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break

        st.write('Generated Recipe:', input_text + " " + output_word)
    else:
        st.write('Please enter some text to start the recipe.')
