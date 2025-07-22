import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.nintendo.co.kr/switch/ranking/ranking_2024_full.html"

response = requests.get(url)

response.content

# 게임 랭킹을 담을 리스트
nintendo_ranking_2024 = []

# HTML 파싱
soup = BeautifulSoup(response.content, "html.parser")

# 모든 게임 추출
games = soup.find_all("div", class_="nc3-c-softCard")

# 각 게임에서 데이터 추출
for game in games:
    title = game.find("p", class_="tit").text

    category = game.find("span", class_="cate")
    if category:
        category = category.text

    types = game.find_all("strong", class_="ico_rel")
    if types:
        types = [t.text for t in types]
    else:
        types = "N/A"

    release_info = game.find("p", class_="releaseInfo").get_text(separator="\n").split("\n")
    if len(release_info) >= 2:
        date = release_info[0]
        company = release_info[1]
    elif len(release_info) == 1 :
        date = "N/A"
        company = release_info[0]

    lang = game.find("p", class_="ico_lang")
    if lang:
        lang = lang.text

    url = game.find("a")["href"]

    # 게임 데이터를 딕셔너리로 저장
    game_data = {
        "title" : title,
        "category" : category,
        "type" : types,
        "date" : date,
        "company" : company,
        "lang" : lang,
        "url" : url
    }

    # 리스트에 추가
    nintendo_ranking_2024.append(game_data)

file = open("nintendo_ranking_2024.csv", "w", encoding="utf-8-sig")
writer = csv.writer(file)
writer.writerow(["title", "category", "type", "date", "company", "lang", "url"])

for game in nintendo_ranking_2024:
    writer.writerow(game.values())