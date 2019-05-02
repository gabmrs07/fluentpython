"""
    https://docs.python.org/3/reference/datamodel.html

    O << data model >> é como uma descrição de Python como um alicerce de fundação. Ele
formaliza a interface da construção de blocos dentro da própria linguagem, como sequences,
iterators, functions, classes, context managers, etc.

    Ao se escrever um código, utiliza-se uma grande quantidade de tempo para se implementar
métodos que são chamados por esse alicerce de fundação da linguagem. O interpretador do
Python invoca métodos especiais que atuam como operações de objetos básicas, frequentemente
acionadas por uma síntaxe especial. Os nomes de métodos especiais são sempre escritos com
prefixos e sufixos de duplos underlines (e. g. __getitem__). Por exemplo, a síntaxe << obj[key] >>
é suportada pelo método especial __getitem__. Quando se executa << my_collection[key] >>, o
interpretador chama << my_collection.__getitem__(key) >>.

    Os nomes de métodos especiais, chamados usualmente de << magic methods >> ou
<< dunder methods >>, permitem seus objetos a implementar, suportar e interagir com construções
básicas da linguagem como: iteration, collections, attribute access, operator overloading,
function and method invocation, object creation and destruction, string representation and
formatting, managed contexts (i. e., with blocks).

"""

"Exemplo 1-1: é uma classe que representa um deck of playing cards."

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __contains__(self, item):
        return item in self._cards

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

"__len__ permite que se chame len() duma instância da classe FrenchDeck"
print(len(deck))

"__getitem__ permite o uso de deck[item] e o uso de slicings"
print(deck[13])
print(deck[0:3])
print(deck[12::13])

"__getitem__ também transforma self._cards em iterable"
for card in deck:
    print('loop:', card)
for card in reversed(deck):
    print('reversed:', card)

"""
Para confirmação de membership em um iterable, o interpretador faz o seguinte movimento:
se __contains__ não está definido, então se faz uma busca em __iter__; e, se a
tentativa é frustrada, passa a __getitem__.
Cf. https://docs.python.org/3/reference/expressions.html#membership-test-details
"""
if Card('Q', 'spades') in deck:
    print('Q of spades is in deck')
if Card('Q', 'dogs') not in deck:
    print("Q of dogs isn't in deck")

"""
Pode-se agrupar facilmente o baralho de cartas de modo que os ases sejam as cartas mais
valorosas e os naipes sejam ordenados na importância a seguir: spades, hearts, diamonds, clubs.
"""
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    """
    Esta função retorna um número único de comparação para sorted().
    rank_index vai de 0 a 12
    rank_index * 4 (que é o total de elementos da lista de naipes) gera isto:
    rank_value = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
    rank_value + suit_values[spades v hearts v diamonds v clubs] gera um número único dentro
    do intervalo dum múltiplo de 4; p. ex.:
    0 + suit_values[clubs] = 0       > 2 of clubs
    0 + suit_values[diamonds] = 1    > 2 of diamonds
    0 + suit_values[hearts] = 2      > 2 of hearts
    0 + suit_values[spades] = 3      > 2 of spades
    4 + suit_values[clubs] = 4       > 3 of clubs
    4 + suit_values[diamonds] = 5    > 3 of diamonds
    ...
    """
    rank_index = FrenchDeck.ranks.index(card.rank)
    rank_value = rank_index * len(suit_values)
    return rank_value + suit_values[card.suit]

for card in sorted(deck, key = spades_high):
    print(card)

print(Card('Q', 'clubs') in deck)
