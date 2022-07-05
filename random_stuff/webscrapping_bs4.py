from bs4 import BeautifulSoup

page = requests.get("https://www.youtube.com/").text

soup = BeautifulSoup(page, "html.parser")

artists = soup.find_all('a')

for artist in artists:
	names = artist.contents[0]
	fullLink = artist.get('href')
	print(names)
	print(fullLink)