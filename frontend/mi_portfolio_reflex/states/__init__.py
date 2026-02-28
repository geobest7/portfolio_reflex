import os
import reflex as rx
import httpx
from typing import List, Optional
from ..translations import TRANSLATIONS
from ..models import Proyecto, Curso, Experiencia, GitHubRepo

API_URL = os.environ.get("API_URL", "http://localhost:8001")


class State(rx.State):
    """Estado principal unificado - Compatible con Reflex (sin herencia múltiple)"""
    
    # ==================== TRACKING ====================
    _visita_registrada: bool = False

    def registrar_visita(self):
        """Recoge datos del navegador via JS y los envía al callback."""
        if self._visita_registrada:
            return
        return rx.call_script(
            """
            JSON.stringify({
                pagina: window.location.pathname,
                referrer: document.referrer || '',
                user_agent: navigator.userAgent || '',
                screen_width: window.screen.width,
                screen_height: window.screen.height,
                idioma: navigator.language || '',
                plataforma: navigator.platform || ''
            })
            """,
            callback=State.enviar_tracking,
        )

    def enviar_tracking(self, datos_json: str):
        """Recibe datos del navegador y los envía al backend FastAPI."""
        if self._visita_registrada:
            return
        self._visita_registrada = True
        try:
            import json
            datos = json.loads(datos_json)
            httpx.post(
                f"{API_URL}/api/analytics/track",
                json=datos,
                timeout=10.0,
            )
        except Exception:
            pass

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
    
    diploma_url_actual: str = ""
    
    def abrir_diploma(self, url: str):
        """Guardar URL del diploma y redirigir a la página visor"""
        self.diploma_url_actual = url
        return rx.redirect("/diploma")
    
    @rx.var
    def ver_diploma(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("ver_diploma", "")
    
    @rx.var
    def ver_certificado(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("ver_certificado", "")
    
    @rx.var
    def ver_descripcion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("ver_descripcion", "")
    
    @rx.var
    def ocultar_descripcion(self) -> str:
        return TRANSLATIONS.get(self.idioma, {}).get("ocultar_descripcion", "")
    
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
                timeout=60.0
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
    
    @staticmethod
    def _limpiar_nulos(d: dict, campos: list[str]):
        """Convierte None a '' para campos opcionales string"""
        for c in campos:
            if d.get(c) is None:
                d[c] = ""
    
    def cargar_proyectos(self):
        self.cargando_proyectos = True
        self.error_proyectos = ""
        
        try:
            response = httpx.get(f"{API_URL}/api/proyectos/", params={"destacados": True})
            if response.status_code == 200:
                data = response.json()
                for p in data:
                    p["github_url"] = p.pop("url_github", "") or ""
                    p["demo_url"] = p.pop("url_demo", "") or ""
                    self._limpiar_nulos(p, ["imagen_url", "video_url"])
                self.proyectos = [Proyecto(**p) for p in data]
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
                for c in data:
                    self._limpiar_nulos(c, [
                        "fecha_fin", "descripcion_es", "descripcion_en",
                        "descripcion_it", "descripcion_ca",
                        "certificado_url", "diploma_pdf",
                    ])
                self.cursos = [Curso(**c) for c in data]
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
            response = httpx.get(f"{API_URL}/api/experiencias/")
            if response.status_code == 200:
                data = response.json()
                for e in data:
                    self._limpiar_nulos(e, [
                        "fecha_inicio", "fecha_fin",
                        "descripcion_es", "descripcion_en",
                        "descripcion_it", "descripcion_ca",
                        "imagen_url", "video_url", "documento_url",
                    ])
                self.experiencias = [Experiencia(**e) for e in data]
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
                for p in data:
                    p["github_url"] = p.pop("url_github", "") or ""
                    p["demo_url"] = p.pop("url_demo", "") or ""
                    self._limpiar_nulos(p, ["imagen_url", "video_url"])
                self.proyectos_admin = [Proyecto(**p) for p in data]
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
        self.reset_upload_urls()
        self._prefetch_video_sign()
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
            tecnologias_raw = form_data.get("tecnologias", "").strip()
            tecnologias = [t.strip() for t in tecnologias_raw.split(",") if t.strip()] if tecnologias_raw else []
            proyecto_data = {
                "titulo_es": form_data["titulo_es"],
                "titulo_en": form_data["titulo_en"],
                "titulo_it": form_data["titulo_it"],
                "titulo_ca": form_data["titulo_ca"],
                "descripcion_es": form_data["descripcion_es"],
                "descripcion_en": form_data["descripcion_en"],
                "descripcion_it": form_data["descripcion_it"],
                "descripcion_ca": form_data["descripcion_ca"],
                "tecnologias": tecnologias,
                "url_github": form_data.get("github_url", "").strip() or None,
                "url_demo": form_data.get("demo_url", "").strip() or None,
                "imagen_url": self.uploaded_imagen_url or form_data.get("imagen_url", "").strip() or form_data.get("imagen_url_manual", "").strip() or None,
                "video_url": self.uploaded_video_url or form_data.get("video_url", "").strip() or form_data.get("video_url_manual", "").strip() or None,
                "destacado": form_data.get("destacado") == "on",
                "orden": int(form_data.get("orden", 0) or 0),
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
                detail = response.json().get("detail", response.text[:200]) if response.text else str(response.status_code)
                return rx.toast.error(f"Error {response.status_code}: {detail}")
                
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")
    
    # ==================== UPLOAD STATE ====================
    uploaded_diploma_url: str = ""
    uploaded_certificado_url: str = ""
    uploaded_video_url: str = ""
    uploaded_imagen_url: str = ""
    uploaded_documento_url: str = ""
    subiendo_archivo: bool = False
    
    # Sign params para upload directo de video a Cloudinary
    video_sign_cloud_name: str = ""
    video_sign_api_key: str = ""
    video_sign_timestamp: str = ""
    video_sign_signature: str = ""
    
    async def _upload_to_cloudinary(self, file_data: bytes, filename: str, content_type: str, timeout: float = 30.0) -> str:
        """Sube archivo a Cloudinary via backend API (async). Retorna URL o lanza excepción."""
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                f"{API_URL}/api/upload/",
                files={"file": (filename, file_data, content_type)},
                headers={"Authorization": f"Bearer {self.token}"},
            )
        if response.status_code == 200:
            return response.json()["url"]
        detail = response.json().get("detail", response.text[:200]) if response.text else str(response.status_code)
        raise Exception(f"Error {response.status_code}: {detail}")
    
    async def upload_diploma(self, files: list[rx.UploadFile]):
        if not files:
            return
        self.subiendo_archivo = True
        yield
        try:
            file = files[0]
            data = await file.read()
            self.uploaded_diploma_url = await self._upload_to_cloudinary(data, file.filename, file.content_type or "application/pdf")
            yield rx.toast.success("Diploma subido correctamente")
        except Exception as e:
            yield rx.toast.error(f"Error al subir: {str(e)}")
        finally:
            self.subiendo_archivo = False
    
    async def upload_certificado(self, files: list[rx.UploadFile]):
        if not files:
            return
        self.subiendo_archivo = True
        yield
        try:
            file = files[0]
            data = await file.read()
            self.uploaded_certificado_url = await self._upload_to_cloudinary(data, file.filename, file.content_type or "application/pdf")
            yield rx.toast.success("Certificado subido correctamente")
        except Exception as e:
            yield rx.toast.error(f"Error al subir: {str(e)}")
        finally:
            self.subiendo_archivo = False
    
    def _prefetch_video_sign(self):
        """Pre-fetch Cloudinary sign params para video upload directo"""
        try:
            resp = httpx.get(
                f"{API_URL}/api/upload/sign",
                params={"resource_type": "video"},
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=10.0,
            )
            if resp.status_code == 200:
                sign = resp.json()
                self.video_sign_cloud_name = sign["cloud_name"]
                self.video_sign_api_key = sign["api_key"]
                self.video_sign_timestamp = str(sign["timestamp"])
                self.video_sign_signature = sign["signature"]
        except Exception:
            pass
    
    def subir_video_directo(self):
        """Lee el video ya seleccionado del file input y lo sube a Cloudinary
        via XHR síncrono desde el navegador. Browser → Cloudinary (1 salto)."""
        if not self.video_sign_cloud_name:
            return rx.toast.error("Error: firma de upload no disponible. Recarga la página.")
        
        self.subiendo_archivo = True
        
        js_code = (
            "(() => {"
            "  const fi = document.getElementById('_vid_file_input');"
            "  if (!fi || !fi.files || !fi.files[0]) return JSON.stringify({error: 'Selecciona un video primero'});"
            "  const file = fi.files[0];"
            "  if (file.size > 100*1024*1024) return JSON.stringify({error: 'Video demasiado grande (máx 100MB)'});"
            "  const fd = new FormData();"
            "  fd.append('file', file);"
            "  fd.append('api_key', '" + self.video_sign_api_key + "');"
            "  fd.append('timestamp', '" + self.video_sign_timestamp + "');"
            "  fd.append('signature', '" + self.video_sign_signature + "');"
            "  fd.append('folder', 'portfolio');"
            "  const xhr = new XMLHttpRequest();"
            "  xhr.open('POST', 'https://api.cloudinary.com/v1_1/" + self.video_sign_cloud_name + "/video/upload', false);"
            "  try { xhr.send(fd); } catch(e) { return JSON.stringify({error: 'Network error: ' + e.message}); }"
            "  if (xhr.status === 200) {"
            "    const d = JSON.parse(xhr.responseText);"
            "    return JSON.stringify({url: d.secure_url});"
            "  } else {"
            "    return JSON.stringify({error: 'Upload failed: HTTP ' + xhr.status});"
            "  }"
            "})()"
        )
        
        return rx.call_script(js_code, callback=State._video_upload_callback)
    
    def _video_upload_callback(self, result: str = ""):
        """Callback: recibe URL del video subido desde el navegador"""
        import json
        self.subiendo_archivo = False
        if not result:
            return rx.toast.error("Error: no se recibió respuesta del upload")
        try:
            data = json.loads(result)
            if "url" in data:
                self.uploaded_video_url = data["url"]
                return rx.toast.success("Video subido correctamente")
            else:
                return rx.toast.error(f"Error: {data.get('error', 'Error desconocido')}")
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")
    
    async def upload_imagen(self, files: list[rx.UploadFile]):
        if not files:
            return
        self.subiendo_archivo = True
        yield
        try:
            file = files[0]
            data = await file.read()
            self.uploaded_imagen_url = await self._upload_to_cloudinary(data, file.filename, file.content_type or "image/jpeg")
            yield rx.toast.success("Imagen subida correctamente")
        except Exception as e:
            yield rx.toast.error(f"Error al subir: {str(e)}")
        finally:
            self.subiendo_archivo = False
    
    async def upload_documento(self, files: list[rx.UploadFile]):
        if not files:
            return
        self.subiendo_archivo = True
        yield
        try:
            file = files[0]
            data = await file.read()
            self.uploaded_documento_url = await self._upload_to_cloudinary(data, file.filename, file.content_type or "application/pdf")
            yield rx.toast.success("Documento subido correctamente")
        except Exception as e:
            yield rx.toast.error(f"Error al subir: {str(e)}")
        finally:
            self.subiendo_archivo = False
    
    def reset_upload_urls(self):
        """Resetear URLs de upload al abrir un formulario nuevo"""
        self.uploaded_diploma_url = ""
        self.uploaded_certificado_url = ""
        self.uploaded_video_url = ""
        self.uploaded_imagen_url = ""
        self.uploaded_documento_url = ""
    
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
                for c in data:
                    self._limpiar_nulos(c, [
                        "fecha_fin", "descripcion_es", "descripcion_en",
                        "descripcion_it", "descripcion_ca",
                        "certificado_url", "diploma_pdf",
                    ])
                self.cursos_admin = [Curso(**c) for c in data]
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
        self.reset_upload_urls()
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
            fecha_inicio = form_data.get("fecha_inicio", "").strip() or None
            fecha_fin = form_data.get("fecha_fin", "").strip() or None
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
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "descripcion_es": form_data.get("descripcion_es", "") or None,
                "descripcion_en": form_data.get("descripcion_en", "") or None,
                "descripcion_it": form_data.get("descripcion_it", "") or None,
                "descripcion_ca": form_data.get("descripcion_ca", "") or None,
                "certificado_url": self.uploaded_certificado_url or form_data.get("certificado_url", "").strip() or form_data.get("certificado_url_manual", "").strip() or None,
                "diploma_pdf": self.uploaded_diploma_url or form_data.get("diploma_pdf", "").strip() or form_data.get("diploma_pdf_manual", "").strip() or None,
                "orden": int(form_data.get("orden", 0) or 0),
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
                detail = response.json().get("detail", response.text[:200]) if response.text else str(response.status_code)
                return rx.toast.error(f"Error {response.status_code}: {detail}")
                
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
                for e in data:
                    self._limpiar_nulos(e, [
                        "fecha_inicio", "fecha_fin",
                        "descripcion_es", "descripcion_en",
                        "descripcion_it", "descripcion_ca",
                        "imagen_url", "video_url", "documento_url",
                    ])
                self.experiencias_admin = [Experiencia(**e) for e in data]
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
        self.reset_upload_urls()
        self._prefetch_video_sign()
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
            tecnologias_raw = form_data.get("tecnologias", "").strip()
            tecnologias = [t.strip() for t in tecnologias_raw.split(",") if t.strip()] if tecnologias_raw else []
            fecha_fin = form_data.get("fecha_fin", "").strip() or None
            experiencia_data = {
                "tipo": form_data["tipo"],
                "empresa": form_data["empresa"],
                "cargo_es": form_data["cargo_es"],
                "cargo_en": form_data["cargo_en"],
                "cargo_it": form_data["cargo_it"],
                "cargo_ca": form_data["cargo_ca"],
                "fecha_inicio": form_data.get("fecha_inicio", "").strip(),
                "fecha_fin": fecha_fin,
                "actual": form_data.get("actual") == "on",
                "descripcion_es": form_data.get("descripcion_es", "") or None,
                "descripcion_en": form_data.get("descripcion_en", "") or None,
                "descripcion_it": form_data.get("descripcion_it", "") or None,
                "descripcion_ca": form_data.get("descripcion_ca", "") or None,
                "tecnologias": tecnologias,
                "imagen_url": self.uploaded_imagen_url or form_data.get("imagen_url", "").strip() or form_data.get("imagen_url_manual", "").strip() or None,
                "video_url": self.uploaded_video_url or form_data.get("video_url", "").strip() or form_data.get("video_url_manual", "").strip() or None,
                "documento_url": self.uploaded_documento_url or form_data.get("documento_url", "").strip() or form_data.get("documento_url_manual", "").strip() or None,
                "orden": int(form_data.get("orden", 0) or 0),
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
                detail = response.json().get("detail", response.text[:200]) if response.text else str(response.status_code)
                return rx.toast.error(f"Error {response.status_code}: {detail}")
                
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")
    
    # ==================== ANALYTICS STATE ====================
    analytics_resumen: dict = {}
    analytics_paginas: list[dict[str, str]] = []
    analytics_dispositivos: list[dict[str, str]] = []
    analytics_navegadores: list[dict[str, str]] = []
    analytics_plataformas: list[dict[str, str]] = []
    analytics_referrers: list[dict[str, str]] = []
    analytics_por_dia: list[dict[str, str]] = []
    analytics_recientes: list[dict[str, str]] = []
    cargando_analytics: bool = False
    error_analytics: str = ""
    
    def descargar_excel_analytics(self):
        """Descargar Excel via backend con auth"""
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            r = httpx.get(
                f"{API_URL}/api/analytics/export?dias=30",
                headers=headers, timeout=30.0
            )
            if r.status_code == 200:
                return rx.download(
                    data=r.content,
                    filename="analytics.xlsx",
                )
            else:
                return rx.toast.error("Error al descargar Excel")
        except Exception as e:
            return rx.toast.error(f"Error: {str(e)}")
    
    def cargar_analytics(self):
        self.cargando_analytics = True
        self.error_analytics = ""
        
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            
            r_resumen = httpx.get(
                f"{API_URL}/api/analytics/resumen",
                headers=headers, timeout=15.0
            )
            if r_resumen.status_code == 200:
                self.analytics_resumen = r_resumen.json()
            
            r_paginas = httpx.get(
                f"{API_URL}/api/analytics/paginas",
                headers=headers, timeout=15.0
            )
            if r_paginas.status_code == 200:
                self.analytics_paginas = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_paginas.json()
                ]
            
            r_dispositivos = httpx.get(
                f"{API_URL}/api/analytics/dispositivos",
                headers=headers, timeout=15.0
            )
            if r_dispositivos.status_code == 200:
                self.analytics_dispositivos = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_dispositivos.json()
                ]
            
            r_navegadores = httpx.get(
                f"{API_URL}/api/analytics/navegadores",
                headers=headers, timeout=15.0
            )
            if r_navegadores.status_code == 200:
                self.analytics_navegadores = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_navegadores.json()
                ]
            
            r_plataformas = httpx.get(
                f"{API_URL}/api/analytics/plataformas",
                headers=headers, timeout=15.0
            )
            if r_plataformas.status_code == 200:
                self.analytics_plataformas = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_plataformas.json()
                ]
            
            r_referrers = httpx.get(
                f"{API_URL}/api/analytics/referrers",
                headers=headers, timeout=15.0
            )
            if r_referrers.status_code == 200:
                self.analytics_referrers = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_referrers.json()
                ]
            
            r_por_dia = httpx.get(
                f"{API_URL}/api/analytics/visitas-por-dia",
                headers=headers, timeout=15.0
            )
            if r_por_dia.status_code == 200:
                self.analytics_por_dia = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_por_dia.json()
                ]
            
            r_recientes = httpx.get(
                f"{API_URL}/api/analytics/recientes",
                headers=headers, timeout=15.0
            )
            if r_recientes.status_code == 200:
                self.analytics_recientes = [
                    {k: str(v) for k, v in item.items()}
                    for item in r_recientes.json()
                ]
                
        except Exception as e:
            self.error_analytics = f"Error al cargar analíticas: {str(e)}"
        finally:
            self.cargando_analytics = False
