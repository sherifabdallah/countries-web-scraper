import pandas as pd
import streamlit as st
from streamlit_player import st_player

st.set_page_config(
    page_title="Slum Dwellers International",
    page_icon='https://sdinet.org/wp-content/themes/sdinet/images/sdi_fav-57x57.png',
)
st.header('The Know Your City Campaign')





hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

style_fullscreen_button_css = """
    button[title="View fullscreen"] {
        display: none;
    }

    button[title="View fullscreen"]:hover {
        display: none;
        }
    """

st.markdown(
    "<style>"
    + style_fullscreen_button_css
    + "</styles>",
    unsafe_allow_html=True,
)

with st.form(key ='Form1'):
    with st.sidebar:
        country = st.sidebar.selectbox('Select Country', 
                        
                        ['38_benin', 'Ghana', 'Kenya', 'Liberia', 'main', 'Malawi', 'Namibia', 'Nigeria', 'Philippines', 'Sierra leone', 'South africa', 'South africa 2', 'Swaziland', 'Tanzania', 'Uganda', 'Zambia', 'Zimbabwe'], 0)


df = pd.read_csv(country + ".csv")  # read a CSV file inside the 'data" folder next to 'app.py'



st.dataframe(df)  # visualize my dataframe in the Streamlit app







file_path =  country + '.csv'
with open(file_path, 'rb') as my_file:
    st.download_button(label = 'Download CSV File', data = my_file, file_name = country + '.csv')      

st.caption('Made With Sherif Abdullah ❤')

submit_video = st.sidebar.button('Show Video', key=None, help=None, on_click=None, args=None, kwargs=None)

if submit_video:
    st_player("https://player.vimeo.com/video/125271509?h=748258302e&dnt=1&app_id=122963")



