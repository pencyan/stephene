from pathlib import Path
import streamlit as st # pip install streamlit
from PIL import Image # pip install Pillow
from streamlit_option_menu import option_menu # pip install streamlit-option-menu


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
aj = current_dir / "styles" / "aj.png"
profile_pic = current_dir / "assets" / "profile-pic.png"
family = current_dir / "assets" / "family.png"
family_pic = current_dir / "assets" / "family_pic.png"
picture = current_dir / "assets" / "picture.jpg"
# --- GENERAL SETTINGS ---
PAGE_TITLE = "STREAMLIT | STEPHENE B. DAUGDAUG"
PAGE_ICON = ":wave:"
NAME ="Stephene B. Daugdaug"
DESCRIPTION = """
Student from SNSU Main Campus
"""
EMAIL = "stephenedaugdaug16@gmail.com"

aj = Image.open(aj)
family = Image.open(family)
family_pic = Image.open(family_pic)
picture = Image.open(picture)
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(aj, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)

with st.sidebar:
    selected = option_menu(
        menu_title="PROFILE",
        options= ["Programming Logic and Design","Personal Information","Family Picture","Contact"],
        icons= ["house","book","","envelope"],
        menu_icon="cast",
        default_index=0,
    )
# --- MAIN ---
if selected == "Programming Logic and Design":
        st.title(f"{selected}")
        st.write("---")
        st.write('\n')
        st.subheader("DESCRIPTION")
        st.write("Hello, this is my Webpage Project in Programming Logic and Design.")
        st.write("My personal Information is on the left side,")
        st.write("just click on it if you want my information.")
        st.write("also you can go to Contacts if you have questions just message or call me. :smiley:")

# --- INFIRMATION ---
if selected == "Personal Information":
    st.title(f"{selected}")
    cols1 , cols2 = st.columns(2)
    with cols1:
        st.markdown("---")
        st.image(picture)
    with cols2:
        with st.container():
         st.markdown("---")
         st.header("Student Information")
         st.write("NAME: Stephene B. Daugdaug")
         st.write("AGE : 20 yrs old")
         st.write("GENDER: Male")
         st.write("BIRTH PLACE: Karihatag, Malimono, SDN")
         st.write("BIRTH DATE : December,16,2002")
         st.write("HOBBIES: Playing Basketball, Online games")
         st.write("SKILLS: Driving")
         st.write("ADDRESS: Karihatag, Malimono, SDN")
         st.markdown("---")

    st.markdown("#")
    st.header("Schools Graduated:")
    st.write(":school: ELEMENTARY: Karihatag Elementary School")
    st.write(":school: JUNIOR HIGH: Surigao State College of Cechnology(SSCT)")
    st.write(":school: SENIOR HIGH: Malimono National High School")
    st.write(":school: COLLEGE: Surigao Del Norte State University(SNSU)1st yr.")
    st.write(":book: PROGRAM/Section: Bachelor of Science in Computer Engineering(BSCpE-1A)")

if selected == "Family Picture":
    st.title(f"{selected}")
    st.image(family_pic, caption = "This is my MOTHER, FATHER, and my SISTER.", width = 400)
    st.image(family, caption = "This is my GRANDMOTHER, GRANDFATHER, and my BROTHER.", width = 400)

# --- CONTACT ---
if selected == "Contact":
    st.title(f"You can {selected} me below.")
    st.write("Click the button :smile:")
    result = st.button("FACEBOOK")
    st.write(result)
    if result:
        st.write("https://www.facebook.com/Stephene_Daugdaug")
    result = st.button("GMAIL")
    st.write(result)
    if result:
        st.write(":envelope: Gmail stephenedaugdaug16@gmail.com")
    result = st.button("PHONE NUMBER")
    st.write(result)
    if result:
        st.write(":phone: 09507306220")