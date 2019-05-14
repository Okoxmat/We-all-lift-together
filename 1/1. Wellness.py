#TILTEL ab
import sqlite3
connection = sqlite3.connect("Wellness.db")

cursor = connection.cursor()

# delete

# cursor.execute("""DROP TABLE Wellness.db ;""")

# Tabelle Gast
sql_command = """
CREATE TABLE IF NOT EXISTS Gast (
GastID CHAR(6) PRIMARY KEY,
Vorname VARCHAR(20),
Name VARCHAR(20),
Geschlecht VARCHAR(1),
GebDat DATE,
Strasse VARCHAR(20),
PLZ CHAR(5),
MasseurID CHAR(6),
R_Vorname VARCHAR(20),
R_Name VARCHAR(20),
R_Strasse VARCHAR(20),
R_PLZ CHAR(5),
FOREIGN KEY(MasseurID) REFERENCES Masseur(MasseurID));"""
connection.execute(sql_command)

#Tabelle Masseur
sql_command = """
CREATE TABLE IF NOT EXISTS Masseur (
MasseurID CHAR(6) PRIMARY KEY,
Vorname VARCHAR(20),
Name VARCHAR(20));"""
connection.execute(sql_command)

# Tabelle Mittel
sql_command = """
CREATE TABLE IF NOT EXISTS Mittel (
MittelID CHAR(6) PRIMARY KEY,
Bezeichnung VARCHAR(20));"""
connection.execute(sql_command)

# Tabelle massiert
sql_command = """
CREATE TABLE IF NOT EXISTS massiert (
GastID CHAR(6),
MasseurID CHAR(6),
Datum DATE,
PRIMARY KEY(GastID, MasseurID, Datum)
FOREIGN KEY(GastID) REFERENCES Gast(GastID),
FOREIGN KEY(MasseurID) REFERENCES Masseur(MasseurID));"""
connection.execute(sql_command)

# Tabelle Behandlung
sql_command = """
CREATE TABLE IF NOT EXISTS Behandlung (
GastID CHAR(6),
MittelID CHAR(6),
PRIMARY KEY(GastID, MittelID),
FOREIGN KEY(GastID) REFERENCES Gast(GastID),
FOREIGN KEY(MittelID) REFERENCES Mittel(MittelID));"""
connection.execute(sql_command)

# Tabelle Bettenbelegung
sql_command = """
CREATE TABLE IF NOT EXISTS Bettenbelegung (
BettID CHAR(6),
GastID CHAR(6),
Anreise DATE,
Abreise DATE,
PRIMARY KEY(BettID, GastID, Anreise)
FOREIGN KEY(GastID) REFERENCES Gast(GastID));"""
connection.execute(sql_command)

# Bett
sql_command = """
CREATE TABLE IF NOT EXISTS Bett(
BettID CHAR(6) PRIMARY KEY,
ZimmerNR INTEGER,
BereichNR,
FOREIGN KEY(BereichNr) REFERENCES Bereich(BereichNR));"""
connection.execute(sql_command)

# Tabelle PLZ_Ort
sql_command = """
CREATE TABLE IF NOT EXISTS Ort (
PLZ CHAR(6) PRIMARY KEY,
Ort VARCHAR(20),
FOREIGN KEY(PLZ) REFERENCES GAST(R_PLZ),
FOREIGN KEY(PLZ) REFERENCES GAST(R_PLZ));"""
connection.execute(sql_command)

# Tabelle Bereich
sql_command = """
CREATE TABLE IF NOT EXISTS Bereich (
BereichNR CHAR(6) PRIMARY KEY,
Bereichbezeichnung VARCHAR(20));"""
connection.execute(sql_command)


# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()

input('Exit')
