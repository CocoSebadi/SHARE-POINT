import streamlit as st
import pandas as pd

def login():
    # Placeholder authentication logic
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username == "demo" and password == "password":
        return True
    else:
        return False

def main():
    st.title("Issues Form")

    if login():
        st.success("Login successful!")

        # Show a pop-up message for choosing to log a new issue or update an existing issue
        issue_action = st.radio("Select an action:", ["Log a New Issue", "Update an Existing Issue"])

        st.header("Issue Details")
        issue_name = st.text_input("Issue Name", "")
        issue_description = st.text_area("Issue Description", "")
        risk_type = st.selectbox("Risk Type", ["Low", "Medium", "High"])
        # Add more form elements as needed

        st.header("Category and Ratings")
        casual_category = st.selectbox("Casual Category", ["Category A", "Category B", "Category C"])
        bu_rating = st.slider("BU Rating", min_value=1, max_value=5, value=3)
        agl_rating = st.slider("AGL Rating", min_value=1, max_value=5, value=3)
        assurance_provider = st.selectbox("Assurance Provider", ["Provider A", "Provider B", "Provider C"])

        st.header("Due Date and Financial Implications")
        due_date = st.date_input("Due Date", help="Select the due date of the issue")
        if due_date > (st.date_input("Today") + pd.DateOffset(days=90)):
            st.warning("This is a milestone.")
        elif due_date > (st.date_input("Today") + pd.DateOffset(years=2)):
            st.error("This is an issue.")

        financially_implicated = st.radio("Is the issue financially implicated?", ["Yes", "No"])

        st.header("Risk Event")
        risk_event_type = st.selectbox("Type of Risk Event", ["Type 1", "Type 2", "Type 3"])

        # Additional elements for updating an existing issue
        if issue_action == "Update an Existing Issue":
            st.header("Update Information")
            update_file = st.file_uploader("Attach a File for Update", type=["pdf", "docx"])
            written_evidence = st.text_area("Provide Written Evidence for Update", "")

        # Add a button to submit the form
        if st.button("Submit"):
            st.success("Form submitted successfully!")

    else:
        st.error("Login failed. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.exception(e)
