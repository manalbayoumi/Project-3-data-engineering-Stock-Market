create table stock
(
    Stock_id int, 
    Stock_name varchar(20) not null,
    Ticker varchar(10) not null,
    primary key (Stock_id)
);

create table Apple_price
    (
        date timestamp,
        stock_id varchar(10),
        Open real not null, 
        High real not null, 
        Low real not null, 
        Close real not null, 
        Month int not null,
        normalization real not null,
        Percentage_change real, 
        accumulation real,
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(Stock_id) references stock(Ticker)
    );

    create table Google_price
    (
        date timestamp,
        stock_id varchar(10),
        Open real not null, 
        High real not null, 
        Low real not null, 
        Close real not null, 
        Month int not null,
        normalization real not null,
        Percentage_change real, 
        accumulation real,
        primary key (date, stock_id),
        constraint fk_stock
            foreign key(stock_id) references stock(Ticker)
    );

    create table Intel_price
    (
        date timestamp,
        stock_id varchar(10),
        Open real not null, 
        High real not null, 
        Low real not null, 
        Close real not null, 
        Month int not null,
        normalization real not null,
        Percentage_change real, 
        accumulation real,
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references stock(Ticker)
    );

    create table Microsoft_price
    (
        date timestamp,
        stock_id varchar(10),
        Open real not null, 
        High real not null, 
        Low real not null, 
        Close real not null, 
        Month int not null,
        normalization real not null,
        Percentage_change real, 
        accumulation real,
        primary key (date, stock_id),
        constraint fk_stock
       foreign key(stock_id) references stock(Ticker)
    );

    create table Oracle_price
    (
        date timestamp,
        stock_id varchar(10),
        Open real not null, 
        High real not null, 
        Low real not null, 
        Close real not null, 
        Month int not null,
        normalization real not null,
        Percentage_change real, 
        accumulation real,
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references stock(Ticker)
    );

    create table Apple_volume
    (
        date timestamp,
        stock_id varchar(10),
        Adj_Close real not null, 
        Volume int not null, 
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references Apple_volume (stock_id),
        foreign key(date) references Apple_volume (date)
    );

    create table Google_volume
    (
        date timestamp,
        stock_id varchar(10),
        Adj_Close real not null, 
        Volume int not null, 
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references Google_volume (stock_id),
        foreign key(date) references Google_volume (date)
    );

    create table Microsoft_volume
    (
        date timestamp,
        stock_id varchar(10),
        Adj_Close real not null, 
        Volume int not null, 
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references Microsoft_volume (stock_id),
        foreign key(date) references Microsoft_volume (date)
    );

    create table Intel_volume
    (
        date timestamp,
        stock_id varchar(10),
        Adj_Close real not null, 
        Volume int not null, 
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references Intel_volume (stock_id),
        foreign key(date) references Intel_volume (date)
    );

    create table Oracle_volume
    (
        date timestamp,
        stock_id varchar(10),
        Adj_Close real not null, 
        Volume int not null, 
        primary key (date, stock_id),
        constraint fk_stock
        foreign key(stock_id) references Oracle_volume (stock_id),
        foreign key(date) references Oracle_volume (date)
    );
  