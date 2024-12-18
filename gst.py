import streamlit as st
import pandas as pd

def load_data(sheet_url):
    try:
        data = pd.read_csv(sheet_url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# access the data related to home entities for oGX
def calculate_ogx(df, select_MC):
    filtered = df[df['Home MC'] == select_MC]

    ans = filtered.groupby(['Home LC', 'Product'], as_index=False).agg({
        'SU-APL': 'mean', 
        'APL-APD': 'mean'  
    }).reset_index(drop=True)
    return ans

# access the data related to host entities for iCX
def calculate_icx(df, select_MC):
    filtered = df[df['Host MC'] == select_MC]

    # focuses more on the APL-APD
    ans = filtered.groupby(['Host LC', 'Product'], as_index=False).agg({
        'APL-APD': 'mean'  
    }).reset_index(drop=True)
    return ans

def main():
    data = load_data("https://docs.google.com/spreadsheets/d/e/2PACX-1vR-cEIAKQ26fGRkvr8hnBqkmuWfzverObjQdgcC3mdbdmIx7P0QOauwzXcC0Uz_aWDfDnaKAhhp3BST/pub?output=csv")
    st.markdown(
                    "<div style='text-align: center;'>"
                    f"<h3>🌍 GST - Head of GID</h3>"
                    "</div>",
                    unsafe_allow_html=True,
                )
    
    st.markdown(
                    "<div style='text-align: center;'>"
                    f"<h4>Applicant Task</h4>"
                    "</div>",
                    unsafe_allow_html=True,
                )

    st.markdown(
                    "<div style='text-align: center;'>"
                    f"<h3>📊Process Time Dashboard</h3>"
                    "</div>",
                    unsafe_allow_html=True,
                )

    st.divider()

    st.subheader("For oGX Process Times")

    select_MC_for_ogx = st.selectbox('Select MC', data['Home MC'].unique())
    ogx_ans = calculate_ogx(data, select_MC_for_ogx)
    
    st.write(ogx_ans)

    st.divider()

    st.subheader("For iCX Process Times")

    select_MC_for_icx = st.selectbox('Select MC', data['Host MC'].unique())
    icx_ans = calculate_icx(data, select_MC_for_icx)
    st.write(icx_ans)

    st.divider()
    st.markdown(
                    "<div style='text-align: left;'>"
                    f"<h6>Prepared by Dinuka Avinash</h6>"
                    "</div>",
                    unsafe_allow_html=True,
                )

if __name__ == "__main__":
    main()
