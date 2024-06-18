import requests

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
    "x-rapidapi-key": "2d50ef8704msh8d9cc2bbd9019d0p1b49c4jsn34e39c59d0e9",
    "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())