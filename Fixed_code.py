import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Function to validate employee number
def validate_employee_number(employee_number):
    valid_employee_numbers = ["emp123", "emp456", "emp789"]
    return employee_number in valid_employee_numbers

# Function to calculate reminder date
def calculate_reminder_date(due_date):
    return due_date - timedelta(days=3 * 30)

# Function to send email (placeholder, implement your email sending logic here)
def send_email(recipient_email, subject, body):
    # Implement your email sending logic here
    pass

# Main function
def main():
    # Login Section
    employee_number = st.text_input("Employee Number", max_chars=7)

    if st.button("Login"):
        if len(employee_number) == 7 and validate_employee_number(employee_number):
            st.success("Login successful!")

            st.title("Project Issues Form")

            # Assuming you want to proceed with the issues form only after successful login
            if st.button("Login"):
                if len(employee_number) == 7 and validate_employee_number(employee_number):
                    issue_action = st.radio("Select an action:", ["Log a New Issue", "Update an Existing Issue"])

                    if issue_action == "Log a New Issue":
                        st.write("You chose to log a new issue.")

                        # Add form elements for logging a new issue
                        issue_name = st.text_input("Issue Name")
                        issue_description = st.text_area("Issue Description", "")
                        issue_status = st.selectbox("Issue Status", ["Open", "Closed", "Risk Accepted", "Overdue"])
                        # ... (rest of the form elements)

                        # Convert the input due_date to datetime object
                        due_date = datetime.combine(due_date, datetime.min.time())

                        # Calculate the reminder date (3 months before the due date)
                        reminder_date = calculate_reminder_date(due_date)

                        # Check if it's time to send the reminder
                        current_date = datetime.now()
                        if current_date >= reminder_date:
                            # Assuming you have some email sending functionality here
                            send_email(issue_owner_email, "Reminder: Upcoming Issue Due Date", f"Dear {issue_owner_name},\n\nThis is a reminder that the issue '{issue_name}' is due on {due_date}. I trust this email finds you well. I wanted to bring to your attention that the deadline for resolving the current issue is fast approaching. As part of the resolution process, we kindly request you to compile an Incident Closure Plan (ICP) using the specified ICP format.")

                        # Display a message in the Streamlit app
                        st.write(f"Reminder email will be sent to {issue_owner_email} on {reminder_date}")

                    elif issue_action == "Update an Existing Issue":
                        st.write("You chose to update an existing issue.")
                        st.subheader("Consolidated Open Issues:")
                        uploaded_file = st.file_uploader("Upload an existing issues tracker file", type=["csv", "xlsx"])

                        if uploaded_file is not None:
                            # Read the uploaded file into a DataFrame
                            existing_issues_df = pd.read_csv(uploaded_file)  # Adjust the reading logic based on the file type
                            st.write("Existing Issues Tracker Loaded:")
                            st.write(existing_issues_df)

                            # Allow the user to select the issue they want to update
                            selected_issue_id = st.selectbox("Select the Issue to Update", existing_issues_df['Issue ID'])

                            # Additional form elements for updating an existing issue
                            issue_owner = st.text_input("Issue Owner")
                            original_date = st.date_input("Original Date")
                            revised_due_date = st.date_input("Revised Due Date")
                            bu_rating_update = st.text_input("BU Rating Update")

                            # File attachment or written evidence for the update
                            attachment = st.file_uploader("Attach a File or Provide Written Evidence", type=["pdf", "docx"])

                            # Add a button to submit the form
                            if st.button("Submit"):
                                st.success("Form submitted successfully!")
                        else:
                            st.warning("Please upload an existing issues tracker file.")

                            # Add a button to submit the form
                            if st.button("Submit"):
                                st.success("Form submitted successfully!")
                else:
                    st.error("Login failed. Please try again.")

if __name__ == "__main__":
    main()
