import pandas as pd
import streamlit as st
st.set_page_config(page_title="My Protofolio",layout="wide",page_icon="💻")
st.header("Menna Allah Ahmed Zakria")
tab1,tab2,tab3,tab4,tab5,tab6,tab7=st.tabs(['About','Educational Background',' Skills','Offered Services','Professional projects','Achievements','Contact'])

with tab1:

   col1,col2=st.columns([1,2])
   with col1:


     st.header("Data Scientist")
     st.image("menna.jpg",use_container_width=True,width=150)
   with col2:
     st.header("About me!")
     st.write("I’m an aspiring Data Scientist passionate about turning data into insights. Skilled in Python, SQL, and visualization tools (Tableau, Power BI), I’m building projects to grow my machine learning knowledge. Curious and persistent, I enjoy finding patterns in data and sharing them in a clear, impactful way.")

with tab2:
  st.title("Educational Background")
  st.write("""◾B.Sc. in Computers and Data Science
        Faculty of Computers and Data Science, Alexandria University
        Second Year Student (2024 – Present)
""")
 
  st.write("""◾Digital Egypt Pioneers Initiative (DEPI) – Data Science & AI Track
         In Progress (2025 – Present)
""")
  st.header("Courses & Certifications")
  st.write("""◾ Python Fundamentals – MaharaTech / ITI (2025)""")
  st.write("""◾Database Fundamentals – MaharaTech / ITI (2025)""")
  st.write("""◾Python 101 for Data Science – IBM (2025)""")
with tab3:
  st.header("Technical Skills")
  st.subheader("Programming Language:")
  st.write(""" Python,sql ( Advanced)""")
  st.progress(90)
  st.subheader("Data Analysis")
  st.write("""Data Cleaning ,pandas,Numpy (Medium)""")
  st.progress(80)
  st.subheader("Visualization")
  st.write("""Matplotlib, Seaborn(Medium)""")
  st.progress(70)
  st.subheader("Machine Learning")
  st.write("Regression, Classification(Beginner)")
  st.progress(40)
  st.header("Tools:")
  st.write("GitHub , Colab Notebook")
  st.header("Soft Skils:")
  st.write("Problem-Solving, Analytical Thinking,Teamwork ")
with tab4:
  st.title("Offered Services")
  st.subheader("◾Data Cleaning & Analysis")
  st.write("""Fix missing values, remove duplicates, and format data so it’s ready for analysis.
""")
  st.subheader("◾Exploratory Data Analysis (EDA)")
  st.write("""  Explore data with summaries and charts to find patterns, trends, and outliers.
""")
  st.subheader("◾SQL Queries & Database Basic")
  st.write("Use SQL to get, filter, and group data from databases quickly and efficiently.")
  st.subheader("◾Python Scripting for Data Tasks")
  st.write("Automate data tasks like cleaning, transforming, and analysis using Python.")
  st.subheader("◾Data Visualization (Matplotlib, Seaborn)")
  st.write("Turn numbers into clear charts and graphs to make insights easy to understand.")
  st.subheader("◾Simple Reports & Dashboards")
  st.write(""" Present results as reports or interactive dashboards for quick decision-making.
""")
with tab5:
  st.title("Professional projects")
  col1,col2=st.columns([1,1])
  with col1:
    st.subheader("Simple Calculator 🔢")
    st.write("""A user-friendly web calculator built with Python and Streamlit for basic arithmetic operations.

""")
    if st.button("Try it Online"):
      st.markdown("[Click here to open the calculator](https://calculator-app-ardewjczspzmlysqe2slom.streamlit.app/)")
    st.image("Screenshot 2025-11-13 174350.png",use_container_width=True,width=40)
    with col2:
     st.subheader("Word Search Game(2025)")
     st.write("""Developed a small game in Python using Pygame and Random libraries.
Implemented word search logic and interactive visuals.

""")
     st.image("ai_pro.jpg",use_container_width=True,width=40)
    
with tab6:
  st.title("Achievements:")
  st.write("🏆Selected for Digital Egypt Pioneers Initiative (DEPI) – Data Science & AI Track (2025)")
  st.write("🏆Completed Python Fundamentals & Database Fundamentals – MaharaTech/ITI (2025)")
  st.write("🏆completed Python 101 for Data Science – IBM (2025)")
  st.write("🏆Delivered an interactive Data Analysis Dashboard with R Shiny as part of a college project.")
with tab7:
  st.title("Let's Work Together")
  col1,col2=st.columns([0.1,6])
  with col1:
   st.image("linkedin.jpg",width=40)
  with col2:
     
   st.markdown("[https://www.linkedin.com/in/menna-elkafory](https://www.linkedin.com/in/menna-elkafory)",unsafe_allow_html=True)


  
  col1,col2=st.columns([0.1,6])
  with col1:
   st.image("4494688.png",width=40)
  with col2:
     
   st.markdown("[https://github.com/mennaelkafory](https://github.com/mennaelkafory)",unsafe_allow_html=True)


  col1,col2=st.columns([0.1,6])
  with col1:
   st.image("images (2).png",width=40)
  with col2:
     
   st.markdown("[mennaelkafory26@gmail.com](mailto:mennaelkafory26@gmail.com)",unsafe_allow_html=True)

  col1,col2=st.columns([0.1,6])
  with col1:
   st.image("phone.jpg",width=40)
  with col2:
     
   st.markdown("[+201202647566](tel:+201202647566)",unsafe_allow_html=True)


  



  