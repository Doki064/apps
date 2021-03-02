import streamlit as st
from multiapp import MultiApp
from apps import home_page, first_map, second_map, third_map, fourth_map  # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("HOME", home_page.app)
app.add_app("FIRST MAP", first_map.app)
app.add_app("SECOND MAP", second_map.app)
app.add_app("THIRD MAP", fourth_map.app)
app.add_app(" FOURTH MAP", third_map.app)


# The main app
app.run()