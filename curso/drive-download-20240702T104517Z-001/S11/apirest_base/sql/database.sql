drop database if exists apirest_base; -- borra DB si existe
create database apirest_base; -- crea DB
use apirest_base; -- selecciona DB

-- crea la tabla "datos"
create table datos(
    id int primary key auto_increment,
    dato varchar(255) not null
);

insert into datos values(default, %s)