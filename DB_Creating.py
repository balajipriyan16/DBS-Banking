import mysql.connector
import Config

# DATABASE CREDENTIALS
DB_HOST = Config.DBS_HOST
DB_PASSWORD = Config.DBS_PASSWORD
DB_USER = Config.DBS_USER

# Connect to MySQL Server
db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)
myc = db.cursor(buffered=True)

# Create database if not exists
myc.execute("CREATE DATABASE IF NOT EXISTS bank;")
db.commit()

# Use the created database
myc.execute("USE bank;")
db.commit()

# Create tables
myc.execute("""
CREATE TABLE IF NOT EXISTS details (
    id VARCHAR(50),
    pin VARCHAR(50),
    name VARCHAR(50),
    balance VARCHAR(50),
    accno VARCHAR(50),
    phno VARCHAR(50),
    state VARCHAR(50),
    state2 VARCHAR(50),
    status VARCHAR(50),
    gmail VARCHAR(50)
);
""")

myc.execute("""
CREATE TABLE IF NOT EXISTS admins (
    Na VARCHAR(50),
    Pw VARCHAR(20),
    id VARCHAR(50)
);
""")

myc.execute("""
CREATE TABLE IF NOT EXISTS requests (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    Ti VARCHAR(50),
    Fr VARCHAR(50),
    Msg VARCHAR(1000)
);
""")

myc.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    F VARCHAR(50),
    Ti VARCHAR(50),
    T VARCHAR(50),
    Amount VARCHAR(50),
    ref VARCHAR(50) UNIQUE
);
""")

# Clear existing entries for fresh setup
myc.execute("DELETE FROM admins;")
myc.execute("DELETE FROM details;")
db.commit()

# Insert default admin
myc.execute("INSERT INTO admins (Na, Pw, id) VALUES (%s, %s, %s);", ('Admin', '1234', 'admin'))

# Insert sample customer
myc.execute("""
INSERT INTO details (id, pin, name, balance, accno, phno, state, state2, status, gmail)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
""", ('ben123', '1234', 'Ben', '100', '123456', '90256456', 'active', 'a', 'online', 'ben@gmail.com'))

db.commit()

# Close connections
myc.close()
db.close()

# Output success message
print("---------------------------")
print("Database Created!")
print("Tables Created!")
print("---------------------------")
print("Default User Created!")
print("---------------------------")
print("Customer.py")
print("Sample User Credentials!")
print("Accno: 123456")
print("Password: 1234")
print("---------------------------")
print("Admin.py")
print("Sample Admin Credentials!")
print("id: admin")
print("Password: 1234")
print("---------------------------")
