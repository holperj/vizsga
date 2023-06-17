class bejegyzes:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        self.ora = int(splitted[0])
        self.perc = int(splitted[1])
        self.db = int(splitted[2])
        self.nev = str(splitted[3])
        self.ido_percben = self.perc + self.ora * 60