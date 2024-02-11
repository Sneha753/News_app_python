import requests
import time
import api_key

top_headlines =  f"https://newsapi.org/v2/top-headlines?country=in&language=en&apiKey={api_key.api_key}"
sports = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&language=en&apiKey={api_key.api_key}"
business = f"https://newsapi.org/v2/top-headlines?country=in&category=business&language=en&apiKey={api_key.api_key}"
health = f"https://newsapi.org/v2/top-headlines?country=in&category=health&language=en&apiKey={api_key.api_key}"
entertainment = f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&language=en&apiKey={api_key.api_key}"
science = f"https://newsapi.org/v2/top-headlines?country=in&category=science&language=en&apiKey={api_key.api_key}"
technology = f"https://newsapi.org/v2/top-headlines?country=in&category=technology&language=en&apiKey={api_key.api_key}"
# url = None
def ask_news():
    global query
    while True:
        user_input = int(input("1-Top Headlines\n2-Sports\n3-Business\n4-Health\n5-Entertainment\n6-Science\n7-Technology\n8-search\n9-Quit\nEnter category: "))
        if user_input == 9:
            break
        elif user_input == 1:
            getnews(top_headlines)
        elif user_input == 2:
            getnews(sports)
        elif user_input == 3:
            getnews(business)
        elif user_input == 4:
            getnews(health)
        elif user_input == 5:
            getnews(entertainment)
        elif user_input == 6:
            getnews(science)
        elif user_input == 7:
            getnews(technology)
        elif user_input == 8:
            date = time.strftime("%Y:%m:%d")
            query = input("Search news:")
            if query == "":
                search = f"https://newsapi.org/v2/everything?&sortBy=publishedAt&pageSize=20&language=en&apiKey=64d5f927e02c4f539c3a2be817e1fcc0"
            else:
                search = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&pageSize=20&language=en&apiKey=64d5f927e02c4f539c3a2be817e1fcc0"
            getnews(search)
        else:
            print("Invalid input")
def getnews(url):
    response = requests.get(url)
    data = response.json()
    news = list(data["articles"])
    for i in range(0,len(news)):
        print(f"{i+1}.{news[i]["title"]}")
        print(news[i]["description"])
        print("-------------------------------------------------------------------------------------------------------")

ask_news()
