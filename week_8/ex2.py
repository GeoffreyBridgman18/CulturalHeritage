import requests
from bs4 import BeautifulSoup

artworks = []

for i in range(0, 3):
    url = f"https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page={i}"
    base_url = "https://www.phillipscollection.org"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    item_containers = soup.find_all("div", class_="card grid__item")

    for item_container in item_containers:
        all_links = item_container.find_all("a")
        for link in all_links:
            href = f"{base_url}{link['href']}"
            page_to_scrape = requests.get(href)

            if page_to_scrape.status_code == 200:
                artwork_soup = BeautifulSoup(page_to_scrape.text, "html.parser")
                sub_title_div = artwork_soup.find("div", class_="collection-header__info")

                if sub_title_div is not None:
                    sub_title_par = sub_title_div.find("p", class_="collection-header__subtitle")

                    if sub_title_par is not None:
                        artist = sub_title_par.find("a")

                        if artist is not None:
                            current_artwork = {'Artist': artist.text}

                            other_container = artwork_soup.find("div", class_="flex-layout")
                            if other_container is not None:
                                spans = other_container.find_all("span", class_="collection-meta__type")

                                for span in spans:
                                    if span.text == "Materials":
                                        materials = span.find_next("span", class_="collection-meta__value").text
                                        current_artwork['Materials'] = materials

                                    elif span.text == "Dimensions":
                                        dimensions = span.find_next("span", class_="collection-meta__value").text
                                        current_artwork['Dimensions'] = dimensions

                            artworks.append(current_artwork)

for artwork in artworks:
    print(artwork)

  

                
            
             