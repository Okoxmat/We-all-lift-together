import sqlite3
connection = sqlite3.connect("Wellness.db")

cursor = connection.cursor()
# Tabelle Gast
sql_command = """INSERT INTO Gast VALUES
("Ga0001", "Hanz", "Peter", "m","17.2.1956", "Hans-Peter-Allee", "13125", "Ma0001", "Hans", "Peter", "Hans-Peter-Allee", "13125"),
("Ga0002", "Peter", "Hans", "m","18.12.1956", "Peter-Hans-Allee", "07743", "Ma0002", "Peter", "Peter", "Hans-Peter-Allee", "07743"),
("Ga0003", "Mimi", "Miriam", "w","18.12.2022", "Lumpenstreet", "37011", "Ma0003", "Mimi", "Miriam", "Lumpenstreet", "37011"),
("Ga0004", "Atticus", "O`Sullivan", "m","8.11.-40", "Olivenallee", "14467", "Ma0004", "Leif", "Helgerson", "Mondgasse", "14467"),
("Ga0005", "Oberon", "Der Guetige", "m","1.4.2005", "Olivenallee", "14467", "Ma0005", "Atticus", "O`Sullivan", "Olivenallee", "14467"),
("Ga0006", "Augustin", "Der Weise", "m","30.6.1945", "Lingusterweg", "38436", "Ma0006", "Augustin", "Der Weise", "Lingusterweg", "38436");"""
cursor.execute(sql_command)

# Tabelle Masseur
sql_command = """INSERT INTO Masseur VALUES
("Ma0001", "Alex", "Ander"),
("Ma0002", "Am", "Erika"),
("Ma0003", "Hufei", "Sen"),
("Ma0004", "Af", "Rika"),
("Ma0005", "Eu", "Ropa"),
("Ma0006", "Aus", "Tralien");"""
cursor.execute(sql_command)

# Eintrag Mittel
sql_command = """INSERT INTO Mittel VALUES
("Mi0001", "Schlaftrunk"),
("Mi0002", "Steine"),
("Mi0003", "Adrenalin"),
("Mi0004", "Holz"),
("Mi0005", "Pizza"),
("Mi0006", "Sand");"""
cursor.execute(sql_command)

# Eintrag massiert
sql_command = """INSERT INTO massiert VALUES
("Ga0001", "Ma0001", "22.04.2019"),
("Ga0002", "Ma0002", "15.05.2017"),
("Ga0001", "Ma0003", "15.06.2017"),
("Ga0004", "Ma0005", "15.02.1987"),
("Ga0002", "Ma0004", "19.06.2015"),
("Ga0006", "Ma0002", "20.02.2019");"""
cursor.execute(sql_command)

# Eintrag Behandlung
sql_command = """INSERT INTO Behandlung VALUES
("Ga0001","Mi0001"),
("Ga0002","Mi0005"),
("Ga0003","Mi0003"),
("Ga0004","Mi0004"),
("Ga0005","Mi0006"),
("Ga0006","Mi0002");"""
cursor.execute(sql_command)

# Eintrag Bettenbelegung
sql_command = """INSERT INTO Bettenbelegung VALUES
("Bt0001", "Bt0001", "21.04.2019", "23.04.2019"),
("Bt0002", "Bt0004", "12.05.2017", "23.06.2017"),
("Bt0001", "Bt0003", "13.05.2017", "23.07.2017"),
("Bt0004", "Bt0006", "05.02.1987", "17.03.1987"),
("Bt0002", "Bt0005", "18.06.2015", "23.06.2015"),
("Bt0006", "Bt0001", "19.02.2019", "21.03.2019");"""
cursor.execute(sql_command)

# Vorlage Tabelle PLZ_Ort
sql_command = """INSERT INTO Ort VALUES
("13125", "Berlin"),
("07743", "Jena"),
("14467", "Potsdam"),
("10431", "Athen"),
("38436", "Wolfsburg"),
("37011", "Tennessee");"""
cursor.execute(sql_command)

# Eintrag Bereich
sql_command = """INSERT INTO Bereich VALUES
("Br0001", "Massage"),
("Br0002", "Meditation"),
("Br0003", "Schlaf"),
("Br0004", "Ruhebereich"),
("Br0005", "Raucherbereich"),
("Br0006", "Anmeldung");"""
cursor.execute(sql_command)

# Eintrag Bett
sql_command = """INSERT INTO Bett VALUES
("Bt0001", "Zi0001", "Br00001"),
("Bt0002", "Zi0002", "Br00002"),
("Bt0003", "Zi0003", "Br00003"),
("Bt0004", "Zi0004", "Br00004"),
("Bt0005", "Zi0005", "Br00005"),
("Bt0006", "Zi0006", "Br00006");"""
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()

input('Exit')
