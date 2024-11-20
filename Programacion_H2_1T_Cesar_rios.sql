DROP DATABASE IF EXISTS HITOPROG2;
CREATE DATABASE HITOPROG2;
USE HITOPROG2;


CREATE TABLE producto (
    idproducto int auto_increment primary key,
    nombre varchar(150),
    medida varchar(100),
    precio int,
    stock int
);

CREATE TABLE cliente (
    idcliente INT auto_increment primary key,
    nombre varchar(100),
    direccion varchar(200),
    tlf int
);


CREATE TABLE pedido (
    idpedido int auto_increment primary key,
    idcliente int,
	fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    foreign key (idcliente) references cliente(idcliente)
);

CREATE TABLE detalle (
	idcliente int,
    idpedido int,
    idproducto int,
    precio float,
    unidades int,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    foreign key (idpedido) references pedido(idpedido),
    foreign key (idproducto) references producto(idproducto),
    foreign key (idcliente) references cliente(idcliente)
);

-- Insertar Productos
INSERT INTO producto (nombre, medida, precio, stock) VALUES
('Pantalón Vaquero', 'M', 25, 40),          -- Producto 1
('Botas de Montaña', '42', 60, 20),         -- Producto 2
('Auriculares Inalámbricos', 'Unidad', 30, 80), -- Producto 3
('Reloj Digital', 'Unidad', 90, 15),        -- Producto 4
('Bolso de Mano', 'Mediano', 50, 25);       -- Producto 5

-- Insertar Clientes
INSERT INTO cliente (nombre, direccion, tlf) VALUES
('Raúl Martínez', 'Av. Primavera 101', 621345789),
('Ana Torres', 'Calle del Sol 56', 634567891),
('David González', 'Plaza Mayor 22', 645678912),
('Clara Fernández', 'Calle Luna 34', 657890123),
('Jorge López', 'Av. España 18', 669012345);

-- Insertar Pedidos
INSERT INTO pedido (idcliente) VALUES
(1), -- Pedido 1 de Raúl Martínez
(2), -- Pedido 2 de Ana Torres
(3), -- Pedido 3 de David González
(4), -- Pedido 4 de Clara Fernández
(5); -- Pedido 5 de Jorge López

-- Insertar Detalles de Pedidos
INSERT INTO detalle (idcliente, idpedido, idproducto, precio, unidades) VALUES
(1, 1, 1, 25, 2),  -- Pedido 1: Raúl Martínez compró 2 pantalones vaqueros
(1, 1, 3, 30, 1),  -- Pedido 1: Raúl Martínez compró 1 auricular inalámbrico
(2, 2, 2, 60, 1),  -- Pedido 2: Ana Torres compró 1 par de botas de montaña
(2, 2, 5, 50, 2),  -- Pedido 2: Ana Torres compró 2 bolsos de mano
(3, 3, 4, 90, 1),  -- Pedido 3: David González compró 1 reloj digital
(4, 4, 1, 25, 3),  -- Pedido 4: Clara Fernández compró 3 pantalones vaqueros
(4, 4, 2, 60, 1),  -- Pedido 4: Clara Fernández compró 1 par de botas de montaña
(5, 5, 5, 50, 1);  -- Pedido 5: Jorge López compró 1 bolso de mano
