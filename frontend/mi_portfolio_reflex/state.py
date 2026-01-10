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

    @rx.var
    def sobre_mi_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("sobre_mi_titulo", "")
    
    @rx.var
    def sobre_mi_descripcion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("sobre_mi_descripcion", "")
    

    @rx.var
    def proyectos_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyectos_titulo", "")
    
    @rx.var
    def proyecto_1_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyecto_1_titulo", "")
    
    @rx.var
    def proyecto_1_desc(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyecto_1_desc", "")
    
    @rx.var
    def proyecto_2_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyecto_2_titulo", "")
    
    @rx.var
    def proyecto_2_desc(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyecto_2_desc", "")
    
    @rx.var
    def proyecto_3_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyecto_3_titulo", "")
    
    @rx.var
    def proyecto_3_desc(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("proyecto_3_desc", "")
    
    @rx.var
    def btn_ver_codigo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("btn_ver_codigo", "")


    @rx.var
    def contacto_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_titulo", "")
    
    @rx.var
    def contacto_subtitulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_subtitulo", "")
    
    @rx.var
    def form_nombre(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("form_nombre", "")
    
    @rx.var
    def form_email(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("form_email", "")
    
    @rx.var
    def form_mensaje(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("form_mensaje", "")
    
    @rx.var
    def btn_enviar(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("btn_enviar", "")


    @rx.var
    def footer_derechos(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("footer_derechos", "")
    
    @rx.var
    def habilidades_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("habilidades_titulo", "")

    @rx.var
    def nav_inicio(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_inicio", "")
    
    @rx.var
    def nav_sobre_mi(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_sobre_mi", "")
    
    @rx.var
    def nav_proyectos(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_proyectos", "")
    
    @rx.var
    def nav_contacto(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_contacto", "")

    
    



 