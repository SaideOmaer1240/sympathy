from fasthtml.common import Head, Meta, Link, Title, Script
def head():
    return Head(
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Meta(charset="UTF-8"),
            Title("Sympathy"),
            Link(href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css", rel="stylesheet"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),

            Link(href="static/css/styles.css", rel="stylesheet"),
             
            Script("""
                function toggleMenu() {
                    var sidebar = document.getElementById("sidebar");
                    sidebar.classList.toggle("hidden");
                }
            """, type="text/javascript"),
 
            Script(src='https://unpkg.com/htmx.org@2.0.2', integrity="sha384-Y7hw+L/jvKeWIRRkqWYfPcvVxHzVzn5REgzbawhxAuQGwX1XWe70vji+VSeHOThJ" ,crossorigin="anonymous"),
        )