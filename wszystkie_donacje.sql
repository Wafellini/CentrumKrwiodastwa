CREATE DEFINER=`root`@`localhost` PROCEDURE `wszytkie_donacje`(in peselin int)
BEGIN
	select k.wynik as "wynik testu", don.ilosc as "oddane mililitry" , don.datta as "data donacji",  w.ilosc as "liczba czekolad"
    from darczyncy d, wydania_kompensacji w, donacje don, kwalifikacje k
    where d.pesel = peselin and w.pesel = peselin and don.pesel = peselin and w.pesel = peselin and don.datta = w.datta and k.datta = w.datta;
    
    
END