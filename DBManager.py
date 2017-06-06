# dbmanager

# import things for database and system
from Tkinter import *
from ttk import *
from ScrolledText import *
import tkMessageBox
import psycopg2

from datetime import datetime
time = str(datetime.now())

filename = 'var/log/dbmanager.log'

# db functions
def writeTarget(string):
    target = open(filename, 'a')
    target.write(time+": "+string+"\n")
    target.close()

def rollback():
    cur.execute("rollback")
    string = "Something went wrong. ROLLBACK."
    writeTarget(string)

def askQuestion(param):
    if param == "table":
        val = tkMessageBox.askyesno(
            "Tabelle",
            "Tabelle wirklich loeschen?")
        if val == True:
            dropTable()
    elif param == "mxntable":
        val = tkMessageBox.askyesno(
            "MxN-Tabelle",
            "MxN-Tabelle wirklich loeschen?")
        if val == True:
            dropMxNTable()
    elif param == "column":
        val = tkMessageBox.askyesno(
            "Spalte",
            "Spalte wirklich loeschen?")
        if val == True:
            dropColumn()
    elif param == "foreignkey":
        val = tkMessageBox.askyesno(
            "Fremdschluessel",
            "Fremdschluessel wirklich loeschen?")
        if val == True:
            dropForeignKey()
    elif param == "content":
        val = tkMessageBox.askyesno(
            "Inhalt",
            "Inhalt wirklich loeschen?")
        if val == True:
            delete()
        tkMessageBox.showinfo(
            "HINWEIS",
            "Nicht vergessen die Sequenz zurueckzusetzen")
    else:
        string = "Kann Objekt nicht finden"
        writeTarget(string)

def showDatabases():
    try:
        cur.execute("begin")
        getDatabases = cur.execute(
            "select datname from pg_database where datistemplate is False")
        databases = cur.fetchall()
        cur.execute("commit")
        infoField = textFieldInfo.get(1.0, 'end-1c')
        if infoField == "":
            for x in databases:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        else:
            textFieldInfo.delete(1.0, END)
            for x in databases:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
    except:
        rollback()

def showUsers():
    try:
        cur.execute("begin")
        getUsernames = cur.execute("select usename from pg_user")
        users = cur.fetchall()
        cur.execute("commit")
        infoField = textFieldInfo.get(1.0, 'end-1c')
        if infoField == "":
            for x in users:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        else:
            textFieldInfo.delete(1.0, END)
            for x in users:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
    except:
        rollback()

def showTables():
    databasename = tab1DBName.get()
    user = tab1UserName.get()
    infoField = textFieldInfo.get(1.0, 'end-1c')
    try:
        cur.execute("begin")
        getTablenames = cur.execute(
            "select tablename from pg_tables where pg_tables.tableowner like '%"
            +user+"'")
        tables = cur.fetchall()
        cur.execute("commit")
        if infoField == "":
            for x in tables:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        else:
            textFieldInfo.delete(1.0, END)
            for x in tables:
                x = x[0] + str("\n")
                textFieldInfo.insert(END, x)
    except:
        rollback()

def showColumns():
    # idea to check
    # set default (input field is empty) as true
    # if one of the tablenames is filled set is as false
    tablename2 = tab2TableName.get()
    tablename4 = tab4TableName.get()
    tablename5 = tab5TableName.get()
    tablename6 = tab6TableName.get()
    tablename = tab7TableName.get()
    infoField = textFieldInfo.get(1.0, 'end-1c')
    if infoField != "" and tablename == "Tabellenname":
        textFieldInfo.delete(1.0, END)
        textFieldInfo.insert(END, "Enter table name first")
    elif infoField == "Enter table name first" or (tablename != "" or tablename != "Tabellenname"):
        textFieldInfo.delete(1.0, END)
        try:
            cur.execute("begin")
            getTablenames = cur.execute(
                "select column_name from information_schema.columns where table_name like '"
                +tablename+"'")
            columns = cur.fetchall()
            cur.execute("commit")
            for x in columns:
                x = x[0]+str("\n")
                textFieldInfo.insert(END, x)
        except:
            rollback()
    else:
        rollback()

# GUI
root = Tk()
root.title("DBManager")
root.minsize(
    width=900,
    height=400
)
root.maxsize(
    width=900,
    height=400
)
root.resizable(
    width=True,
    height=True
)
note = Notebook(root)
note2 = Notebook(root)

# import logic
#execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/DBLogik.py') # no function anymore
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab1Datenbank.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab2Tabelle.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab3MxN-Tabelle.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab4Spalte.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab5Fremdschluessel.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab6Sequenz.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Logik/tab7Inhalt.py')

# import views
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab1Datenbank.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab2Tabelle.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab3MxN-Tabelle.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab4Spalte.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab5Fremdschluessel.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab6Sequenz.py')
execfile('/home/raphael/HomeServer/Programmierung/Entwicklung/Python/DBManager/Views/tab7Inhalt.py')

textFieldInfo = Text(
    root,
    height=13,
    width=25
)
textFieldInfo.insert(END, "")
textFieldInfo.grid(
    row=0,
    column=1
)

note.grid(
    row=0,
    column=0,
    ipadx=92
)

Button(
    note2,
    text="Datenbanken anzeigen",
    width=25,
    command=showDatabases
).grid(row=1, column=0)

Button(
    note2,
    text="Benutzer anzeigen",
    width=25,
    command=showUsers
).grid(row=1, column=1)

Button(
    note2,
    text="Tabellen anzeigen",
    width=25,
    command=showTables
).grid(row=1, column=2)

Button(
    note2,
    text="Spalten anzeigen",
    width=25,
    command=showColumns
).grid(row=1, column=3)

Button(
    note2,
    text="Close",
    width=104,
    command=closeDB
).grid(row=2, column=0, columnspan=4)

note2.grid(
    row=1,
    column=0,
    columnspan=2)

root.mainloop()
