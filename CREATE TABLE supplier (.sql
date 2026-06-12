CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO SUPPLIER (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Alex', 20, 'London'),
('S2', 'Belal', 40, 'Dhaka'),
('S3', 'Eles', 10, 'Rajshahi'),
('S4', 'Badhon', 20, 'Naogan'),
('S5', 'Emon', 30, 'Paris');

SELECT * FROM supplier;