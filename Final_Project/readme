# 🍲 Recipe Generation with LSTM Networks

Welcome to the Recipe Generation project! This repository contains the code and resources used to build an LSTM-based model that generates cooking recipes. The model was trained using the **RecipeNLG** dataset, which includes over 2.2 million cooking recipes.

## 📂 Project Structure

- **`data/`**: This folder contains the dataset (e.g., `RecipeNLG_dataset.csv`). Due to the large file size, this file is not included in the repository.
- **`notebooks/`**: Jupyter notebooks for exploratory data analysis and model development.
- **`models/`**: Saved models and tokenizers.
- **`src/`**: Python scripts for data preprocessing, model training, and recipe generation.
- **`reports/`**: Documentation and the final project report.
- **`training_history.png`**: A visualization of the training and validation loss/accuracy.
- **`README.md`**: This file.

## 🛠️ Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Satyajithchary/META_SCIFOR_TECHNOLOGIES_ML_INTERNSHIP/Final_Project/major-project-receipe-generation.git
   cd recipe-generation-lstm
   ```

2. **Install Dependencies:**

   Make sure you have Python 3.7+ installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Dataset:**

   The dataset is not included in the repository due to its size. You can download the RecipeNLG dataset from Kaggle and place it in the `data/` directory.

## 🧑‍💻 Usage

### 1. Data Exploration and Preprocessing

```python
from src.preprocessing import load_and_preprocess_data

# Load and preprocess the data
df = load_and_preprocess_data('data/RecipeNLG_dataset.csv')
```

### 2. Data Preparation

```python
from src.preprocessing import prepare_sequences

# Prepare input sequences and tokenizer
padded_sequences, tokenizer = prepare_sequences(df['processed_directions'], max_sequence_length=100, max_words=10000)
```

### 3. Model Building

```python
from src.model import build_model

# Build the LSTM model
model = build_model(vocab_size=10000, embedding_dim=100, max_sequence_length=99)
```

### 4. Training

```python
from src.training import train_model

# Train the model
history = train_model(model, X_train, y_train, epochs=50, batch_size=128)
```

### 5. Recipe Generation

```python
from src.generation import generate_recipe

# Generate a new recipe
seed_text = "to make chicken soup"
generated_recipe = generate_recipe(model, tokenizer, seed_text, max_sequence_length=99, num_words=50)
print(generated_recipe)
```

## 📊 Results and Evaluation

The model was trained for 50 epochs, and the training and validation loss/accuracy were tracked. 

## 🚀 Project Report

The complete documentation, including the methodology, model performance, challenges, and generated recipes, is available in the `reports/` directory.

## 💡 Future Work

- **Improve Model Performance:** Experiment with different model architectures, such as GRU or Transformer-based models.
- **Incorporate Ingredients:** Train the model to generate recipes with a focus on the ingredients.
- **Recipe Personalization:** Implement a feature that generates recipes based on user preferences or dietary restrictions.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
