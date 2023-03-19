import streamlit as st

st.title(":red[Hello!] :blue[I am Vishal]")
st.header("I am a Data Science intern at  Innomatics Research Labs")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()