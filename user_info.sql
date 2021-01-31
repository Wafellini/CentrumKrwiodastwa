CREATE DEFINER=`root`@`localhost` PROCEDURE `user_info`(in peselin varchar(11))
BEGIN
	select d.*, (select count(*) from donacje where pesel = peselin) as "Liczba donacji" from darczyncy d where d.pesel = peselin;
END