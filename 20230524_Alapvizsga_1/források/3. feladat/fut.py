class futo:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        self.name = splitted[0]
        self.rajtszam = int(splitted[1])
        self.kategoria = splitted[2]
        self.ido = splitted[3]
        splitted_ido = splitted[3].split(':')
        self.hour = int(splitted_ido[0])
        self.minute = int(splitted_ido[1])
        self.sec = int(splitted_ido[2])
        self.tavszazalek = int(splitted[4])
    def IdőÓrában(self):
        return self.hour + self.minute / 60 + self.sec / 3600
        