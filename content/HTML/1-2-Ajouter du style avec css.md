Title:  Ajouter du style avec css
date: 2014-11-04
modified: 2015-10-09
Chapitre: 1
series:  Créer des pages web en html5
series_index: 2
Tags: icn, html5, css, w3c

<a title="Par W3C (http://www.w3.org/html/logo/) [CC-BY-3.0 (http://creativecommons.org/licenses/by/3.0)], via Wikimedia Commons" href="http://commons.wikimedia.org/wiki/File%3AClass-header-css3.jpg"><img width="256" alt="Class-header-css3" src="//upload.wikimedia.org/wikipedia/commons/5/52/Class-header-css3.jpg"/></a>

> Les feuilles de style en cascade, généralement appelées CSS de l'anglais Cascading Style Sheets, forment un langage informatique qui décrit la présentation des documents HTML et XML. Les standards définissant CSS sont publiés par le World Wide Web Consortium (W3C). Introduit au milieu des années 1990, CSS devient couramment utilisé dans la conception de sites web et bien pris en charge par les navigateurs web dans les années 2000. [Source Wikipedia](https://fr.wikipedia.org/wiki/Feuilles_de_style_en_cascade)



#Syntaxe

Une règle css est constituée d'un sélecteur suivi d'un bloc de déclaration entre accolades. Chaque déclaration se termine par un point-virgule.

*exemple*
```
p {
    color: red;
    text-align: center;
}
```
Cette règle permet de colorier en rouge et de centrer tous les balise `<p>` du document html.

Il est possible de sélectionner plusieurs éléments en les séparant par des virgules.

Les commentaires utilisent la syntaxe suivante: `/* Un commentaire */`

#Intégration de code css dans une page html

Il existe trois façons d'insérer une feuille de style au sein d'un document html:

##Insertion directe dans les balises html

On utilise alors l'attribut style au sein de la balise ouvrante de l'élément à styler.

```
 <h1 style="color:blue; margin-left:30px;">This is a heading.</h1>
```
*Cette méthode est peu recommandée en raison du but même la définition des langages html et css qui est de séparer le fond et la forme.*

##Utilisation d'une feuille de style interne

On intègre le code css au sein de balises `<style>` dans l'entête du document(le <head>).

```
<head>
    <style>
        body {
        background-color: linen;
        }
    h1 {
        color: maroon;
        margin-left: 40px;
        }
    </style>
</head>
```

*Méthode pratique lorsque l'on a des documents html d'une seule page ou avec des styles spécifiques.*

##Utilisation d'une feuille de style externe

on écrit le code css dans un fichier avec l'extension `.css` et on l'appelle dans l'entête du document(le <head>).

```
<head>
    <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

C'est la méthode préférée lorsque l'on a un ensemble de pages qui contiennent des styles identiques, cela permet d'alléger l'écriture du code et les requêtes vers le serveur de documents.

#Ordre d'application des règles

Ce n'est pas pour rien qu'on parle de feuilles de styles en cascade, car en fait la difficulté en css est souvent que l'on définit des règles différentes pour des tags identiques, et qu'il faut savoir qu'elle règle va s'appliquer sur notre élément.

Par ordre de priorité croissante:

- Règles par défaut du navigateur
- Feuille de style externe
- Feuille de style interne
- Style au sein d'un élément html.

#Sélecteurs plus élaborés
- Il est possible de sélectionner **plusieurs balises** à la fois pour leur appliquer une règle commune, ces balises doivent alors être séparées par des *virgules*.

  h1, h2, h3 {color: lime;}

- La virgule est très importante, car si on sépare les sélecteurs par des *espaces* il s'agit d'une **sélection par descendence**, le code css suivant par exemple ne sélectionne que les paragraphes contenus dans une balise `div`([voir mdn pour plus de détails](https://developer.mozilla.org/fr/docs/Web/CSS/S%C3%A9lecteurs_descendant)).

  div p {background-color: red;}

- Pour appliquer *un même style à plusieurs éléments* on peut leur ajouter un attribut html `class="class-name"`, qui pourra être sélectionné en css avec le sélecteur `.class-name`.

**Code html**

```
<h2 class="souligne">Un titre de niveau 2 avec la classe souligne</h2>
<p>Un paragraphe normal</p>
<h2>Un titre de niveau 2 normal</h2>
<p class="souligne">Un paragraphe avec la classe souligne</p>
```

**Code css**
```
.souligne {
text-decoration: underline;
}
```

**Rendu**
<h2 style="text-decoration: underline;">Un titre de niveau 2 avec la classe souligne</h2>
<p>Un paragraphe normal</p>
<h2>Un titre de niveau 2 normal</h2>
<p style="text-decoration: underline;">Un paragrapĥe avec la classe souligne</p>

- Pour appliquer *un style specifique à un unique élément* on lui ajoute un attribut html `id="id-name"`, qui pourra être sélectionné en css avec le sélecteur `#id-name`.

#Des styles plus élaborés
##Références des propriétés `css`
Cette référence CSS sur [MDN](https://developer.mozilla.org/fr/docs/Web/CSS/Reference) liste toutes les propriétés standards CSS.

##Tutoriels et exemples en ligne
Le site [w3cschools](http://www.w3schools.com/css/css_examples.asp) présente des exemples éditables et dynamiques de situations courantes lors du stylage d'une page web, voir notamment les pages suivantes:
  

- [CSS Backgrounds](http://www.w3schools.com/css/css_background.asp) et [CSS3 Backgrounds](http://www.w3schools.com/css/css3_backgrounds.asp) pour les **arrières plans**
- [CSS Text](http://www.w3schools.com/css/css_text.asp), [CSS Fonts](http://www.w3schools.com/css/css_font.asp) et [CSS3 Fonts](http://www.w3schools.com/css/css3_fonts.asp) pour la **mise en forme du texte**
- [CSS Lists](http://www.w3schools.com/css/css_list.asp) pour les **listes** numérotées on non.
- [CSS Box Model](http://www.w3schools.com/css/css_boxmodel.asp) et [CSS3 Borders](http://www.w3schools.com/css/css3_borders.asp) pour les modèles de **boîtes**
- [CSS3 Transitions](http://www.w3schools.com/css/css3_transitions.asp) et [CSS3 Animations](http://www.w3schools.com/css/css3_animations.asp) pour des effets **dynamiques** sur vos pages.

#Déboguer son code css
##Inspecteur de styles du navigateur
Pour savoir qu'elle règle a été utilisée par le navigateur, la console web du navigateur est d'un grand secours. On peut par exemple inspecter un élément et savoir qu'elles règles css s'appliquent et qu'elles règles css ont été suplantés.

Pour accéder à la console web, taper <kbd>CTRL+MAJ+K</kbd> sur firefox, pour inspecter un élément il suffit de le sélectionner et de faire un click droit de la souris puis de taper <kbd>x</kbd>.

##Validateur du w3c
Le site du w3c propose comme pour le language html un (validateur)[http://jigsaw.w3.org/css-validator/#validate_by_input+with_options] de fichier css:
