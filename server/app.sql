
CREATE TABLE user_data (
id int NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id),
number_user int,
full_name_user VARCHAR(64),
password varchar(14),
number_of_the_car varchar(6),
the_model_of_car varchar(14)
);

CREATE TABLE name_of_cars (
id int NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id),
brand_of_cars varchar(15),
machine_model varchar(15),
numbers int,
nambers_VIN varchar(16),
car_charging_speed int,
engine_power int,
charging_type varchar(10)
);

CREATE TABLE documents_table (
id int NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id),
documents_name varchar(10)
); 

