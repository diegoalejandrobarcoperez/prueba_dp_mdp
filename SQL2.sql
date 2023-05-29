INSERT INTO punto_2 (desc_clase, num_tj_inac)
SELECT  Cstr(CATALOGO_CLASE.desc_clase) AS desc_clase, CLNG(COUNT(Tarjetas.tjnrotrj)) AS num_tj_inac
FROM CATALOGO_CLASE 
INNER JOIN Tarjetas ON Cstr(CATALOGO_CLASE.clase) = Cstr(Tarjetas.tjclstrj)
WHERE Cstr(Tarjetas.tjesttrj) <> 'ACTIVA' AND Cstr(Tarjetas.tjtpotrj) = 'TARJETA MASTERDEBIT'
GROUP BY Cstr(CATALOGO_CLASE.desc_clase)