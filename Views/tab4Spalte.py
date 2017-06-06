# Spaltenoption

tab4 = Frame(note)
note.add(
    tab4,
    text="Spalte"
)

columnlabel = Label(
    tab4,
    text="Tabellenname"
).grid(row=0)
tab4TableName = Entry(
    tab4,
    textvariable = StringVar()
)
tab4TableName.insert(0, "")
tab4TableName.grid(row=0, column=1)

columnlabel = Label(
    tab4,
    text="Spaltenname"
).grid(row=1)
tab4ColumnName = Entry(
    tab4,
    textvariable = StringVar()
)
tab4ColumnName.insert(0, "")
tab4ColumnName.grid(row=1, column=1)

columnlabel = Label(
    tab4,
    text="Spaltentyp"
).grid(row=2)
tab4ColumnType = Entry(
    tab4,
    textvariable = StringVar()
)
tab4ColumnType.insert(0, "")
tab4ColumnType.grid(row=2, column=1)

Button(
    tab4,
    text="Spalte anlegen",
    width=25,
    command=addColumn
).grid(row=3, column=1)

Button(
    tab4,
    text="Spalte loeschen",
    width=25,
    command=lambda: askQuestion(param="column")
).grid(row=4, column=1)

note.grid()
