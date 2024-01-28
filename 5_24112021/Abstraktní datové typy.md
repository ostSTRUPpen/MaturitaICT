# 5 Abstraktní datové typy

1. Linked list
	- List který kromě hodnoty obsahuje také pointer na následující (někdy i předchozí) hodnotu
  	![Linked list](https://miro.medium.com/v2/resize:fit:1400/0*0XVK02Guco9xJMJL.png "Linked list")
2. Zásobník (stack)
  	- Sloup jednotlivcýh záznamů
  	- Princip *Last In - First Out* **LIFO**
  	![Stack](https://www.masaischool.com/blog/content/images/wordpress/2022/04/Last-in-first-out-1024x683.png "Stack")
3. Fronta (queue)
  	- Doslova fronta záznamů
  	- Princip *First In - First Out* **FIFO**
  	![Queue](https://media.geeksforgeeks.org/wp-content/uploads/FIFO.jpg "Queue")
4. Binarní strom (binary tree)
  	- Body, které obsahují hodnotu a odkaz na levý a pravý bod
  	- Vlevo většinou menší hodnota

  	1. Tvorba binárního stromu
    	0. Vstup
    	1. Vybereme si prostřední hodnotu ze vstupu
    	2. Každé číslo porovnáváme s hodnotou v daném bodě
        	- Pokud je **větší** než hodnota v daném bodě, dáme se **doprava**
        	- Pokud je **menší** než hodnota v daném bodě, dáme se **doleva**
    	3. Krok 2 opakujeme dokud jsme neprošli celý vstup
    	4. Výsledek:
		![Binary tree](https://www.mikeperham.com/wp-content/uploads/2014/11/binary-tree.png "Binary tree")

  	2. Hledání v binárním stromě
    	0. Hledáme číslo *5*
    	1. Víme, že *5* je **menší** než *7* dáme se proto **doleva**
    	2. Víme, že *5* je **větší** než *3* dáme se proto **doprava**
    	3. Víme, že *5* je **menší** než *6* dáme se proto **doleva**
    	4. Víme, že *5* je **větší** než *4* dáme se proto **doprava**
    	5. Hotovo
    
  	3. Přidání hodnoty do binárního stromu
    	0. Chceme přidat číslo 16¨
    	1. Víme, že *16* je **větší** než *7* dáme se proto **doprava**
    	2. Víme, že *16* je **větší** než *12* dáme se proto **doprava**
    	3. Víme, že *16* je **větší** než *13* dáme se proto **doprava**
    	4. Víme, že *16* je **větší** než *15* dáme se proto **doprava**
    	5. Hotovo