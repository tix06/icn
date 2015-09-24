Title:  Structure d'un document html
date: 2014-11-04
modified: 2015-09-24
Chapitre: 1
series:  Créer des pages web en html5
series_index: 1
Tags: icn, html5, w3c

<a title="W3C [CC-BY-3.0 (http://creativecommons.org/licenses/by/3.0)], via Wikimedia Commons" href="http://commons.wikimedia.org/wiki/File%3AHTML5_logo_and_wordmark.svg"><img width="256" alt="HTML5 logo and wordmark" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/256px-HTML5_logo_and_wordmark.svg.png"/></a>

> HTML5 (HyperText Markup Language 5) est la dernière révision majeure d'HTML (format de données conçu pour représenter les pages web).

> Dans le langage courant, HTML5 désigne souvent un ensemble de technologies Web (HTML5, CSS3 et JavaScript) permettant notamment le développement d'applications (cf. DHTML). [Source Wikipedia](https://fr.wikipedia.org/wiki/HTML5)

Vous pouvez afficher le code html d'une page web, en cliquant droit sur celle-ci et en choisissant `Afficher le code source de la page`, ou en utilisant sur Mozilla le raccourci: <kbd>CTRL+U</kbd>.

#Balises et attributs
## Balises
Le langage html utilise des balises pour indiquer le sens sémantique des éléments d'une page. Ces balises ou tags permettent de construire une hiérarchie au sein du document appelée DOM(Document Object Model)

Ces balises sont référencées sur le site [MDN](https://developer.mozilla.org/fr/docs/Web/HTML/Element)

*Par exemple:*

- les balises de titre (headings) `<h1>...</h1>` jusqu'à  `<h6>...</h6>` permettent d'utiliser jusqu'à six niveaux de titres dans la page.

- la balise de paragraphe `<p>...</p>`.

- la balise d'ancre `<a>...</a>` permet de créer un lien hypertexte.

- les balises `<div>...</div>` permettent d'englober plusieurs autres éléments, ce sont des conteneurs qui permettent de rassembler ensemble divers éléments.

Certaines balises sont auto-fermantes c'est à dire qu'elles ne présentent pas de balises fermantes. Par exemple la balise d'image `<img>`.

*Remarque: habituellement, on écrit les balises en minuscules.*

## Les attributs d'une balise

Les balises ouvrantes peuvent contenir des attributs permettant de préciser certains éléments relatifs au contenu de la balise.

Par exemple, une balise d'ancre `<a>` doit obligatoirement spécifier l'attribut `href="..."` qui donne la cible du lien à viser lorsque l'utilisateur clique sur le texte de l'ancre.

```
<a href="https://duckduckgo.com/">Un moteur de recherche alternatif</a>
```
*s'affichera*

<a href="https://duckduckgo.com/">Un moteur de recherche alternatif</a>


Autre exemple, la balise `<img>` doit obligatoirement spécifier les attributs `src` et `alt` de notre image.

- `src`: adresse de l'image.
- `alt`: texte à afficher si la source ne peut-être trouvée.

```
<img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Mozilla_Aurora_icon.png" alt="Mozilla Aurora icon"/>
```
*s'affichera*

<img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Mozilla_Aurora_icon.png" alt="Mozilla Aurora icon"/>


## Imbrications des balises

> Les balises ouvrantes et fermantes doivent toujours être correctement imbriquées, c'est à dire que les balises fermantes doivent êtres écrites dans l'ordre inverse des balises d'ouverture. Une bonne imbrication des balises est une des règles à respecter afin d'avoir un code valide.
[Source MDN](https://developer.mozilla.org/fr/docs/Web/Guide/HTML/Introduction#Les_balises)

Voici un exemple de code valide :

```
<p>Ceci est <strong>très</strong> important</p>.
```

Voici un exemple de code non-valide :

```
<em>Ceci est <strong>très</em> important</strong>.
```

# Structure minimale d'un fichier html

Le fichier doit commencer par le doctype html `<!doctype html>`

L'ensemble du document est imbriqué à l'intérieur de balises `<html>`

La balise `html` possède deux balises filles:

- la balise `<head>` qui contient des informations telles que le titre ou l'encodage des caractères de la page qui ne sont pas affichées mais qui sont utiles au navigateur pour le rendu ou encore aux moteurs de recherche pour l'indexation de votre page.
- la balise `<body>` qui contient l'ensemble du **code à afficher** lors du rendu.

# Exemple de fichier `html` minimal

*L'indentation n'est pas obligatoire, mais elle rend le fichier plus lisible.*

```
<!doctype html>
<html lang="fr">

  <head>
    <meta charset="utf-8" />
    <title>Un document minuscule</title>
  </head>

  <body>
    <h1>Titre principal de mon document</h1>
    <!-- Ceci est un commentaire -->
    <p>Regarde maman, je suis en train de coder en <abbr title="Hyper Text Markup Language" lang="en">HTML</abbr> !</p>
  </body>

</html>
```

# Validation et nettoyage de votre page web

Pour vérifier si votre code html est valide, et être informés sur les erreurs et recommandations, on peut utiliser le validateur html5 mis au point par la fondation mozilla:

<https://html5.validator.nu/>

Vous pouvez même nettoyer votre code et le réindenter avec l'outil en ligne suivant:

<http://jsbeautifier.org/>
