import streamlit as st
import random

st.title("Number Guessing Game")

n = random.randint(1, 100)
guess_count = 0

guess = st.number_input("Enter your guess number:", min_value=1, max_value=100, step=1)
submit = st.button("Check Guess")

if "target_number" not in st.session_state:
    st.session_state.target_number = n
    st.session_state.guess_count = 0

if submit:
    st.session_state.guess_count += 1
    if guess > st.session_state.target_number:
        st.write("Lower number please")
    elif guess < st.session_state.target_number:
        st.write("Higher number please")
    else:
        st.success(f"Your guess is correct! The number is {st.session_state.target_number}. ")
        st.write(f"You guessed it in {st.session_state.guess_count} attempts.")
        st.session_state.target_number = random.randint(1, 100)  # Reset the game
        st.session_state.guess_count = 0
