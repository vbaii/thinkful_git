import sqlite3 as sql

con = sql.connect("getting_started.db")
with con:
    cur = con.cursor()
    query = '''
    select
        c.name cityName
        ,avg(w.average_high) avgHighMean
    from cities c
    left outer join weather w
        on c.name = w.city
    where c.state = 'CA'
    group by c.name
    order by avgHighMean desc
    '''
    cur.execute(query)
    data = cur.fetchall()
    print data
    print '\n'
    for row in data:
        print row

