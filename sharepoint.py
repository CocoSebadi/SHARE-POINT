import streamlit as st
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('project_issues.db')
c = conn.cursor()

# Create a table to store issues
c.execute('''
          CREATE TABLE IF NOT EXISTS issues (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              rating INTEGER,
              overdue_issues TEXT,
              due_date DATE,
              risk_type TEXT
          )
          ''')
conn.commit()

# Streamlit App
def main():
    st.title("Project Issues Form")

    # Login Section (Dummy Authentication)
    if st.button("Login"):
        st.success("Login Successful!")
        show_form()

def show_form():
    # Project Issues Form
    st.header("Project Issues Form")

    rating = st.selectbox("Rating:", [1, 2, 3, 4, 5])
    overdue_issues = st.text_input("Overdue Issues:")
    due_date = st.date_input("Due Date:")
    risk_type = st.selectbox("Risk Type:", ["Low", "Medium", "High"])

    if st.button("Submit"):
        # Save the issue to the database
        save_issue(rating, overdue_issues, due_date, risk_type)
        st.success("Issue submitted successfully!")

def save_issue(rating, overdue_issues, due_date, risk_type):
    c.execute("INSERT INTO issues (rating, overdue_issues, due_date, risk_type) VALUES (?, ?, ?, ?)",
              (rating, overdue_issues, due_date, risk_type))
    conn.commit()

if __name__ == "__main__":
    main()
