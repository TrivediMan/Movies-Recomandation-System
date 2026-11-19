<div align="center">

# 🎬 Movie Recommender System

**Content-based movie recommendation app built with Python, Scikit-learn and Streamlit.**

Pick a movie you like and get 5 similar movies instantly.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://movies-recomandation-system.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### 👉 [Try the live app](https://movies-recomandation-system.streamlit.app/) 👈

</div>

---

## 📌 About the Project

This project recommends movies based on **content similarity**. Instead of using user ratings, it compares movies using their **overview, genres, keywords, top 3 cast members and director**. Movies whose content is closest to the selected movie are shown as recommendations.

The model is trained on the **TMDB 5000 Movies dataset** and deployed as a web app using **Streamlit Cloud**.

## ✨ Features

- 🔍 Search or select from 4,800+ movies using a dropdown
- ⚡ Get **5 similar movies** with one click
- 🧠 Content-based filtering using **Bag of Words + Cosine Similarity**
- 🚀 Fast loading with Streamlit caching (`st.cache_data`, `st.cache_resource`)
- 🛡️ Error handling for missing or mismatched model files
- 🌐 Deployed online, no installation needed to try it

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn (CountVectorizer, Cosine Similarity) |
| Model Storage | Joblib / Pickle |
| Web App | Streamlit |
| Deployment | Streamlit Community Cloud |
| Large File Storage | Git LFS |

## 🧠 How It Works

```
TMDB Dataset (movies + credits)
        │
        ▼
Merge datasets on movie title
        │
        ▼
Keep: overview, genres, keywords, cast (top 3), crew (director)
        │
        ▼
Clean text (remove spaces in names, e.g. "Sam Worthington" → "SamWorthington")
        │
        ▼
Combine everything into a single "tags" column
        │
        ▼
CountVectorizer (5000 features, English stop words removed)
        │
        ▼
Cosine Similarity matrix (movies × movies)
        │
        ▼
Top 5 most similar movies → shown in Streamlit app
```

**Step by step:**

1. **Data merging:** `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` are merged on the movie title.
2. **Feature selection:** Only useful columns are kept: `overview`, `genres`, `keywords`, `cast`, `crew`.
3. **Preprocessing:** JSON-like text is converted to lists, the top 3 actors and the director are extracted, and spaces inside names are removed so each person becomes one unique token.
4. **Tag creation:** All features are joined into one `tags` text per movie.
5. **Vectorization:** `CountVectorizer` converts tags into vectors using the 5000 most common words.
6. **Similarity:** `cosine_similarity` calculates how close every movie is to every other movie.
7. **Recommendation:** For the selected movie, the 5 movies with the highest similarity score are returned.

## 📁 Project Structure

```
Movies-Recomandation-System/
│
├── Data/
│   ├── tmdb_5000_movies.csv      # Movies metadata
│   └── tmdb_5000_credits.csv     # Cast and crew data
│
├── Model/
│   ├── movie_list.pkl            # Processed movie data
│   └── similarity.pkl            # Similarity matrix (stored with Git LFS)
│
├── Notebook/
│   └── Movies Recomandation.ipynb  # Data cleaning, model building, experiments
│
├── app.py                        # Streamlit web app
├── requirements.txt              # Python dependencies
├── .gitattributes                # Git LFS configuration
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

`similarity.pkl` is stored with **Git LFS**, so install Git LFS first from [git-lfs.com](https://git-lfs.com).

```bash
git lfs install
git clone https://github.com/TrivediMan/Movies-Recomandation-System.git
cd Movies-Recomandation-System
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## 🔁 Regenerate the Model (Optional)

If you want to rebuild `movie_list.pkl` and `similarity.pkl` yourself:

1. Open `Notebook/Movies Recomandation.ipynb` in Jupyter Notebook or VS Code.
2. Run all cells from top to bottom.
3. The notebook saves the new files inside the `Model/` folder.

> 💡 **Tip:** To reduce file size, save with compression:
> `joblib.dump(similarity, "similarity.pkl", compress=3)`

## 📊 Dataset

- **Source:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (Kaggle)
- **Files used:** `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`

## 🔮 Future Improvements

- [ ] Show movie posters using the TMDB API
- [ ] Add movie details (rating, release year, overview) on click
- [ ] Use TF-IDF or word embeddings for better similarity
- [ ] Add genre and year filters
- [ ] Hybrid recommendation (content + collaborative filtering)
- [ ] Reduce model size for faster loading

## 🤝 Contributing

Suggestions and improvements are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 👤 Author

**Man Trivedi**

- GitHub: [@TrivediMan](https://github.com/TrivediMan)

---

<div align="center">

⭐ If you like this project, please give it a star on GitHub!

</div>
