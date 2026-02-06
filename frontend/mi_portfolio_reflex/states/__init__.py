import os
import reflex as rx
import httpx
from typing import List, Optional
from ..translations import TRANSLATIONS
from ..models import Proyecto, Curso, Experiencia, GitHubRepo
from ..utils import convertir_youtube_url

API_URL = os.environ.get("API_URL", "http://localhost:8001")


class State(rx.State):
    """Estado principal unificado - Compatible con Reflex (sin herencia múltiple)"""
    
    # ==================== BASE STATE - Idioma y Menú ====================
    idioma: str = "es"
    menu_abierto: bool = False
    def cambiar_idioma(self, nuevo_idioma: str):
        self.idioma = nuevo_idioma
    
    def toggle_menu(self):
        self.menu_abierto = not self.menu_abierto
    
    def cerrar_menu(self):
        self.menu_abierto = False
    
    # Propiedades computadas para traducciones
    @rx.var
    def hero_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("hero_titulo", "")
    
    @rx.var
    def hero_subtitulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("hero_subtitulo", "")
    
    @rx.var
    def sobre_mi_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("sobre_mi_titulo", "")
    
    @rx.var
    def sobre_mi_descripcion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("sobre_mi_descripcion", "")
    

    @rx.var
    def experiencia_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("experiencia_titulo", "")


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
    def tecnologias_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("tecnologias_titulo", "")
    
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
    
    @rx.var
    def formacion_titulo(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("formacion_titulo", "")
    
    # ==================== FORM STATE - Formulario de Contacto ====================
    form_nombre_value: str = ""
    form_email_value: str = ""
    form_mensaje_value: str = ""
    form_enviando: bool = False
    form_mensaje_estado: str = ""
    form_mensaje_texto: str = ""
    
    def set_nombre(self, value: str):
        self.form_nombre_value = value
    
    def set_email(self, value: str):
        self.form_email_value = value
    
    def set_mensaje(self, value: str):
        self.form_mensaje_value = value
    
    def validar_email(self, email: str) -> bool:
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def enviar_formulario(self):
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
        
        self.form_enviando = True
        
        try:
            response = httpx.post(
                f"{API_URL}/api/contacto/",
                json={
                    "nombre": self.form_nombre_value.strip(),
                    "email": self.form_email_value.strip(),
                    "mensaje": self.form_mensaje_value.strip(),
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                self.form_mensaje_estado = "exito"
                self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_exito", "")
                self.form_nombre_value = ""
                self.form_email_value = ""
                self.form_mensaje_value = ""
            else:
                self.form_mensaje_estado = "error"
                detail = response.json().get("detail", "Error al enviar")
                self.form_mensaje_texto = detail
        except httpx.TimeoutException:
            self.form_mensaje_estado = "error"
            self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_error_timeout", "Error: tiempo de espera agotado")
        except Exception:
            self.form_mensaje_estado = "error"
            self.form_mensaje_texto = TRANSLATIONS.get(self.idioma, {}).get("form_error_servidor", "Error al conectar con el servidor")
        finally:
            self.form_enviando = False
    
    def limpiar_mensaje_formulario(self):
        self.form_mensaje_estado = ""
        self.form_mensaje_texto = ""
        self.form_nombre_value = ""
        self.form_email_value = ""
        self.form_mensaje_value = ""
    
    def cerrar_menu_y_limpiar(self):
        self.menu_abierto = False
        self.form_mensaje_estado = ""
        self.form_mensaje_texto = ""
        self.form_nombre_value = ""
        self.form_email_value = ""
        self.form_mensaje_value = ""
    
    # ==================== DATA STATE - Datos Públicos ====================
    proyectos: List[Proyecto] = []
    cursos: List[Curso] = []
    experiencias: List[Experiencia] = []
    repos_github: list[GitHubRepo] = []
    
    cargando_proyectos: bool = False
    cargando_cursos: bool = False
    cargando_experiencias: bool = False
    cargando_repos: bool = False
    
    error_proyectos: str = ""
    error_cursos: str = ""
    error_experiencias: str = ""
    error_repos: str = ""
    
    def cargar_datos_iniciales(self):
        if len(self.proyectos) == 0:
            self.cargar_proyectos()
        if len(self.cursos) == 0:
            self.cargar_cursos()
        if len(self.experiencias) == 0:
            self.cargar_experiencias()
        if len(self.repos_github) == 0:
            self.cargar_repos_github()
    
    def cargar_proyectos(self):
        self.cargando_proyectos = True
        self.error_proyectos = ""
        
        try:
            response = httpx.get(f"{API_URL}/api/proyectos/", params={"destacados": True})
            if response.status_code == 200:
                data = response.json()
                for proyecto in data:
                    if proyecto.get("github_url") is None:
                        proyecto["github_url"] = ""
                    if proyecto.get("demo_url") is None:
                        proyecto["demo_url"] = ""
                    if proyecto.get("imagen_url") is None:
                        proyecto["imagen_url"] = ""
                    if proyecto.get("video_url") is None:
                        proyecto["video_url"] = ""
                    else:
                        proyecto["video_url"] = convertir_youtube_url(proyecto["video_url"])
                self.proyectos = [Proyecto(**proyecto) for proyecto in data]
            else:
                self.error_proyectos = f"Error {response.status_code}"
        except Exception as e:
            self.error_proyectos = f"Error de conexion: {str(e)}"
        finally:
            self.cargando_proyectos = False
    
    def cargar_cursos(self):
        self.cargando_cursos = True
        self.error_cursos = ""
        
        try:
            response = httpx.get(f"{API_URL}/api/cursos/")
            if response.status_code == 200:
                data = response.json()
                for curso in data:
                    if curso.get("fecha_fin") is None:
                        curso["fecha_fin"] = ""
                    if curso.get("certificado_url") is None:
                        curso["certificado_url"] = ""
                    if curso.get("diploma_pdf") is None:
                        curso["diploma_pdf"] = ""
                self.cursos = [Curso(**curso) for curso in data]
            else:
                self.error_cursos = f"Error {response.status_code}"
        except Exception as e:
            self.error_cursos = f"Error de conexion: {str(e)}"
        finally:
            self.cargando_cursos = False
    
    def cargar_experiencias(self):
        self.cargando_experiencias = True
        self.error_experiencias = ""
        
        try:
            response = httpx.get(f"{API_URL}/api/experiencias/", params={"mostrar_en_web": True})
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
                    if exp.get("video_url") is None:
                        exp["video_url"] = ""
                    else:
                        exp["video_url"] = convertir_youtube_url(exp["video_url"])
                self.experiencias = [Experiencia(**exp) for exp in data]
            else:
                self.error_experiencias = f"Error {response.status_code}"
        except Exception as e:
            self.error_experiencias = f"Error de conexion: {str(e)}"
        finally:
            self.cargando_experiencias = False
    
    def cargar_repos_github(self):
        self.cargando_repos = True
        self.error_repos = ""
        
        try:
            response = httpx.get(f"{API_URL}/api/github/repos")
            if response.status_code == 200:
                data = response.json()
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
    
    # ==================== AUTH STATE - Autenticación ====================
    token: str = ""
    usuario_autenticado: dict = {}
    esta_autenticado: bool = False
    error_login: str = ""
    cargando_login: bool = False
    
    def login(self, form_data: dict):
        self.cargando_login = True
        self.error_login = ""
        
        try:
            data = {
                "username": form_data["username"],
                "password": form_data["password"],
            }
            
            # Timeout de 10 segundos para evitar esperas largas
            response = httpx.post(
                f"{API_URL}/api/auth/login",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=10.0
            )
            
            if response.status_code == 200:
                result = response.json()
                self.token = result["access_token"]
                self.esta_autenticado = True
                
                # Guardar username del form para evitar segundo request
                self.usuario_autenticado = {"username": form_data["username"]}
                
                # Obtener info completa del usuario en background (no bloquea)
                try:
                    user_response = httpx.get(
                        f"{API_URL}/api/auth/me",
                        headers={"Authorization": f"Bearer {self.token}"},
                        timeout=5.0
                    )
                    if user_response.status_code == 200:
                        self.usuario_autenticado = user_response.json()
                except:
                    pass  # Si falla, ya tenemos el username básico
                
                self.cargando_login = False
                return rx.redirect("/admin")
                
            else:
                self.error_login = "Usuario o contraseña incorrectos"
                
        except httpx.TimeoutException:
            self.error_login = "Timeout - servidor lento, intenta de nuevo"
        except Exception as e:
            self.error_login = f"Error de conexión: {str(e)}"
        finally:
            self.cargando_login = False
    
    def logout(self):
        self.token = ""
        self.usuario_autenticado = {}
        self.esta_autenticado = False
        return rx.redirect("/login")
    
    # ==================== CUENTA - Cambio de credenciales ====================
    mostrar_modal_password: bool = False
    mostrar_modal_username: bool = False
    error_cambio: str = ""
    mensaje_exito: str = ""
    cargando_cambio: bool = False
    
    def abrir_modal_password(self):
        self.mostrar_modal_password = True
        self.error_cambio = ""
        self.mensaje_exito = ""
    
    def cerrar_modal_password(self):
        self.mostrar_modal_password = False
        self.error_cambio = ""
        self.mensaje_exito = ""
    
    def abrir_modal_username(self):
        self.mostrar_modal_username = True
        self.error_cambio = ""
        self.mensaje_exito = ""
    
    def cerrar_modal_username(self):
        self.mostrar_modal_username = False
        self.error_cambio = ""
        self.mensaje_exito = ""
    
    def cambiar_password(self, form_data: dict):
        self.cargando_cambio = True
        self.error_cambio = ""
        self.mensaje_exito = ""
        
        try:
            response = httpx.put(
                f"{API_URL}/api/auth/change-password",
                json={
                    "current_password": form_data["current_password"],
                    "new_password": form_data["new_password"]
                },
                headers={"Authorization": f"Bearer {self.token}"}
            )
            
            if response.status_code == 200:
                self.mensaje_exito = "Contraseña actualizada correctamente"
                self.mostrar_modal_password = False
                return rx.toast.success("Contraseña actualizada")
            else:
                error = response.json().get("detail", "Error al cambiar contraseña")
                self.error_cambio = error
                return rx.toast.error(error)
        except Exception as e:
            self.error_cambio = f"Error de conexión: {str(e)}"
            return rx.toast.error("Error de conexión")
        finally:
            self.cargando_cambio = False
    
    def cambiar_username(self, form_data: dict):
        self.cargando_cambio = True
        self.error_cambio = ""
        self.mensaje_exito = ""
        
        try:
            response = httpx.put(
                f"{API_URL}/api/auth/change-username",
                json={
                    "new_username": form_data["new_username"],
                    "password": form_data["password"]
                },
                headers={"Authorization": f"Bearer {self.token}"}
            )
            
            if response.status_code == 200:
                # Re-login para obtener token nuevo con el username actualizado
                login_response = httpx.post(
                    f"{API_URL}/api/auth/login",
                    data={
                        "username": form_data["new_username"],
                        "password": form_data["password"]
                    }
                )
                if login_response.status_code == 200:
                    self.token = login_response.json()["access_token"]
                self.usuario_autenticado["username"] = form_data["new_username"]
                self.mensaje_exito = "Usuario actualizado correctamente"
                self.mostrar_modal_username = False
                return rx.toast.success("Usuario actualizado")
            else:
                error = response.json().get("detail", "Error al cambiar usuario")
                self.error_cambio = error
                return rx.toast.error(error)
        except Exception as e:
            self.error_cambio = f"Error de conexión: {str(e)}"
            return rx.toast.error("Error de conexión")
        finally:
            self.cargando_cambio = False
    
    # ==================== ADMIN STATE - CRUD Admin ====================
    proyectos_admin: List[Proyecto] = []
    cargando_proyectos_admin: bool = False
    error_proyectos_admin: str = ""
    proyecto_editando: Optional[Proyecto] = None
    modo_edicion: bool = False
    
    def cargar_proyectos_admin(self):
        self.cargando_proyectos_admin = True
        self.error_proyectos_admin = ""
        
        try:
            response = httpx.get(
                f"{API_URL}/api/proyectos/",
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
                    if proyecto.get("video_url") is None:
                        proyecto["video_url"] = ""
                self.proyectos_admin = [Proyecto(**proyecto) for proyecto in data]
            else:
                self.error_proyectos_admin = f"Error {response.status_code}"
        except Exception as e:
            self.error_proyectos_admin = f"Error: {str(e)}"
        finally:
            self.cargando_proyectos_admin = False
    
    def eliminar_proyecto(self, proyecto_id: int):
        try:
            response = httpx.delete(
                f"{API_URL}/api/proyectos/{proyecto_id}",
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
        if proyecto_id > 0:
            proyecto = next((p for p in self.proyectos_admin if p.id == proyecto_id), None)
            if proyecto:
                self.proyecto_editando = proyecto
                self.modo_edicion = True
        else:
            self.proyecto_editando = None
            self.modo_edicion = False
        return rx.redirect("/admin/proyectos/form")
    
    def cancelar_edicion_proyecto(self):
        self.proyecto_editando = None
        self.modo_edicion = False
        return rx.redirect("/admin/proyectos")
    
    def guardar_proyecto(self, form_data: dict):
        try:
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
                "video_url": form_data.get("video_url", ""),
                "destacado": form_data.get("destacado", False),
                "orden": int(form_data.get("orden", 0)),
                "activo": True,
            }
            
            if self.modo_edicion and self.proyecto_editando:
                response = httpx.put(
                    f"{API_URL}/api/proyectos/{self.proyecto_editando.id}",
                    json=proyecto_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            else:
                response = httpx.post(
                    f"{API_URL}/api/proyectos/",
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
    
    cursos_admin: List[Curso] = []
    cargando_cursos_admin: bool = False
    error_cursos_admin: str = ""
    curso_editando: Optional[Curso] = None
    modo_edicion_curso: bool = False
    
    def cargar_cursos_admin(self):
        self.cargando_cursos_admin = True
        self.error_cursos_admin = ""
        
        try:
            response = httpx.get(
                f"{API_URL}/api/cursos/",
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
                    if curso.get("diploma_pdf") is None:
                        curso["diploma_pdf"] = ""
                self.cursos_admin = [Curso(**curso) for curso in data]
            else:
                self.error_cursos_admin = f"Error {response.status_code}"
        except Exception as e:
            self.error_cursos_admin = f"Error: {str(e)}"
        finally:
            self.cargando_cursos_admin = False
    
    def eliminar_curso(self, curso_id: int):
        try:
            response = httpx.delete(
                f"{API_URL}/api/cursos/{curso_id}",
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
        self.curso_editando = None
        self.modo_edicion_curso = False
        return rx.redirect("/admin/cursos")
    
    def guardar_curso(self, form_data: dict):
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
                "diploma_pdf": form_data.get("diploma_pdf", ""),
                "activo": True,
            }
            
            if self.modo_edicion_curso and self.curso_editando:
                response = httpx.put(
                    f"{API_URL}/api/cursos/{self.curso_editando.id}",
                    json=curso_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            else:
                response = httpx.post(
                    f"{API_URL}/api/cursos/",
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
    
    experiencias_admin: List[Experiencia] = []
    cargando_experiencias_admin: bool = False
    error_experiencias_admin: str = ""
    experiencia_editando: Optional[Experiencia] = None
    modo_edicion_experiencia: bool = False
    
    def cargar_experiencias_admin(self):
        self.cargando_experiencias_admin = True
        self.error_experiencias_admin = ""
        
        try:
            response = httpx.get(
                f"{API_URL}/api/experiencias/",
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
                    if exp.get("video_url") is None:
                        exp["video_url"] = ""
                self.experiencias_admin = [Experiencia(**exp) for exp in data]
            else:
                self.error_experiencias_admin = f"Error {response.status_code}"
        except Exception as e:
            self.error_experiencias_admin = f"Error: {str(e)}"
        finally:
            self.cargando_experiencias_admin = False
    
    def eliminar_experiencia(self, experiencia_id: int):
        try:
            response = httpx.delete(
                f"{API_URL}/api/experiencias/{experiencia_id}",
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
        self.experiencia_editando = None
        self.modo_edicion_experiencia = False
        return rx.redirect("/admin/experiencias")
    
    def guardar_experiencia(self, form_data: dict):
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
                "video_url": form_data.get("video_url", ""),
                "orden": int(form_data.get("orden", 0)),
                "mostrar_en_web": form_data.get("mostrar_en_web", False),
                "activo": True,
            }
            
            if self.modo_edicion_experiencia and self.experiencia_editando:
                response = httpx.put(
                    f"{API_URL}/api/experiencias/{self.experiencia_editando.id}",
                    json=experiencia_data,
                    headers={"Authorization": f"Bearer {self.token}"}
                )
            else:
                response = httpx.post(
                    f"{API_URL}/api/experiencias/",
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
    
    # ==================== ANALYTICS STATE ====================
    analytics_resumen: dict = {}
    analytics_paginas: list[dict] = []
    analytics_dispositivos: list[dict] = []
    analytics_navegadores: list[dict] = []
    analytics_por_dia: list[dict] = []
    analytics_recientes: list[dict] = []
    cargando_analytics: bool = False
    error_analytics: str = ""
    
    def cargar_analytics(self):
        self.cargando_analytics = True
        self.error_analytics = ""
        
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            
            r_resumen = httpx.get(
                f"{API_URL}/api/analytics/resumen",
                headers=headers, timeout=10.0
            )
            if r_resumen.status_code == 200:
                self.analytics_resumen = r_resumen.json()
            
            r_paginas = httpx.get(
                f"{API_URL}/api/analytics/paginas",
                headers=headers, timeout=10.0
            )
            if r_paginas.status_code == 200:
                self.analytics_paginas = r_paginas.json()
            
            r_dispositivos = httpx.get(
                f"{API_URL}/api/analytics/dispositivos",
                headers=headers, timeout=10.0
            )
            if r_dispositivos.status_code == 200:
                self.analytics_dispositivos = r_dispositivos.json()
            
            r_navegadores = httpx.get(
                f"{API_URL}/api/analytics/navegadores",
                headers=headers, timeout=10.0
            )
            if r_navegadores.status_code == 200:
                self.analytics_navegadores = r_navegadores.json()
            
            r_por_dia = httpx.get(
                f"{API_URL}/api/analytics/visitas-por-dia",
                headers=headers, timeout=10.0
            )
            if r_por_dia.status_code == 200:
                self.analytics_por_dia = r_por_dia.json()
            
            r_recientes = httpx.get(
                f"{API_URL}/api/analytics/recientes",
                headers=headers, timeout=10.0
            )
            if r_recientes.status_code == 200:
                self.analytics_recientes = r_recientes.json()
                
        except Exception as e:
            self.error_analytics = f"Error al cargar analíticas: {str(e)}"
        finally:
            self.cargando_analytics = False
