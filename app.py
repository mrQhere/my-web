import streamlit as st

# 1. PAGE CONFIGURATION (Must be the first Streamlit command)
st.set_page_config(page_title="My Polished App", page_icon="🚀", layout="centered")

# 2. CUSTOM CSS FOR POLISH & FOOTER
# Why we do this: Default Streamlit has standard headers/footers. Injecting CSS overrides 
# them for a cleaner, professional look and locks your custom text to the bottom.
st.markdown("""
    <style>
    /* Hide default Streamlit artifacts */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Create the custom bottom footer */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #888888;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-family: sans-serif;
    }
    </style>
    <div class="custom-footer">
        made with curiosity
    </div>
""", unsafe_allow_html=True)

# 3. PASSWORD AUTHENTICATION LOGIC
# Why we do this: We use 'session_state' to remember if the user has unlocked the app 
# so they don't have to type the password every time they click a button.
def check_password():
    """Returns `True` if the user had the correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == "hello1234": # <--- CHANGE THIS PASSWORD
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Delete password from memory for security
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run: show input for password.
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Incorrect password: show input + error message.
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect. Try again.")
        return False
    else:
        # Password correct: unlock the app.
        return True

# 4. MAIN WEB APP CONTENT
if check_password():
    # Everything indented under here only shows up IF the password is correct.
    st.title("Welcome to the App! ✨")
    st.write("You have successfully passed the security gate.")
    
    st.divider() # Adds a clean horizontal line
    
    st.subheader("Interactive Dashboard")
    st.info("This is where the actual functionality of your app will live.")
    
    # Example of a polished interactive element
    user_name = st.text_input("What is your name?")
    if user_name:
        st.success(f"It is great to meet you, {user_name}!")