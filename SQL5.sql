INSERT INTO punto_5 (portafolio, num_tj_activas)
SELECT  Cstr(tjtpotrj) AS portafolio, CLNG(COUNT(tjnrotrj)) AS num_tj_activas
FROM Tarjetas
WHERE  Cstr(tjesttrj) = 'ACTIVA'
GROUP BY Cstr(tjtpotrj)