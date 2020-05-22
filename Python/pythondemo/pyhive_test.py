from pyhive import hive

# conn = hive.Connection(host='49.234.176.188', port=10000, username='hive', password='hive', auth='LDAP', database='default')
# conn = hive.Connection(host='49.234.176.188', port=10000, database='default', auth='NONE')
conn = hive.Connection(host='192.168.1.98', port=10000, database='default', auth='CUSTOM', username='hive', password='hive')
cursor = conn.cursor()
cursor.execute('show database')

for result in cursor.fetchall():
    print(result)

cursor.close()
conn.close()