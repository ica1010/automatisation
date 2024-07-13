import re  # Importation du module des expressions régulières

# Spécifications des tokens avec des expressions régulières
token_specification = [
    ('Nombre',   r'\d+'),                  # Reconnaître les nombres entiers
    ('Identifient', r'[A-Za-z][A-Za-z0-9]*'), # Reconnaître les identificateurs (lettres suivies de chiffres optionnels)
    ('Operateur', r'[+\-*/=]'),            # Reconnaître les opérateurs arithmétiques incluant '='
    ('Parenthese_ouvrente', r'\('),        # Reconnaître la parenthèse ouvrante '('
    ('Parenthse_fermente', r'\)'),         # Reconnaître la parenthèse fermante ')'
    ('Tabulation', r'[ \t]'),              # Reconnaître les espaces et tabulations
    ('Expression_inconnue', r'.'),         # Reconnaître tout caractère non défini ci-dessus
]

# Regrouper les expressions régulières en une seule
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def tokenize(code):
    """
    Analyse une expression pour identifier les identificateurs, nombres et opérateurs.

    :param code: Chaîne de caractères contenant l'expression à analyser
    :return: Liste des tokens générés, chaque token est un tuple (type_de_token, valeur)
    """
    tokens = []  # Liste pour stocker les tokens
    for match in re.finditer(token_regex, code):  # Itérer sur chaque correspondance trouvée dans l'expression
        kind = match.lastgroup  # Obtenir le type de token trouvé
        value = match.group()   # Obtenir la valeur du token trouvé
        if kind == 'Nombre':
            tokens.append((kind, int(value)))  # Ajouter un nombre comme entier
        elif kind in ('Identifient', 'Operateur', 'Parenthese_ouvrente', 'Parenthse_fermente'):
            tokens.append((kind, value))  # Ajouter les autres types de tokens
        elif kind == 'Tabulation':
            continue  # Ignorer les espaces et tabulations
        elif kind == 'Expression_inconnue':
            raise RuntimeError(f'{value} est une expression inconnue')  # Gérer les caractères non reconnus
    return tokens  # Retourner la liste des tokens
