(function() {
    if (window._tracked) return;
    window._tracked = true;
    try {
        var api = window.location.hostname === 'localhost'
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
})();
