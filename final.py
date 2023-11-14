import streamlit as st
import pandas as pd

# Placeholder for existing issues data
existing_issues_data = {
    'Issue ID': [1, 2, 3],
    'Issue Name': ['Example Issue 1', 'Example Issue 2', 'Example Issue 3'],
    'Description': ['Description 1', 'Description 2', 'Description 3'],
    'Risk Type': ['High', 'Medium', 'Low'],
    'Casual Category': ['Category A', 'Category B', 'Category C'],
    'BU Rating': ['A', 'B', 'C'],
    'AGL Rating': [1, 2, 3],
    'Assurance Provider': ['Provider X', 'Provider Y', 'Provider Z'],
    'Due Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'Financial Implication': ['Yes', 'No', 'Yes'],
    'Type of Risk Event': ['Event 1', 'Event 2', 'Event 3'] }

existing_issues_df = pd.DataFrame(existing_issues_data)

def login():
    # Placeholder authentication logic
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username == "demo" and password == "password":
        return True
    else:
        return False

def main():
    st.title("Project Issues Form")

    if login():
        st.success("Login successful!")

        # Show a pop-up message for choosing to log a new issue or update an existing issue
        issue_action = st.radio("Select an action:", ["Log a New Issue", "Update an Existing Issue"])

        # Form elements for logging a new issue
        st.header("Log a New Issue" if issue_action == "Log a New Issue" else "Update an Existing Issue")

        issue_name = st.text_input("Issue Name")
        description = st.text_area("Issue Description", "")
        risk_type = st.selectbox("Risk Type", ["High", "Medium", "Low"])
        casual_category = st.selectbox("Casual Category", ["Category A", "Category B", "Category C"])
        bu_rating = st.slider("BU Rating", min_value=1, max_value=5, value=3)
        agl_rating = st.slider("AGL Rating", min_value=1, max_value=5, value=3)
        assurance_provider = st.selectbox("Assurance Provider", ["Provider X", "Provider Y", "Provider Z"])
        due_date = st.date_input("Due Date")
        financial_implication = st.radio("Is the issue financially implicated?", ["Yes", "No"])
        risk_event_type = st.text_input("Type of Risk Event")

        if issue_action == "Update an Existing Issue":
            # Display existing issues table for selection
            st.header("Existing Issues for Update")
            st.table(existing_issues_df)

            selected_issue_id = st.number_input("Select Issue ID to Update", min_value=1, max_value=len(existing_issues_df), step=1)

            # Form elements for updating an existing issue
            updated_description = st.text_area("Updated Issue Description", "")

            # Option to attach a file or provide written evidence
            attachment_option = st.radio("Select Attachment Option:", ["Attach a File", "Provide Written Evidence"])

            if attachment_option == "Attach a File":
                uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

            elif attachment_option == "Provide Written Evidence":
                written_evidence = st.text_area("Provide Written Evidence", "")

        # Add a button to submit the form
        if st.button("Submit"):
            st.success("Form submitted successfully!")

    else:
        st.error("Login failed. Please try again.")

if __name__ == "__main__":
    main()
