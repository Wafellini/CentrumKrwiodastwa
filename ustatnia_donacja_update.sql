CREATE DEFINER=`root`@`localhost` FUNCTION `ostatnia_donacja_update`(peselin int) RETURNS date
    READS SQL DATA
BEGIN

	DECLARE done INT DEFAULT FALSE;
	declare osd_don date;
    declare date_it date;
    DECLARE cur1 CURSOR FOR select datta from donacje where pesel = peselin;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    open cur1;
    
    select ostatnia_donacja from darczyncy where pesel = peselin into osd_don;
    
	read_loop: LOOP
		FETCH cur1 INTO date_it;
        IF done THEN
			LEAVE read_loop;
		END IF;
		IF date_it > osd_don THEN
			set osd_don = date_it;
		END IF;
	END LOOP;
    
    close cur1;
    
RETURN osd_don;
END