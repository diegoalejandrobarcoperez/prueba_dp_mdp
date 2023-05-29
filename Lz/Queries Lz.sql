-- Cantidad de tarjetas activas de tarjeta débito por clase de tarjeta.
SELECT Cast(CATALOGO_CLASE.desc_clase as string) AS desc_clase, Cast(COUNT(distinct Tarjetas.tjnrotrj) as BIGINT) AS num_tj_acti
FROM proceso_clientes.DP2_CATALOGO_CLASE  as CATALOGO_CLASE
INNER JOIN proceso_clientes.DP2_Tarjetas as Tarjetas 
ON Cast(CATALOGO_CLASE.clase as string) = Cast(Tarjetas.tjclstrj as string)
WHERE Cast(Tarjetas.tjesttrj as string) = 'ACTIVA'
GROUP BY Cast(CATALOGO_CLASE.desc_clase as string)
;
-- Cantidad de tarjetas inactivas de MasterDebit por descripción de clase de tarjeta.
SELECT  Cast(CATALOGO_CLASE.desc_clase as string) AS desc_clase, Cast(COUNT(distinct Tarjetas.tjnrotrj) as bigint) AS num_tj_inac
FROM proceso_clientes.DP2_CATALOGO_CLASE  as CATALOGO_CLASE
INNER JOIN proceso_clientes.DP2_Tarjetas as Tarjetas
ON  Cast(CATALOGO_CLASE.clase as string) = Cast(Tarjetas.tjclstrj as string)
WHERE Cast(Tarjetas.tjesttrj as string) <> 'ACTIVA' AND Cast(Tarjetas.tjtpotrj as string) = 'TARJETA MASTERDEBIT'
GROUP BY Cast(CATALOGO_CLASE.desc_clase as string)
;
-- Cantidad de tarjetas débito maestro por segmento de clientes.
SELECT Cast(Clientes.segmento as string) AS segmento, Cast(COUNT(distinct Tarjetas.tjnrotrj)as bigint) AS num_tj_deb_maes
FROM proceso_clientes.DP2_Clientes as Clientes
INNER JOIN proceso_clientes.DP2_Tarjetas as Tarjetas
ON Cast(Clientes.num_doc as string) = Cast(Tarjetas.tjnrodoc as string)
WHERE  Cast(Tarjetas.tjtpotrj as string) = 'TARJETA DEBITO MAESTRO' 
GROUP BY Cast(Clientes.segmento as string)
;
-- Las 10 cuentas activas con mayor cantidad de tarjetas activas asociadas organizado de menor a mayor.
SELECT  Cast(Cuentas.canrocta as string) AS cuenta_activa, Cast(COUNT(distinct Tarjetas.tjnrotrj) as bigint) AS num_tj_activas
FROM proceso_clientes.DP2_Cuentas as Cuentas
INNER JOIN proceso_clientes.DP2_Tarjetas as Tarjetas 
ON Cast(Cuentas.canrotrj as string) = Cast(Tarjetas.tjnrotrj as string)
WHERE Cast(Cuentas.caestcta as string) = 'ACTIVA' AND Cast(Tarjetas.tjesttrj as string) = 'ACTIVA'
GROUP BY Cast(Cuentas.canrocta as string)
ORDER BY Cast(COUNT(distinct Tarjetas.tjnrotrj) as bigint) desc
LIMIT 10
;
-- Cantidad de plásticos activos por cada tipo de tarjeta del portafolio de débito
SELECT  Cast(tjtpotrj as string) AS portafolio, Cast(COUNT(distinct tjnrotrj) as bigint) AS num_tj_activas
FROM proceso_clientes.DP2_Tarjetas as Tarjetas
WHERE  Cast(tjesttrj as string) = 'ACTIVA'
GROUP BY Cast(tjtpotrj as string)