# Fremdschluesseloption

tab5 = Frame(note)
note.add(
    tab5,
    text="Fremdschluessel"
)

ftlabel = Label(
    tab5,
    text="Tabellenname"
).grid(row=0)
tab5TableName = Entry(
    tab5,
    textvariable = StringVar()
)
tab5TableName.insert(0, "")
tab5TableName.grid(row=0, column=1)

ftlabel = Label(
    tab5,
    text="Spaltenname"
).grid(row=1)
tab5ColumnName = Entry(
    tab5,
    textvariable = StringVar()
)
tab5ColumnName.insert(0, "")
tab5ColumnName.grid(row=1, column=1)

ftlabel = Label(
    tab5,
    text="Referenzierte Tabelle"
).grid(row=2)
tab5RefTableName = Entry(
    tab5,
    textvariable = StringVar()
)
tab5RefTableName.insert(0, "")
tab5RefTableName.grid(row=2, column=1)

Button(
    tab5,
    text="Fremdschluessel hinzufuegen",
    width=25,
    command=addForeignKey
).grid(row=3, column=1)

Button(
    tab5,
    text="Fremdschluessel loeschen",
    width=25,
    command=lambda: askQuestion(param="foreignkey")
).grid(row=4, column=1)

note.grid()