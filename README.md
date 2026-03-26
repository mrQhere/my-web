# 🚀 Secure Streamlit Web Application

## Project Overview
This repository contains a fully functional, deployed web application built using Python and Streamlit. The application demonstrates core web development principles by integrating a secure password authentication gateway, custom front-end styling via CSS injection, and stateful session management.

## What This Application Does
1. **Gatekeeping & Security:** Users are greeted with a secure login screen and cannot access the main dashboard without the correct credentials.
2. **State Management:** It remembers the user's logged-in status across interactions without requiring them to re-enter the password for every click.
3. **Custom UI/UX Styling:** It overrides default framework aesthetics to provide a polished, minimalist interface, including a persistent "made with curiosity" footer.
4. **Interactive Dashboard:** It provides a gated area for interactive data processing and user inputs.

## Academic & Syllabus Alignment
This project acts as a practical implementation of several core computer science and software engineering syllabus topics:

* **Web Development Fundamentals:** Demonstrates the client-server model and front-end rendering using a modern Python web framework.
* **Information Security & Access Control:** Implements basic authentication logic to restrict access to sensitive application states, a fundamental concept in cybersecurity modules.
* **Application State Management:** Utilizes session states (`st.session_state`) to persist data across application reruns. This addresses the stateless nature of HTTP, a crucial concept in full-stack development.
* **UI/UX Design Principles:** Applies custom CSS to modify the Document Object Model (DOM) rendering, demonstrating an understanding of aesthetics and user-centric design.
* **Software Deployment & Cloud Computing:** Showcases continuous deployment by linking a version control repository (GitHub) directly to a cloud hosting environment (Streamlit Community Cloud).

## Installation & Local Execution
To run this project on a local machine rather than the cloud server, follow these steps:

1. Clone this repository to your local machine.
2. Ensure Python is installed.
3. Install the required dependencies using the terminal command: `pip install -r requirements.txt`
4. Run the application using the terminal command: `streamlit run app.py`

## Technologies Used
* **Language:** Python 3
* **Framework:** Streamlit
* **Styling:** HTML / CSS
* **Version Control:** Git / GitHub
* **Hosting:** Streamlit Community Cloud
