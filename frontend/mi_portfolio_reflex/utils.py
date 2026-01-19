def convertir_youtube_url(url: str) -> str:
    """Convierte URL de YouTube a formato embed"""
    if not url:
        return ""
    # Convertir watch?v= a embed/
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    # Si ya es embed, devolverla tal cual
    if "embed/" in url:
        return url
    # Si es youtu.be/ID
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    return url
