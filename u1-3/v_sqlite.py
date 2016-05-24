import sqlite3 as lite
con = lite.connect('getting_started.db')
'''
with con:
    cur = con.cursor()
    cur.execute('select sqlite_version()')
    data = cur.fetchone()
    print"SQLite version: {0}".format(data)
    print '\n'
    print('SQLite version: %s' % data)
'''
'''
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January',75)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January',80)")
'''

cities = (  ('Las Vegas', 'NV'),
            ('Atlanta', 'GA'))

weather = ( ('Las Vegas', 2013, 'July', 'December', 81),
            ('Atlanta', 2013, 'July', 'January', 77))

with con:
    cur = con.cursor()
    cur.executemany('insert into cities values(?,?)', cities)
    cur.executemany('insert into weather values(?,?,?,?,?)', weather)
