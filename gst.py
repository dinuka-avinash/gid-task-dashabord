import streamlit as st
import pandas as pd

def load_data(sheet_url):
    try:
        data = pd.read_csv(sheet_url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

data = load_data("https://docs.google.com/spreadsheets/d/e/2PACX-1vR-cEIAKQ26fGRkvr8hnBqkmuWfzverObjQdgcC3mdbdmIx7P0QOauwzXcC0Uz_aWDfDnaKAhhp3BST/pub?output=csv")

# to select the MC available in the data file
# select_MC = st.selectbox('Select MC', data['Home MC'].unique())
# selec_Product = st.selectbox("Select Product", data['Product'].unique())

def calculate_(df, select_MC):
    # filtered = df[df['Home MC'] == select_MC]
    ans = df.groupby('Home MC')['SU-APL'].avg().reset_index()
    ans_by_product = ans.groupby('Product')

    return ans_by_product