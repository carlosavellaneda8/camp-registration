from datetime import datetime
import webbrowser
import streamlit as st
import streamlit.components.v1 as components
from camp_registration.airtable import check_id_exists, Person, Parent, create_person_record

PERSON_FORM = "https://airtable.com/appX6rFINfrR0vPSI/shroMlTuqwoXYiZ93"
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
if 'name' not in st.session_state:
    st.session_state.name = ''
if 'last_name' not in st.session_state:
    st.session_state.last_name = ''
if 'phone' not in st.session_state:
    st.session_state.phone = 0
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'date_birth' not in st.session_state:
    st.session_state.date_birth = datetime.now()
ministries = ["Transición", "Bachilleres", "Pareja de apoyo"]
if 'ministry' not in st.session_state:
    st.session_state.ministry = ministries[0]
if 'parent_id_number' not in st.session_state:
    st.session_state.parent_id_number = 0
if 'parent_name' not in st.session_state:
    st.session_state.parent_name = ''
if 'parent_last_name' not in st.session_state:
    st.session_state.parent_last_name = ''
if 'parent_phone' not in st.session_state:
    st.session_state.parent_phone = 0

# ID Check Form
with st.form("id_form"):
    id_number = st.number_input("Número de documento:", min_value=0, value=st.session_state.id_number, key='id_number_form')
    check_button = st.form_submit_button("Check ID")

if check_button:
    st.session_state.id_number = id_number
    id_exists = check_id_exists(id_number=id_number)

    if id_exists:
        st.write(REGISTERED_TEXT)
        webbrowser.open(url=PAYMENT_FORM, new=0)
    else:
        st.session_state.form_shown = True

# Registration Form
if st.session_state.get('form_shown', False):
    st.markdown("""
### Completa el siguiente formulario

Una vez termines de completar el formulario, recarga esta página para poder subir el comprobante de abono del retiro""")
    # Embed the Airtable form using HTML
    airtable_url = "https://airtable.com/embed/appX6rFINfrR0vPSI/shroMlTuqwoXYiZ93"
    iframe_html = f"""
<iframe class="airtable-embed" src="{airtable_url}" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>
"""

    components.html(iframe_html, height=533)
#     with st.form("registration_form"):
#         st.text_input("Nombre", value=st.session_state.name, key='name')
#         st.text_input("Apellido", value=st.session_state.last_name, key='last_name')
#         st.number_input("Teléfono", min_value=0, value=st.session_state.phone, key='phone')
#         st.text_input("Email", value=st.session_state.email, key='email')
#         st.date_input(
#             "Fecha de nacimiento",
#             min_value=MIN_DATE,
#             value=st.session_state.date_birth,
#             key='date_birth'
#         )
# 
#         st.selectbox(
#             "Ministerio",
#             ministries,
#             index=ministries.index(st.session_state.ministry),
#             key="ministry"
#         )
# 
#         if st.session_state.ministry in ["Transición", "Bachilleres"]:
#             st.markdown("### Información del acudiente:")
#             st.number_input("Número de documento", min_value=0, value=st.session_state.parent_id_number, key='parent_id_number')
#             st.text_input("Nombre", value=st.session_state.parent_name, key='parent_name')
#             st.text_input("Apellido", value=st.session_state.parent_last_name, key='parent_last_name')
#             st.number_input("Télefono", min_value=0, value=st.session_state.parent_phone, key='parent_phone')
# 
#         submit_button = st.form_submit_button("Enviar")
# 
#     if submit_button:
#         parent = None
#         if st.session_state.ministry in ["Transición", "Bachilleres"]:
#             parent = Parent(
#                 parent_id_number=st.session_state.parent_id_number,
#                 parent_name=st.session_state.parent_name,
#                 parent_last_name=st.session_state.parent_last_name,
#                 parent_phone=st.session_state.parent_phone,
#             )
# 
#         person = Person(
#             id_number=st.session_state.id_number,
#             name=st.session_state.name,
#             last_name=st.session_state.last_name,
#             phone=st.session_state.phone,
#             email=st.session_state.email,
#             date_birth=st.session_state.date_birth.strftime("%Y-%m-%d"),
#             ministry=st.session_state.ministry,
#             parent=parent,
#         )
#         create_person_record(person_info=person)
#         st.success("Registration successful!")
