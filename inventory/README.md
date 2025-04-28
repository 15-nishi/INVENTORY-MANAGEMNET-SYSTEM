# Inventory Management System

A comprehensive MySQL-based inventory management system built with Python. This application helps businesses track inventory, manage customers and suppliers, process sales and purchases, and generate insightful reports.

## Features

- **Item Management:** Add, edit, search, and delete inventory items with their purchase and sale rates
- **Customer Management:** Maintain a database of customers with contact information
- **Supplier Management:** Keep track of suppliers and their details
- **Transaction Processing:** Record sales to customers and purchases from suppliers with automatic inventory adjustment
- **Reporting:** Generate inventory, customer, supplier, sales, and purchase reports with visualizations

## Installation

### Prerequisites

- Python 3.7+
- MySQL Server 5.7+ or 8.0+
- Git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/15-nishi/inventory-management.git
cd inventory-management
```

### Step 2: Install Required Python Packages

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database

1. Ensure MySQL service is running
2. Log in to MySQL as a user with CREATE DATABASE privileges:

```bash
mysql -u root -p
```

3. Import the database schema:

```sql
source inventory_schema.sql
```

### Step 4: Configure Database Connection (Optional)

If your MySQL credentials are different from the default (root/root), modify the connection parameters in each Python file or create a config file.

## Usage

Run the main program from the command line:

```bash
python menu.py
```

### Main Menu Options

1. **Items** - Manage inventory items
   - Add Items
   - Edit Item
   - Fix Rate
   - Search Item
   - Delete Item

2. **Customers** - Manage customer information
   - Add Customer
   - Edit Customer
   - Search Customer
   - Delete Customer

3. **Suppliers** - Manage supplier records
   - Add Supplier
   - Edit Supplier
   - Search Supplier
   - Delete Supplier

4. **Transactions** - Process sales and purchases
   - Sale
   - Purchase

5. **Reports** - Generate analytical reports
   - Item Details
   - Customer Details
   - Supplier Details
   - Sale Report
   - Purchase Report
   - Best Selling Report
   - Sales Performance

## Database Schema

### Core Tables
- `ITEM` - Stores product inventory details
- `CUSTOMER` - Stores customer information
- `SUPPLIER` - Stores supplier information

### Transaction Tables
- `SALE_MASTER` & `SALE_DETAIL` - For tracking sales to customers
- `PURCHASE_MASTER` & `PURCHASE_DETAIL` - For tracking purchases from suppliers
- `SALE_TEMP` & `PURCHASE_TEMP` - Temporary tables for transaction processing

## Project Structure

```
inventory-management/
├── menu.py                  # Main application entry point
├── item.py                  # Item management functions
├── customer.py              # Customer management functions
├── supplier.py              # Supplier management functions
├── transaction.py           # Sales and purchase processing
├── report.py                # Reporting and analytics
├── inventory_schema.sql     # Database schema and sample data
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Verify MySQL service is running
   - Check credentials in the Python files
   - Ensure the `inventory` database exists

2. **Missing Python Dependencies**
   - Run `pip install -r requirements.txt`
   - Ensure you're using Python 3.7+

3. **Import Errors**
   - Make sure all Python files are in the same directory
   - Check for typos in import statements

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request
