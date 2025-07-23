DELIMITER //

CREATE TRIGGER pagar_creditos_trigger
AFTER INSERT ON PagoCreditos
FOR EACH ROW
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE factura_id INT;
    DECLARE factura_saldo FLOAT;
    DECLARE pago_restante FLOAT;
    
    DECLARE cur CURSOR FOR
        SELECT id, saldo
        FROM Factura
        WHERE Cliente_id = NEW.Cliente_id
            AND credito = 1
            AND anulada = 0
            AND saldo > 0
        ORDER BY fecha ASC;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET pago_restante = NEW.total;

    OPEN cur;
    factura_loop: LOOP
        FETCH cur INTO factura_id, factura_saldo;
        IF done THEN
            LEAVE factura_loop;
        END IF;

        IF pago_restante <= 0 THEN
            LEAVE factura_loop;
        END IF;

        IF pago_restante >= factura_saldo THEN
            INSERT INTO detallepago (monto, Factura_id, PagoCreditos_id)
            VALUES (factura_saldo, factura_id, NEW.id);

            UPDATE Factura SET saldo = 0 WHERE id = factura_id;

            SET pago_restante = pago_restante - factura_saldo;
        ELSE
            INSERT INTO detallepago (monto, Factura_id, PagoCreditos_id)
            VALUES (pago_restante, factura_id, NEW.id);

            UPDATE Factura SET saldo = saldo - pago_restante WHERE id = factura_id;

            SET pago_restante = 0;
        END IF;
    END LOOP;
    CLOSE cur;

    UPDATE Cliente SET saldo = saldo - NEW.total
    WHERE id = NEW.Cliente_id;

END//

DELIMITER ;

INSERT INTO Cliente (id, nombre, nit, direccion, saldo)
VALUES (1, 'Juan Pérez', '1234567-8', 'Zona 1', 1500);


INSERT INTO Factura (id, fecha, total, credito, impresa, saldo, anulada, Cliente_id)
VALUES 
(1, NOW() - INTERVAL 10 DAY, 500, 1, 1, 500, 0, 1),
(2, NOW() - INTERVAL 5 DAY, 600, 1, 1, 600, 0, 1),
(3, NOW() - INTERVAL 2 DAY, 700, 1, 1, 700, 0, 1);

INSERT INTO PagoCreditos (id, fechacha, total, Cliente_id)
VALUES (2, NOW(), 200, 1);

SELECT * FROM factura;
