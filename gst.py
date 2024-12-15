import streamlit as st

data = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR-cEIAKQ26fGRkvr8hnBqkmuWfzverObjQdgcC3mdbdmIx7P0QOauwzXcC0Uz_aWDfDnaKAhhp3BST/pub?output=csv"

# to select the MC available in the data file
select_MC = st.selectbox("Select MC", data["Home MC"].unique())
# selec_Product = st.selectbox("Select Product", data['Product'].unique())

def calculate_(df, select_MC):
    filtered = df[df['Home MC'] == select_MC]
    ans = filtered.groupby('Home LC')['SU-APL'].avg().reset_index()
    ans_by_product = ans.groupby('Product')

    return ans_by_product