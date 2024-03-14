create table users
(
    id INT PRIMARY KEY NOT NULL UNIQUE,
    first_name VARCHAR(255) NOT NULL,
    second_name VARCHAR(255) NOT NULL,
    third_name VARCHAR(255),
    1C_Аптека BOOLEAN,
    1C_Кадры BOOLEAN,
    1С_БГУ_1 BOOLEAN,
    1с_БГУ_2 BOOLEAN,
    1С_Диетпитание BOOLEAN,
    МИС BOOLEAN,
    ТИС BOOLEAN,
    СЭД BOOLEAN,

);

alter table users
    owner to postgres