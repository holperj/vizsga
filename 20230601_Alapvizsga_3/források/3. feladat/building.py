class epulet:
    def __init__(self, row) -> None:
        splitted = row.split(';')
        self.nev = splitted[0]
        self.varos = splitted[1]
        self.orszag = splitted[2]
        self.height = float(splitted[3].replace(',','.'))
        self.floor = int(splitted[4])
        self.year = int(splitted[5].strip())
