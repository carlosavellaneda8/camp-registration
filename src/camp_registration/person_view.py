from datetime import datetime
import streamlit as st
import webbrowser
from camp_registration.airtable import Person, Parent, create_person_record

PAYMENT_FORM = "https://airtable.com/embed/appX6rFINfrR0vPSI/shrng3slIs06vrox2"
MIN_DATE = datetime.strptime("1920/01/01", "%Y/%m/%d")


def open_payment_form() -> None:
    """Function to open the payment form"""
    webbrowser.open(PAYMENT_FORM)


def person_view(id_number: int) -> dict:
    """Function that displays the person info form"""
    with st.form("person-form"):
        st.markdown("Diligencia el siguiente formulario. **Todos los campos son obligatorios**")
        id_number = st.number_input("Número de documento", value=id_number)
        name = st.text_input("Nombre")
        last_name = st.text_input("Apellido")
        phone = st.number_input("Teléfono", value=None, min_value=0)
        email = st.text_input("Email")
        date_birth = st.date_input("Fecha de nacimiento", min_value=MIN_DATE)
        ministry = st.selectbox(
            "Ministerio",
            ("Transición", "Bachilleres", "Pareja de apoyo"),
            index=None,
            key="ministry",
        )

        parent_id_number = None
        parent_name = None
        parent_last_name = None
        parent_phone = None

        if st.session_state.ministry in ["Transición", "Bachilleres"]:
            st.markdown("### Información del acudiente")
            parent_id_number = st.number_input("Número de documento de acudiente")
            parent_name = st.text_input("Nombre de acudiente")
            parent_last_name = st.text_input("Apellido de acudiente")
            parent_phone = st.number_input("Teléfono de acudiente")

        submitted = st.form_submit_button("Submit")
        if submitted:
            parent = None

            if ministry in ["Transición", "Bachilleres"] and parent_id_number and parent_name and parent_last_name and parent_phone:
                parent = Parent(
                    parent_id_number=parent_id_number,
                    parent_name=parent_name,
                    parent_last_name=parent_last_name,
                    parent_phone=parent_phone,
                )

            try:
                person = Person(
                    id_number=id_number,
                    name=name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    date_birth=date_birth.strftime("%Y-%m-%d"),
                    ministry=ministry,
                    parent=parent,
                )
                status = create_person_record(person_info=person)
                print(status)
                return person
            except Exception as e:
                st.error(f"Error: {str(e)}")
                return None
    return None
