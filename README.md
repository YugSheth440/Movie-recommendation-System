## 🎬 Project Overview
This system suggests similar movies based on content features like:
- Genre
- Cast members
- Director
- Plot keywords
- Overview text

Using cosine similarity, it finds the most relevant matches from the TMDB dataset.

## ✨ Key Features
- **Smart Recommendations**: Returns top 5 most similar movies
- **Multi-feature Analysis**: Combines:
  - Title
  - Genre
  - Keywords
  - Cast
  - Director
- **User-Friendly**: Simple CLI/Web interface
- **Fast Performance**: Optimized for quick responses

## 📊 Dataset Details
**TMDB 5000 Movie Dataset** includes:
- 4,803 movies
- 24 features per movie
- **Primary features used**:
  - `title`
  - `genres` 
  - `keywords`
  - `overview`
  - `cast`
  - `crew`

Dataset source: [The Movie Database (TMDB)](https://www.themoviedb.org/)
