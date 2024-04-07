import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password"
)

cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS db.clientes (
                     id INT UNSIGNED,
    surname VARCHAR(255),
    birthday DATE,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    age INT UNSIGNED,
    zip INT UNSIGNED)''')

data = pd.read_csv('customer_data.csv')
data['birthday']=pd.to_datetime(data['birthday'])
for index, row in data.iterrows():
    cursor.execute(
        f'''INSERT INTO db.clientes (id, surname, birthday, address, phone_number, age, zip) VALUES
        ({row['id']}, '{row['surname']}', '{row['birthday']}', '{row['address']}', '{row['phone_number']}', '{row['Edad']}', '{int(row['zipcode'])}')'''
    ) 

conn.commit()

print(cursor.rowcount, "record inserted.")

cursor.execute('''CREATE TABLE IF NOT EXISTS db.contratos (
                id INT UNSIGNED,
                Contract_start DATE,
                Contract_end DATE,
                total_amount INT UNSIGNED,
                days_duration INT UNSIGNED,
                payment_freq INT UNSIGNED,
                payment_amount FLOAT
            );''')

loansdf = pd.read_csv('LOAN_DATA.csv')
for index, row in loansdf.iterrows():
    cursor.execute(
        f'''INSERT INTO db.contratos (id, Contract_start, Contract_end, total_amount, days_duration, payment_freq, payment_amount) VALUES
        ({row['id']}, '{row['Contract_start']}', '{row['Contract_end']}', '{row['total_amount']}', '{row['days_duration']}', '{row['payment_freq']}', '{row['payment_amount']}')'''
    ) 

conn.commit()

print(cursor.rowcount, "record inserted.")

cursor.execute('''CREATE TABLE IF NOT EXISTS db.pagos (
                    id INT UNSIGNED,
                    payment_dates DATETIME,
                    status VARCHAR(255)
                );''')

paymentsdf = pd.read_csv('PAYMENT_DATA.csv')
for index, row in paymentsdf.iterrows():
    cursor.execute(
        f'''INSERT INTO db.pagos (id, payment_dates, status) VALUES
        ({row['id']}, '{row['payment_dates']}', '{row['status']}')'''
    ) 

conn.commit()

print(cursor.rowcount, "record inserted.")

cursor.execute('''CREATE INDEX idx_id_payment_dates ON db.pagos (id, payment_dates);''')
conn.commit()
cursor.execute('''CREATE INDEX idx_id_clientes ON db.clientes (id);''')
conn.commit()

cursor.close()
conn.close()