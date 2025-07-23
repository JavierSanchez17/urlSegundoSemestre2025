from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import uic
import hashlib
import requests
import time
import math

from simpleLinkedList import SimplyLinkedList
from doublyLinkedList import DoublyLinkedList


def get_character(page, limit, id):
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


def generate_image_load(characterUrl, characterExtension):
    url = characterUrl + "." + characterExtension
    imageGenerated = QImage()
    imageGenerated.loadFromData(requests.get(url).content)
    return imageGenerated


endpoint = 'https://gateway.marvel.com/v1/public/characters/'
timestamp = time.time()
public_key = '3a8d20be0b21934df76336d1718650b9'
secret_key = '2abfd64c04eb658f49ff81f1bf4fbd942c33d5a0'

access = f"{timestamp}{secret_key}{public_key}"
ultra_secret = hashlib.md5(access.encode())

# variables de control
total_pages = 0
page = 0
limit = 10
list_characters = []


class DetailCharacterWindow(QMainWindow):
    def __init__(self, id):
        QMainWindow.__init__(self)
        uic.loadUi("detailCharacterWindow.ui", self)
        self.id_character = id
        self.character = get_character(0, 10, self.id_character)
        list_comics = self.get_comics()
        list_events = self.get_events()

        self.detailNameCharacter.setText(
            f'<html><head/><body><p align="center">'
            f'<span style=" font-size:18pt; font-weight:600;">{self.character[0]["name"]}</span></p></body></html>')

        if self.character[0]["description"] == "":
            self.detailDescriptionCharacter.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:16pt; font-weight:600;">No hay descripción disponible</span></p></body></html>')
        else:
            self.detailDescriptionCharacter.setText(
                f'<html><head/><body><p align="center">'
                f'<span style=" font-size:12pt;">{self.character[0]["description"]}</span></p></body></html>')

        self.detailImageCharacter.setPixmap(
            QPixmap(generate_image_load(self.character[0]["thumbnail"]["path"], self.character[0]["thumbnail"]["extension"])))

        # ---------------------------------------- Colocacion de comics ----------------------------------------
        self.detailICharacterComic_1.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(0).data}</span></p></body></html>')
        self.detailICharacterComic_2.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(1).data}</span></p></body></html>')
        self.detailICharacterComic_3.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(2).data}</span></p></body></html>')
        self.detailICharacterComic_4.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(3).data}</span></p></body></html>')
        self.detailICharacterComic_5.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(4).data}</span></p></body></html>')
        self.detailICharacterComic_6.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(5).data}</span></p></body></html>')
        self.detailICharacterComic_7.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(6).data}</span></p></body></html>')
        self.detailICharacterComic_8.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(7).data}</span></p></body></html>')
        self.detailICharacterComic_9.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(8).data}</span></p></body></html>')
        self.detailICharacterComic_10.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_comics.search_by_position(9).data}</span></p></body></html>')

        # ---------------------------------------- Colocacion de eventos ----------------------------------------
        self.detailICharacterEvent_1.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(0).data}</span></p></body></html>')
        self.detailICharacterEvent_2.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(1).data}</span></p></body></html>')
        self.detailICharacterEvent_3.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(2).data}</span></p></body></html>')
        self.detailICharacterEvent_4.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(3).data}</span></p></body></html>')
        self.detailICharacterEvent_5.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(4).data}</span></p></body></html>')
        self.detailICharacterEvent_6.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(5).data}</span></p></body></html>')
        self.detailICharacterEvent_7.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(6).data}</span></p></body></html>')
        self.detailICharacterEvent_8.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(7).data}</span></p></body></html>')
        self.detailICharacterEvent_9.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(8).data}</span></p></body></html>')
        self.detailICharacterEvent_10.setText(
            f'<html><head/><body><p><span style=" font-size:12pt;">{list_events.find_at(9).data}</span></p></body></html>')

    def get_comics(self):
        i = 0
        list_character_comics = DoublyLinkedList()
        if self.character[0]["comics"]["available"] < 10:
            remainder = 10 - len(self.character[0]["comics"]["items"])
            for comic in self.character[0]["comics"]["items"]:
                list_character_comics.add_to_start(comic["name"])
            for i in range(remainder):
                list_character_comics.add_to_end("No existe en este comic")
        else:
            for comic in self.character[0]["comics"]["items"]:
                list_character_comics.add_to_start(comic["name"])
                i += 1
                if i == 10:
                    break
        return list_character_comics

    def get_events(self):
        i = 0
        list_character_events = SimplyLinkedList()
        if self.character[0]["series"]["available"] < 10:
            remainder = 10 - len(self.character[0]["series"]["items"])
            for event in self.character[0]["series"]["items"]:
                list_character_events.unshift(event["name"])
            for i in range(remainder):
                list_character_events.append("No existe en este comic")
        else:
            for event in self.character[0]["series"]["items"]:
                list_character_events.unshift(event["name"])
                i += 1
                if i == 10:
                    break
        return list_character_events
