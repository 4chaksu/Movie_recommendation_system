# 🎬 Movie Recommendation System

This project is a **Content-Based Movie Recommender System** that suggests similar movies based on user selection. It uses metadata like movie genres, cast, crew, keywords, and overview to find recommendations using **cosine similarity**.

---

## ✅ Features

- Built using the **TMDB dataset** with 5,000 movies.
- Extracts and combines relevant content: **overview, genres, keywords, cast, and crew**.
- Performs **text preprocessing** and **vectorization** to understand movie similarities.
- Recommends **Top 5 similar movies** based on **cosine similarity**.
- A simple and clean **Streamlit UI** to interact with the system.

---

## 🧠 Approach

1. **Data Cleaning**: Removed irrelevant features and kept key columns like overview, genres, keywords, cast, and crew.
2. **Preprocessing**: Text cleaning and normalization.
3. **Vectorization**: Combined text features into a single string and applied **CountVectorizer**.
4. **Similarity Measure**: Used **cosine similarity** to compare movies.
5. **Recommendation**: Sorted and returned the top 5 most similar movies.

---

## 🛠️ Technologies & Tools Used

- **Python**
- **Pandas** (for data handling)
- **NLP & Text Preprocessing**
- **Scikit-learn** (for vectorization and cosine similarity)
- **Streamlit** (for user interface)
- **Jupyter Notebook** (for experimentation)
- **VS Code** (for development)

---

## 🚀 How to Run


1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Movie_recommendation_system.git
2. Navigate to the project directory
   ```bash
   cd Movie_recommendation_system
3. Install the dependencies
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit app
   ```bash
   streamlit run app.py
5. Open your browser and go to http://localhost:8501 to use the app.

---

## 📸 Demo
First image with input "Ironman"
  ![First image](https://github.com/4chaksu/Movie_recommendation_system/blob/main/Result/test_case_0.png)

second image with input "Skyfall"
  ![second image](https://github.com/4chaksu/Movie_recommendation_system/blob/main/Result/test_case_1.png)

third image with input "Batman"
  ![third image](https://github.com/4chaksu/Movie_recommendation_system/blob/main/Result/test_case_2.png)
  
---

## 📂 Dataset Source
  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 📬 Contact
  Created with ❤️ by Vinay  
  Connect with me on https://www.linkedin.com/in/vinaybora/
