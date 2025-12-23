import reflex as rx 
from .translations import TRANSLATIONS

class State(rx.State):
    # variable de estado para el idioma actual
    idioma: str = "es" # valor por defecto

    # metodo para cambiar el idioma
    def cambiar_idioma(self, nuevo_idioma: str):
        self.idioma = nuevo_idioma
    

    # Propiedades computadas para cada traducción
    @rx.var
    def hero_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("hero_titulo", "")
    
    @rx.var
    def hero_subtitulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("hero_subtitulo", "")
    
    @rx.var
    def hero_descripcion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("hero_descripcion", "")
    
    @rx.var
    def btn_proyectos(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("btn_proyectos", "")
    
    @rx.var
    def btn_cv(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("btn_cv", "")

    
    



 