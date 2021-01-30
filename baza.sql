create table Placowki(
	id_plac int(6) primary key AUTO_INCREMENT,
	adres varchar(50) not null);

create table Laboratoria(
	id_lab int(6) primary key AUTO_INCREMENT,
	adres varchar(50) not null);

--tu
create table Bilansy_Krwi(
	typ_krwi varchar(2) not null,
	ilosc int(10) not null,
	id_plac int(6) not null references Placowki(id_plac),
	foreign key (id_plac) references Placowki(id_plac),
	primary key(id_plac));

--tu
create table Magazyny_kompensacji(
	nazwa varchar(50),
	ilosc int(10) not null,
	id_plac int(6) not null references Placowki(id_plac),
	foreign key (id_plac) references Placowki(id_plac),
	primary key(nazwa, id_plac));
	
--tu
create table Badania_krwi(
	datta date not null,
	wynik varchar(50) not null,
	id_bad int(6) AUTO_INCREMENT,
	id_lab int(6) not null references Laboratoria(id_lab),
	foreign key (id_bad) references Badania_krwi(id_bad),
	primary key(id_bad, id_lab));
	
    
create table Darczyncy(
	pesel int(11) primary key,
	imie varchar(50) not null,
	nazwisko varchar(50) not null,
	typ_krwi varchar(2) not null,
	ostatnia_donacja date null);
	
--tu
create table Kwalifikacje(
	id_kwal int(6) primary key AUTO_INCREMENT,
	datta date not null,
	wynik varchar(50) not null,
	pesel int(11) not null references Darczyncy(pesel)),
	foreign key (pesel) references Darczyncy(pesel);

--tu
create table Donacje(
	datta date,
	ilosc int(6) not null,
	id_bad int(6) not null references Badania_krwi(id_bad),
	id_kwal int(6) not null references Kwalifikacje(id_kwal),
	pesel int(11) not null references Darczyncy(pesel),
	foreign key (id_bad) references Badania_krwi(id_bad),
	foreign key (id_kwal) references Kwalifikacje(id_kwal),
	foreign key (pesel) references Darczyncy(pesel),
	primary key(datta, pesel));


--tu
create table Wydania_kompensacji(
	ilosc int(6) not null,
	datta date,
	pesel int(11) not null references Darczyncy(pesel),
	nazwa varchar(50) not null references Magazyny_kompensacji(nazwa),
	foreign key (pesel) references Darczyncy(pesel),
	foreign key (nazwa) references Magazyny_kompensacji(nazwa),
	primary key(datta, pesel, nazwa));

--tu
create table Pracownicy_plac(
	imie varchar(50) not null,
	id_prac int(6) AUTO_INCREMENT,
	nazwisko varchar(50) not null,
	stanowisko varchar(50) not null,
	id_plac int(6) not null references Placowki(id_plac),
	foreign key (id_plac) references Placowki(id_plac),
	primary key(id_prac, id_plac));

--tu
create table Pracownicy_lab(
	imie varchar(50) not null,
	id_prac int(6) AUTO_INCREMENT,
	nazwisko varchar(50) not null,
	stanowisko varchar(50) not null,
	id_lab int(6) not null references Laboratoria(id_lab),
	foreign key (id_lab) references Laboratoria(id_lab),
	primary key(id_prac, id_lab));