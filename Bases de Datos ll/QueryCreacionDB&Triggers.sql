CREATE DATABASE IF NOT EXISTS sistema_proyectos;
USE sistema_proyectos;

CREATE TABLE Encargado (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(45) NOT NULL,
    Direccion VARCHAR(45),
    DPI VARCHAR(45) UNIQUE
);

CREATE TABLE Proyecto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(45) NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFin DATE,
    Presupuesto FLOAT,
    finalizado BOOLEAN DEFAULT FALSE,
    Encargado_id INT,
    FOREIGN KEY (Encargado_id) REFERENCES Encargado(id)
);

CREATE TABLE FamiliaBeneficiada (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Direccion VARCHAR(45),
    IngresoMensual FLOAT,
    Proyecto_id INT,
    FOREIGN KEY (Proyecto_id) REFERENCES Proyecto(id)
);

CREATE TABLE Integrante (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(45) NOT NULL,
    Apellido VARCHAR(45) NOT NULL,
    Edad FLOAT,
    FamiliaBeneficiada_id INT,
    FOREIGN KEY (FamiliaBeneficiada_id) REFERENCES FamiliaBeneficiada(id)
);

CREATE TABLE Servicios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Servicio VARCHAR(45) NOT NULL,
    Precio FLOAT NOT NULL,
    cantidad FLOAT DEFAULT 0
);

CREATE TABLE DetalleProyecto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cantidad FLOAT NOT NULL,
    subtotal FLOAT NOT NULL,
    Proyecto_id INT,
    Servicios_id INT,
    FOREIGN KEY (Proyecto_id) REFERENCES Proyecto(id),
    FOREIGN KEY (Servicios_id) REFERENCES Servicios(id)
);

DELIMITER //
CREATE TRIGGER proyecto_finalizado_trigger
AFTER UPDATE ON Proyecto
FOR EACH ROW
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE servicio_id INT;
    DECLARE cur_cantidad FLOAT;
    DECLARE cur_subtotal FLOAT;
    
    DECLARE detalle_cursor CURSOR FOR 
        SELECT Servicios_id, cantidad, subtotal 
        FROM DetalleProyecto 
        WHERE Proyecto_id = NEW.id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    IF NEW.finalizado = TRUE AND OLD.finalizado = FALSE THEN
        OPEN detalle_cursor;
        
        detalle_loop: LOOP
            FETCH detalle_cursor INTO servicio_id, cur_cantidad, cur_subtotal;
            IF done THEN
                LEAVE detalle_loop;
            END IF;
            
            UPDATE DetalleProyecto SET cantidad = 0 WHERE Proyecto_id = NEW.id AND Servicios_id = servicio_id;
            UPDATE Servicios SET cantidad = cantidad + 1 WHERE id = servicio_id;
        END LOOP;
        
        CLOSE detalle_cursor;
    END IF;
END//
DELIMITER ;


DELIMITER //
CREATE TRIGGER eliminar_beneficiarios_trigger
AFTER UPDATE ON Proyecto
FOR EACH ROW
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE familia_id INT;
    
    DECLARE familia_cursor CURSOR FOR 
        SELECT id FROM FamiliaBeneficiada WHERE Proyecto_id = NEW.id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    IF NEW.finalizado = TRUE AND OLD.finalizado = FALSE THEN
        OPEN familia_cursor;
        
        familia_loop: LOOP
            FETCH familia_cursor INTO familia_id;
            IF done THEN
                LEAVE familia_loop;
            END IF;
            
            DELETE FROM Integrante WHERE FamiliaBeneficiada_id = familia_id;
            DELETE FROM FamiliaBeneficiada WHERE id = familia_id;
        END LOOP;
        
        CLOSE familia_cursor;
    END IF;
END//
DELIMITER ;