# 9 Internet, jazyk HTML CSS a JS

## Internet

-   Internet je celosvětový systém propojených počítačových sítí („síť sítí“), ve kterých mezi sebou počítače komunikují pomocí rodiny protokolů TCP/IP. Používá se ke sdílení a výměně data a komunikaci.

## HTML

-   Hyper Text Markup Language
-   Struktura webové stránky
-   Využívá tagů v ostrých závorkách
    -   Container tags mají otevírací i uzavírací tag např.: \<div\>\</div\>, \<p\>\</p\>, ..
    -   Empty tags mají pouze otevírací tag např.: \<img\>\</img\>, ...
    -   Do tagů se dávají takzvané atributy class="", id="", ...

## CSS

-   Cascading Style sheets
-   Vzhled webové stránky
-   Zapisuje se buď do tagu \<style>\</style> nebo do samostatného dokumentu .css na který je v .html v head části odkaz
-   Využívá selectorů
    -   p -> tagy p
    -   #p -> tag s id atributem p
    -   .p -> tagy s class atributem p
-   a pravidel
    -   color: red;

## JS

-   JavaScript
-   Fungování webové stránky
-   Zapisuje se buď do tagu \<script>\</script> nebo do samostatného dokumentu .js na který je v .html v body části odkaz

## Jednoduchá HTML stránka:

<code>

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <!-- Meta tagy určují informace o stránce -->
    	<meta charset="UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<style>
    		p {
    			color: red;
    		}

    		.form {
    			font-size: larger;
    		}

    		#add-button {
    			rotate: 15deg;
    		}
    	</style>
    	<!--
    	Odkaz na vnější css soubor
    	 <link rel="stylesheet" href="PATH/NAME.css">
    	-->
    	<title>Test</title>
    </head>

    <body>

    	<p>Počet:</p>
    	<div class="form">
    		<p id="output">0</p>
    		<button id="add-button" onclick="add()">Přičíst</button>
    	</div>
    	<script>
    		function add() {
    			let count = parseInt(document.getElementById("output").innerHTML);
    			count += 1
    			document.getElementById("output").innerHTML = count++;
    		}
    	</script>
    	<!--
    	Odkaz na vnější js soubor
    	<script src="PATH/NAME.js"></script>
    	-->
    </body>

    </html>

</code>

## Frameworky

-   Slouží k usnadnění práce pro programátora
-   Různé typy - v dnešní době hlavně zaměření na HTML a CSS
-   React.js / Svelte (jedny z mnoha)
-   Moderní webové stránky často využívají též Typescript (JS s datovými typy) a např tailwind (zjednodušení práce s CSS)

-   Stejná stránka ve frameworku Svelte

<code>

    <script>
        let count = 0

        function add(){
    			count++
        }
    </script>

    <p>Počet:</p>
    <div class="form">
    	<p>{count}</p>
    	<button id="add-button" on:click={add}>Přičíst</button>
    </div>

    <style>
        p {
        	color: red;
        }
        .form {
        	font-size: larger;
        }
        #add-button {
        	rotate: 15deg;
        }
    </style>

</code>
