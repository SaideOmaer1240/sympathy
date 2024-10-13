from fasthtml.common import Html,Body, Div
from components.hero.template import Navbar
from components.head.template import head
from app.templates.forms import template_login

def conectar():
    return Html( 
        head(),
     Body(
        Div(
        Navbar(),
        template_login()
         ,
        cls='w-full bg-gradient-to-r from-gray-900 to-indigo-800 h-screen'
    ), id='body', cls='max-h-screen'

        )
        , 
)

