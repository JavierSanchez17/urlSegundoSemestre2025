from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import uic
import hashlib
import requests
import time
import math

from comic import Comic
from communicate_character import CommunicateCharacter
from detail_comic_window import DetailComicWindow




def get_comics_ascendent(page, limit):
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": auth_hash.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}{resource_comics_ascendent}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    comics = data
    return comics


def get_comics_date(page, limit):
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": auth_hash.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}{resource_comics_date}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    comics = data
    return comics


def get_comics_search_title(page, limit, title):
    correctTitle = title.replace(" ", "%20")
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": auth_hash.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}comics?title={correctTitle}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    comics = data
    return comics


def get_comics_search_date(page, limit, date):
    global total_pages
    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": auth_hash.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}comics?startYear={date}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    comics = data
    return comics


# Funcion para poder mandar la imagen a la interfaz
def generate_image_load(comicURl, comicExtension):
    url = comicURl + "." + comicExtension
    image_generated = QImage()
    image_generated.loadFromData(requests.get(url).content)
    return image_generated


endpoint = 'https://gateway.marvel.com/v1/public/'
resource_characters = 'characters'
resource_comics_ascendent = 'comics?orderBy=title'
resource_comics_date = 'comics?orderBy=onsaleDate'
timestamp = time.time()
public_key = '3a8d20be0b21934df76336d1718650b9'
secret_key = '2abfd64c04eb658f49ff81f1bf4fbd942c33d5a0'

access = f"{timestamp}{secret_key}{public_key}"
auth_hash = hashlib.md5(access.encode())

total_pages = 0
global page
page = 0
global limit
limit = 10
global option
option = 1
list_comics = []
comics = get_comics_ascendent(page, limit)


class ComicsWindow(QMainWindow):
    def __init__(self, communicate_character: CommunicateCharacter):
        QMainWindow.__init__(self)
        # Se carga la interfaz
        uic.loadUi("comicWindow.ui", self)
        self.communicateCharacter = communicate_character
        self.btnComicsViewCharacters.clicked.connect(self.view_character_window)
        self.load_items()

        self.comicBtn_c1.setCheckable(True)
        self.comicBtn_c1.clicked.connect(self.open_detail)
        self.comicBtn_c2.setCheckable(True)
        self.comicBtn_c2.clicked.connect(self.open_detail)
        self.comicBtn_c3.setCheckable(True)
        self.comicBtn_c3.clicked.connect(self.open_detail)
        self.comicBtn_c4.setCheckable(True)
        self.comicBtn_c4.clicked.connect(self.open_detail)
        self.comicBtn_c5.setCheckable(True)
        self.comicBtn_c5.clicked.connect(self.open_detail)
        self.comicBtn_c6.setCheckable(True)
        self.comicBtn_c6.clicked.connect(self.open_detail)
        self.comicBtn_c7.setCheckable(True)
        self.comicBtn_c7.clicked.connect(self.open_detail)
        self.comicBtn_c8.setCheckable(True)
        self.comicBtn_c8.clicked.connect(self.open_detail)
        self.comicBtn_c9.setCheckable(True)
        self.comicBtn_c9.clicked.connect(self.open_detail)
        self.comicBtn_c10.setCheckable(True)
        self.comicBtn_c10.clicked.connect(self.open_detail)

        self.btnComicSearchName.setCheckable(True)
        self.btnComicSearchDate.setCheckable(True)

        self.btnNextComic.clicked.connect(self.page_forward)
        self.btnPreviousComic.clicked.connect(self.return_page)
        self.btnComicOrderByName.clicked.connect(self.order_by_name)
        self.btnComicOrderByDate.clicked.connect(self.order_by_date)
        self.btnComicSearchName.clicked.connect(self.search_name)
        self.btnComicSearchDate.clicked.connect(self.search_date)

    def load_items(self):
        global option
        global total_pages
        global page
        self.no_result()
        if option == 1:
            comics_data = get_comics_ascendent(page, limit)
            comics = comics_data["results"]
        elif option == 2:
            comics_data = get_comics_date(page, limit)
            comics = comics_data["results"]
        elif option == 3:
            search_title = self.textComicName.text()
            comics_data = get_comics_search_title(page, limit, search_title)
            comics = comics_data["results"]
            if comics_data["count"] == 0:
                QMessageBox.warning(self, "Error", "No se han encontrado resultados.")
                return None
        elif option == 4:
            search_date = self.lineEditComicDate.date()
            search_date = str(search_date.toPyDate())
            search_date = search_date[0:4]
            comics_data = get_comics_search_date(page, limit, search_date)
            comics = comics_data["results"]
            if comics_data["count"] == 0:
                QMessageBox.warning(self, "Error", "No se han encontrado resultados.")
                return None
        else:
            QMessageBox.warning(self, "Error", "Ha ocurrido un error.")

        # -- PARTE DEL PROYECTO MARVEL API --
        for comic in comics:
            current = Comic(comic["id"], comic["title"], comic["isbn"], comic["thumbnail"]["path"], comic["thumbnail"]["extension"],
                            comic["description"])
            list_comics.append(current)
        # -- PARTE DEL PROYECTO MARVEL API --

        if comics_data["count"] == 1:
            self.load_one()
        elif comics_data["count"] == 2:
            self.load_two()
        elif comics_data["count"] == 3:
            self.load_three()
        elif comics_data["count"] == 4:
            self.load_four()
        elif comics_data["count"] == 5:
            self.load_five()
        elif comics_data["count"] == 6:
            self.load_six()
        elif comics_data["count"] == 7:
            self.load_seven()
        elif comics_data["count"] == 8:
            self.load_eight()
        elif comics_data["count"] == 9:
            self.load_nine()
        elif comics_data["count"] == 10:
            self.load_ten()

        self.comicPagesCount.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt;">Pagina '
            f'{page + 1} de {total_pages}</span></p></body></html>')

    def no_result(self):
        self.comicName_c1.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c1.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c1.setEnabled(False)

        self.comicName_c2.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c2.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c2.setEnabled(False)

        self.comicName_c3.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c3.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c3.setEnabled(False)

        self.comicName_c4.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c4.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c4.setEnabled(False)

        self.comicName_c5.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c5.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c5.setEnabled(False)

        self.comicName_c6.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c6.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c6.setEnabled(False)

        self.comicName_c7.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c7.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c7.setEnabled(False)

        self.comicName_c8.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c8.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c8.setEnabled(False)

        self.comicName_c9.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c9.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c9.setEnabled(False)

        self.comicName_c10.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'Sin Resultado</span></p></body></html>')
        self.characterComic_c10.setPixmap(
            QPixmap('img/noDisponible.PNG'))
        self.comicBtn_c10.setEnabled(False)

        self.comicPagesCount.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt;">Pagina '
            f'0 de 0</span></p></body></html>')

    def load_one(self):
        # Atributo para colocar el nombre del personaje con texto
        self.comicName_c1.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[0].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c1.setPixmap(
            QPixmap(generate_image_load(list_comics[0].image, list_comics[0].extension)))
        self.comicBtn_c1.setEnabled(True)

    def load_two(self):
        self.load_one()
        self.comicName_c2.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[1].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c2.setPixmap(
            QPixmap(generate_image_load(list_comics[1].image, list_comics[1].extension)))
        self.comicBtn_c2.setEnabled(True)

    def load_three(self):
        self.load_two()
        self.comicName_c3.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[2].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c3.setPixmap(
            QPixmap(generate_image_load(list_comics[2].image, list_comics[2].extension)))
        self.comicBtn_c3.setEnabled(True)

    def load_four(self):
        self.load_three()
        self.comicName_c4.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[3].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c4.setPixmap(
            QPixmap(generate_image_load(list_comics[3].image, list_comics[3].extension)))
        self.comicBtn_c4.setEnabled(True)

    def load_five(self):
        self.load_four()
        self.comicName_c5.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[4].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c5.setPixmap(
            QPixmap(generate_image_load(list_comics[4].image, list_comics[4].extension)))
        self.comicBtn_c5.setEnabled(True)

    def load_six(self):
        self.load_five()
        self.comicName_c6.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[5].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c6.setPixmap(
            QPixmap(generate_image_load(list_comics[5].image, list_comics[5].extension)))
        self.comicBtn_c6.setEnabled(True)

    def load_seven(self):
        self.load_six()
        self.comicName_c7.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[6].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c7.setPixmap(
            QPixmap(generate_image_load(list_comics[6].image, list_comics[6].extension)))
        self.comicBtn_c7.setEnabled(True)

    def load_eight(self):
        self.load_seven()
        self.comicName_c8.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[7].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c8.setPixmap(
            QPixmap(generate_image_load(list_comics[7].image, list_comics[7].extension)))
        self.comicBtn_c8.setEnabled(True)

    def load_nine(self):
        self.load_eight()
        self.comicName_c9.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[8].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c9.setPixmap(
            QPixmap(generate_image_load(list_comics[8].image, list_comics[8].extension)))
        self.comicBtn_c9.setEnabled(True)

    def load_ten(self):
        self.load_nine()
        self.comicName_c10.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">'
            f'{list_comics[9].title}</span></p></body></html>')
        # Atributo para colocar la imagen del personaje
        self.characterComic_c10.setPixmap(
            QPixmap(generate_image_load(list_comics[9].image, list_comics[9].extension)))
        self.comicBtn_c10.setEnabled(True)

    def page_forward(self):
        global page
        self.btnNextComic.setChecked(False)
        page += 1
        if page >= total_pages:
            page -= 1
            QMessageBox.warning(self, "Error", "Ha alcanzado el maximo de paginas totales.")
        else:
            list_comics.clear()
            self.load_items()

    def return_page(self):
        global page
        self.btnPreviousComic.setChecked(False)
        page -= 1

        if page < 0:
            page += 1
            QMessageBox.warning(self, "Error", "Se ha decrecido la mayor cantidad de paginas existentes.")
        else:
            list_comics.clear()
            self.load_items()

    def order_by_name(self):
        global option
        if option == 1:
            QMessageBox.warning(self, "Error", "El listado de comics ya esta ordenado por nombre")
        else:
            option = 1
            list_comics.clear()
            self.load_items()

    def order_by_date(self):
        global option
        if option == 2:
            QMessageBox.warning(self, "Error", "El listado de comics ya esta ordenado por fecha de lanzamiento")
        else:
            option = 2
            list_comics.clear()
            self.load_items()

    def search_name(self):
        global option
        global page
        self.btnComicSearchName.setChecked(False)
        page = 0
        search_title = self.textComicName.text()
        if not search_title:
            QMessageBox.warning(self, "Error", "La linea de texto esta vacia.")
        else:
            option = 3
            list_comics.clear()
            self.load_items()

    def search_date(self):
        global option
        global page
        self.btnComicSearchDate.setChecked(False)
        page = 0
        option = 4
        list_comics.clear()
        self.load_items()

    def open_detail(self) -> None:
        if self.comicBtn_c1.isChecked():
            self.comicBtn_c1.setChecked(False)
            self.detail_comic_window = DetailComicWindow(103374)
        elif self.comicBtn_c2.isChecked():
            self.comicBtn_c2.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[1].id)
        elif self.comicBtn_c3.isChecked():
            self.comicBtn_c3.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[2].id)
        elif self.comicBtn_c4.isChecked():
            self.comicBtn_c4.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[3].id)
        elif self.comicBtn_c5.isChecked():
            self.comicBtn_c5.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[4].id)
        elif self.comicBtn_c6.isChecked():
            self.comicBtn_c6.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[5].id)
        elif self.comicBtn_c7.isChecked():
            self.comicBtn_c7.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[6].id)
        elif self.comicBtn_c8.isChecked():
            self.comicBtn_c8.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[7].id)
        elif self.comicBtn_c9.isChecked():
            self.comicBtn_c9.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[8].id)
        elif self.comicBtn_c10.isChecked():
            self.comicBtn_c10.setChecked(False)
            self.detail_comic_window = DetailComicWindow(list_comics[9].id)
        self.detail_comic_window.show()

    def view_character_window(self):
        self.communicateCharacter.verify_code.emit()
