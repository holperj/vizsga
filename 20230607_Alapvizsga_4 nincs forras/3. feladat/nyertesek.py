class eredmeny:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        self.ev = int(splitted[0] )
        self.het = int(splitted[1])
        self.ford = int(splitted[2])
        self.db = int(splitted[3])
        self.nyeremeny = int(splitted[4])
        self.eredmeny = splitted[5]