# python-e-podreczniki

![python_logo](https://www.python.org/static/community_logos/python-powered-w-200x80.png)

Kody źródłowe używane w E-Podręcznikach [Zintegrowana Platforma Edukacyjna](https://zpe.gov.pl)


## Kody tworzone w projektach:

- „Tworzenie zestawów narzędzi edukacyjnych, scenariuszy lekcji i zajęć dla obszaru II: Przedmioty humanistyczne i artystyczne”. Nr umowy o dofinansowanie UDA-POWR.02.10.00-00-2011/20-00 dofinansowanego ze środków Europejskiego Funduszu Społecznego w ramach Programu Operacyjnego Wiedza Edukacja Rozwój 2014-2020, Oś priorytetowa II: Efektywne polityki publiczne dla rynku pracy, gospodarki i edukacji, Działanie 2.10 Wysoka jakość systemu oświaty.

- ​„Stworzenie wysokiej jakości E-materiałów dydaktycznych do informatyki (950 e-materiałów) dla uczniów czteroletniego liceum ogólnokształcącego i pięcioletniego technikum” Nr umowy o dofinansowanie UDA-POWR.02.10.00-00-6034/18-00

----

W materiałach dla Liceum i technikum wykorzysywany jest Python 3.6, a w materiałach dla szkoły podstawowej Python 3.10; w większości kody powinny działać na każdej wersji, jednak sugeruję instalowanie przynajmniej wersji 3.10 lub nowszej, gdyż w kodach dla szkoły podstawowej znajduje się wykorzystanie tzw. „**walrus operator**” (https://peps.python.org/pep-0572/):

```
# przykład użycia walrus operator (Python 3.8)

while licznik := int(input("Podaj licznik: ")) <= 0:
    print("Błąd: licznik powinien być większy od 0.")
```
