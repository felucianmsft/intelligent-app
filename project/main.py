# main.py  
from langchain.chains import LangChain  
import pyodbc  

def get_user_orders(userid):  
    query = f"SELECT * FROM orders WHERE username = '{userid}'"  
    cursor.execute(query)  
    return cursor.fetchall()  

def main():  
    # Initialize LangChain  
    chain = LangChain()  
  
    # Example usage: Summarize text  
    input_text = "Artificial Intelligence (AI) is a branch of computer science that is concerned with building smart machines capable of performing tasks that typically require human intelligence."  
    summary = chain.summarize(input_text)  
    print("Summary:", summary)  
  
if __name__ == "__main__":  
    main()  
