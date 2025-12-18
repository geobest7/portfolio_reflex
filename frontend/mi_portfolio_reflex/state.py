import reflex as rx 
from .translations import TRANSLATIONS

class State(rx.State):
    # variable de estado para el idioma actual
    idioma: str = "es" # valor por defecto

    # metodo para cambiar el idioma
    def cambiar_idioma(self, nuevo_idioma: str):
        self.idioma = nuevo_idioma
    

    def t(self, key: str) -> str:
        """Obtiene la traducción de una clave según el idioma actual"""
        return TRANSLATIONS.get(self.idioma, {}).get(key, key)



 