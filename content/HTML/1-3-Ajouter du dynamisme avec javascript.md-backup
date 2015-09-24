Title:  Ajouter du dynamisme avec javascript
date: 2014-11-04
Chapitre: 1
series:  Créer des pages web en html5
series_index: 3
Tags: icn, html5, javascript

<a title="Par Chris Williams [Public domain], via Wikimedia Commons" href="http://commons.wikimedia.org/wiki/File%3AUnofficial_JavaScript_logo_2.svg"><img width="256" alt="Unofficial JavaScript logo 2" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/256px-Unofficial_JavaScript_logo_2.svg.png"/></a>

> JavaScript est un langage de programmation de scripts principalement employé dans les pages web interactives mais aussi pour les serveurs. >Le langage a été créé en 1995 par Brendan Eich (Brendan Eich étant membre du conseil d'administration de la fondation Mozilla à cette époque) pour le compte de Netscape Communications Corporation. [Source Wikipedia](http://fr.wikipedia.org/wiki/JavaScript)

**Attention à ne pas confondre le javascript et le java**, ce sont des langages différents.

#Intégration de code `javascript` dans une page html

Le code javascript peut être intégré directement grâce à la balise html `<script>`, soit dans écrit directement dans l'en-tête du document(`<head>`), soit en utilisant un fichier séparé avec l'extension `.js`.

##Directement dans la page html

```
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8" />
        <title>Un peu de javascript</title>
        <script type="text/javascript" charset="utf-8">
          // Alert crée une fenêtre d'affichage sur l'écran pour l'utilisateur
          alert("Hello world !");
          // console.log() écrit dans la console du navigateur pour le développeur
          console.log("Script Hello world exécuté.")
        </script>
    </head>
    <body>
        <h1>Titre principal de mon document</h1>
        <p>Regarde maman, je suis en train d'ajouter du code javascript à ma page.</p>
    </body>

</html>
```

##Dans un fichier `script.js` séparé

```
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <title>Un document minuscule</title>
    <script src="script.js"></script> 
  </head>
  <body>
    <h1>Titre principal de mon document</h1>
    <p>Regarde maman, je suis en train d'ajouter du code javascript à ma page.</p>
  </body>
</html>
```

##Tester du code javascript grâce à l'ardoise

La plupart de navigateurs dispose d'une console pour tester le code javascript. Dans le cas de firefox, on la lance avec le raccourci <kbd>MAJ+F4</kbd>. Sinon, vous pouvez y accéder par le menu de `Développement web`.

Il est aussi très utile d'ouvrir également la console <kbd>CTRL+MAJ+K</kbd> web pour pouvoir afficher des résultats dans celle-ci grâce à la fonction `console.log()`.

L'éxecution du code javascript s'effectue en appuyant sur le bouton `Exécuter` (ou le raccourci clavier <kbd>CTRL+R</kbd>)

#Syntaxe du javascript

Il s'agit d'un langage très complet, qui ne peut pas être expliqué en quelques lignes, pour une référence plus complète, voir l'article Wikipedia [Syntaxe javascript](http://fr.wikipedia.org/wiki/Syntaxe_JavaScript)

- Les **commentaires** sont notés précédés de deux barres obliques: `//`.
- Les instructions simples sont terminées par un **point-virgule**: `;`.
- L'**indentation** des blocs d'instruction n'est pas obligatoire comme en python, mais souhaitable.
- Les blocs d'instructions sont entourés d'accolades.
```
if (expression1)
 {
   //instructions réalisées si expression1 est vraie;
 }
 else
 {
   //instructions réalisées dans les autres cas;
 }
```

#Variables javascript

Les variables n'ont pas de type défini, on parle de typage dynamique comme en python. Il est possible de modifier le type de donnée contenue dans une variable.

Coller le code suivant dans l'ardoise javascript pour l'éxecuter et l'éxaminer.
```
var myString = '123.456'
// console.log permet d'afficher la valeur dans la console web
console.log(myString);

// On peut directement inspecter une ligne directement
// en la sélectionnant puis Examiner (CTRL+I)
typeof(myString); // value:string

// Ou un beau console.log pour garder des traces de l'éxecution du programme
console.log('myString est actuellement du type:' + typeof(myString) );

// Illustration du typage dynamique
var myString = Number(myString);
console.log(myString);
typeof myString; // value:number
console.log('myString est actuellement du type:' + typeof(myString) );
```

Il est vivement conseillé de déclarer ses variables avec l'instruction `var` pour des questions de portée de variable.

*Remarque* le javascript définit aussi des **constantes** avec l'instruction `const` qui comme son nom l'indique ne peut pas changer de valeur grâce à une assignation ou être re-déclarée au cours du programme contrairement à une variable.

```
// Réassignation possible avec les variables
var c = 6;
console.log(c); // donne 6
c = 4;
console.log(c); // donne 4

// Réassignation impossible avec les constantes
const a = 5;
a = 4;  // Exception: redeclaration of const a
```

#Fonctions javascript

Une fonction est déclarée de la façon suivante en javascript:

```
function nomDeMaFonction (argument1, argument2, ...) {
  instructions
  return valeur_renvoyée_par_ma fonction
}
```

**Exemple**: la fonction carré

```
// Déclaration de la fonction
function carré(nombre) {
  return nombre * nombre
}

// Appel de la fonction

carré(2);  // retourne 4!
```

**Attention**: Lorsqu'on déclare une variable dans une fonction, celle-ci a une portée locale et ne peut pas être utilisée en dehors de la fonction.

```
// n ici une variable locale dans la fonction
function quatreFois(nombre) {
  var n = 4
  return n * nombre
}

// Elle n'existe pas en dehors de la fonction
quatreFois(2);  // retourne 8!
n * 2; // Exception: n is not defined

```

#Modifier le code html grâce à javascript
##Execution différée
Il convient d'attendre que la page html soit chargée avant d'éxecuter le code javascript. De nombreux développeurs placent le code javascript à la fin du corps du document avant la balise fermante `</body>`.

Cependant il est aussi possible de lancer le code javascript qu'après le chargement de la fenêtre en placant le code dans une fonction anonyme s'executant après le chargement de la page.*(Vous allez voir, en javascript, les fonctions sont très présentes)*

```
window.onload = function() { 
  // code javascript à éxecuter
  // après le chargement de la page
}
```

##Accéder à un élément html

La méthode `document.getElementById()` permet de sélectionner un élément html à partir de son `id`.

On peut alors modifier son contenu grâce à la propriété `innerHTML`, 

```
document.getElementById("this-id").innerHTML = "New text!";
```

ou encore modifier son style grâce à la prpriété `style`.

```
document.getElementById("this-id").style.color = "##FFAA85";
```


*Exemple de code permettant d'afficher l'heure à laquelle vous avez ouvert la page.*

```
<!doctype html>
<html lang="fr">

    <head>
        <meta charset="utf-8" />
        <title>Un peu de javascript</title>
        <script type="text/javascript" charset="utf-8">
            window.onload = function() {
                    // Stocke l'heure dans la vaariable d
                    var d = new Date();
                    // Ajoute cette heure dans l'élément html ayant pour id heure
                    document.getElementById("heure").innerHTML = d.toLocaleTimeString();

                }
        </script>
    </head>

    <body>
        <h1>Javascript en action</h1>
        <p>Page ouverte à: <span id="heure"></span>
        </p>
    </body>

</html>
```

*Encore mieux afficher l'heure actuelle en éxecutant l'affichage toutes les mille millisecondes*

```
!doctype html>
<html lang="fr">

    <head>
        <meta charset="utf-8" />
        <title>Un peu de javascript</title>

        <script type="text/javascript" charset="utf-8">
            window.onload = function() {
                function myTimer() {
                    var d = new Date();
                    document.getElementById("heure").innerHTML = d.toLocaleTimeString();

                }
          
                setInterval(function() {
                        myTimer()
                    }, 1000);
            }
        </script>
    </head>

    <body>
        <h1>Javascript en action</h1>
        <p>Il est: <span id="heure"></span>
        </p>
    </body>

</html>
```

##Contrôler des événements

On éxecuter du javascript lorsqu'on **presse un bouton** avec  l'attribut `onclick` 

```
<!DOCTYPE html>
<html>
    <body>

        <h1 id="id1">Mon titre de niveau 1</h1>

        <button type="button" onclick="document.getElementById('id1').style.color = 'red'">
            Attention! Que va-t-il se passer?</button>

    </body>
</html>
```

Ou encore lorsque la souris survole un élément avec l'attribut `onmouseover`.

```
<!DOCTYPE html>
<html>

    <body>

        <div onmouseover="mOver(this)" onmouseout="mOut(this)" style="background-color:#D5AA12;font-size: 13rem;width:19rem;padding:40px;">
            Sol</div>

        <script>
            function mOver(obj) {
                obj.innerHTML = "Fa";
                obj.style.background = "#FF5546";
            }

            function mOut(obj) {
                obj.innerHTML = "Sol";
                obj.style.background = "#D5AA12";
            }
        </script>

    </body>

</html>

```

##Pour aller plus loin

Lorsqu'on modifie une page html grâce à javascript, on manipule le `DOM`: Document Object Model. Pour plus de précisions et d'autres exemples interactifs voir l'excellent site [w3schools](http://www.w3schools.com/js/js_htmldom.asp)



