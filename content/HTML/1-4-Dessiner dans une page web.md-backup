Title:  Dessiner dans une page web
date: 2014-11-04
Chapitre: 1
series:  Créer des pages web en html5
series_index: 4
Tags: icn, html5, canvas, svg

Il existe deux grands types de formats d'images:

- les images matricielles,
- et les images vectorielles.

Ces deux types d'images peuvent être intégrées dans une page web grâce à la balise `<img>`, mais elles peuvent être aussi codées directement dans la page grâce aux balises `<svg>` et `<canvas>`.


#Dessin vectoriel en `svg`
<a title="W3C [CC-BY-2.5 (http://creativecommons.org/licenses/by/2.5)], via Wikimedia Commons" href="http://commons.wikimedia.org/wiki/File%3ASVG_Logo.svg"><img width="256" alt="SVG Logo" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4f/SVG_Logo.svg/256px-SVG_Logo.svg.png"/></a>

Le format svg est un format d'image vectoriel proposé par le W3C.

Dans ce format, les dessins sont décrits par un ensemble formes géométriques simples (arcs de cercle ou d'ellipse, segments de droite, courbes de Bézier...)

##Syntaxe

Le fichier svg est un fichier xml qui indique les formes présentes dans le dessin(`rect` pour rectangle, `circle` pour cercle,...)

**Exemple:**

Créer un fichier texte appelé `image.svg` avec le contenu suivant.

```
<?xml version="1.0" standalone="no"?>
<svg width="200" height="250" version="1.1" xmlns="http://www.w3.org/2000/svg">

  <rect x="10" y="10" width="30" height="30" stroke="black" fill="transparent" stroke-width="5"/>
  <rect x="60" y="10" rx="10" ry="10" width="30" height="30" stroke="black" fill="transparent" stroke-width="5"/>

  <circle cx="25" cy="75" r="20" stroke="red" fill="transparent" stroke-width="5"/>
  <ellipse cx="75" cy="75" rx="20" ry="5" stroke="red" fill="transparent" stroke-width="5"/>

  <line x1="10" x2="50" y1="110" y2="150" stroke="orange" fill="transparent" stroke-width="5"/>
  <polyline points="60 110 65 120 70 115 75 130 80 125 85 140 90 135 95 150 100 145"
      stroke="orange" fill="transparent" stroke-width="5"/>

  <polygon points="50 160 55 180 70 180 60 190 65 205 50 195 35 205 40 190 30 180 45 180"
      stroke="green" fill="transparent" stroke-width="5"/>

  <path d="M20,230 Q40,205 50,230 T90,230" fill="none" stroke="blue" stroke-width="5"/>
</svg>

```

Lorsque vous ouvrez ce fichier avec une visionneuse d'images, vous devriez obtenir l'image suivante:

<div style='background-color: lightgray;'>
<svg width="200" height="250" version="1.1" xmlns="http://www.w3.org/2000/svg">

  <rect x="10" y="10" width="30" height="30" stroke="black" fill="transparent" stroke-width="5"/>
  <rect x="60" y="10" rx="10" ry="10" width="30" height="30" stroke="black" fill="transparent" stroke-width="5"/>

  <circle cx="25" cy="75" r="20" stroke="red" fill="transparent" stroke-width="5"/>
  <ellipse cx="75" cy="75" rx="20" ry="5" stroke="red" fill="transparent" stroke-width="5"/>

  <line x1="10" x2="50" y1="110" y2="150" stroke="orange" fill="transparent" stroke-width="5"/>
  <polyline points="60 110 65 120 70 115 75 130 80 125 85 140 90 135 95 150 100 145"
      stroke="orange" fill="transparent" stroke-width="5"/>

  <polygon points="50 160 55 180 70 180 60 190 65 205 50 195 35 205 40 190 30 180 45 180"
      stroke="green" fill="transparent" stroke-width="5"/>

  <path d="M20,230 Q40,205 50,230 T90,230" fill="none" stroke="blue" stroke-width="5"/>
</svg>
</div>

Essayez modifier certains des paramètres du fichier svg pour vous familiariser avec sa syntaxe, vous pourrez parfaire votre connaissance en utilisant cette page du [Tutoriel sur MDN](https://developer.mozilla.org/fr/docs/Web/SVG/Tutoriel/Formes_de_base)


##Intégration

Il peut être intégré à des pages web soit:

1. En appelant un fichier `svg` externe grâce à la balise `<img>`

```
<img src="image.svg">
```



2. Soit en intégrant directement le code `svg` dans le code `html` de la page grâce à la baise `<svg>`

```
<!doctype html>
<html>

  <body>

    <h1>Un dessin vectoriel en svg</h1>

    <svg width="200" height="200" style="background-color: lightgray;">
      <circle cx="50%" cy="50%" r="40%" stroke="green" stroke-width="3%" fill="yellow" />
    </svg>

  </body>

</html>

```

**RENDU:**

<svg width="200" height="200" style="background-color: lightgray;">
<circle cx="50%" cy="50%" r="40%" stroke="green" stroke-width="3%" fill="yellow" />
</svg>


#Dessin matriciel dans le `canvas`

La balise `<canvas>` qui fait partie de la spécification **HTML5** du *W3C* permet d'effectuer des rendus dynamiques d'images bitmap dans le navigateur grâce à des scripts `javascript`.

Pour utiliser les zones de dessin canvas, on ajoute un élément `<canvas>` vide dans le corps du document avec un id afin de pouvoir le modifier à partir du javascript.

##Code `html`

```
<canvas id="monCanvas" width="500" height="400">
	Votre navigateur ne  supporte pas la balise HTML5 Canvas.
</canvas>
```

*Le texte présent dans l'élément canvas n'est affiché que si le navigateur ne connait pas cette balise.*

##Code `javascript`

Nous allons maintenant dessiner dans ce `canvas` grâce à un script javascript qu'on intégrera comme n'importe quel code javascript(voir [Ajouter du dynamisme avec javascript]({filename}1-3-Ajouter du dynamisme avec javascript.md))

```
var theCanvas = document.getElementById("monCanvas");
var context = theCanvas.getContext("2d");

function drawScreen() {
    //background
    context.fillStyle = "#ffffaa";
    context.fillRect(0, 0, 500, 300);

    //text
    context.fillStyle = "#333333";
    context.font = "20px Sans-Serif";
    context.textBaseline = "top";
    context.fillText("Bienvenue dan sle monde du canvas", 195, 80);

    //box
    context.strokeStyle = "#000000";
    context.strokeRect(5, 5, 490, 290);

}

drawScreen();
```

Voici le code html complet:

```
<!doctype html>
<html lang="fr">

    <head>
        <meta charset="utf-8">
        <title>Dessin en canvas</title>
        <script type="text/javascript" charset="utf-8">
            window.onload = function() {

                var theCanvas = document.getElementById("monCanvas");
                var ctx = theCanvas.getContext("2d");

                function drawScreen() {
                    //background
                    ctx.fillStyle = "#ffffaa";
                    ctx.fillRect(0, 0, 500, 400);

                    //text
                    ctx.fillStyle = "#333333";
                    ctx.font = "18px Sans-Serif";
                    ctx.textBaseline = "top";
                    ctx.fillText("Bienvenue dans le monde du canvas", 95, 110);
                    //box
                    ctx.strokeStyle = "#000000";
                    ctx.strokeRect(5, 5, 490, 390);

                    //smiley
                    ctx.beginPath();
                    ctx.arc(250, 200, 50, 0, Math.PI * 2, true); // Tête
                    ctx.fillStyle = "#FFFF00";
                    ctx.fill(); // Colorier la tête en jaune
                    ctx.moveTo(285, 200);
                    ctx.arc(250, 200, 35, 0, Math.PI, false); // Bouche
                    ctx.moveTo(240, 190);
                    ctx.arc(235, 190, 5, 0, Math.PI * 2, true); // Oeil gauche
                    ctx.moveTo(270, 190);
                    ctx.arc(265, 190, 5, 0, Math.PI * 2, true); // Oeil droit

                    ctx.lineWidth = 5;
                    ctx.stroke();

                }

                drawScreen();

            }
        </script>
    </head>

    <body>

        <canvas id="monCanvas" width="500" height="400">
            Votre navigateur ne supporte pas la balise HTML5 Canvas.
        </canvas>

    </body>

</html>
```

**RENDU**
{% img center {filename}/images/HTML/canvas-smiley.png Rendu de l'élément canvas %}

Essayez modifier certains des paramètres du code pour vous familiariser avec sa syntaxe, puis ajouter des éléments en utilisant cette page de référence de [w3schools](http://www.w3schools.com/tags/ref_canvas.asp)

##Créer des animations
Pou animer un dessin canvas, nous allons utiliser la méthode `window.requestAnimationFrame()`, cette méthode permet d'éxecuter une fonction à chaque affichage de la fenêtre du navigateur(soit environ 60 images/seconde).

On crée ainsi une fonction `anime()` qui s'appelle elle-même à chaque rafraichissement de l'affichage.

```
// Création de la fonction
function anime() {
    requestAnimationFrame(anime);
    // Commandes de dessin
}

// Appel de la fonction pour lancer l'animation
anime();
```

Ensuite pour que l'affichage soit différent à chaque rafraichissement il faut que les commandes dessin utilisent des variables de coordonnées.

###Créer un monstre animé

Utiliser le lien suivant pour voir comment créer un dessin animé en utilisant des coordonnées aléatoires.

<http://jsbin.com/garagowe/14/edit>

###Déplacer un objet et détecter les bords pour qu'il rebondisse

Voici par exemple comment on peut dessiner le même smiley que tout à l'heure, mais à des coordonnées x et y, données en paramètres de la fonction. Grâce à cette fonction il suffira d'éxecuter `Smiley(60,70)` pour dessiner un smiley centré aux coordonnées `x = 60` et `y = 70`.

```
function Smiley(x, y) {
	this.x = x;
	this.y = y;

	this.dessineToi = function() {
		//smiley
		ctx.beginPath();
		ctx.arc(this.x, this.y, 50, 0, Math.PI * 2, true); // Tête
		ctx.fillStyle = "#FFFF00";
		ctx.fill(); // Colorier la tête en jaune
		ctx.moveTo(this.x + 35, this.y);
		ctx.arc(this.x, this.y, 35, 0, Math.PI, false); // Bouche
		ctx.moveTo(this.x - 10, this.y - 10);
		ctx.arc(this.x - 15, this.y - 10, 5, 0, Math.PI * 2, true); // Oeil gauche
		ctx.moveTo(this.x + 20, this.y - 10);
		ctx.arc(this.x + 15, this.y - 10, 5, 0, Math.PI * 2, true); // Oeil droit

		ctx.lineWidth = 5;
		ctx.stroke();
	};
```

On crée ensuite une méthode `deplaceToi` à l'objet  `Smiley`  qui ajoute `vx` à la coordonnée `x` et `vy` à la coordonnée `y` à chaque image.

Puis une fonction `checkWallCollision()` qui vérifie que le smiley ne touche pas les bords de l'écran, et qui inverse une des composante de la vitesse lorsque le smiley touche une paroi horizontale ou verticale.


###Code complet
```
<!doctype html>
<html lang="fr">

    <head>
        <meta charset="utf-8">
        <title>Dessin en canvas</title>
        <script type="text/javascript" charset="utf-8">
            window.onload = function() {
                // Variable qui correspond au canvas
                var monCanvas = document.getElementById("monCanvas");
                // Dimensions du canvas
                var width = monCanvas.width;
                var height = monCanvas.height;
                // contexte graphique 2D
                var ctx = monCanvas.getContext('2d');

                // Inititialisation des coordonnées et vitesses du smiley
                var smiley = new Smiley(width / 2, height / 2, (10 * Math.random()) - 5, (10 * Math.random()) - 5);

                // Lancement de l'animation
                anime();

                function anime() {
                    // 1) On dessine le fond du canvas
                    dessineFond();

                    // 2) On déplace le smiley
                    smiley.deplaceToi();

                    // 3) On regarde si le smiley touche un mur
                    checkWallCollision(smiley);

                    // 3) On dessine le smiley
                    smiley.dessineToi();

                    // On demande une nouvelle frame d'animation
                    window.requestAnimationFrame(anime);
                }

                function dessineFond() {
                    // On efface l'écran
                    ctx.clearRect(0, 0, monCanvas.width, monCanvas.height);

                    //background
                    ctx.fillStyle = "#ffffcc";
                    ctx.fillRect(0, 0, monCanvas.width, monCanvas.height);

                    //box
                    ctx.strokeStyle = "#000000";
                    ctx.strokeRect(5, 5, 490, 390);
                }

                // fonction smiley qui stocke ses coordonnées et sa vitesse
                // et qui possède deux méthodes pour se dessiner et se déplacer

                function Smiley(x, y, vx, vy) {
                    this.x = x;
                    this.y = y;
                    this.vx = vx;
                    this.vy = vy;
                    this.radius = 50;

                    this.dessineToi = function() {
                        //smiley
                        ctx.beginPath();
                        ctx.arc(this.x, this.y, 50, 0, Math.PI * 2, true); // Tête
                        ctx.fillStyle = "#FFFF00";
                        ctx.fill(); // Colorier la tête en jaune
                        ctx.moveTo(this.x + 35, this.y);
                        ctx.arc(this.x, this.y, 35, 0, Math.PI, false); // Bouche
                        ctx.moveTo(this.x - 10, this.y - 10);
                        ctx.arc(this.x - 15, this.y - 10, 5, 0, Math.PI * 2, true); // Oeil gauche
                        ctx.moveTo(this.x + 20, this.y - 10);
                        ctx.arc(this.x + 15, this.y - 10, 5, 0, Math.PI * 2, true); // Oeil droit

                        ctx.lineWidth = 5;
                        ctx.stroke();
                    };

                    this.deplaceToi = function() {

                        this.x += this.vx;
                        this.y += this.vy;
                    };
                }

                function checkWallCollision(objet) {
                    if (objet.x < objet.radius) {
                        objet.x = objet.radius;
                        objet.vx *= -1;
                    }
                    if (objet.x > width - (objet.radius)) {
                        objet.x = width - (objet.radius);
                        objet.vx *= -1;
                    }
                    if (objet.y < objet.radius) {
                        objet.y = objet.radius;
                        objet.vy *= -1;
                    }
                    if (objet.y > height - (objet.radius)) {
                        objet.y = height - (objet.radius);
                        objet.vy *= -1;
                    }
                }


            }
        </script>
    </head>

    <body>

        <canvas id="monCanvas" width="500" height="400">
            Votre navigateur ne supporte pas la balise HTML5 Canvas.
        </canvas>

    </body>

</html>
```

**RENDU**
*Attention ce rendu est une vidéo de capture d'écran à 15 image par seconde, le rendu réél est beaucoup plus fluide et continu.*

 <video autoplay loop id="myVideo" src="{filename}/images/HTML/smiley.webm" type="video/webm">
	Votre navigateur ne supporte pas les vidéos.
</video>

<script type="text/javascript" charset="utf-8">
// script permettant de tourner en boucle car loop marche pas
var myVideo = document.getElementById('video');
if (typeof myVideo.loop == 'boolean') { // loop supported
    myVideo.loop = true;
} else { // loop property not supported
    myVideo.on('ended', function () {
    this.currentTime = 0;
    this.play();
    }, false);
}
myVideo.play();
</script>
