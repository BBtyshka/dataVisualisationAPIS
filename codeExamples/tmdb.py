import requests

api_key = 'your_api_key_here'
time_window = 'day'  # or 'week'

url = f"https://api.themoviedb.org/3/trending/movie/{time_window}"
params = {
    'api_key': api_key
}

response = requests.get(url, params=params)
data = response.json()

for movie in data['results']:
    print(f"Title: {movie['title']}, Release Date: {movie.get('release_date')}, Popularity: {movie.get('popularity')}")
