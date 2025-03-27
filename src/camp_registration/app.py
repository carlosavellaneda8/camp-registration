import streamlit as st
import streamlit.components.v1 as components
from camp_registration.airtable import check_id_exists
from camp_registration.utils import (
    format_embed_url,
    PAYMENT_FORM,
    PERSON_FORM,
    REGISTERED_TEXT,
    UNREGISTERED_TEXT,
)


st.title("Life Of Legends - Retiro TB 2025")

# Initialize session state variables if they do not exist
if 'id_number' not in st.session_state:
    st.session_state.id_number = 0

# ID Check Form
with st.form("id_form"):
    id_number = st.number_input(
        "Número de documento:",
        min_value=0,
        value=st.session_state.id_number,
        key='id_number_form',
    )
    check_button = st.form_submit_button("Consultar")

if check_button:
    st.session_state.id_number = id_number
    id_exists = check_id_exists(id_number=id_number)

    if id_exists:
        st.write(REGISTERED_TEXT)
        st.link_button("Registra tu abono", PAYMENT_FORM)
    else:
        st.session_state.form_shown = True

# Registration Form
if st.session_state.get('form_shown', False):
    st.markdown(UNREGISTERED_TEXT)
    # Embed the Airtable form using HTML
    components.html(format_embed_url(url=PERSON_FORM), height=533)
