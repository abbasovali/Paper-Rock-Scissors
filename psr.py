import streamlit as st
import random
import time

header = st.container()

with header:
    st.title("Welcome to 'Paper Scissors Rock game!'")
    time.sleep(1)
    st.write("3,2,1! Lets go!")
    time.sleep(1)
    option = st.selectbox(
        'Select your choice:',
        (' ', 'Paper', 'Scissors', 'Rock'))
    st.write('Your choice:', option)
    time.sleep(1)
    if option != ' ':
        compchoise = random.choice(["Rock", "Scissors", "Paper"])
        st.write("Computer choice:", compchoise)
        if (option == "Paper" and compchoise == "Rock") or (option == "Scissors" and compchoise == "Paper") or (
                option == "Rock" and compchoise == "Scissors"):
            st.success("You won!")
            st.balloons()
        elif option == compchoise:
            st.text("Draw! Try again!")
        elif option == ' ':
            st.text(" ")
        else:
            st.text("You lose :(")
