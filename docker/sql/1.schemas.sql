DROP SCHEMA IF EXISTS `hackathon`;

CREATE SCHEMA IF NOT EXISTS `hackathon` DEFAULT CHARACTER SET utf8;
USE `hackathon`;

create table categorie
(
    id             int auto_increment,
    categorie_name varchar(255) null,
    constraint theme_id_uindex
        unique (id)
);

create table question
(
    id       int auto_increment
        primary key,
    question varchar(255) null,
    `order`  int          null
);