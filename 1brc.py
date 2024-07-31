import duckdb
from sys import argv


with duckdb.connect() as conn:
    data = conn.sql(
        f"""
        SELECT
            station_name,
            MIN(measurement) AS min_measurement,
            ROUND(AVG(measurement), 1) AS avg_measurement,
            MAX(measurement) AS max_measurement
        FROM
            READ_CSV(
                '{argv[1]}',
                columns = {{
                    'station_name': 'VARCHAR',
                    'measurement': 'DOUBLE'
                }}
            )
        GROUP BY
            station_name
        """
    )
    print('{', end='')
    for row in sorted(data.fetchall()):
        print(f'{row[0]}={row[1]}/{row[2]}/{row[3]}', end='')
    print('}', end='')
