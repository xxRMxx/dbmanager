# MxN-Tabellenoption

tab3 = Frame(note)
note.add(
    tab3,
    text="MxN-Tabelle"
)

mxntablelabel = Label(
    tab3,
    text="MxN-Tabellenname"
).grid(row=0)
tab3MxNTableName = Entry(
    tab3,
    textvariable = StringVar()
)
tab3MxNTableName.insert(0, "")
tab3MxNTableName.grid(row=0, column=1)

Button(
    tab3,
    text="MxN-Tabelle anlegen",
    width=25,
    command=addMxNTable
).grid(row=1, column=1)

Button(
    tab3,
    text="MxN-Tabelle loeschen",
    width=25,
    command=lambda: askQuestion(param="mxntable")
).grid(row=2, column=1)

note.grid()