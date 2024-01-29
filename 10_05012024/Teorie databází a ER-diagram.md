# 10 Databáze: Teorie databází, ER-diagram
Databáze (neboli datová základna, též databanka) je systém souborů s pevnou strukturou záznamů. Tyto soubory jsou mezi sebou navzájem propojeny pomocí klíčů. V širším smyslu jsou součástí databáze i softwarové prostředky, které umožňují manipulaci s uloženými daty a přístup k nim. Tento software se v české odborné literatuře nazývá systém řízení báze dat (DataBaseManagementSystem). Běžně se označením databáze – v závislosti na kontextu – myslí jak uložená data, tak i software (DBMS). [Wikipedia](https://cs.wikipedia.org/wiki/Datab%C3%A1ze)

Redundance dat nastává, když je stejná část dat uložena na dvou nebo více oddělených místech. Tento stav je nežádoucí neboť ukládáme stejné údaje vícekrát, také hrozí, že mezi uloženými údaji mohou být nežádoucí rozdíly. Zároveň ale poskytuje výhody neboť je možné poškozený údaj nahradit za nepoškozený. Jedná se tedy v podstatě o formu zálohování a zabezpečení dat. [sgwebdigital](https://sgwebdigital.com/cs/co-je-to-redundance-dat/)

## ERD
Slouží k abstraktnímu grafickému vyobrazení databáze a samotných informací, které budou uchovávány. Využívá se struktury propojených obdélníků, které symbolizují jednotlivé tabulky databáze

### Pojmy
- Entita (věc) 
	- Jedná se o objekt ze skutečného světa. Vždy musí být rozeznatelný od jiných entit. Například konkrétní lektor, klient nebo i odučená hodina.
- Entitní množina
	- Skupina objektů stejného typu se společnými vlastnostmi. Tyto množiny věcí se zachycují v ERD.
- Vztah 
    - Zobrazuje návaznost mezi množinami. Například mentor vede lektora.
- Množina vztahů 
    - Skupina vztahů stejného typu se stejnými vlastnostmi. Například existují entitní množiny mentor a lektor, mezi nimiž je vztahová množina vyjadřující, že mentor vede lektora.
- Vlastnosti vztahů 
    - Slouží k upřesnění vztahu mezi entitními množinami. Například: množina mentor vede množinu lektor s tím, že jeden mentor vede jednoho a více lektorů, ale lektor může mít pouze jednoho mentora.
- Primární klíč (primary key) 
    - Také označován jako identifikační klíč, identifikační číslo nebo zkratkou PK. Slouží k identifikaci konkrétní entity v množině entit. Pro každý objekt musí být v rámci skupiny objektů jedinečný.
- Cizí klíč (foreign key) 
    - Označován též jako sekundární klíč nebo zkratkou FK je importovaný klíč odkazující na entitu v jiné množině entit.
[SOČ](https://1drv.ms/b/s!ArJptXeCnkq-nzuLKwGY-iPh13J-?e=7gm3NE)
- Vazební tabulka
	- Nenese sama o sobě žádná data a slouží pouze k propojení
dvou tabulek. Každý řádek vazební tabulky obsahuje pouze ID řádků v jiných tabulkách, které spojuje.
[itnetwork](https://www.itnetwork.cz/ms-sql/mssql-tutorial-joiny-a-vazba-m-n)

<div style="page-break-after: always;"></div>

## Možné otázky
- Navrhněte prosím systém, který nám umožní efektivně spravovat naši **knihovnu**. Potřebujeme nástroj, který nám pomůže sledovat, které **knihy** máme k dispozici, kdo jsou naši **členové** a jaké knihy si od nás půjčují. V systému bychom rádi měli možnost evidovat informace o každé knize, včetně jejího názvu, autora a kategorie. Dále potřebujeme spravovat informace o našich členech, jako jsou jejich jména, adresy a kontaktní údaje. Proces **výpůjček** by měl být také součástí systému, kde budeme udržovat záznamy o tom, kdo si jakou knihu půjčil a kdy ji vrátil. Cílem je vytvořit přehledný systém, který nám usnadní správu knihovny a umožní nám lépe porozumět poptávce po knihách ze strany našich členů.

- Navrhněte prosím systém pro správu **osobních úkolů** a plánování času. Potřebujeme nástroj, který nám umožní sledovat **naše úkoly**, jejich termíny splnění a prioritu. V systému bychom rádi měli možnost evidovat informace o každém úkolu, včetně jeho názvu, popisu a termínu splnění. Dále potřebujeme možnost přiřadit úkoly **kategorie** a přidělit je **konkrétním osobám nebo týmům**. Proces plánování by měl být součástí systému, kde budeme schopni vytvářet **plány a rozvrhy úkolů**, sledovat jejich stav a přidělovat je různým členům týmu. Cílem je vytvořit efektivní nástroj, který nám pomůže organizovat naše pracovní i osobní úkoly a zlepšit naši produktivitu a časový management.