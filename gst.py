import streamlit as st
import pandas as pd

def load_data(sheet_url):
    try:
        data = pd.read_csv(sheet_url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None


# to select the MC available in the data file
# select_MC = st.selectbox('Select MC', data['Home MC'].unique())
# selec_Product = st.selectbox("Select Product", data['Product'].unique())

def calculate_ogx(df, select_MC):
    filtered = df[df['Home MC'] == select_MC]
    # ans = filtered.groupby('Home LC')['SU-APL'].sum().reset_index()
    # ans_by_product = ans.groupby('Product')
    ans = filtered.groupby(['Home LC', 'Product'], as_index=False).agg({
        'SU-APL': 'mean',  # Example aggregation for SU-APL
        'APL-APD': 'mean'  # Replace with the actual column name and aggregation method
    }).reset_index()
    return ans

def calculate_icx(df, select_MC):
    filtered = df[df['Host MC'] == select_MC]
    # ans = filtered.groupby('Home LC')['SU-APL'].sum().reset_index()
    # ans_by_product = ans.groupby('Product')
    ans = filtered.groupby(['Host LC', 'Product'], as_index=False).agg({
        'SU-APL': 'mean',  # Example aggregation for SU-APL
        'APL-APD': 'mean'  # Replace with the actual column name and aggregation method
    }).reset_index()
    return ans

def main():
    data = load_data("https://docs.google.com/spreadsheets/d/e/2PACX-1vR-cEIAKQ26fGRkvr8hnBqkmuWfzverObjQdgcC3mdbdmIx7P0QOauwzXcC0Uz_aWDfDnaKAhhp3BST/pub?output=csv")
    
    st.title("GST Task - Process Time Dashboard")
    st.divider()

    st.subheader("For oGX Process Times")

    select_MC_for_ogx = st.selectbox('Select MC', data['Home MC'].unique())
    ogx_ans = calculate_ogx(data, select_MC_for_ogx)
    st.write(ogx_ans)

    st.divider()

    st.subheader("For oGX Process Times")

    select_MC_for_icx = st.selectbox('Select MC', data['Host MC'].unique())
    icx_ans = calculate_icx(data, select_MC_for_icx)
    st.write(icx_ans)

if __name__ == "__main__":
    main()
