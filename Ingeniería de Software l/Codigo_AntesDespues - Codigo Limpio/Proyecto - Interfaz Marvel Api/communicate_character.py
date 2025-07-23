from PyQt6.QtCore import QObject, pyqtSignal


class CommunicateCharacter(QObject):
    verify_code = pyqtSignal()