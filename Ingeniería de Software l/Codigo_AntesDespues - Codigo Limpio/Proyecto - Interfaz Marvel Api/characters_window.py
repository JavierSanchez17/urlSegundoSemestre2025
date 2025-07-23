from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import uic
import hashlib
import requests
import time
import math

from character import Character
from communicate_comics import CommunicateComics
from detail_character_window import DetailCharacterWindow

from circularList import CircularList

# -- PARTE DEL PROYECTO MARVEL API --
def get_characters(page, limit):
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": ultra_secret.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}{resource_characters}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    characters = data
    return characters


def get_characters_search_name(page, limit, name):
    correctName = name.replace(" ", "%20")
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": ultra_secret.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}characters?name={correctName}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    characters = data
    return characters


# Funcion para poder mandar la imagen a la interfaz
def generate_image_load(characterUrl, characterExtension):
    url = characterUrl + "." + characterExtension
    imageGenerated = QImage()
    imageGenerated.loadFromData(requests.get(url).content)
    return imageGenerated


# -- PARTE DEL PROYECTO MARVEL API --
endpoint = 'https://gateway.marvel.com/v1/public/'
resource_characters = 'characters?orderBy=name'
timestamp = time.time()
public_key = '3a8d20be0b21934df76336d1718650b9'
secret_key = '2abfd64c04eb658f49ff81f1bf4fbd942c33d5a0'

access = f"{timestamp}{secret_key}{public_key}"
ultra_secret = hashlib.md5(access.encode())

total_pages = 0
global page
page = 0
global limit
limit = 10
global option
option = 1
global id_character
id_character = 0
list_characters = CircularList()


# -- PARTE DEL PROYECTO MARVEL API --


class CharactersWindow(QMainWindow):
    def __init__(self, communicate_comics: CommunicateComics):
        QMainWindow.__init__(self)
        # Se carga la interfaz
        uic.loadUi("untitled.ui", self)
        # Se ejecuta la funcion para mostrar los personajes
        self.load_items()
        self.communicateComics = communicate_comics

        # Botones para verificar si se presiono el boton y ejecuta la funcion
        self.characterBtn_c1.setCheckable(True)
        self.characterBtn_c1.clicked.connect(self.open_detail)

        self.characterBtn_c2.setCheckable(True)
        self.characterBtn_c2.clicked.connect(self.open_detail)

        self.characterBtn_c3.setCheckable(True)
        self.characterBtn_c3.clicked.connect(self.open_detail)

        self.characterBtn_c4.setCheckable(True)
        self.characterBtn_c4.clicked.connect(self.open_detail)

        self.characterBtn_c5.setCheckable(True)
        self.characterBtn_c5.clicked.connect(self.open_detail)

        self.characterBtn_c6.setCheckable(True)
        self.characterBtn_c6.clicked.connect(self.open_detail)

        self.characterBtn_c7.setCheckable(True)
        self.characterBtn_c7.clicked.connect(self.open_detail)

        self.characterBtn_c8.setCheckable(True)
        self.characterBtn_c8.clicked.connect(self.open_detail)

        self.characterBtn_c9.setCheckable(True)
        self.characterBtn_c9.clicked.connect(self.open_detail)

        self.characterBtn_c10.setCheckable(True)
        self.characterBtn_c10.clicked.connect(self.open_detail)

        self.btnCharacterSearchName.setCheckable(True)

        self.btnNextCharacter.clicked.connect(self.page_forward)
        self.btnPreviousCharacter.clicked.connect(self.return_page)
        self.btnCharapterViewComics.clicked.connect(self.view_comics_window)
        self.btnCharacterSearchName.clicked.connect(self.search_name)
        self.btnCharacterOrderByName.clicked.connect(self.order_by_name)

    def load_items(self) -> None:
        global option
        global total_pages
        global page
        self.no_result()
        if option == 1:
            characters_data = get_characters(page, limit)
            characters = characters_data["results"]
        elif option == 2:
            search_name = self.textCharacterName.text()
            characters_data = get_characters_search_name(page, limit, search_name)
            characters = characters_data["results"]
            if characters_data["count"] == 0:
                QMessageBox.warning(self, "Error", "No se han encontrado resultados.")
                return None
        # -- PARTE DEL PROYECTO MARVEL API --
        for character in characters:
            current = Character(character["id"], character["name"], character["thumbnail"]["path"],
                                character["thumbnail"]["extension"], character["description"])
            list_characters.add_to_end(current)
        # -- PARTE DEL PROYECTO MARVEL API --

        if characters_data["count"] == 1:
            self.load_one()
        elif characters_data["count"] == 2:
            self.load_two()
        elif characters_data["count"] == 3:
            self.load_three()
        elif characters_data["count"] == 4:
            self.load_four()
        elif characters_data["count"] == 5:
            self.load_five()
        elif characters_data["count"] == 6:
            self.load_six()
        elif characters_data["count"] == 7:
            self.load_seven()
        elif characters_data["count"] == 8:
            self.load_eight()
        elif characters_data["count"] == 9:
            self.load_nine()
        elif characters_data["count"] == 10:
            self.load_ten()

        self.characterPagesCount.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt;">Pagina '
            f'{page + 1} de {total_pages}</span></p></body></html>')

    def no_result(self):
        self.characterName_c1.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c1.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c1.setEnabled(False)

        self.characterName_c2.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c2.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c2.setEnabled(False)

        self.characterName_c3.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c3.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c3.setEnabled(False)

        self.characterName_c4.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c4.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c4.setEnabled(False)

        self.characterName_c5.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c5.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c5.setEnabled(False)

        self.characterName_c6.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c6.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c6.setEnabled(False)

        self.characterName_c7.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c7.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c7.setEnabled(False)

        self.characterName_c8.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c8.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c8.setEnabled(False)

        self.characterName_c9.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c9.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c9.setEnabled(False)

        self.characterName_c10.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterImage_c10.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.characterBtn_c10.setEnabled(False)

        self.characterPagesCount.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt;">Pagina '
            f'0 de 0</span></p></body></html>')

    def load_one(self):
        self.characterName_c1.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_characters.find_by_position(0).name}</span></p></body></html>')
        self.characterImage_c1.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(0).image, list_characters.find_by_position(0).extension)))
        self.characterBtn_c1.setEnabled(True)

    def load_two(self):
        self.load_one()
        self.characterName_c2.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_characters.find_by_position(1).name}</span></p></body></html>')
        self.characterImage_c2.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(1).image, list_characters.find_by_position(1).extension)))
        self.characterBtn_c2.setEnabled(True)

    def load_three(self):
        self.load_two()
        self.characterName_c3.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_characters.find_by_position(2).name}</span></p></body></html>')
        self.characterImage_c3.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(2).image, list_characters.find_by_position(2).extension)))
        self.characterBtn_c3.setEnabled(True)

    def load_four(self):
        self.load_three()
        self.characterName_c4.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_characters.find_by_position(3).name}</span></p></body></html>')
        self.characterImage_c4.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(3).image, list_characters.find_by_position(3).extension)))
        self.characterBtn_c4.setEnabled(True)

    def load_five(self):
        self.load_four()
        self.characterName_c5.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">{list_characters.find_by_position(4).name}</span></p></body></html>')
        self.characterImage_c5.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(4).image, list_characters.find_by_position(4).extension)))
        self.characterBtn_c5.setEnabled(True)

    def load_six(self):
        self.load_five()
        self.characterName_c6.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">{list_characters.find_by_position(5).name}</span></p></body></html>')
        self.characterImage_c6.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(5).image, list_characters.find_by_position(5).extension)))
        self.characterBtn_c6.setEnabled(True)

    def load_seven(self):
        self.load_six()
        self.characterName_c7.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">{list_characters.find_by_position(6).name}</span></p></body></html>')
        self.characterImage_c7.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(6).image, list_characters.find_by_position(6).extension)))
        self.characterBtn_c7.setEnabled(True)

    def load_eight(self):
        self.load_seven()
        self.characterName_c8.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">{list_characters.find_by_position(7).name}</span></p></body></html>')
        self.characterImage_c8.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(7).image, list_characters.find_by_position(7).extension)))
        self.characterBtn_c8.setEnabled(True)

    def load_nine(self):
        self.load_eight()
        self.characterName_c9.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">{list_characters.find_by_position(8).name}</span></p></body></html>')
        self.characterImage_c9.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(8).image, list_characters.find_by_position(8).extension)))
        self.characterBtn_c9.setEnabled(True)

    def load_ten(self):
        self.load_nine()
        self.characterName_c10.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">{list_characters.find_by_position(9).name}</span></p></body></html>')
        self.characterImage_c10.setPixmap(
            QPixmap(generate_image_load(list_characters.find_by_position(9).image, list_characters.find_by_position(9).extension)))
        self.characterBtn_c10.setEnabled(True)

    def page_forward(self):
        global page
        self.btnNextCharacter.setChecked(False)
        page += 1
        if page >= total_pages:
            page -= 1
            QMessageBox.warning(self, "Error", "Ha alcanzado el maximo de paginas totales.")
        else:
            list_characters.clear()
            self.load_items()

    def return_page(self):
        global page
        self.btnPreviousCharacter.setChecked(False)
        page -= 1
        if page < 0:
            page += 1
            QMessageBox.warning(self, "Error", "Se ha decrecido la mayor cantidad de paginas existentes.")
        else:
            list_characters.clear()
            self.load_items()

    def order_by_name(self):
        global option
        if option == 1:
            QMessageBox.warning(self, "Error", "El listado de comics ya esta ordenado por nombre")
        else:
            option = 1
            list_characters.clear()
            self.load_items()

    def search_name(self):
        global option
        global page
        self.btnCharacterSearchName.setChecked(False)
        page = 0
        search_name = self.textCharacterName.text()
        if not search_name:
            QMessageBox.warning(self, "Error", "La linea de texto esta vacia.")
        else:
            option = 2
            list_characters.clear()
            self.load_items()

    def open_detail(self) -> None:
        # * Necesito que averiguen como mandar datos de un archivo .py a otro .py *
        if self.characterBtn_c1.isChecked():
            self.characterBtn_c1.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(0).id)
        elif self.characterBtn_c2.isChecked():
            self.characterBtn_c2.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(1).id)
        elif self.characterBtn_c3.isChecked():
            self.characterBtn_c3.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(2).id)
        elif self.characterBtn_c4.isChecked():
            self.characterBtn_c4.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(3).id)
        elif self.characterBtn_c5.isChecked():
            self.characterBtn_c5.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(4).id)
        elif self.characterBtn_c6.isChecked():
            self.characterBtn_c6.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(5).id)
        elif self.characterBtn_c7.isChecked():
            self.characterBtn_c7.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(6).id)
        elif self.characterBtn_c8.isChecked():
            self.characterBtn_c8.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(7).id)
        elif self.characterBtn_c9.isChecked():
            self.characterBtn_c9.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(8).id)
        elif self.characterBtn_c10.isChecked():
            self.characterBtn_c10.setChecked(False)
            self.detail_character_window = DetailCharacterWindow(list_characters.find_by_position(9).id)
        self.detail_character_window.show()

    def view_comics_window(self):
        self.communicateComics.verify_code.emit()
