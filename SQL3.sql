SELECT Cstr(Clientes.segmento) AS segmento, CLNG(COUNT(Tarjetas.tjnrotrj)) AS num_tj_deb_maes
FROM Clientes
INNER JOIN Tarjetas ON Cstr(Clientes.num_doc) = Cstr(Tarjetas.tjnrodoc)
WHERE  Cstr(Tarjetas.tjtpotrj) = 'TARJETA DEBITO MAESTRO' 
GROUP BY Cstr(Clientes.segmento)