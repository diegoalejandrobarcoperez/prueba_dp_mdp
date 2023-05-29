INSERT INTO punto_4 (cuenta_activa, num_tj_activas)
SELECT TOP 10 Cstr(Cuentas.canrocta) AS cuenta_activa, CLNG(COUNT(Tarjetas.tjnrotrj)) AS num_tj_activas
FROM Cuentas
INNER JOIN Tarjetas ON Cstr(Cuentas.canrotrj) = Cstr(Tarjetas.tjnrotrj)
WHERE Cstr(Cuentas.caestcta) = 'ACTIVA' AND Cstr(Tarjetas.tjesttrj) = 'ACTIVA'
GROUP BY Cstr(Cuentas.canrocta)
ORDER BY CLNG(COUNT(Tarjetas.tjnrotrj)) ASC