import sqlite3 as lite
import pandas as pd
'''
Write a script called "database.py" to print out the cities with
the July being the warmest month. Your script must:

Connect to the database
Create the cities and weather tables
    (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>;
    to remove the table before you execute the CREATE TABLE ... statement)
Insert data into the two tables
Join the data together
Load into a pandas DataFrame
Print out the resulting city and state in a full sentence.
For example: "The cities that are warmest in July are:
    Las Vegas, NV, Atlanta, GA..."
'''


con = lite.connect("challenge.db")

with con:
    cur = con.cursor()
    create_fixed = 'create table '
    insert_fixed = 'insert into '
    table_cities = 'cities (name text, state text);'
    table_weather = """weather (city text,
                                year integer,
                                warm_month text,
                                cold_month text,
                                average_high integer);"""
    insert_cities = """
        cities (name, state) VALUES 
            ('New York City', 'NY'),
            ('Boston', 'MA'),
            ('Chicago', 'IL'),
            ('Miami', 'FL'),
            ('Dallas', 'TX'),
            ('Seattle', 'WA'),
            ('Portland', 'OR'),
            ('San Francisco', 'CA'),
            ('Los Angeles', 'CA')
            ;
            """
    insert_weather = """weather (city,year,warm_month,cold_month,average_high)
    VALUES 
    ('New York City'   ,2013    ,'July'        ,'January'     ,62),
    ('Boston'          ,2013    ,'July'        ,'January'     ,59),
    ('Chicago'         ,2013    ,'July'        ,'January'     ,59),
    ('Miami'           ,2013    ,'August'      ,'January'     ,84),
    ('Dallas'          ,2013    ,'July'        ,'January'     ,77),
    ('Seattle'         ,2013    ,'July'        ,'January'     ,61),
    ('Portland'        ,2013    ,'July'        ,'December'    ,63),
    ('San Francisco'   ,2013    ,'September'   ,'December'    ,64),
    ('Los Angeles'     ,2013    ,'September'   ,'December'    ,75);
    """
    
    create_cities = create_fixed + table_cities
    create_weather = create_fixed + table_weather
    insert_cities_values = insert_fixed + insert_cities
    insert_weather_values = insert_fixed + insert_weather

    cur.execute('DROP TABLE IF EXISTS cities;')
    cur.execute('DROP TABLE IF EXISTS weather;')

    cur.execute(create_cities)
    cur.execute(create_weather)
    cur.execute(insert_cities_values)
    cur.execute(insert_weather_values)


with con:
    join_query = """
        select
            c.name || ',' || c.state cityState
            ,w.warm_month
        from cities c
        left outer join weather w
            on c.name = w.city
        where w.warm_month = 'July'; """
    # cur = con.cursor()
    # cur.execute(join_query)
    # data = cur.fetchall()
    # print data
    panded = pd.read_sql(join_query, con)


sent = ['The cities that are the warmest in July are: ']
for item in panded['cityState']:
    sent.append(item)
print sent[0] + ','.join(sent[1:])
