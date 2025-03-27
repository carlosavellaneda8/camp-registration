"""Constants and formatting helper function"""

PAYMENT_FORM = "https://app.ilbd.org:8080/Eventos/form"
PERSON_FORM = "https://airtable.com/embed/appX6rFINfrR0vPSI/shroMlTuqwoXYiZ93"
REGISTERED_TEXT = """
### ¡Ya estás registrado!

Haz clic en el botón a continuación para registrar un nuevo abono
"""
UNREGISTERED_TEXT = """
### Completa el siguiente formulario

Una vez termines de completarlo, recarga esta página para poder subir el comprobante de abono del retiro
"""


def format_embed_url(url: str) -> str:
    iframe_html = f"""
<iframe class="airtable-embed" src="{url}" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>
"""
    return iframe_html
