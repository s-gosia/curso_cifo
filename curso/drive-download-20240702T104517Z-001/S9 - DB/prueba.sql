drop database if exists prueba;
create database prueba;
use prueba;

create table mis_datos(
    id int primary key auto_increment,
    dato varchar(255)
);