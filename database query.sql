CREATE DATABASE dbproject;

CREATE TABLE Cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL
   
);
ALTER TABLE Customer ADD COLUMN password VARCHAR(255);

CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    product_type VARCHAR(20) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    image VARCHAR(255),  -- For image, since it's an ImageField in Django, storing the file path here
    stock INT,
    color VARCHAR(255),  
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE OrderTable (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    address_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    CHECK (status IN ('Pending', 'Delivered')),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (address_id) REFERENCES Address(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE OrderItems (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES OrderTable(order_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Address (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key for Address
    country VARCHAR(50),
    city VARCHAR(50),
    street VARCHAR(100),
    house_number VARCHAR(10),
    zip_code VARCHAR(10),
    customer_id INT,  -- This references the Customer table
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)  -- Assuming Customer table has column 'id' as primary key
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

