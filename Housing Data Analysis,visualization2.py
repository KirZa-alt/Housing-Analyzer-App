import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("🏡 Data Analyzer Through histogram Plot")

uploaded_file = st.file_uploader("Upload your Housing CSV file", type=["csv"])
column = st.text_input("Enter your column name for visualization")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of Data")
    st.write(data.head())

    st.title("Housing Data:")
    st.write(data)

    # Only make histogram if the column exists
    if column and column in data.columns:
        fig, ax = plt.subplots()
        data[column].plot(kind="hist", bins=20, edgecolor="black", ax=ax)
        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        st.pyplot(fig)
    elif column:
        st.error(f"Column '{column}' not found in the dataset.")

else:
    st.warning("Please upload a CSV file to proceed.")
