from serpapi import GoogleSearch
import json
import matplotlib.pyplot as plt
import pandas as pd
import squarify as sq

def getSearch(coutryCode):
    params = {
        "engine" : "google_trends_trending_now",
        'geo': coutryCode,
        'category_id':4,
        'api_key': '8dde83fa0a5568de696e13f9bf35dccd976d66116d9742cc135958ec06bec477'
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results

def getArticles(coutryCode):
    params = {
        "engine" : "google_news",
        'gl': coutryCode,
        'topic_token':"CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB",  
        "api_key": '8dde83fa0a5568de696e13f9bf35dccd976d66116d9742cc135958ec06bec477'
        }

    search = GoogleSearch(params)
    results = search.get_dict()

    with open(f'news{coutryCode}.txt', 'w', encoding='utf-8') as f:
        for i in results['news_results']:
            try:
                f.write(i['highlight']['title'])
            except KeyError:
                f.write(i['title'])
            f.write('\n')
    
    return results

def pie(results):

    trends = []
    volume = []
    increasePCT = []

    for i in results["trending_searches"]:
        trends.append(i["query"])
        volume.append(i["search_volume"])
        increasePCT.append(i["increase_percentage"])

    df = pd.DataFrame({
        'trends': trends,
        'volume': volume,
        'increase_percentage': increasePCT
    })

    df = df.sort_values(by='volume', ascending=False)

    start = df.head(10)

    #plt.pie(start['volume'], labels=start['trends'].tolist(), autopct='%1.1f%%', startangle=140)
    #plt.show()
    for i, j in enumerate(start['trends'].tolist()):
        print(j, start['volume'].tolist()[i], start['increase_percentage'].tolist()[i])

def square(results):
    trends = []
    volume = []
    increasePCT = []

    for i in results["trending_searches"]:
        trends.append(i["query"])
        volume.append(i["search_volume"])
        increasePCT.append(i["increase_percentage"])

    df = pd.DataFrame({
        'trends': trends,
        'volume': volume,
        'increase_percentage': increasePCT
    })

    df = df.sort_values(by='volume', ascending=False)

    start = df.head(10)

    col = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c2f0c2','#ff6666','#c2f0f0','#d9d9d9']

    """
    plt.figure(figsize=(12, 8))
    sq.plot(sizes=start['volume'], label=start['trends'].tolist(), alpha=0.7, color=col)
    plt.axis('off')
    plt.show()
    """
    for i, j in enumerate(start['trends'].tolist()):
        print(j, start['volume'].tolist()[i], start['increase_percentage'].tolist()[i])

country = input("Enter the country code (e.g., 'US' for United States): ")
res = getArticles(country)
#pie(results=res)
#square(results=res)
with open(f'celebs{country}.json','w', encoding='utf-8') as f:
    json.dump(res, f, indent=4, ensure_ascii=False)
