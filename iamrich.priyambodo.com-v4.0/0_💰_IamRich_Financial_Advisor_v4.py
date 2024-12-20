import streamlit as st
from streamlit.logger import get_logger
#import authrich

#authrich.authenticate()
LOGGER = get_logger(__name__)

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
html_code = """
    "IamRich" is a cutting-edge personal financial advisor application designed to empower users in managing their finances with intelligence and ease. This innovative app combines smart technology with personalized guidance to provide a comprehensive financial experience.
    """

def run():
    st.set_page_config(page_icon="image/usd.ico")
    st.markdown(vNoLabel, unsafe_allow_html=True)
    st.write("# 💰 IamRich - Your Smart Personal Financial Advisor application (v3.0)")
    st.caption("[https://iamrich.priyambodo.com] | [https://iamtelco.priyambodo.com] | [https://iamgemini.priyambodo.com]")
    st.write(html_code)
   
    st.markdown(
        """
        **👈 Select the menu from the sidebar** to start your experience. 
        """
    )
    st.image("image/logo.png", width=700)
    st.write("*(The logo image above is created by Google AI using Imagen 2 model.)*")
    #st.write("prompt imagen2: I am Rich is a Financial AI super hero advisor application designed to empower users to earn more money. Create big text written \"I am Rich\". Create in a volumetric lighting, high resolution, hdr, sharpen picture.")

    st.write("""
    <div style="text-align:center;padding:1em 0;"> 
        <table style="width: 100%;">
        <tr>
            <th style="color: gray; text-align: left;">Current local time in</th>
            <th style="text-align: left;">Jakarta, Indonesia</th>
        </tr>
        <tr>
            <td colspan="2">
            <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=en&size=medium&timezone=Asia%2FJakarta" width="100%" height="115" frameborder="0" seamless></iframe>
            </td>
        </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        This application is maintained by <b>Doddi Priyambodo</b> (priyambodo@google.com | doddi@bicarait.com)   
        App Name & latest Version: <b>IamRich-v3.0</b>
        """, unsafe_allow_html=True
    )
    
if __name__ == "__main__":
    run()
