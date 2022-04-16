import streamlit as st

st.title('**Customizing the theme of Streamlit apps**')
st.write('*Contents of the `.streamlit/config.toml` file of this app*')

st.code("""
[theme]
base="light"
primaryColor="#E67E22"
backgroundColor="#F7DC6F"
secondaryBackgroundColor="#82E0AA"
textColor="#6C3483"
font="serif"
""")

number = st.sidebar.slider('Select a number:', 0, 20, 10)
st.write('Selected number from slider widget is:', number)

# primaryColor -- sets the color in the slider widget
# backgroundColor -- sets the background color of the main panel
# secondaryBackgroundColor -- sets color of the sidebar & the background color of the code box in the main panel