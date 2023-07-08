import requests
import json
import tkinter as tk

api_key = "575e0611"

base_url = "http://www.omdbapi.com/"

def search_movie():
    
    movie_title = movie_entry.get()
    
    complete_url = base_url + "?t=" + movie_title + "&apikey=" + api_key
    
    response = requests.get(complete_url)
    
    movie_data = json.loads(response.content.decode())
    
    result_label.config(text="")
    
    if movie_data["Response"] == "False":
    
        result_label.config(text="Movie not found!")
    else:
        title = movie_data["Title"]
        year = movie_data["Year"]
        genre = movie_data["Genre"]
        director = movie_data["Director"]
        plot = movie_data["Plot"]
        imdb_rating = movie_data["imdbRating"]
        metascore = movie_data["Metascore"]
        
        result_label.config(text=f"Title: {title}\nYear: {year}\nGenre: {genre}\nDirector: {director}\nPlot: {plot}\nIMDB Rating: {imdb_rating}\nMetascore: {metascore}")
        
        reviews_url = base_url + "?t=" + movie_title + "&apikey=" + api_key + "&type=movie&plot=full&r=json&tomatoes=true"
        reviews_response = requests.get(reviews_url)
        reviews_data = json.loads(reviews_response.content.decode())
        
        imdb_reviews = reviews_data["imdbID"] + "/reviews"
        tomatoes_reviews = reviews_data["tomatoURL"]
        
        reviews_label.config(text=f"IMDB Reviews: {imdb_reviews}\nRotten Tomatoes Reviews: {tomatoes_reviews}")

window = tk.Tk()
window.title("Movie Search")

movie_label = tk.Label(window, text="Movie Title:")
movie_label.pack()
movie_entry = tk.Entry(window)
movie_entry.pack()

search_button = tk.Button(window, text="Search", command=search_movie)
search_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()
reviews_label = tk.Label(window, text="")
reviews_label.pack()

window.mainloop()