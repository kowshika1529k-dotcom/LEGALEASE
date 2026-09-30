import streamlit as st
from datetime import date
from docx import Document

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.info(
    "LegalEase creates general legal document drafts for educational "
    "and informational purposes. Please consult a qualified legal "
    "professional before using any document for a real legal matter."
)

document_type = st.selectbox(
    "Select Document Type",
    [
        "Rental Agreement",
        "Leave and License Agreement",
        "General Legal Notice"
    ]
)

st.header("Enter Details")

party1 = st.text_input("First Party / Sender Name")
party2 = st.text_input("Second Party / Receiver Name")
address = st.text_area("Address / Property Details")
purpose = st.text_area("Purpose / Main Terms")
start_date = st.date_input("Start / Effective Date", date.today())
duration = st.text_input("Duration")
amount = st.text_input("Amount (Optional)")
additional_terms = st.text_area("Additional Terms (Optional)")


if st.button("Generate Legal Document"):

    document_text = f"""
LEGAL DOCUMENT DRAFT

Document Type: {document_type}

Date: {date.today().strftime("%d-%m-%Y")}

First Party / Sender:
{party1}

Second Party / Receiver:
{party2}

Address / Property Details:
{address}

Purpose / Main Terms:
{purpose}

Effective Date:
{start_date.strftime("%d-%m-%Y")}

Duration:
{duration}

Amount:
{amount}

Additional Terms:
{additional_terms}


DISCLAIMER:
This document is an automatically generated draft for
educational and general informational purposes only.
It is not legal advice. Please have the document reviewed
by a qualified legal professional before using it.
"""

    st.success("Legal document draft generated!")

    st.text_area(
        "Generated Document",
        document_text,
        height=500
    )

    doc = Document()

    for line in document_text.splitlines():
        doc.add_paragraph(line)

    file_name = "LegalEase_Document.docx"
    doc.save(file_name)

    with open(file_name, "rb") as file:
        st.download_button(
            label="Download Word Document",
            data=file,
            file_name=file_name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
