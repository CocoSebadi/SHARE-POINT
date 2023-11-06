
import streamlit as st 


#Mock employee login
st.title("Employee Login")
username = st.text_input("Username")
password= st.text_input("Password", type ="password")
login_button= st.button("Login")


if login_button:
   # check credentials and redirect to dashboard if valid
   if username == "employee" and password == "password":
       st.success("Login successful")
       st.text("Redirecting to dasboard....")
       
#Mock employee dashboard
if username == "employee":
    st.title("Employee Dashboard")
    work_description = st.text_area("Work Description")
    submit_button = st.button("Submit Work")
    
    if submit_button:
        #submit work and display success message 
        st.success("Work submitted successfully")
        
#mock real-tim work tracking 
if username == "employee" or username== "manager":
    st.title("Real-Time Work Tracking")
    st.table({"Work Item": ["Task 1","Task 2","Task 3"],
              "Status":["In Progress","Completed","In Review"],
              "Assigned To":["Employee A ","Employee B","Employee C"]})
    
st.sidebar.title("Navigation")
if st.sidebar.button("Logout"):
    st.experimental_rerun()
    
    #run the streamlit app
#st.write("you can run this app using streamlit run.app.py")
