from fasthtml.common import Div, H1, Script, A
def notice(msg, url1=None, actionName1=None, url2=None, actionName2=None):
    return Div(
        Div(
            H1(f"{msg}", 
               cls="text-5xl font-bold text-white mb-4 animate-fade-in lg:mr-20 md:mr-10 sm:mr-4"),
             Div(
                A(f"{actionName1 if actionName1 is not None else ''}", hx_get=f"{url1}", hx_target='#hero', hx_swap='outerHTML',  
                cls="bg-white text-indigo-600 px-6 py-3 rounded-full font-semibold hover:bg-gray-200 transition duration-300"),
                A(f"{ actionName2 if actionName2 is not None else '' }", hx_get=f"{url2}", 
                 hx_target='#hero', hx_swap='outerHTML',   cls="ml-4 bg-indigo-500 text-white px-6 py-3 rounded-full font-semibold hover:bg-indigo-700 transition duration-300"),
                cls="flex justify-center space-x-4"
            ),
            cls="text-center"
        ),
        Script(src='static/js/toggle/agendasRecents.js'),
        Script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"),
        Script(src='static/js/toggle/toggleSidebar.js' ),

        cls="bg-gradient-to-r from-gray-900 to-indigo-800 h-screen flex items-center justify-center w-full", id='hero',  
    )