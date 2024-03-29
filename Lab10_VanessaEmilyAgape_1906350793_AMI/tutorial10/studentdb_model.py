import csv
 
class Mahasiswa(object):
 
    def __init__(self, npm="", nama="", kelas="B"):
        self.npm = npm # unique
        self.nama = nama
        self.kelas = kelas
 
    def __str__(self):
        strMhs = self.npm + ", " + self.nama + ", " + self.kelas
        return strMhs
 
    def __lt__(self, anotherMhs):
        return self.nama < anotherMhs.nama
 
    def __eq__(self, anotherMhs):
        return self.nama == anotherMhs.nama
 
 
class MahasiswaDB(object):
 
    def __init__(self, daftar = {}):
        self.daftar = daftar
 
    def importFromCSV(self, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                if len(line) == 3 and line[0] != "":
                    aMhs = Mahasiswa(line[0], line[1], line[2])
                    self.daftar[line[0]] = aMhs
 
    def cariByNama(self, aName):
 
        result = []
        for v in self.daftar.values():
            if aName.lower() in v.nama.lower():
                result.append(v)
 
        return result