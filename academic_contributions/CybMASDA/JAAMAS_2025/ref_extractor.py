import re

# Fichiers à définir
tex_file = "article.tex"
bib_file = "references.bib"
out_bib_file = "filtered_references.bib"

# Étape 1 : extraire les clés des \cite
with open(tex_file, 'r', encoding='utf-8') as f:
    tex_content = f.read()

# Regex pour capturer toutes les clés citées
cite_keys = set(re.findall(r'\\cite\{([^\}]+)\}', tex_content))
# Gérer les cas de \cite{key1, key2}
cite_keys = set([key.strip() for group in cite_keys for key in group.split(',')])

print(f"Nombre de clés citées trouvées : {len(cite_keys)}")

# Étape 2 : filtrer le fichier .bib
with open(bib_file, 'r', encoding='utf-8') as f:
    bib_content = f.read()

# Séparer les entrées bibtex
entries = re.split(r'@', bib_content)
entries = ['@' + e for e in entries if e.strip()]

# Garder uniquement les entrées correspondant aux clés citées
filtered_entries = []
for entry in entries:
    match = re.match(r'@(\w+)\{([^,]+),', entry)
    if match:
        key = match.group(2).strip()
        if key in cite_keys:
            filtered_entries.append(entry)

# Sauvegarde du fichier filtré
with open(out_bib_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(filtered_entries))

print(f"Nombre de références extraites : {len(filtered_entries)}")
