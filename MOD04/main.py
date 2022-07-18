from sqlalchemy import create_engine
import pandas as pd 

engine = create_engine('postgresql+psycopg2://root:root@localhost/test_db')

sql = '''
select count(1) from billboard b;
'''

df = pd.read_sql_query(sql, engine)

df_cb = pd.read_sql_query('''select song
      ,artist
from billboard b
where artist = 'Chuck Berry';''', engine)


sql = '''insert into tb_artist
(select "date"
      ,"rank"
      ,artist
      ,song
from billboard b
where artist LIKE 'Elvis%%'
order by artist, song, "date");
'''

engine.execute(sql)