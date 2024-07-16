drop database if exists app;
create database app;
use app;

create table usuarios(
    dni varchar(9) not null primary key,
    nombre varchar(255), 
    direccion varchar(255),
    email varchar(255), 
    password varchar(255)
);

create table perros(
    chip char(25) not null primary key,
    nombre varchar(255), 
    raza varchar(255), 
    genero varchar(10)
);

create table registro_perros(
    id int primary key auto_increment,
    dni_usuario char(9) not null,
    chip_perro char(25) not null unique,
    fecha_cita date not null,
    foreign key (dni_usuario) references usuarios(dni),
    foreign key (chip_perro) references perros(chip)
);

