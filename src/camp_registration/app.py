from datetime import datetime
import webbrowser
import streamlit as st
import streamlit.components.v1 as components
from camp_registration.airtable import check_id_exists

PAYMENT_FORM = "https://airtable.com/appX6rFINfrR0vPSI/shrng3slIs06vrox2"
REGISTERED_TEXT = """
### ¡Ya estás registrado!

En un momento te direccionaremos para que cargues el comprobante de tu abono
"""
MIN_DATE = datetime.strptime("1920-01-01", "%Y-%m-%d")

st.title("Life Of Legends - Retiro TB 2025")

# Initialize session state variables if they do not exist
if 'id_number' not in st.session_state:
    st.session_state.id_number = 0

# ID Check Form
with st.form("id_form"):
    id_number = st.number_input("Número de documento:", min_value=0, value=st.session_state.id_number, key='id_number_form')
    check_button = st.form_submit_button("Check ID")

if check_button:
    st.session_state.id_number = id_number
    id_exists = check_id_exists(id_number=id_number)

    if id_exists:
        st.write(REGISTERED_TEXT)
        webbrowser.open(url=PAYMENT_FORM)
    else:
        st.session_state.form_shown = True

# Registration Form
if st.session_state.get('form_shown', False):
    st.markdown("""
### Completa el siguiente formulario

Una vez termines de completarlo, recarga esta página para poder subir el comprobante de abono del retiro""")
    # Embed the Airtable form using HTML
    airtable_url = "https://airtable.com/embed/appX6rFINfrR0vPSI/shroMlTuqwoXYiZ93"
    iframe_html = f"""
<iframe class="airtable-embed" src="{airtable_url}" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>
"""

    components.html(iframe_html, height=533)
