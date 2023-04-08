# import requests
# from bs4 import BeautifulSoup
# import numpy as np
#
#
# def get_poster(link):
#     images = []
#     for i in ddf['link']:
#         r = requests.get(i)
#         soup = BeautifulSoup(r.content, "html.parser")
#         try:
#             image_url = page_html.find('div', class_='poster').img['src']
#         except:
#             image_url = np.nan
#         images.append(image_url)