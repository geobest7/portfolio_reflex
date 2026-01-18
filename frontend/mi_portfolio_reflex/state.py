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
    institucion_es: str
    institucion_en: str
    institucion_it: str
    institucion_ca: str
    fecha_inicio: str
    fecha_fin: str = ""  
    certificado_url: str = ""  
    activo: bool
    orden: int


class Experiencia(BaseModel):
    id: int
    tipo: str
    empresa: str
    cargo_es: str
    cargo_en: str
    cargo_it: str
    cargo_ca: str
    fecha_inicio: str
    fecha_fin: str = ""
    actual: bool
    descripcion_es: str = ""
    descripcion_en: str = ""
    descripcion_it: str = ""
    descripcion_ca: str = ""
    tecnologias: List[str]
    orden: int
    activo: bool
    mostrar_en_web: bool


class GitHubRepo(BaseModel):
    """Modelo para repositorio de GitHub"""
    id: int
    repo_id: int
    name: str
    full_name: str
    description: str = ""
    html_url: str
    homepage: str = ""
    language: str = ""
    stargazers_count: int = 0
    forks_count: int = 0
    topics: list[str] = []
    created_at: str = ""
    updated_at: str = ""
    pushed_at: str = ""


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


    # Variables para experiencias
    experiencias: List[Experiencia] = []
    cargando_experiencias: bool = False
    error_experiencias: str = ""


    # GitHub repos
    repos_github: list[GitHubRepo] = []
    cargando_repos: bool = False
    error_repos: str = ""


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
    def nav_experiencia(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_experiencia", "")

    @rx.var
    def nav_github(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("nav_github", "")


    @rx.var
    def github_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("github_titulo", "")

    @rx.var
    def github_subtitulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("github_subtitulo", "")

    @rx.var
    def github_ver_repo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("github_ver_repo", "")
        
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


    # Propiedades computadas para Formación
    @rx.var
    def formacion_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_titulo", "")



    def cargar_datos_iniciales(self):
        """Cargar proyectos y cursos automáticamente al montar la página"""
        if len(self.proyectos) == 0:
            self.cargar_proyectos()
        if len(self.cursos) == 0:
            self.cargar_cursos()
        if len(self.experiencias) == 0:
            self.cargar_experiencias()
        if len(self.repos_github) == 0:
            self.cargar_repos_github()

    def cargar_proyectos(self):
        """Cargar proyectos desde la API"""
        self.cargando_proyectos = True
        self.error_proyectos = ""
        
        try:
            response = httpx.get("http://localhost:8001/api/proyectos/", params={"destacados": True})
            if response.status_code == 200:
                data = response.json()
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

    
    def cargar_experiencias(self):
        """Cargar experiencias desde la API"""
        self.cargando_experiencias = True
        self.error_experiencias = ""
        
        try:
            response = httpx.get("http://localhost:8001/api/experiencias/", params={"mostrar_en_web": True})
            if response.status_code == 200:
                data = response.json()
                # Convertir None a string vacío
                for exp in data:
                    if exp.get("fecha_fin") is None:
                        exp["fecha_fin"] = ""
                    if exp.get("descripcion_es") is None:
                        exp["descripcion_es"] = ""
                    if exp.get("descripcion_en") is None:
                        exp["descripcion_en"] = ""
                    if exp.get("descripcion_it") is None:
                        exp["descripcion_it"] = ""
                    if exp.get("descripcion_ca") is None:
                        exp["descripcion_ca"] = ""
                self.experiencias = [Experiencia(**exp) for exp in data]
            else:
                self.error_experiencias = f"Error {response.status_code}"
        except Exception as e:
            self.error_experiencias = f"Error de conexion: {str(e)}"
        finally:
            self.cargando_experiencias = False

    

    def cargar_repos_github(self):
        """Cargar repositorios de GitHub desde la API"""
        self.cargando_repos = True
        self.error_repos = ""
        
        try:
            response = httpx.get("http://localhost:8001/api/github/repos")
            if response.status_code == 200:
                data = response.json()
                # Convertir None a valores por defecto
                for repo in data:
                    if repo.get("description") is None:
                        repo["description"] = ""
                    if repo.get("homepage") is None:
                        repo["homepage"] = ""
                    if repo.get("language") is None:
                        repo["language"] = ""
                    if repo.get("topics") is None:
                        repo["topics"] = []
                self.repos_github = [GitHubRepo(**repo) for repo in data]
            else:
                self.error_repos = f"Error {response.status_code}"
        except Exception as e:
            self.error_repos = f"Error de conexión: {str(e)}"
        finally:
            self.cargando_repos = False

    # ==================== AUTENTICACIÓN ====================
    # Token y usuario autenticado
    token: str = ""
    usuario_autenticado: dict = {}
    esta_autenticado: bool = False
    error_login: str = ""
    cargando_login: bool = False

    def login(self, form_data: dict):
        """Login de usuario admin"""
        self.cargando_login = True
        self.error_login = ""
        
        try:
            # Preparar datos para OAuth2
            data = {
                "username": form_data["username"],
                "password": form_data["password"],
            }
            
            response = httpx.post(
                "http://localhost:8001/api/auth/login",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            
            if response.status_code == 200:
                result = response.json()
                self.token = result["access_token"]
                self.esta_autenticado = True
                
                # Obtener info del usuario
                user_response = httpx.get(
                    "http://localhost:8001/api/auth/me",
                    headers={"Authorization": f"Bearer {self.token}"}
                )
                
                if user_response.status_code == 200:
                    self.usuario_autenticado = user_response.json()
                    return rx.redirect("/admin")
                
            else:
                self.error_login = "Usuario o contraseña incorrectos"
                
        except Exception as e:
            self.error_login = f"Error de conexión: {str(e)}"
        finally:
            self.cargando_login = False

    def logout(self):
        """Cerrar sesión"""
        self.token = ""
        self.usuario_autenticado = {}
        self.esta_autenticado = False
        return rx.redirect("/login")



    # ==================== CRUD PROYECTOS ====================
    proyectos_admin: List[Proyecto] = []
    cargando_proyectos_admin: bool = False
    error_proyectos_admin: str = ""
    proyecto_editando: Optional[Proyecto] = None
    modo_edicion: bool = False

    def cargar_proyectos_admin(self):
        """Cargar todos los proyectos para admin (incluye inactivos)"""
        self.cargando_proyectos_admin = True
        self.error_proyectos_admin = ""
        
        try:
            response = httpx.get(
                "http://localhost:8001/api/proyectos/",
                params={"limit": 100},
                headers={"Authorization": f"Bearer {self.token}"}
            )
            if response.status_code == 200:
                data = response.json()
                for proyecto in data:
                    if proyecto.get("github_url") is None:
                        proyecto["github_url"] = ""
                    if proyecto.get("demo_url") is None:
                        proyecto["demo_url"] = ""
                    if proyecto.get("imagen_url") is None:
                        proyecto["imagen_url"] = ""
                self.proyectos_admin = [Proyecto(**proyecto) for proyecto in data]
            else:
                self.error_proyectos_admin = f"Error {response.status_code}"
        except Exception as e:
            self.error_proyectos_admin = f"Error: {str(e)}"
        finally:
            self.cargando_proyectos_admin = False

    def eliminar_proyecto(self, proyecto_id: int):
        """Eliminar proyecto (soft delete)"""
        try:
            response = httpx.delete(
                f"http://localhost:8001/api/proyectos/{proyecto_id}",
                headers={"Authorization": f"Bearer {self.token}"}
            )
            if response.status_code == 200:
                self.cargar_proyectos_admin()
                return rx.toast.success("Proyecto eliminado correctamente")
            else:
                return rx.toast.error("Error al eliminar proyecto")
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")

    def abrir_formulario_proyecto(self, proyecto_id: int = 0):
        """Abrir formulario para crear o editar proyecto"""
        if proyecto_id > 0:
            # Buscar el proyecto
            proyecto = next((p for p in self.proyectos_admin if p.id == proyecto_id), None)
            if proyecto:
                self.proyecto_editando = proyecto
                self.modo_edicion = True
        else:
            self.proyecto_editando = None
            self.modo_edicion = False
        return rx.redirect("/admin/proyectos/form")

    def cancelar_edicion_proyecto(self):
        """Cancelar edición y volver a la lista"""
        self.proyecto_editando = None
        self.modo_edicion = False
        return rx.redirect("/admin/proyectos")

    def guardar_proyecto(self, form_data: dict):
        """Crear o actualizar proyecto"""
        try:
            # Preparar datos
            proyecto_data = {
                "titulo_es": form_data["titulo_es"],
                "titulo_en": form_data["titulo_en"],
                "titulo_it": form_data["titulo_it"],
                "titulo_ca": form_data["titulo_ca"],
                "descripcion_es": form_data["descripcion_es"],
                "descripcion_en": form_data["descripcion_en"],
                "descripcion_it": form_data["descripcion_it"],
                "descripcion_ca": form_data["descripcion_ca"],
                "tecnologias": form_data.get("tecnologias", "").split(",") if form_data.get("tecnologias") else [],
                "github_url": form_data.get("github_url", ""),
                "demo_url": form_data.get("demo_url", ""),
                "imagen_url": form_data.get("imagen_url", ""),
                "destacado": form_data.get("destacado", False),
                "orden": int(form_data.get("orden", 0)),
                "activo": True,
            }
            
            if self.modo_edicion and self.proyecto_editando:
                # Actualizar
                response = httpx.put(
                    f"http://localhost:8001/api/proyectos/{self.proyecto_editando.id}",
                    json=proyecto_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            else:
                # Crear
                response = httpx.post(
                    "http://localhost:8001/api/proyectos/",
                    json=proyecto_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            
            if response.status_code in [200, 201]:
                self.proyecto_editando = None
                self.modo_edicion = False
                self.cargar_proyectos_admin()
                return rx.redirect("/admin/proyectos")
            else:
                return rx.toast.error(f"Error al guardar: {response.status_code}")
                
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")


    # ==================== CRUD CURSOS ====================
    cursos_admin: List[Curso] = []
    cargando_cursos_admin: bool = False
    error_cursos_admin: str = ""
    curso_editando: Optional[Curso] = None
    modo_edicion_curso: bool = False

    def cargar_cursos_admin(self):
        """Cargar todos los cursos para admin"""
        self.cargando_cursos_admin = True
        self.error_cursos_admin = ""
        
        try:
            response = httpx.get(
                "http://localhost:8001/api/cursos/",
                params={"limit": 100},
                headers={"Authorization": f"Bearer {self.token}"}
            )
            if response.status_code == 200:
                data = response.json()
                for curso in data:
                    if curso.get("fecha_fin") is None:
                        curso["fecha_fin"] = ""
                    if curso.get("certificado_url") is None:
                        curso["certificado_url"] = ""
                self.cursos_admin = [Curso(**curso) for curso in data]
            else:
                self.error_cursos_admin = f"Error {response.status_code}"
        except Exception as e:
            self.error_cursos_admin = f"Error: {str(e)}"
        finally:
            self.cargando_cursos_admin = False

    def eliminar_curso(self, curso_id: int):
        """Eliminar curso (soft delete)"""
        try:
            response = httpx.delete(
                f"http://localhost:8001/api/cursos/{curso_id}",
                headers={"Authorization": f"Bearer {self.token}"}
            )
            if response.status_code == 200:
                self.cargar_cursos_admin()
                return rx.toast.success("Curso eliminado correctamente")
            else:
                return rx.toast.error("Error al eliminar curso")
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")

    def abrir_formulario_curso(self, curso_id: int = 0):
        """Abrir formulario para crear o editar curso"""
        if curso_id > 0:
            curso = next((c for c in self.cursos_admin if c.id == curso_id), None)
            if curso:
                self.curso_editando = curso
                self.modo_edicion_curso = True
        else:
            self.curso_editando = None
            self.modo_edicion_curso = False
        return rx.redirect("/admin/cursos/form")

    def cancelar_edicion_curso(self):
        """Cancelar edición y volver a la lista"""
        self.curso_editando = None
        self.modo_edicion_curso = False
        return rx.redirect("/admin/cursos")

    def guardar_curso(self, form_data: dict):
        """Crear o actualizar curso"""
        try:
            curso_data = {
                "tipo": form_data["tipo"],
                "titulo_es": form_data["titulo_es"],
                "titulo_en": form_data["titulo_en"],
                "titulo_it": form_data["titulo_it"],
                "titulo_ca": form_data["titulo_ca"],
                "institucion_es": form_data["institucion_es"],
                "institucion_en": form_data["institucion_en"],
                "institucion_it": form_data["institucion_it"],
                "institucion_ca": form_data["institucion_ca"],
                "fecha_inicio": form_data["fecha_inicio"],
                "fecha_fin": form_data.get("fecha_fin", ""),
                "certificado_url": form_data.get("certificado_url", ""),
                "activo": True,
            }
            
            if self.modo_edicion_curso and self.curso_editando:
                response = httpx.put(
                    f"http://localhost:8001/api/cursos/{self.curso_editando.id}",
                    json=curso_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            else:
                response = httpx.post(
                    "http://localhost:8001/api/cursos/",
                    json=curso_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            
            if response.status_code in [200, 201]:
                self.curso_editando = None
                self.modo_edicion_curso = False
                self.cargar_cursos_admin()
                return rx.redirect("/admin/cursos")
            else:
                return rx.toast.error(f"Error al guardar: {response.status_code}")
                
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")


    # ==================== CRUD EXPERIENCIAS ====================
    experiencias_admin: List[Experiencia] = []
    cargando_experiencias_admin: bool = False
    error_experiencias_admin: str = ""
    experiencia_editando: Optional[Experiencia] = None
    modo_edicion_experiencia: bool = False

    def cargar_experiencias_admin(self):
        """Cargar todas las experiencias para admin"""
        self.cargando_experiencias_admin = True
        self.error_experiencias_admin = ""
        
        try:
            response = httpx.get(
                "http://localhost:8001/api/experiencias/",
                params={"limit": 100},
                headers={"Authorization": f"Bearer {self.token}"}
            )
            if response.status_code == 200:
                data = response.json()
                for exp in data:
                    if exp.get("fecha_fin") is None:
                        exp["fecha_fin"] = ""
                    if exp.get("descripcion_es") is None:
                        exp["descripcion_es"] = ""
                    if exp.get("descripcion_en") is None:
                        exp["descripcion_en"] = ""
                    if exp.get("descripcion_it") is None:
                        exp["descripcion_it"] = ""
                    if exp.get("descripcion_ca") is None:
                        exp["descripcion_ca"] = ""
                self.experiencias_admin = [Experiencia(**exp) for exp in data]
            else:
                self.error_experiencias_admin = f"Error {response.status_code}"
        except Exception as e:
            self.error_experiencias_admin = f"Error: {str(e)}"
        finally:
            self.cargando_experiencias_admin = False

    def eliminar_experiencia(self, experiencia_id: int):
        """Eliminar experiencia (soft delete)"""
        try:
            response = httpx.delete(
                f"http://localhost:8001/api/experiencias/{experiencia_id}",
                headers={"Authorization": f"Bearer {self.token}"}
            )
            if response.status_code == 200:
                self.cargar_experiencias_admin()
                return rx.toast.success("Experiencia eliminada correctamente")
            else:
                return rx.toast.error("Error al eliminar experiencia")
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")

    def abrir_formulario_experiencia(self, experiencia_id: int = 0):
        """Abrir formulario para crear o editar experiencia"""
        if experiencia_id > 0:
            exp = next((e for e in self.experiencias_admin if e.id == experiencia_id), None)
            if exp:
                self.experiencia_editando = exp
                self.modo_edicion_experiencia = True
        else:
            self.experiencia_editando = None
            self.modo_edicion_experiencia = False
        return rx.redirect("/admin/experiencias/form")

    def cancelar_edicion_experiencia(self):
        """Cancelar edición y volver a la lista"""
        self.experiencia_editando = None
        self.modo_edicion_experiencia = False
        return rx.redirect("/admin/experiencias")

    def guardar_experiencia(self, form_data: dict):
        """Crear o actualizar experiencia"""
        try:
            experiencia_data = {
                "tipo": form_data["tipo"],
                "empresa": form_data["empresa"],
                "cargo_es": form_data["cargo_es"],
                "cargo_en": form_data["cargo_en"],
                "cargo_it": form_data["cargo_it"],
                "cargo_ca": form_data["cargo_ca"],
                "fecha_inicio": form_data["fecha_inicio"],
                "fecha_fin": form_data.get("fecha_fin", ""),
                "actual": form_data.get("actual", False),
                "descripcion_es": form_data.get("descripcion_es", ""),
                "descripcion_en": form_data.get("descripcion_en", ""),
                "descripcion_it": form_data.get("descripcion_it", ""),
                "descripcion_ca": form_data.get("descripcion_ca", ""),
                "tecnologias": form_data.get("tecnologias", "").split(",") if form_data.get("tecnologias") else [],
                "orden": int(form_data.get("orden", 0)),
                "mostrar_en_web": form_data.get("mostrar_en_web", False),
                "activo": True,
            }
            
            if self.modo_edicion_experiencia and self.experiencia_editando:
                response = httpx.put(
                    f"http://localhost:8001/api/experiencias/{self.experiencia_editando.id}",
                    json=experiencia_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            else:
                response = httpx.post(
                    "http://localhost:8001/api/experiencias/",
                    json=experiencia_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            
            if response.status_code in [200, 201]:
                self.experiencia_editando = None
                self.modo_edicion_experiencia = False
                self.cargar_experiencias_admin()
                return rx.redirect("/admin/experiencias")
            else:
                return rx.toast.error(f"Error al guardar: {response.status_code}")
                
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")