# Taller 3 BDNR - Dashboard Analítico con Apache Doris

Proyecto desarrollado para el Taller 3 de Bases de Datos No Relacionales.

El sistema implementa un dashboard analítico de compras masivas utilizando Apache Doris como motor OLAP columnar, FastAPI como backend, React como frontend y Docker para levantar los servicios.

El objetivo principal es analizar un volumen masivo de datos de compras mediante KPIs, gráficos y filtros dinámicos.

---

## Tecnologías utilizadas

- Apache Doris
- FastAPI
- React
- Docker / Docker Compose
- Stream Load para carga de datos
- MySQL client para conexión con Doris

---

## Estructura del proyecto

```txt
taller3-analitica-compras/
├── backend/
├── frontend/
├── database/
│   └── init.sql
├── data/
│   └── compras.csv   # No incluido en GitHub por tamaño
├── docker-compose-doris.yaml
├── docker-compose-app.yml
├── start-doris.sh
└── README.md
```

---

## Importante sobre el archivo CSV

El archivo `compras.csv` no está incluido en el repositorio.

Debe descargarse aparte y colocarse manualmente en:

```txt
data/compras.csv
```

---

## Archivo `.env`

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
BACKEND_PORT=8000
FRONTEND_PORT=5173

DORIS_HOST=172.17.0.1
DORIS_PORT=9030
DORIS_USER=root
DORIS_PASSWORD=
DORIS_DATABASE=taller3_analitica
```

---

## Levantar Apache Doris

Desde la raíz del proyecto:

```bash
docker compose -f docker-compose-doris.yaml up -d
```

Esperar unos segundos y verificar que los contenedores estén activos:

```bash
docker ps
```

Deben aparecer contenedores similares a:

```txt
taller3-analitica-compras-fe-1
taller3-analitica-compras-be-1
```

---

## Crear base de datos y tabla

Copiar el script SQL al contenedor FE de Doris:

```bash
docker cp ./database/init.sql taller3-analitica-compras-fe-1:/tmp/init.sql
```

Ejecutar el script dentro del contenedor:

```bash
docker exec -it taller3-analitica-compras-fe-1 bash -lc "mysql -h127.0.0.1 -P9030 -uroot < /tmp/init.sql"
```

Verificar que la base fue creada:

```bash
docker exec -it taller3-analitica-compras-fe-1 bash -lc "mysql -h127.0.0.1 -P9030 -uroot -e 'SHOW DATABASES;'"
```

Debe aparecer:

```txt
taller3_analitica
```

Verificar que la tabla existe:

```bash
docker exec -it taller3-analitica-compras-fe-1 bash -lc "mysql -h127.0.0.1 -P9030 -uroot -e 'USE taller3_analitica; SHOW TABLES;'"
```

Debe aparecer:

```txt
compras
```

---

## Cargar el archivo CSV en Doris

Primero asegurarse de que el archivo exista en:

```txt
data/compras.csv
```

Luego copiar el CSV al contenedor FE:

```bash
docker cp ./data/compras.csv taller3-analitica-compras-fe-1:/tmp/compras.csv
```

Ejecutar Stream Load:

```bash
docker exec -it taller3-analitica-compras-fe-1 bash -lc 'curl --location-trusted -u root: \
  -H "label: compras_load_$(date +%s)" \
  -H "format: csv" \
  -H "column_separator: ," \
  -H "skip_lines: 1" \
  -H "columns: usuarioid,edad,ciudad,producto,categoria,precio,fecha,hora,metodopago" \
  -T /tmp/compras.csv \
  http://127.0.0.1:8030/api/taller3_analitica/compras/_stream_load'
```

Debe responder con:

```txt
"Status": "Success"
```

---

## Verificar cantidad de registros

```bash
docker exec -it taller3-analitica-compras-fe-1 bash -lc "mysql -h127.0.0.1 -P9030 -uroot -e 'USE taller3_analitica; SELECT COUNT(*) AS total FROM compras;'"
```

Resultado esperado:

```txt
5000000
```

---

## Levantar backend y frontend

Desde la raíz del proyecto:

```bash
docker compose -f docker-compose-app.yml up --build
```

---

## Acceso al sistema

Frontend:

```txt
http://localhost:5173/
```

Backend:

```txt
http://localhost:8000/api/dashboard/resumen
```
