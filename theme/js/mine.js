/*
 * Configuration de Mathjax
 * Inspire de mathjaxutils.js de ipython
 */
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [
            ['$', '$'],
            ["\\(", "\\)"]
        ],
        displayMath: [
            ['$$', '$$'],
            ["\\[", "\\]"]
        ],
        processEscapes: true,
        processEnvironments: true
    },
    // Center justify equations in code and markdown cells. Elsewhere
    // we use CSS to left justify single line equations in code cells.
    displayAlign: 'center',
    "HTML-CSS": {
        styles: {
            '.MathJax_Display': {
                "margin": 0
            }
        },
        linebreaks: {
            automatic: true
        }
    }
});
MathJax.Hub.Configured();

/*
 * Table des matières automatique
 * http://css-tricks.com/automatic-table-of-contents/
 */
$(document).ready(function() {

    var ToC =
        '<nav role="navigation" class="table-of-contents">' +
        '<h2>Sommaire</h2>' +
        '<ul>';

    var newLine, el, title, link;

    $('article h1').each(function() {

        el = $(this);
        title = el.text();
        link = '#' + el.attr('id');

        newLine = '<li>' + '<a href=' + link + '>' + title + '</a>' + '</li>';

        ToC += newLine;

    });

    ToC +=
        '</ul>' +
        '</nav>';

    $('#toc').append(ToC);
    console.log(ToC);

});
