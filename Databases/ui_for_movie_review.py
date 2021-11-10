from typing import cast
import streamlit as st
from movie_review import open_db
from movie_review import Movie

def add_review():
    with st.form('f1'):
        movie_name=st.text_input("Enter Movie's name")
        director=st.text_input("Enter Director's name")
        cast=st.text_input("Enter Movie's Cast")
        run_time=st.text_input("Enter Movie's run-time")
        review=st.text_input("Enter Review")
        btn=st.form_submit_button("Submit Review")
    
    if btn and movie_name and director and cast and run_time and review:
        db = open_db()
        db.add(Movie(movie_name=movie_name,director=director,cast=cast,run_time=run_time,review=review))
        db.commit()
        db.close()
        st.success("Saved movie review")


st.title("Movie Review")
options = ['View Movie Review','Add Movie Review']
choice = st.sidebar.radio("Select any option", options) 

if choice == options[0]:
    pass
elif choice == options[1]:
    add_review()