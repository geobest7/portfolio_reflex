'''
Es el archivo de configuración principal de Reflex. 
Define el nombre de la app, el puerto donde correrá, etc.
'''

import reflex as rx

config = rx.Config(
    app_name="mi_portfolio_reflex",
    favicon="favicon.ico",
    port=3000,
)


