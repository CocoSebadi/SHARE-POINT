import streamlit as st

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

        st.header("Issue Details")

        issue_name = st.text_input("Issue Name")
        issue_description = st.text_area("Issue Description")

        risk_type = st.selectbox("Risk Type", ["Low", "Medium", "High"])

        entities = st.multiselect("Entities", ["Entity A", "Entity B", "Entity C"])

        causal_category = st.selectbox("Causal Category", ["Category 1", "Category 2", "Category 3"])

        bu_rating = st.slider("BU Rating", min_value=1, max_value=5)

        agile_rating = st.slider("Agile Rating", min_value=1, max_value=5)

        assurance_provider = st.text_input("Assurance Provider")

        due_date = st.date_input("Due Date")

        # If updating an existing issue, ask for additional evidence
        if issue_action == "Update an Existing Issue":
            st.header("Update Evidence")
            update_evidence = st.text_area("Provide written evidence for the update")

            # Option to attach a file
            uploaded_file = st.file_uploader("Attach a File (if any)", type=["pdf", "docx", "xlsx"])

        # Add a button to submit the form
        if st.button("Submit"):
            # Add logic to handle form submission, storing the data, etc.
            st.success("Form submitted successfully!")

    else:
        st.error("Login failed. Please try again.")

if __name__ == "__main__":
    main()
