-- Create database
CREATE DATABASE IF NOT EXISTS inventory;
USE inventory;

-- Drop tables if they exist to avoid errors (in reverse order of dependencies)
DROP TABLE IF EXISTS SALE_TEMP;
DROP TABLE IF EXISTS PURCHASE_TEMP;
DROP TABLE IF EXISTS SALE_DETAIL;
DROP TABLE IF EXISTS PURCHASE_DETAIL;
DROP TABLE IF EXISTS SALE_MASTER;
DROP TABLE IF EXISTS PURCHASE_MASTER;
DROP TABLE IF EXISTS ITEM;
DROP TABLE IF EXISTS CUSTOMER;
DROP TABLE IF EXISTS SUPPLIER;

-- Create tables
CREATE TABLE SUPPLIER (
    Supplier_id INT PRIMARY KEY,
    Supplier_name VARCHAR(100) NOT NULL,
    Supplier_address VARCHAR(255),
    Supplier_mobile VARCHAR(20)
);

CREATE TABLE CUSTOMER (
    Customer_id INT PRIMARY KEY,
    Customer_name VARCHAR(100) NOT NULL,
    Customer_address VARCHAR(255),
    Customer_mobile VARCHAR(20)
);

CREATE TABLE ITEM (
    Item_no INT PRIMARY KEY,
    Item_name VARCHAR(100) NOT NULL,
    Purchase_rate DECIMAL(10,2) NOT NULL,
    Sale_rate DECIMAL(10,2) NOT NULL,
    Qty_on_hand INT NOT NULL
);

CREATE TABLE PURCHASE_MASTER (
    Purchase_id INT PRIMARY KEY,
    Purchase_date DATE NOT NULL,
    Supplier_id INT,
    Total DECIMAL(12,2),
    FOREIGN KEY (Supplier_id) REFERENCES SUPPLIER(Supplier_id)
);

CREATE TABLE PURCHASE_DETAIL (
    Purchase_id INT,
    Item_no INT,
    Qty INT NOT NULL,
    Rate DECIMAL(10,2) NOT NULL,
    Total DECIMAL(12,2),
    PRIMARY KEY (Purchase_id, Item_no),
    FOREIGN KEY (Purchase_id) REFERENCES PURCHASE_MASTER(Purchase_id),
    FOREIGN KEY (Item_no) REFERENCES ITEM(Item_no)
);

CREATE TABLE SALE_MASTER (
    Sale_id INT PRIMARY KEY,
    Sale_date DATE NOT NULL,
    Customer_id INT,
    Total DECIMAL(12,2),
    FOREIGN KEY (Customer_id) REFERENCES CUSTOMER(Customer_id)
);

CREATE TABLE SALE_DETAIL (
    Sale_id INT,
    Item_no INT,
    Qty INT NOT NULL,
    Rate DECIMAL(10,2) NOT NULL,
    Total DECIMAL(12,2),
    PRIMARY KEY (Sale_id, Item_no),
    FOREIGN KEY (Sale_id) REFERENCES SALE_MASTER(Sale_id),
    FOREIGN KEY (Item_no) REFERENCES ITEM(Item_no)
);

-- Temporary tables for transaction processing
CREATE TABLE PURCHASE_TEMP (
    Purchase_id INT,
    Item_no INT,
    Qty INT NOT NULL,
    Rate DECIMAL(10,2) NOT NULL,
    Total DECIMAL(12,2),
    PRIMARY KEY (Purchase_id, Item_no)
);

CREATE TABLE SALE_TEMP (
    Sale_id INT,
    Item_no INT,
    Qty INT NOT NULL,
    Rate DECIMAL(10,2) NOT NULL,
    Total DECIMAL(12,2),
    PRIMARY KEY (Sale_id, Item_no)
);

-- Insert some sample data
-- Sample suppliers
INSERT INTO SUPPLIER VALUES (1, 'ABC Distributors', '123 Supply St, Industrial Zone', '9876543210');
INSERT INTO SUPPLIER VALUES (2, 'XYZ Wholesale', '456 Commerce Blvd, Business Park', '8765432109');
INSERT INTO SUPPLIER VALUES (3, 'Global Goods Ltd', '789 Import Ave, Trade District', '7654321098');

-- Sample customers
INSERT INTO CUSTOMER VALUES (1, 'John Smith', '101 Main St, Downtown', '1234567890');
INSERT INTO CUSTOMER VALUES (2, 'Jane Doe', '202 Park Ave, Uptown', '2345678901');
INSERT INTO CUSTOMER VALUES (3, 'Bob Johnson', '303 Lake Rd, Suburbs', '3456789012');

-- Sample items
INSERT INTO ITEM VALUES (101, 'Laptop', 800.00, 1200.00, 25);
INSERT INTO ITEM VALUES (102, 'Smartphone', 350.00, 600.00, 40);
INSERT INTO ITEM VALUES (103, 'Tablet', 250.00, 400.00, 30);
INSERT INTO ITEM VALUES (104, 'Headphones', 50.00, 90.00, 100);
INSERT INTO ITEM VALUES (105, 'Monitor', 150.00, 250.00, 20);
