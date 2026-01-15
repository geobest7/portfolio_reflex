import reflex as rx 
from .translations import TRANSLATIONS
import httpx
from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class Proyecto(BaseModel):
    id: int
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    descripcion_es: str
    descripcion_en: str
    descripcion_it: str
    descripcion_ca: str
    tecnologias: List[str]
    github_url: str = ""  
    demo_url: str = "" 
    imagen_url: str = ""     
    destacado: bool
    activo: bool
    orden: int

class Curso(BaseModel):
    id: int
    tipo: str
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    institucion: str
    fecha_inicio: str
    fecha_fin: str = ""  
    certificado_url: str = ""  
    activo: bool
    orden: int


class State(rx.State):
    # variable de estado para el idioma actual
    idioma: str = "es" # valor por defecto
    
    # variable de estado para el menú móvil
    menu_abierto: bool = False

    # Variables de estado para el formulario de contacto
    form_nombre_value: str = ""
    form_email_value: str = ""
    form_mensaje_value: str = ""
    form_enviando: bool = False
    form_mensaje_estado: str = ""  # "exito", "error", o ""
    form_mensaje_texto: str = ""

    # Variables para datos de la API
    proyectos: List[Proyecto] = []
    cursos: List[Curso] = []
    cargando_proyectos: bool = False
    cargando_cursos: bool = False
    error_proyectos: str = ""
    error_cursos: str = ""

    # metodo para cambiar el idioma
    def cambiar_idioma(self, nuevo_idioma: str):
        self.idioma = nuevo_idioma
    
    # metodo para toggle del menú móvil
    def toggle_menu(self):
        self.menu_abierto = not self.menu_abierto
    
    # metodo para cerrar el menú
    def cerrar_menu(self):
        self.menu_abierto = False
    

    # Métodos para el formulario de contacto
    def set_nombre(self, value: str):
        self.form_nombre_value = value
    
    def set_email(self, value: str):
        self.form_email_value = value
    
    def set_mensaje(self, value: str):
        self.form_mensaje_value = value
    
    def validar_email(self, email: str) -> bool:
        """Validación básica de email"""
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def enviar_formulario(self):
        """Enviar formulario de contacto"""
        # Validaciones
        if not self.form_nombre_value.strip():
            self.form_mensaje_estado = "error"
            self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_error_nombre", "")
            return
        
        if not self.form_email_value.strip():
            self.form_mensaje_estado = "error"
            self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_error_email_vacio", "")
            return
        
        if not self.validar_email(self.form_email_value):
            self.form_mensaje_estado = "error"
            self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_error_email_invalido", "")
            return
        
        if not self.form_mensaje_value.strip():
            self.form_mensaje_estado = "error"
            self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_error_mensaje", "")
            return
        
        # Simular envío (aquí irá la integración con EmailJS o backend)
        self.form_enviando = True
        
        # TODO: Integrar con servicio de email
        # Por ahora, solo mostramos mensaje de éxito
        
        self.form_mensaje_estado = "exito"
        self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_exito", "")
        self.form_enviando = False
        
        # Limpiar formulario
        self.form_nombre_value = ""
        self.form_email_value = ""
        self.form_mensaje_value = ""


    def limpiar_mensaje_formulario(self):
        """Limpiar mensaje de estado y campos del formulario al navegar"""
        self.form_mensaje_estado = ""
        self.form_mensaje_texto = ""
        self.form_nombre_value = ""
        self.form_email_value = ""
        self.form_mensaje_value = ""



    def cerrar_menu_y_limpiar(self):
        """Cerrar menú móvil y limpiar mensaje y campos del formulario"""
        self.menu_abierto = False
        self.form_mensaje_estado = ""
        self.form_mensaje_texto = ""
        self.form_nombre_value = ""
        self.form_email_value = ""
        self.form_mensaje_value = ""

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
    def contacto_info_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_info_titulo", "")
    
    @rx.var
    def contacto_email(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_email", "")
    
    @rx.var
    def contacto_telefono(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_telefono", "")
    
    @rx.var
    def contacto_linkedin(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_linkedin", "")
    
    @rx.var
    def contacto_github(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("contacto_github", "")


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

    @rx.var
    def nav_formacion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_formacion", "")

    @rx.var
    def nav_cv(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_cv", "")


    # Propiedades computadas para Experiencia
    @rx.var
    def experiencia_subtitulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("experiencia_subtitulo", "")

    @rx.var
    def exp_cargo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("exp_cargo", "")

    @rx.var
    def exp_empresa(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("exp_empresa", "")

    @rx.var
    def exp_periodo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("exp_periodo", "")

    @rx.var
    def exp_descripcion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("exp_descripcion", "")

    @rx.var
    def exp_tecnologias(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("exp_tecnologias", "")


    # Propiedades computadas para Formación
    @rx.var
    def formacion_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_titulo", "")

    @rx.var
    def formacion_diploma_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_diploma_titulo", "")

    @rx.var
    def formacion_diploma_institucion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_diploma_institucion", "")

    @rx.var
    def formacion_diploma_periodo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_diploma_periodo", "")

    @rx.var
    def formacion_cursos_subtitulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_cursos_subtitulo", "")

    @rx.var
    def curso1_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso1_titulo", "")

    @rx.var
    def curso1_institucion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso1_institucion", "")

    @rx.var
    def curso1_periodo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso1_periodo", "")

    @rx.var
    def curso2_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso2_titulo", "")

    @rx.var
    def curso2_institucion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso2_institucion", "")

    @rx.var
    def curso2_periodo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso2_periodo", "")

    @rx.var
    def curso3_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso3_titulo", "")

    @rx.var
    def curso3_institucion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso3_institucion", "")

    @rx.var
    def curso3_periodo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("curso3_periodo", "")


    def cargar_proyectos(self):
        """Cargar proyectos desde la API"""
        self.cargando_proyectos = True
        self.error_proyectos = ""
        
        try:
            response = httpx.get("http://localhost:8001/api/proyectos/", params={"destacados": True})
            if response.status_code == 200:
                data = response.json()
                # Convertir None a string vacío
                # Convertir None a string vacío
                for proyecto in data:
                    if proyecto.get("github_url") is None:
                        proyecto["github_url"] = ""
                    if proyecto.get("demo_url") is None:
                        proyecto["demo_url"] = ""
                    if proyecto.get("imagen_url") is None:
                        proyecto["imagen_url"] = ""
                self.proyectos = [Proyecto(**proyecto) for proyecto in data]
            else:
                self.error_proyectos = f"Error {response.status_code}"
        except Exception as e:
            self.error_proyectos = f"Error de conexion: {str(e)}"
        finally:
            self.cargando_proyectos = False

    def cargar_cursos(self):
        """Cargar cursos desde la API"""
        self.cargando_cursos = True
        self.error_cursos = ""
        
        try:
            response = httpx.get("http://localhost:8001/api/cursos/")
            if response.status_code == 200:
                data = response.json()
                # Convertir None a string vacio
                for curso in data:
                    if curso.get("fecha_fin") is None:
                        curso["fecha_fin"] = ""
                    if curso.get("certificado_url") is None:
                        curso["certificado_url"] = ""
                self.cursos = [Curso(**curso) for curso in data]
            else:
                self.error_cursos = f"Error {response.status_code}"
        except Exception as e:
            self.error_cursos = f"Error de conexion: {str(e)}"
        finally:
            self.cargando_cursos = False