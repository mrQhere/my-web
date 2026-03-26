import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="My Polished App", page_icon="🚀", layout="wide")

# 2. CUSTOM CSS (Footer)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: transparent; color: #888888;
        text-align: center; padding: 10px; font-size: 14px;
    }
    </style>
    <div class="custom-footer">made with curiosity</div>
""", unsafe_allow_html=True)

# 3. MOCK DATABASE INITIALIZATION
# This acts as our temporary memory for users.
if "user_db" not in st.session_state:
    st.session_state.user_db = {"admin": "password123"} # Default test account

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# 4. AUTHENTICATION UI FUNCTION
def auth_page():
    # Use columns to push the login box to the center of the screen
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        st.write("") # Spacing
        st.write("")
        
        # The "Nice Box" container
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center;'>Welcome</h3>", unsafe_allow_html=True)
            
            # Create interactive tabs inside the box
            tab_login, tab_signup, tab_reset = st.tabs(["Login", "Sign Up", "Reset Password"])
            
            # --- LOGIN TAB ---
            with tab_login:
                login_user = st.text_input("Username", key="login_user")
                login_pass = st.text_input("Password", type="password", key="login_pass")
                if st.button("Log In", use_container_width=True, type="primary"):
                    if login_user in st.session_state.user_db and st.session_state.user_db[login_user] == login_pass:
                        st.session_state.authenticated = True
                        st.session_state.current_user = login_user
                        st.rerun() # Refresh to clear login screen
                    else:
                        st.error("Invalid username or password")
                        
            # --- SIGN UP TAB ---
            with tab_signup:
                new_user = st.text_input("New Username", key="new_user")
                new_pass = st.text_input("New Password", type="password", key="new_pass")
                if st.button("Create Account", use_container_width=True):
                    if new_user in st.session_state.user_db:
                        st.error("Username already exists!")
                    elif len(new_user) > 0 and len(new_pass) > 0:
                        st.session_state.user_db[new_user] = new_pass
                        st.success("Account created! Please switch to the Login tab.")
                    else:
                        st.warning("Please fill out both fields.")
                        
            # --- RESET PASSWORD TAB ---
            with tab_reset:
                st.info("Demo mode: Direct reset without email verification.")
                reset_user = st.text_input("Username to Reset", key="reset_user")
                reset_pass = st.text_input("New Password", type="password", key="reset_new_pass")
                if st.button("Reset Password", use_container_width=True):
                    if reset_user in st.session_state.user_db:
                        st.session_state.user_db[reset_user] = reset_pass
                        st.success("Password reset successful! You can now log in.")
                    else:
                        st.error("User not found.")

# 5. MAIN APP ROUTING
if not st.session_state.authenticated:
    # Show the login box if not authenticated
    auth_page()
else:
    # --- EVERYTHING BELOW THIS LINE IS YOUR ACTUAL APP ---
    st.title(f"Welcome back, {st.session_state.current_user}! ✨")
    
    # A logout button for better UX
    if st.button("Log Out"):
        st.session_state.authenticated = False
        st.rerun()
    
    st.divider()
    
    st.subheader("Machine Learning Dashboard")
    st.write("This is where you can securely upload your datasets, trigger your training algorithms, and visualize your stock market prediction outputs.")