import requests

query = input("Kya news dekhni hai? ")

api = "e3120e9e13ec4f0db0db080954b21019"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-08-06&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)

data = r.json()

if data["status"] == "ok":
    articles = data["articles"]

    for index, article in enumerate(articles):
        print(index + 1, article["title"])
        print(article["url"])
        print("\n****************************\n")
else:
    print("Error:", data["message"])