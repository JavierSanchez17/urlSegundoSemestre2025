from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import uic
import hashlib
import requests
import time
import math


def get_comic(page, limit, id):
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": ultra_secret.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}{id}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    characters = data["results"]
    return characters


def get_characters_search_name(name):
    correctName = name.replace(" ", "%20")
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": ultra_secret.hexdigest(),
        "limit": 10,
        "offset": 0 * 10
    }

    response = requests.get(f"{endpoint_search}characters?name={correctName}", params=params)
    data = response.json()["data"]
    characters = data["results"]
    return characters


def get_creator_search_name(first_name, last_name):
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": ultra_secret.hexdigest(),
        "limit": 10,
        "offset": 0 * 10
    }

    response = requests.get(f"{endpoint_search}creators?firstName={first_name}&lastName={last_name}", params=params)
    data = response.json()["data"]
    characters = data["results"]
    return characters


def generate_image_load(characterUrl, characterExtension):
    url = characterUrl + "." + characterExtension
    imageGenerated = QImage()
    imageGenerated.loadFromData(requests.get(url).content)
    return imageGenerated


endpoint = 'https://gateway.marvel.com/v1/public/comics/'
endpoint_search = 'https://gateway.marvel.com/v1/public/'
timestamp = time.time()
public_key = '3a8d20be0b21934df76336d1718650b9'
secret_key = '2abfd64c04eb658f49ff81f1bf4fbd942c33d5a0'

access = f"{timestamp}{secret_key}{public_key}"
ultra_secret = hashlib.md5(access.encode())

# variables de control
total_pages = 0
page = 0
limit = 10
list_comics = []


class DetailComicWindow(QMainWindow):
    def __init__(self, id):
        QMainWindow.__init__(self)
        uic.loadUi("detailComicsWindow.ui", self)
        self.id_comic = id
        self.comic = get_comic(0, 10, self.id_comic)
        self.get_characters()
        self.get_creators()

        self.detailNameComic.setText(
            f'<html><head/><body><p align="center">'
            f'<span style=" font-size:18pt; font-weight:600;">{self.comic[0]["title"]}</span></p></body></html>')

        if self.comic[0]["description"] is None:
            self.detailDescriptionComic.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">Descripción no disponible</span></p></body></html>')
        else:
            self.detailDescriptionComic.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:12pt;">{self.comic[0]["description"]}</span></p></body></html>')

        if self.comic[0]["isbn"] == "":
            self.detailIsbnComic.setText(
                f'<html><head/><body><p><span style=" font-size:12pt;">ISBN no disponible</span></p></body></html>')
        else:
            self.detailIsbnComic.setText(
                f'<html><head/><body><p><span style=" font-size:12pt;">{self.comic[0]["isbn"]}</span></p></body></html>')

    def get_characters(self):
        if self.comic[0]["characters"]["available"] == 0:
            self.detailImageCreatorComic_1.setPixmap(
                QPixmap('img/noDisponible.PNG'))
            self.detailNameCreatorComic_1.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">No disponible</span></p></body></html>')
            self.detailImageCreatorComic_2.setPixmap(
                QPixmap('img/noDisponible.PNG'))
            self.detailNameCreatorComic_2.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">No disponible</span></p></body></html>')
        elif self.comic[0]["characters"]["available"] == 1:
            name_character_1 = self.comic[0]["characters"]["items"][0]["name"]
            complete_character_1 = get_characters_search_name(name_character_1)
            self.detailNameCreatorComic_1.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:18pt; '
                f'font-weight:600;">{complete_character_1[0]["name"]}</span></p></body></html>')
            self.detailImageCreatorComic_1.setPixmap(
                QPixmap(generate_image_load(
                    complete_character_1[0]["thumbnail"]["path"], complete_character_1[0]["thumbnail"]["extension"])))
            self.detailImageCreatorComic_2.setPixmap(
                QPixmap('img/noDisponible.PNG'))
            self.detailNameCreatorComic_2.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">No disponible</span></p></body></html>')
        elif self.comic[0]["characters"]["available"] >= 2:
            name_character_1 = self.comic[0]["characters"]["items"][0]["name"]
            name_character_2 = self.comic[0]["characters"]["items"][1]["name"]
            complete_character_1 = get_characters_search_name(name_character_1)
            complete_character_2 = get_characters_search_name(name_character_2)
            self.detailNameCreatorComic_1.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:18pt; '
                f'font-weight:600;">{complete_character_1[0]["name"]}</span></p></body></html>')
            self.detailImageCreatorComic_1.setPixmap(
                QPixmap(generate_image_load(
                    complete_character_1[0]["thumbnail"]["path"], complete_character_1[0]["thumbnail"]["extension"])))

            self.detailNameCreatorComic_2.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:18pt; '
                f'font-weight:600;">{complete_character_2[0]["name"]}</span></p></body></html>')
            self.detailImageCreatorComic_2.setPixmap(
                QPixmap(generate_image_load(
                    complete_character_2[0]["thumbnail"]["path"], complete_character_2[0]["thumbnail"]["extension"])))

    def get_creators(self):
        if self.comic[0]["creators"]["available"] == 0:
            self.detailImageCharacterComic_1.setPixmap(
                QPixmap('img/noDisponible.PNG'))
            self.detailNameCharacterComic_1.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">No disponible</span></p></body></html>')
            self.detailImageCharacterComic_2.setPixmap(
                QPixmap('img/noDisponible.PNG'))
            self.detailNameCharacterComic_2.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">No disponible</span></p></body></html>')
        elif self.comic[0]["creators"]["available"] == 1:
            name_creator_1 = self.comic[0]["creators"]["items"][0]["name"]
            name_character_1 = name_creator_1.split()
            complete_creator_1 = get_creator_search_name(name_character_1[0], name_character_1[len(name_character_1) - 1])

            self.detailImageCharacterComic_1.setPixmap(
                QPixmap(generate_image_load(
                    complete_creator_1[0]["thumbnail"]["path"], complete_creator_1[0]["thumbnail"]["extension"])))
            self.detailNameCharacterComic_1.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">{complete_creator_1[0]["fullName"]}</span></p></body></html>')
            self.detailImageCharacterComic_2.setPixmap(
                QPixmap('img/noDisponible.PNG'))
            self.detailNameCharacterComic_2.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">No disponible</span></p></body></html>')
        elif self.comic[0]["creators"]["available"] > 1:
            name_creator_1 = self.comic[0]["creators"]["items"][0]["name"]
            name_creator_2 = self.comic[0]["creators"]["items"][1]["name"]
            name_character_1 = name_creator_1.split()
            name_character_2 = name_creator_2.split()
            complete_creator_1 = get_creator_search_name(name_character_1[0], name_character_1[len(name_character_1) - 1])
            complete_creator_2 = get_creator_search_name(name_character_2[0], name_character_2[len(name_character_2) - 1])

            self.detailImageCharacterComic_1.setPixmap(
                QPixmap(generate_image_load(
                    complete_creator_1[0]["thumbnail"]["path"], complete_creator_1[0]["thumbnail"]["extension"])))
            self.detailNameCharacterComic_1.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">{complete_creator_1[0]["fullName"]}</span></p></body></html>')
            self.detailImageCharacterComic_2.setPixmap(
                QPixmap(generate_image_load(
                    complete_creator_2[0]["thumbnail"]["path"], complete_creator_2[0]["thumbnail"]["extension"])))
            self.detailNameCharacterComic_2.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:18pt; font-weight:600;">{complete_creator_2[0]["fullName"]}</span></p></body></html>')
