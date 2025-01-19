import streamlit as st

st.header("Using slider with range of values", divider="rainbow")
range_nums = st.slider("Select a range of number", 0.1, 1.6, value=(0.2, 1.0),step=0.2)
st.write(range_nums)

st.header("Using select slider with list of values", divider="rainbow")
start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)
