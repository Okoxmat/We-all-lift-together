#-------------------------------------------------------------------------------
# Name:        Wellfrage
# Purpose:
#
# Author:      jolanda.schumann
#
# Created:     13.05.2019
# Copyright:   (c) jolanda.schumann 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sqlite3
connection = sqlite3.connect("Wellness.db")

cursor = connection.cursor()

def result_ausgabe(r):
    r = str(r)
    r = r.replace("(","")
    r = r.replace(")","")
    r = r.replace("'","")
    r = r.replace("[","")
    r = r.replace("]","")
    r = r.replace(",","")
    print(r)
    return 0

#SQL Abfrage
cursor.execute("SELECT * FROM Gast")
print("Alle Datensaetze der Tabelle Gast:")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

    
#Selektion
cursor.execute("SELECT * FROM Masseur WHERE Name= 'Ropa'")
print("\nName = Ropa:")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

cursor.execute("SELECT * FROM Gast WHERE(Name='Der Weise') AND (Strasse='Lingusterweg')")
print("\nName= Der Weise und Strasse= Lingusterweg:")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

#Projektion
cursor.execute("SELECT Bezeichnung FROM Mittel") 
print("\nMittel Bezeichnungen:")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

cursor.execute("SELECT DISTINCT PLZ FROM Gast") 
print("\nPLZ(deutlich) von allen Gaesten:")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

cursor.execute("SELECT GastID, Name, GebDAt FROM Gast") 
print("\nGeburtstage der Gaeste:")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

#Sortierung
cursor.execute("SELECT * FROM Gast ORDER BY Name") 
print("\nMitarbeiter (ASC):")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)

cursor.execute("SELECT * FROM Gast ORDER BY Name DESC") 
print("\nMitarbeiter (DESC):")
result = cursor.fetchall()
for r in result:
    result_ausgabe(r)
    
input()
