import streamlit as st
import pandas as pd

# Placeholder data for the consolidated open issues table
consolidated_open_issues_data = {
    'Issue ID': [1, 2, 3],
    'Issue Owner': ['User1', 'User2', 'User3'],
    'Original Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'Revised Due Date': ['2023-02-01', '2023-03-01', '2023-04-01'],
    'BU Rating': ['High', 'Medium', 'Low']
}

consolidated_open_issues_df = pd.DataFrame(consolidated_open_issues_data)

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

        if issue_action == "Log a New Issue":
            st.write("You chose to log a new issue.")
            # Add form elements for logging a new issue
            issue_name = st.text_input("Issue Name", "")
            issue_description = st.text_area("Issue Description", "")
            risk_type = st.selectbox("Risk Type", ["Low", "Medium", "High"])
            # Add more form elements as needed

        elif issue_action == "Update an Existing Issue":
            st.write("You chose to update an existing issue.")
            
            # Display the consolidated open issues table
            st.write("Consolidated Open Issues:")
            st.table(consolidated_open_issues_df)

            # Allow the user to select the issue they want to update by Issue ID
            selected_issue_id = st.number_input("Select Issue ID to Update", min_value=1, max_value=len(consolidated_open_issues_df))

            if selected_issue_id:
                # Prompt for selecting the column to update
                update_column = st.selectbox("Select Column to Update", consolidated_open_issues_df.columns)

                # Prompt for providing the new value
                new_value = st.text_input(f"Enter new value for {update_column}", consolidated_open_issues_df.loc[selected_issue_id - 1, update_column])

                # Prompt for attaching a file or providing written evidence
                evidence = st.text_area("Provide Written Evidence or Attach a File")

                # Add logic to update the selected issue in the DataFrame or database
                # ...

                st.success(f"Issue ID {selected_issue_id} successfully updated in column {update_column} with value: {new_value}")

        # Add a button to submit the form
        if st.button("Submit"):
            st.success("Form submitted successfully!")

    else:
        st.error("Login failed. Please try again.")

if __name__ == "__main__":
    main()
