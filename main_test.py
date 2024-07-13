import unittest
from main import tokenize
import unittest  # Importation du module de test unitaire

class TestLexer(unittest.TestCase):

    def test_identificateurs(self):
        """Tester la reconnaissance des identificateurs"""
        self.assertEqual(tokenize('a'), [('Identifient', 'a')])  # Tester un identifiant simple
        self.assertEqual(tokenize('variable1'), [('Identifient', 'variable1')])  # Tester un identifiant avec des chiffres
        self.assertEqual(tokenize('x2y'), [('Identifient', 'x2y')])  # Tester un identifiant avec chiffres au milieu

    def test_nombres(self):
        """Tester la reconnaissance des nombres entiers"""
        self.assertEqual(tokenize('123'), [('Nombre', 123)])  # Tester un nombre simple
        self.assertEqual(tokenize('007'), [('Nombre', 7)])  # Tester un nombre avec des zéros initiaux

    def test_operateurs(self):
        """Tester la reconnaissance des opérateurs arithmétiques"""
        self.assertEqual(tokenize('+'), [('Operateur', '+')])  # Tester l'opérateur '+'
        self.assertEqual(tokenize('-'), [('Operateur', '-')])  # Tester l'opérateur '-'
        self.assertEqual(tokenize('*'), [('Operateur', '*')])  # Tester l'opérateur '*'
        self.assertEqual(tokenize('/'), [('Operateur', '/')])  # Tester l'opérateur '/'
        self.assertEqual(tokenize('='), [('Operateur', '=')])  # Tester l'opérateur '='

    def test_parentheses(self):
        """Tester la reconnaissance des parenthèses"""
        self.assertEqual(tokenize('('), [('Parenthese_ouvrente', '(')])  # Tester la parenthèse ouvrante '('
        self.assertEqual(tokenize(')'), [('Parenthse_fermente', ')')])  # Tester la parenthèse fermante ')'

    def test_expression_complexe(self):
        """Tester la reconnaissance d'une expression complexe"""
        expression = 'a = 5 + 3 * (b - 2)'  # Expression complexe à analyser
        tokens_attendus = [
            ('Identifient', 'a'), ('Operateur', '='), ('Nombre', 5), ('Operateur', '+'),
            ('Nombre', 3), ('Operateur', '*'), ('Parenthese_ouvrente', '('), ('Identifient', 'b'),
            ('Operateur', '-'), ('Nombre', 2), ('Parenthse_fermente', ')')
        ]
        self.assertEqual(tokenize(expression), tokens_attendus)  # Comparer le résultat de la tokenisation avec les tokens attendus

    def test_erreurs(self):
        """Tester la gestion des caractères non reconnus"""
        with self.assertRaises(RuntimeError):  # Vérifier qu'une erreur est levée pour un caractère inconnu
            tokenize('a @ b')  # '@' est un caractère inconnu

if __name__ == '__main__':
    unittest.main()  # Exécuter les tests si ce fichier est exécuté directement
