drop database if exists app;
create database app;
use app;

create table usuarios(
    dni char(9) not null primary key,
    nombre varchar(255), 
    email varchar(255), 
    password varchar(255)
);

create table libros(
    isbn char(13) not null primary key,
    titulo varchar(255), 
    autor varchar(255), 
    genero varchar(255)
);

create table prestamos(
    id int not null primary key auto_increment,
    dni_usuario char(9) not null,
    isbn_libro char(13) not null,
    fecha_prestamo date not null,
    foreign key (dni_usuario) references usuarios(dni),
    foreign key (isbn_libro) references libros(isbn)
);