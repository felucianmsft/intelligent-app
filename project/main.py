# main.py  
from langchain.chains import LangChain  
import pyodbc  
  
# Replace the connection string with your actual SQL Server credentials and details  
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_username;PWD=your_password')  
cursor = conn.cursor()  
  
# Create a table for demonstration purposes  
cursor.execute('''  
IF OBJECT_ID('users', 'U') IS NOT NULL  
    DROP TABLE users;  
CREATE TABLE users (  
    id INT PRIMARY KEY IDENTITY(1,1),  
    username NVARCHAR(50),  
    password NVARCHAR(50)  
)  
''')  
conn.commit()  
  
# Insert some dummy data  
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'admin123'))  
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user', 'user123'))  
conn.commit()  
  
def get_user_details(username):  
    query = "SELECT * FROM users WHERE username = ?"  
    cursor.execute(query, username)  
    return cursor.fetchall()  
  
user_input = input("Enter the username: ")  
user_details = get_user_details(user_input)  
print("User Details:", user_details)  
  
conn.close()  

def main():  
    # Initialize LangChain  
    chain = LangChain()  
  
    # Example usage: Summarize text  
    input_text = "Artificial Intelligence (AI) is a branch of computer science that is concerned with building smart machines capable of performing tasks that typically require human intelligence."  
    summary = chain.summarize(input_text)  
    print("Summary:", summary)  
  
if __name__ == "__main__":  
    main()  
