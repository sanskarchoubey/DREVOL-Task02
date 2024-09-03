import mysql.connector as connector
from tabulate import tabulate
class DBDrevol:
    def __init__(self):
        # Extablishing connection with database
        self.con=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='sans@14',
                                    database='DREVOL')
        
        # Query to create table in database
        query='''CREATE TABLE IF NOT EXISTS sales
                 (Order_id INT PRIMARY KEY, 
                 customer_number VARCHAR(200), 
                 item_number VARCHAR(200), 
                 qty VARCHAR(200), 
                 price INT)'''
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    # Function to insert values in table
    def insert_user(self,Order_id, customer_number,item_number,qty,price):
        query='''INSERT INTO SALES(Order_id,customer_number,item_number,qty,price)
        values({},'{}','{}','{}','{}')'''.format(
        Order_id,customer_number,item_number,qty,price)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sales saved to db")
    def fetch_all(self):
        query='select * from sales'
        cur=self.con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        headers = ['Order ID', 'Customer Number', 'Item Number', 'Quantity', 'Price']
        print(tabulate(rows, headers, tablefmt='grid'))
drevol=DBDrevol()
#insert the data
# drevol.insert_user(116,"9876","7","4","10000")
# drevol.insert_user(112,"9877","9","5","11000")
# drevol.insert_user(113,"9878","11","1","12000")
# drevol.insert_user(114,"9879","12","2","23000")
# drevol.insert_user(115,"9880","13","3","25000")
drevol.fetch_all()