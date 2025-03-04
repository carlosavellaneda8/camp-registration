from typing import Optional
import streamlit as st
from pyairtable import Api
from pydantic import BaseModel

api = Api(st.secrets["airtable"]["api_key"])


class Parent(BaseModel):
    parent_id_number: int
    parent_name: str
    parent_last_name: str
    parent_phone: int


class Person(BaseModel):
    id_number: int
    name: str
    last_name: str
    phone: int
    email: str
    date_birth: str
    ministry: str
    parent: Optional[Parent]


class Payment(BaseModel):
    id_number: int
    payment_date: str
    payment_value: int


def check_id_exists(
    id_number: int,
) -> bool:
    """
    """
    base_id = st.secrets["airtable"]["base_id"]
    table_id = st.secrets["airtable"]["id_table"]
    table = api.table(base_id, table_id)
    all_records = table.all(fields=["Número de documento"])
    if all([not record["fields"] for record in all_records]):
        return False
    id_list = [record["fields"]["Número de documento"] for record in all_records]
    id_set = set(id_list)
    return id_number in id_set


def create_person_record(person_info: Person) -> dict:
    table = api.table(
        st.secrets["airtable"]["base_id"],
        st.secrets["airtable"]["id_table"],
    )
    breakpoint()table_id
    try:
        table.create(person_info.dict())
        return {"status": "ok"}
    except Exception as e:
        return {"status": f"error: {e}"}


def create_payment_record(payment_info: Payment) -> dict:
    pass
