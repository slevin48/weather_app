import streamlit as st
import mymodel as m

st.sidebar.write("""# My Weather App
Forecasting Weather with regression model""")

k = st.slider("range",0,40,30)
st.write(m.run(k))