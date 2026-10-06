CREATE TABLE books (
bok_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT,
year INTEGER CHECK (year > 0)
)

--DROP TABLE books