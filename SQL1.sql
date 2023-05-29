INSERT INTO punto_1 (desc_clase, num_tj_acti)
SELECT Cstr(CATALOGO_CLASE.desc_clase) AS desc_clase, CLNG(COUNT(Tarjetas.tjnrotrj)) AS num_tj_acti
FROM CATALOGO_CLASE 
INNER JOIN Tarjetas ON Cstr(CATALOGO_CLASE.clase) = Cstr(Tarjetas.tjclstrj)
WHERE Cstr(Tarjetas.tjesttrj) = 'ACTIVA'
GROUP BY Cstr(CATALOGO_CLASE.desc_clase)