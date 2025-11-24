import requests


base_url = 'https://api.spaceflightnewsapi.net/v4/'

def get_latest_articles():
    
    articles_url = f"{base_url}articles/"
    response = requests.get(articles_url)
    data = response.json()
    
    articles_list = []
    
    # article title
    for article in data['results']:
        
        # creates a new dict every loop
        new_dict = {}
        
        # gets the data from title and summary keys from json response and puts it in a new key in the new dict
        new_dict['title'] = article['title']
        new_dict['summary'] = article['summary']
        
        # appends new dict to a list to make a list of dictionaries
        articles_list.append(new_dict)
        
    print(articles_list)
    return articles_list
    

        

    

