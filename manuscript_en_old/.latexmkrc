# Utiliser pdflatex pour la compilation
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';

# Utiliser biber comme backend bibliographique
$bibtex_use = 2;

# Commande biber avec encodage UTF-8
$biber = 'biber --input-encoding=utf8 %O %S';

# Nombre de passes nécessaires pour mettre à jour les références
$clean_ext .= ' bbl bcf blg run.xml';