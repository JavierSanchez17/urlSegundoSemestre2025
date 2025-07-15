# Cursores

delimiter //
DROP TRIGGER IF EXISTS Anular //

CREATE TRIGGER Anular
AFTER UPDATE ON Venta
FOR EACH ROW
BEGIN
DECLARE vMenu
DECLARE vVenta INTENGER DEFAULT 0;
DECLARE CONT INSERT DEFAULT 0;
DECLARE CursorDetalles CURSOS FOR SELECT venta_id, menu_id FROM detalle_venta where venta_id = New.id;
DECLAINCONTINUE HANDLER FOR SQLSTATE " 0x2000" SET CONT = 1;

OPEN CursorDetalles;

FETCH CursorDetalles INTO vVenta, VMenu; 

WHILE NOT CONT DO
	UPDATE detalle_venta SET cantidad=0, subtotal=0 WHERE venta_id=vVenta AND menu_id= vMenu;
	FETCH CursorDetalles INTO vVenta; 
END WHILE;

END;
delimiter;