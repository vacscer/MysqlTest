# ¿Que incluye la carpeta?

    - docker-compose.yml:
        - Ejecutar con docker compose up. Generará la base de datos de Mysql para crear la base de datos. Es necesario contar con docker instalado.

    - work.ipynb
        - Requirements:
            - CUSTOMER.CSV
            - ZIPCODES.csv
            - Contracts.csv
        - Archivo encargado de generar tres archivos, requeridos para llenar y crear las tablas en la base de datos.
            - Outputs:
                - LOAN_DATA.csv
                - customer_data.csv
                - PAYMENT_DATA.csv

    - insert.py
        - Se conecta y genera las tablas en la base de datos, además de insertar la información de los csv's.

    - queries.ipynb
        - Notebook con las queries de los ejercicios solicitados.
        
    - asks.py
        - Notebook con las respuestas a todas las preguntas solicitadas.

# ¿Como probar?
- Ejecutar docker compose up
- Ejecutar celdas de work.ipynb
- Ejecutar python inert.py
- Ejecutar las celdas en queries.ipynb

            
    
    