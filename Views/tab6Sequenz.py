# Sequenzoption

tab6 = Frame(note)
note.add(
    tab6,
    text="Sequenz"
)

sequencelabel = Label(
    tab6,
    text="Tabellenname"
).grid(row=0)
tab6SequenceName = Entry(
    tab6,
    textvariable = StringVar()
)
tab6SequenceName.insert(0, "")
tab6SequenceName.grid(row=0, column=1)

Button(
    tab6,
    text="Sequenz zuruecksetzen",
    width=25,
    command=lambda: setSequence(tablename="")
).grid(row=1, column=1)

note.grid()
