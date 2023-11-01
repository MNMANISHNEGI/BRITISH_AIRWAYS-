import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.airlinequality.com/airline-reviews/british-airways"
pages=10
page_size=100
reviews=[]
for i in range(1,pages+1):
    print(f"page no{i}")
    newurl=f"{url}/page/{i}?sortby=post_date%3ADesc&pagesize={page_size}"

    response=requests.get(newurl)
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())

    print(f"   ---> {len(reviews)} total reviews")
df = pd.DataFrame()
df["reviews"] = reviews
print(df.head())
df.to_csv("C:\\Users\\91789\\PycharmProjects\\britishairwaystask/BA_reviews.csv")