CREATE TABLE types_of_charging (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    name varchar(32)
);

CREATE TABLE companies (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    name varchar(32)
);

CREATE TABLE charging_points (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    adress varchar(132),
    types_of_charging int,
FOREIGN KEY (types_of_charging)
REFERENCES types_of_charging (id),
    coordinates varchar(132),
    numbers_of_places int,
    avalible_count int,
    cost int,
    company_of_charging_point int,
FOREIGN KEY (company_of_charging_point)
REFERENCES companies (id)
);