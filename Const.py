SUITS = ['H', 'D', 'C', 'S', ]
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
PRINTED = {'ace':
               """*Ace*""",
           'king':
               """*King*""",
           'queen':
               """*Queen*""",
           'jack':
               """*Jack*"""}

MESSAGES = {
    'ask_start': 'Want to play?(y/n) ',
    'ask_card': 'Want new card?(y/n)',
    'eq' : '{player} player has {points} points so it eq with dealer points\n {player} bid will be back',
    'win' : '{} player are win',
    'lose': '{} player are lose'
}