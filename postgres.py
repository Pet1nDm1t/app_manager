import psycopg2 as ps

connection = ps.connect(
     host='192.168.11.50',
     user='postgres',
     password='Oktopass_911',
     database='postgres'
)

cursor = connection.cursor()

apps_tb = '''
    CREATE TABLE IF NOT EXISTS apps (
        app_id SERIAL PRIMARY KEY,
        app_name VARCHAR(255) NOT NULL,
        app_url VARCHAR(2048) NOT NULL,
        description VARCHAR(2048) NOT NULL
        
    );
'''

cursor.execute(apps_tb)

_7_zip = ('7-zip', 'https://www.7-zip.org/', '7-Zip — свободный файловый архиватор с высокой степенью сжатия данных.' )

def addapp(app):
    cursor.execute("INSERT INTO apps (app_name, app_url, description) VALUES (%s, %s,%s)", app)

addapp(_7_zip)

connection.commit()


cursor.close()
connection.close()
