# This is for daily_animal project. 
from lxml import html
import json
import requests

# Request the Worms page html
url = "http://marinespecies.org/photogallery.php?pic=138429"

def get_page(url):
	response = requests.get(url)
	tree = html.fromstring(response.content)

	return tree


def save_page(file_name, content):
	f = open(file_name, 'w+')
	f.write(content)
	f.close()


content = get_page(url)


image_selector = "#photogallery_resized_img > img"
spp_name_selector = "#photogallery_left > span > div"
spp_description_selector = "#photogallery_left > span > span.photogallery_caption.photogallery_descr"


image_url = content.cssselect(image_selector)[0].get('src')
spp_name = content.cssselect(spp_name_selector)[0].text
spp_description = content.cssselect(spp_description_selector)[0].text_content()

animal_obj = {
	'image_url': image_url,
	'spp_name': spp_name,
	'spp_description': spp_description
}

json_animal_obj = json.dumps(animal_obj, indent=4, sort_keys=True)

save_page('fishie.json', json_animal_obj)




# parse page to get key info
# write the key into a file
# write the content to github once a day 