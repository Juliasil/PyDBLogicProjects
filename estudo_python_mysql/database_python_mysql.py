import mysql.connector
from mysql.connector import Error
import configparser

def get_database_credentials():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return {
        'host': config['MySQL']['host'],
        'user': config['MySQL']['user'],
        'password': config['MySQL']['password']
    }

def main():
    credentials = get_database_credentials()
    try:
        database_connection = mysql.connector.connect(
            host= credentials['host'],
            port= 3306,
            user= credentials['user'],
            password= credentials['password'],
        )
        cursor = database_connection.cursor()
        
        database_name = input('Enter database name: ') 

        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cursor.fetchone()
        print(result)
        if not result:
            print(f'Database {database_name} does not exist. Creating...')
            cursor.execute(f"CREATE DATABASE {database_name}")
            cursor.execute(f"USE {database_name}") 
            print("Database created.")

            database_connection.database = database_name

        while True:
            print("\n1. Create table")
            print("2. Insert data")
            print("3. Read data")
            print("4. Update data")
            print("5. Delete data")
            print("6. Exit")
            
            option = int(input("Choose an option: "))

            match option:
                case 1:
                    create_table(cursor)
                case 2:
                    insert_data(database_connection, cursor)
                case 3:
                    read_data(cursor)
                case 4:
                    update_data(database_connection, cursor)
                case 5:
                    delete_data(database_connection, cursor)
                case 6:
                    print("Exiting program.")
                    break
                case _:
                    print("==================")
                    print("Invalid option")
                    print("==================")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if database_connection.is_connected:
            cursor.close()
            database_connection.close()    
            print("MySQL connection is closed.")

def create_table(cursor):
    table_name = input("Enter table name: ")

    columns_details = input("Enter columns and types (e.g., id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)): ")

    cursor.execute(f"CREATE TABLE {table_name} ({columns_details})")
    print(f"Table '{table_name}' created.")

def insert_data(database_connection, cursor):
    table_name = input("Enter table name: ")

    columns = input("Enter columns: (e.g., id, name)")
    values = input("Enter values: (e.g., 1, 'John Doe')")
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    cursor.execute(query)
    database_connection.commit()
    print("Data inserted.")

def read_data(cursor):
    table_name = input("Enter table name: ")
    wildcard = input("Enter wildcard: ")
    query = f"SELECT * FROM {table_name} WHERE name LIKE %s"
    cursor.execute(query, ('%' + wildcard + '%',))
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        print('--------------')

def update_data(database_connection, cursor):
    table_name = input("Enter table name: ")
    set_clause = input("Enter SET clause (e.g., name = 'Jane Doe')")
    filter_clause = input("Enter WHERE clause (e.g., id = 1): ")
    cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {filter_clause}")
    database_connection.commit()
    print("Data updated.")

def delete_data(database_connection, cursor):
    table_name = input("Enter table name: ")
    condition = input("Enter condition: (e.g., id = 1)")
    cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
    database_connection.commit()
    print("Data deleted.")


main()
