import urllib.request

url = 'https://www.sedna.de/wp-content/uploads/2020/01/offne_Stellen_1600x900_fuer_Web.jpg'
urllib.request.urlretrieve(url, "image.jpg")