import sys
from PyQt5.QtSql import QSqlDatabase

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

if not con.open():
    print("Unable to connect to the database")
    sys.exit(1)
