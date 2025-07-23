from PyQt6.QtCore import QObject, pyqtSignal


class CommunicateComics(QObject):
    verify_code = pyqtSignal()