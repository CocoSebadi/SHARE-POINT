import streamlit as st
import pandas as pd

# Placeholder data for consolidated open issues table
open_issues_data = {
    "Issue ID": [1, 2, 3,4],
    "Issue Owner": ["User1", "User2", "User3","User3"],
    "Original Date": ["2023-01-01", "2023-02-01", "2023-03-01","2023-05-01"],
    "Revised Due Date": ["2023-02-01", "2023-03-01", "2023-04-01","2023-06-01"],
    "BU Rating": ["High", "Medium","Moderate","Low"]
}

open_issues_df = pd.DataFrame(open_issues_data)

# Placeholder data for dropdowns
risk_types = ["Type1", "Type2", "Type3"]
subrisk_types = ["SubType1", "SubType2", "SubType3"]
Risk_categories = ["Category1", "Category2", "Category3"]
agl_ratings = ["Limited", "Major", "Moderate", "Critical"]
BU_ratings = ["Rating1", "Rating2", "Rating3"]
assurance_providers = ["Provider1", "Provider2", "Provider3"]
risk_events = ["Event1", "Event2", "Event3"]

def main():
    st.title("Project Issues Form")

    if login():
        st.success("Login successful!")

        issue_name = st.text_input("Issue Name")
        issue_description = st.text_area("Issue Description")

        risk_type = st.selectbox("Risk Type", risk_types)
        subrisk_type = st.selectbox("Subrisk Type", subrisk_types)
        casual_category = st.selectbox("Casual Category", Risk_categories)
        bu_rating = st.selectbox("BU Rating", ["High", "Medium", "Low"])
        agl_rating = st.selectbox("AGL Rating", agl_ratings)
        rating = st.selectbox("Rating", BU_ratings)
        assurance_provider = st.selectbox("Assurance Provider", assurance_providers)

        due_date = st.date_input("Due Date")

        financially_implicated = st.radio("Is the issue financially implicated?", ["Yes", "No"])

        risk_event = st.selectbox("Type of Risk Event", risk_events)

        # If updating an existing issue, show consolidated open issues table
        if st.radio("Select an action:", ["Log a New Issue", "Update an Existing Issue"]) == "Update an Existing Issue":
            st.write("Consolidated Open Issues Table:")
            st.write(open_issues_df)

            selected_issue_id = st.number_input("Select Issue ID to Update", min_value=1, max_value=len(open_issues_df))

            if st.button("Update Issue"):
                selected_issue = open_issues_df[open_issues_df["Issue ID"] == selected_issue_id].iloc[0]

                st.write(f"Updating Issue ID: {selected_issue_id}")

                update_options = st.multiselect("Select columns to update:", open_issues_df.columns)
                if update_options:
                    st.write(f"Updating the following columns: {update_options}")

                    # Add more form elements for updating specific columns

                    # File upload
                    uploaded_file = st.file_uploader("Attach a file or provide written evidence", type=["pdf", "txt"])
                    if uploaded_file is not None:
                        st.success("File attached successfully.")

        # Add a button to submit the form
        if st.button("Submit"):
            st.success("Form submitted successfully!")

    else:
        st.error("Login failed. Please try again.")

def login():
    # Placeholder authentication logic
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username == "demo" and password == "password":
        return True
    else:
        return False

if __name__ == "__main__":
    main()


