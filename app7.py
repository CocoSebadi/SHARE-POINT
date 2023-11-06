# !pip install streamlit 
# import streamlit as st 


# #Mock employee login
# st.title("Employee Login")
# username = st.text_input("Username")
# password= st.text_input("Password", type ="password")
# login_button= st.button("Login")


# if login_button:
#    # check credentials and redirect to dashboard if valid
#    if username == "employee" and password == "password":
#        st.success("Login successful")
#        st.text("Redirecting to dashboard....")
       
# #Mock employee dashboard
# if username == "employee":
#     st.title("Employee Dashboard")
#     work_description = st.text_area("Work Description")
#     submit_button = st.button("Submit Work")
    
#     if submit_button:
#         #submit work and display success message 
#         st.success("Work submitted successfully")
        
# #mock real-tim work tracking 
# if username == "employee" or username== "manager":
#     st.title("Real-Time Work Tracking")
#     st.table({"Work Item":["Task 1","Task 2","Task 3"],
#               "Status":["In Progress","Completed","In Review"],
#               "Assigned To":["Employee A ","Employee B",,"Employee C"]})
    
# st.sidebar.title("Navigation")
# if st.sidebar.button("Logout"):
#     st.experimental_rerun()
    
#     #run the streamlit app
# st.write("you can run this app using streamlit run.app.py")




# import streamlit as st

# # Simulated data (you should replace this with actual data from your database)
# work_data = [
#     {"employee": "John", "work_description": "Task 1", "status": "In Progress"},
#     {"employee": "Jane", "work_description": "Task 2", "status": "Completed"},
#     {"employee": "Bob", "work_description": "Task 3", "status": "In Progress"},
# ]

# # Set the title and subtitle
# st.title("Employee Work Submission and Tracking")
# st.subheader("Real-Time Work Tracking")

# # Display a table of work data
# st.table(work_data)



# import streamlit as st

# # Simulated data (you should replace this with actual data from your database)
# work_data = [
#     {"employee": "John", "work_description": "Task 1", "status": "In Progress"},
#     {"employee": "Jane", "work_description": "Task 2", "status": "Completed"},
#     {"employee": "Bob", "work_description": "Task 3", "status": "In Progress"},
# ]

# # Create a login page
# st.title("Employee Work Submission and Tracking")

# # Add login form
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     # Check username and password against your authentication system/database
#     if username == "employee" and password == "password":
#         st.success("Login successful!")

#         # Sidebar for navigation
#         page = st.sidebar.selectbox("Select Page", ["Submit Work", "Work Tracking"])

#         if page == "Submit Work":
#             st.subheader("Work Submission")
#             # Add a form to submit work
#             work_description = st.text_area("Work Description")
#             if st.button("Submit Work"):
#                 # Handle work submission logic here
#                 st.success("Work submitted successfully!")

#         elif page == "Work Tracking":
#             st.subheader("Real-Time Work Tracking")
#             # Display a table of work data
#             st.table(work_data)

#     else:
#         st.error("Login failed. Please check your credentials.")

# import streamlit as st

# # Create a login page
# st.title("Employee Work Submission and Tracking")

# # Add login form
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     # Check username and password against your authentication system/database
#     if username == "employee" and password == "password":
#         st.success("Login successful!")
#         st.subheader("Work Submission")
#         # Add a form to submit work
#         work_description = st.text_area("Work Description")
#         if st.button("Submit Work"):
#             # Handle work submission logic here
#             st.success("Work submitted successfully!")

#         st.subheader("Real-Time Work Tracking")
#         # Add a section to display real-time work tracking information
#     else:
#         st.error("Login failed. Please check your credentials.")

# # Run the app with 'streamlit run your_app.py'

# import streamlit as st

# # Create a title for the app
# st.title("Employee Work Submission")

# # Create a form for work submission
# employee_name = st.text_input("Employee Name")
# work_description = st.text_area("Work Description")
# status_options = ["In Progress", "Completed", "Not Started"]
# status = st.selectbox("Status", status_options)
# submission_date = st.date_input("Submission Date")
# submission_time = st.time_input("Submission Time")

# # Create a button to submit the work
# if st.button("Submit Work"):
#     # You can add code here to handle the work submission, like storing it in a database
#     st.success("Work submitted successfully!")

# import streamlit as st

# # User roles (you would replace this with actual user roles and authentication logic)
# user_roles = {
#     "user1": "Employee",
#     "user2": "Manager",
#     "user3": "Admin"
# }

# # Simulated data (you should replace this with actual data from your database)
# work_data = [
#     {"employee": "John", "work_description": "Task 1", "status": "In Progress"},
#     {"employee": "Jane", "work_description": "Task 2", "status": "Completed"},
#     {"employee": "Bob", "work_description": "Task 3", "status": "In Progress"},
# ]

# # Set the title and subtitle
# st.title("Employee Dashboard")

# # Sidebar for navigation
# page = st.sidebar.selectbox("Select Page", ["Submit Work", "Work Tracking"])

# # Get the current user (you would replace this with real authentication)
# current_user = st.text_input("Enter your username")

# if current_user in user_roles:
#     user_role = user_roles[current_user]
# else:
#     user_role = "Guest"

# if page == "Submit Work":
#     st.subheader("Work Submission")

#     if user_role == "Employee" or user_role == "Manager" or user_role == "Admin":
#         # Create a form for work submission
#         employee_name = st.text_input("Employee Name")
#         work_description = st.text_area("Work Description")
#         status_options = ["In Progress", "Completed", "Not Started"]
#         status = st.selectbox("Status", status_options)
#         submission_date = st.date_input("Submission Date")
#         submission_time = st.time_input("Submission Time")

#         # Create a button to submit the work
#         if st.button("Submit Work"):
#             # You can add code here to handle the work submission, like storing it in a database
#             st.success("Work submitted successfully!")
#     else:
#         st.warning("Access Denied: You do not have permission to submit work.")

# elif page == "Work Tracking":
#     st.subheader("Real-Time Work Tracking")

#     if user_role == "Manager" or user_role == "Admin":
#         # Display a table of work data
#         st.table(work_data)
#     else:
#         st.warning("Access Denied: You do not have permission to view work tracking.")
# else:
#     st.warning("Invalid Page Selection")

# st.sidebar.write("Current User Role:", user_role)

import streamlit as st

# Create a title for the app
st.title("Employee Work Submission")

# Create a container for notifications
notifications_container = st.empty()

# Create a form for work submission
employee_name = st.text_input("Employee Name")
work_description = st.text_area("Work Description")
status_options = ["In Progress", "Completed", "Not Started"]
status = st.selectbox("Status", status_options)
submission_date = st.date_input("Submission Date")
submission_time = st.time_input("Submission Time")

# Create a button to submit the work
if st.button("Submit Work"):
    # You can add code here to handle the work submission
    # For this example, we'll simulate a success message
    notifications_container.success("Work submitted successfully!")

# Create a button to clear notifications
if st.button("Clear Notifications"):
    notifications_container.empty()



