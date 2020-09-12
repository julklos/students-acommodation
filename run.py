import pandas as pd
from clustering import *

excel_file = "students_2020.xlsx"
students = pd.read_excel(excel_file)


#tylko studenci bez preferencji
studentsWithoutPreferences = students[students["Złożyłem preferencje składu w systemie kwaterunkowym *"]=="Nie"]

#niepotrzebne kolumny- opisowe
studentsWithoutPreferences = studentsWithoutPreferences.drop(columns=[
'Kierunek studiów','Złożyłem preferencje składu w systemie kwaterunkowym *',
'Wolę mieszkać z osobą *', 'Moja najbardziej charakterystyczna cecha to',
'Najbardziej cenię sobie', 'Najłatwiej z równowagi wyprowadza mnie',
'Moje zainteresowania2', 'Jeśli uprawiam sport, to2',
'Jeśli oglądam sport, to2', 'Muzyka w moich uszach2', 'Uwagi2'])

#podział na płcie
girls = studentsWithoutPreferences[studentsWithoutPreferences["Płeć"]=="Kobieta"]
boys = studentsWithoutPreferences[studentsWithoutPreferences["Płeć"]=="Mężczyzna"]


girls = girls.reset_index()
boys = boys.reset_index()

#linkage- 'single', 'complete', 'average', 'weighted' and 'ward'
#criterion- 'distance', 'maxclust'

#clustering(students = girls, k=5, linkage="single" , criterion="maxclust")
clustering(students = boys, k= 100, linkage="single" , criterion="maxclust")