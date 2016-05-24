import sqlite3 as lite
import pandas as pd
con = lite.connect('getting_started.db')
'''
with con:
    cur = con.cursor()
    cur.execute('select * from cities')

    rows = cur.fetchall()
    
    for row in rows:
        print row
'''

with con:
    cur = con.cursor()
    cur.execute('select * from cities')

    rows = cur.fetchall()
    '''
    cur.description attribute, which is a read-only attribute that
    contains 7 tuples:
        name
        type_code
        display_size
        internal_size
        precision
        scale
        null_okay
    '''
    cols = [desc[0] for desc in cur.description]
    
    df = pd.DataFrame(rows, columns=cols)
