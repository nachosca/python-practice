import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=New-Delhi")

# print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# find('a')
# find_all("div")
# find_parent("a")
# find_next_siblings("a")

cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})
# print(card)


for card in cards:
	price = card.find("span",attrs={"class":"luxury-srp-card__price"})
	# print(price.text.strip().strip("	").strip("\n"))
	title = card.find("span",attrs={"class":"m-srp-card__title__bhk"})
	# print(title.text.strip())

	carpet_area = card.find("div",attrs={"class":"luxury-srp-card__area__value"})
# print(carpet_area.text)

	data = "{} {} {}".format(title.text.strip(), price.text.strip().strip("	").strip("\n"), carpet_area.text)
	print(data)