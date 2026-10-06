CREATE TABLE books (
bok_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT,
year INTEGER CHECK (year > 1400)
)

ALTER TABLE books ADD COLUMN isbn TEXT;

--DROP TABLE books;

CREATE TABLE reviews (
review_id INTEGER PRIMARY KEY,
product_id INTEGER,
rating INTEGER CHECK (rating > 0 AND rating < 6), 
comment TEXT,
FOREIGN KEY (product_id) REFERENCES products (product_id)
);
--DROP TABLE reviews;

INSERT INTO reviews (rating)
VALUES (6);

INSERT INTO reviews (product_id, rating)
VALUES (50, 5);

CREATE TABLE suppliers (
supplier INTEGER PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
country TEXT  DEFAULT "Sweden",
email TEXT
);

INSERT INTO suppliers(name)
VALUES("volvo");

SELECT * FROM suppliers;

INSERT INTO suppliers(name) 
VALUES("volvo");--Result: UNIQUE constraint failed: suppliers.name

CREATE TABLE coupons (
code TEXT PRIMARY KEY,
discount INTEGER CHECK (discount >= 1 AND discount <= 90),
valid_until TEXT NOT NULL
);

INSERT INTO coupons (code, discount, valid_until)
VALUES ('summer20', 99 , 2026-12-01) -- Result: CHECK constraint failed: discount >= 1 AND discount <= 90

INSERT INTO suppliers (name)
VALUES ('Nordic Textiles') -- gets next available key number

ALTER TABLE suppliers 
RENAME COLUMN email TO contact_email;

PRAGMA table_info(products)

CREATE TABLE product_suppliers(
product_id INTEGER,
supplier_id INTEGER,
price CHECK (price > 0),
PRIMARY KEY (product_id, supplier_id),
FOREIGN KEY (product_id) REFERENCES products(product_id),
FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier)
);

INSERT INTO product_suppliers(product_id, supplier_id, price)
VALUES(1,99, 15);
