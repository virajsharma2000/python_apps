CREATE TABLE members(
member_id int NOT NULL AUTO_INCREMENT,
first_name VARCHAR(255),
last_name VARCHAR(255),
gender VARCHAR(255),
age INT,
description TEXT,
PRIMARY KEY(member_id)
);

CREATE TABLE expenses(
expense_id int NOT NULL AUTO_INCREMENT,
expense_name VARCHAR(255),
expense_description TEXT,
created_datetime datetime,
amount FLOAT,
PRIMARY KEY(expense_id)
);
