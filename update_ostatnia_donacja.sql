CREATE DEFINER=`root`@`localhost` PROCEDURE `update_ostatnia_donacja`(in peselin varchar(11))
BEGIN
	declare don date;
    set don = ostatnia_donacja_update(peselin);
    update darczyncy set ostatnia_donacja = don  where pesel = peselin;
END