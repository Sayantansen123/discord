import requests


#jokes api
url1 = "https://daddyjokes.p.rapidapi.com/random"

headers1 = {
	"X-RapidAPI-Key": "238b5f8336msh80c2347c3e41953p1c4f10jsna37138f632a4",
	"X-RapidAPI-Host": "daddyjokes.p.rapidapi.com"
    }

jokes1 = requests.get(url1, headers=headers1)


#gif api
url2 = "https://any-anime.p.rapidapi.com/v1/anime/gif/1"

headers2 = {
	"X-RapidAPI-Key": "238b5f8336msh80c2347c3e41953p1c4f10jsna37138f632a4",
	"X-RapidAPI-Host": "any-anime.p.rapidapi.com"
    }

response2 = requests.get(url1, headers=headers2)