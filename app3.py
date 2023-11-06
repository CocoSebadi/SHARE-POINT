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
#        st.text("Redirecting to dasboard....")
       
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



import streamlit as st

# Simulated data (you should replace this with actual data from your database)
work_data = [
    {"employee": "John", "work_description": "Task 1", "status": "In Progress"},
    {"employee": "Jane", "work_description": "Task 2", "status": "Completed"},
    {"employee": "Bob", "work_description": "Task 3", "status": "In Progress"},
]

# Create a login page
st.title("Employee Work Submission and Tracking")

# Add login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Check username and password against your authentication system/database
    if username == "employee" and password == "password":
        st.success("Login successful!")

        # Sidebar for navigation
        page = st.sidebar.selectbox("Select Page", ["Submit Work", "Work Tracking"])

        if page == "Submit Work":
            st.subheader("Work Submission")
            # Add a form to submit work
            work_description = st.text_area("Work Description")
            if st.button("Submit Work"):
                # Handle work submission logic here
                st.success("Work submitted successfully!")

        elif page == "Work Tracking":
            st.subheader("Real-Time Work Tracking")
            # Display a table of work data
            st.table(work_data)

    else:
        st.error("Login failed. Please check your credentials.")
