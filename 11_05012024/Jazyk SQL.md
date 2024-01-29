# 11 Databáze: jazyk SQL
Structured Query Language (SQL) je jazyk sloužící k manipulaci se strukturovanými daty uloženými v databázi a s databází samotnou.

## Syntax [w3schools](https://www.w3schools.com/sql/)
- Možný SQL příkaz
```sql
SELECT * 
FROM Customers;
```

- SELECT a FROM
	- **FROM** určuje tabulku ze které sloupce vybíráme
	- **SELECT** Slouží k vybrání sloupců z databáze
		- Pokud chceme všechny sloupce, použijeme *
		```sql
		SELECT *
		FROM clients;
		```
		- Jinak vypíšeme jednotlivé sloupce
		```sql
		SELECT id, name, surname 
		FROM clients;
		```	
- WHERE
	- Slouží k vybrání pouze řádků, které splňují podmínku
	- Syntax: **WHERE** *sloupec*=*podmínka*
	```sql
	SELECT id, name, surname 
	FROM clients
	WHERE surname='Pavel';
	```		

<div style="page-break-after: always;"></div>

- ORDER BY
	- Slouží k seřazení výsledků
	- V základu ASC (Vzestupně) nebo DESC (sestupně)
	- U stringů řadí podle abecedy (Buď ASC nebo DESC)
	- Lze určit více sloupců - v tom případě se řadí nejdříve podle 1., poté pokud je 1. stejný, tak podle 2. atd...
	```sql
	SELECT id, name, surname, order, money_amount
	FROM clients
	WHERE order='Maska'
	ORDER BY money_amount ASC, surname DESC;
	```	
- JOIN [Lepší na w3schools](https://www.w3schools.com/sql/sql_join.asp)
	- INNER JOIN
		- vrací záznamy které mají shodné hodnoty v obou tabulkách
		```sql
		SELECT column_names
		FROM table1
		INNER JOIN table2
		ON table1.column_name = table2.column_name;
		```
	- LEFT JOIN
		- Vrací všechny záznamy z první tabulky a záznamy se shodnou hodnotou z druhé tabulky
		```sql
		SELECT column_names
		FROM table1
		LEFT JOIN table2
		ON table1.column_name = table2.column_name;
		```
	- RIGHT JOIN
		- Vrací všechny záznamy z druhé tabulky a záznamy se shodnou hodnotou z první tabulky
		```sql
		SELECT column_names
		FROM table1
		RIGHT JOIN table2
		ON table1.column_name = table2.column_name;
		```
	<img src="https://www.codeproject.com/KB/database/Visual_SQL_Joins/Visual_SQL_JOINS_orig.jpg" width="400">
- CREATE DB
	- Slouží k vytvoření databáze
	```sql
	CREATE DATABASE databasename;
	```
- DROP DB
	- Slouží ke smazání databáze
	```sql
	DROP DATABASE databasename;
	```
- CREATE TABLE
	- SLouží k vytvoření nové tabulky
	```sql
	CREATE TABLE table_name (
    	column1 datatype,
    	column2 datatype,
   		....
	);
	```
- DROP TABLE
	- Slouží ke smazání tabulky
	```sql
	DROP TABLE table_name;
	```