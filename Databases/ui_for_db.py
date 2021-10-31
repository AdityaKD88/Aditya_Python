# run in terminal (ctrl+j)
# streamlit run Databases/ui_for_db.py
import streamlit as st
from db_example1 import open_db
from db_example1 import Student, Grade


def   show_student_form():
    with st.form('f1'):
        name=st.text_input("Enter student's name")
        c1,c2 = st.columns(2)
        klass=c1.text_input("Enter student's class")
        section=c2.text_input("Enter student's section")
        is_online=st.checkbox("Is student attending online?")
        btn=st.form_submit_button("Add student")

    if btn and name and klass and section:
        db = open_db()
        db.add(Student(name=name,section=section,klass=klass))   # add the student detail
        db.commit() # save
        db.close()  #close the db
        st.success("Saved student details")

def   show_grading_form():
    pass


# UI Code
st.title("Database Example for Newbies")

options = ['View Students','View Grades','Add Student','Add Grades']

choice = st.sidebar.radio("Select any option", options)

if choice == options[0]:
    pass
elif choice == options[1]:
    pass
elif choice == options[2]:
    show_student_form()
elif choice == options[4]:
    show_grading_form()
