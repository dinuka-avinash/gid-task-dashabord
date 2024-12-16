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

def calculate_(df, select_MC):
    filtered = df[df['Home MC'] == select_MC]
    ans = filtered.groupby('Home MC')['SU-APL'].sum().reset_index()
    # ans_by_product = ans.groupby('Product')

    return ans

def main():
    data = load_data("https://docs.google.com/spreadsheets/d/e/2PACX-1vR-cEIAKQ26fGRkvr8hnBqkmuWfzverObjQdgcC3mdbdmIx7P0QOauwzXcC0Uz_aWDfDnaKAhhp3BST/pub?output=csv")
    
    st.title("GST")
    # st.write(data)
    select_MC = st.selectbox('Select MC', data['Home MC'].unique())
    ans = calculate_(data, select_MC)
    st.write(ans)

    # col1, col2, col3 = st.columns([1, 1, 1])

    #         # Display the total applications in the first column
    # with col1:
    #     st.markdown(
    #         "<div style='text-align: center;'>"
    #         f"<h3>🌍 {data_mode} Applications</h3>"
    #         f"<p style='font-size: 32px;'>{total_applied}</p>"
    #         "</div>",
    #         unsafe_allow_html=True,
    #     )

if __name__ == "__main__":
    main()
