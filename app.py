import pickle
import joblib
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------
# 1. Project paths
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Model"

MOVIE_FILE = MODEL_DIR / "movie_list.pkl"
SIMILARITY_FILE = MODEL_DIR / "similarity.pkl"


# --------------------------------
# 2. Load model files
# --------------------------------

def load_model(file_path):

    if not file_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {file_path}"
        )

    # First try Joblib (supports compressed Joblib files)
    try:
        return joblib.load(file_path)

    except Exception as joblib_error:

        # Then try standard Pickle
        try:
            with open(file_path, "rb") as file:
                return pickle.load(file)

        except Exception as pickle_error:
            raise RuntimeError(
                f"Cannot load {file_path.name}.\n"
                f"Joblib error: {joblib_error}\n"
                f"Pickle error: {pickle_error}\n"
                "The file may be corrupted or saved in "
                "another format. Regenerate the file."
            )


# --------------------------------
# 3. Load movie data
# --------------------------------

@st.cache_data
def get_movies():
    return load_model(MOVIE_FILE)


@st.cache_resource
def get_similarity():
    return load_model(SIMILARITY_FILE)


# --------------------------------
# 4. Recommendation function
# --------------------------------

def recommend(movie):

    movie_indices = movies.index[
        movies["title"] == movie
    ].tolist()

    if not movie_indices:
        return []

    index = movie_indices[0]

    movie_scores = similarity[index]

    # Handle sparse similarity matrices
    if hasattr(movie_scores, "toarray"):
        movie_scores = movie_scores.toarray().flatten()
    else:
        movie_scores = np.asarray(movie_scores).flatten()

    distances = sorted(
        list(enumerate(movie_scores)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:

        recommended_movies.append(
            movies.iloc[i[0]]["title"]
        )

    return recommended_movies


# --------------------------------
# 5. Streamlit application
# --------------------------------

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommender System")

try:

    movies = get_movies()
    similarity = get_similarity()

    if not isinstance(movies, pd.DataFrame):
        movies = pd.DataFrame(movies)

    if "title" not in movies.columns:
        st.error("Movie dataset must contain a title column.")
        st.stop()

    if len(movies) != similarity.shape[0]:
        st.error(
            "Movie data and similarity matrix dimensions "
            "do not match. Regenerate both files."
        )
        st.stop()
        
            
    movie_list = movies["title"].dropna().values

    selected_movie = st.selectbox(
        "Type or select a movie",
        movie_list
    )

    if st.button("Show Recommendation"):

        recommendations = recommend(selected_movie)

        if recommendations:

            st.subheader("Recommended Movies")

            cols = st.columns(5)

            for col, movie_name in zip(
                cols, recommendations
            ):

                with col:
                    st.markdown(f"### 🎥 {movie_name}")

        else:
            st.warning("No recommendations found.")

except Exception as e:

    st.error(f"Application Error: {e}")

    st.info(
        "Check your Model folder and regenerate "
        "the model files if necessary."
    )
