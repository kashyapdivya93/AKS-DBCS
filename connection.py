##############################################################################################
# Sample script to connect Oracle Database Cloud Service
#
# 
# Written using SQLAlchemy and cx_Oracle,  https://docs.sqlalchemy.org/en/13/dialects/oracle.html
#
##############################################################################################
import sqlalchemy
import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import base64
import os

#Oracle Database Cloud Service credentials
#documentation https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/connectingDB.htm
username = base64.b64decode(os.environ['username']).decode('utf-8')
password = base64.b64decode(os.environ['password']).decode('utf-8')
ip = base64.b64decode(os.environ['dbhostIP']).decode('utf-8')
service_name = base64.b64decode(os.environ['service_name']).decode('utf-8')
tableName = base64.b64decode(os.environ['table_name']).decode('utf-8')


#Creating Connection sursor
print("\n\nInitiating connection\n\n")
dsn = cx_Oracle.makedsn(ip,'1521',service_name=service_name)
engine = create_engine('oracle+cx_oracle://%s:%s@%s' % (username, password, dsn))
conn = engine.connect()
print("\n\nConnection established\n\n")

DBSession = sessionmaker(bind=engine)
session = DBSession()
print("\n\nSession Strated\n\n")

metadata = sqlalchemy.MetaData() 
table = sqlalchemy.Table(tableName, metadata, autoload=True, autoload_with=engine)
column_keys = table.columns.keys()
print(column_keys)
query = sqlalchemy.select([table])
res = conn.execute(query)
res_set = res.fetchall()
print(res_set)
#session.close()
