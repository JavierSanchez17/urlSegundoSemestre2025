import sys
from PyQt6.QtWidgets import QApplication

from characters_window import CharactersWindow
from comics_window import ComicsWindow
from communicate_comics import CommunicateComics
from communicate_character import CommunicateCharacter

app = QApplication(sys.argv)
communicateComics = CommunicateComics()
communicateCharacter = CommunicateCharacter()

principalCharacterWindow = CharactersWindow(communicateComics)
comicWindow = ComicsWindow(communicateCharacter)


def openPrincipalWindow():
    principalCharacterWindow.show()
    comicWindow.close()


def openComicsWindow():
    comicWindow.show()
    principalCharacterWindow.close()


def main():
    principalCharacterWindow.close()
    comicWindow.close()

    openPrincipalWindow()
    communicateComics.verify_code.connect(openComicsWindow)
    communicateCharacter.verify_code.connect(openPrincipalWindow)
    app.exec()


main()
