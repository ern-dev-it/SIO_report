import streamlit as st
import pandas as pd
from data_processing import process_data
import datetime

# title element
st.title('SIO report processor')

# instruction element
st.subheader('Input CSV')

# streamlit function - creates a widget that reads a file
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

# for the output button - although st.dataframe below also allows csv download... just to make it easier
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

timestamp = datetime.datetime.now().strftime("%Y%m%d")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        processed = process_data(df)
        csv = convert_df_to_csv(processed)
        # download
        file_name = f"processed_data_{timestamp}.csv"
        st.download_button(
                label="Download Processed Data as CSV",
                data=csv,
                file_name=file_name,
                mime='text/csv'
            )
        st.dataframe(processed)
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.write("Please upload a file before processing.")
