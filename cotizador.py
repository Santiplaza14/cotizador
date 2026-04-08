import streamlit as st

st.title("Calculadora de Descuento (%)")

precio_lista = st.number_input("Ingrese el precio de lista (Salesforce)", min_value=0.0, format="%.2f")
precio_real = st.number_input("Ingrese el precio de Legacy", min_value=0.0, format="%.2f")

if precio_lista > 0:
    porcentaje_desc = ((precio_lista - precio_real) / precio_lista) * 100
    st.success(f"El descuento es: {porcentaje_desc:.2f}%")

