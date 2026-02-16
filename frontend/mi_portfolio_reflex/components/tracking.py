"""Componente de tracking que usa useEffect de React para ejecutar JS al montar."""
import reflex as rx


class TrackingComponent(rx.Component):
    """Componente invisible que ejecuta tracking JS via React useEffect."""

    def _get_hooks(self) -> str:
        return """
const trackingRan = useRef(false);
useEffect(() => {
    if (trackingRan.current) return;
    trackingRan.current = true;
    try {
        const api = window.location.hostname === 'localhost'
            ? 'http://localhost:8001'
            : 'https://portfolio-reflex-pwdv.onrender.com';
        fetch(api + '/api/analytics/track', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                pagina: window.location.pathname,
                referrer: document.referrer || '',
                user_agent: navigator.userAgent || '',
                screen_width: window.screen.width,
                screen_height: window.screen.height,
                idioma: navigator.language || '',
                plataforma: navigator.platform || ''
            })
        });
    } catch(e) {}
}, []);
"""

    def _get_imports(self) -> dict:
        return {"react": ["useEffect", "useRef"]}

    def render(self):
        return ""


def tracking_script() -> rx.Component:
    """Helper para incluir el tracking en cualquier página."""
    return TrackingComponent.create()
