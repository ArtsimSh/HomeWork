create table categories(
    id smallserial primary key,
    parent_id  smallint,
    is_published boolean default(false),
    name_en varchar(20) unique not null,
    foreign key (parent_id) references categories(id) on delete cascade);

create table products(
    id serial primary key,
    category_id smallint not null,
    price float,
    media text,
    total float,
    is_published boolean default(false),
    name_en varchar(20) unique not null,
    name varchar(20) unique not null,
    foreign key (category_id) references categories(id) on update cascade);

create table languages(
    id serial primary key,
    languages_code char(2) not null);

create table languages(
    id serial primary key,
    name varchar(20) unique not null);

create table users(
    id serial primary key,
    is_blocked boolean default(false),
    balance float,
    languages_id smallint not null,
    foreign key (language_id) references languages(id) on delete cascade);

create table invoices(
    id serial primary key,
    user_id smallint not null,
    date_create text,
    total float not null,
    status_id smallint not null,
    foreign key (user_id) references users(id) on delete cascade,
    foreign key (status_id) references statuses(id) on delete cascade);

create table invoices(
    id serial primary key,
    user_id smallint not null,
    date_create text,
    invoice_id smallint not null,
    status_id smallint not null,
    foreign key (user_id) references users(id) on delete cascade,
    foreign key (status_id) references statuses(id) on delete cascade);
    foreign key (invoice_id) references invoices(id) on delete cascade);

create table order_items(
    id serial primary key,
    order_id smallint not null,
    product_id smallint not null,
    total float,
    foreign key (order_id) references orders(id) on delete cascade);
    foreign key (product_id) references products(id) on delete cascade);
