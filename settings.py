#size
APP_SIZE = (400,700)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

#text
FONT = 'helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {'gap': 0.5,'corner-radius': 0}

NUM_POSITIONS = {
    '.':{'col': 2,'row': 6,'span': 1},
    '0':{'col': 0,'row': 6,'span': 2},
    '1':{'col': 0,'row': 5,'span': 1},
    '2':{'col': 1,'row': 5,'span': 1},
    '3':{'col': 2,'row': 5,'span': 1},
    '4':{'col': 0,'row': 4,'span': 1},
    '5':{'col': 1,'row': 4,'span': 1},
    '6':{'col': 2,'row': 4,'span': 1},
    '7':{'col': 0,'row': 3,'span': 1},
    '8':{'col': 1,'row': 3,'span': 1},
    '9':{'col': 2,'row': 3,'span': 1}
}

MATH_POSITIONS = {
    '/':{'col': 3,'row': 2,'character': '/','operator':'/'},
    '*':{'col': 3,'row': 3,'character': 'X','operator':'*'},
    '-':{'col': 3,'row': 4,'character': '-','operator':'-'},
    '=':{'col': 3,'row': 6,'character': '=','operator':'='},
    '+':{'col': 3,'row': 5,'character': '+','operator':'+'}
}

OPERATORS = {
    'clear':{'col': 0,'row': 2,'text': 'AC','operator':'/'},
    'invert':{'col': 1,'row': 2,'text': '±','operator':'/'},
    'percent':{'col': 2,'row': 2,'text': '%','operator':'/'}
}

COLORS = {
    'light-gray':{'fg': ('#505050','#D4D4D2'),'hover': ('#686868','#efefed'),'text': ('white','black')},
    'dark-gray':{'fg': ('#D4D4D2','#505050'),'hover': ('#efefed','#686868'),'text': ('black','white')},
    'orange':{'fg': '#ff9500','hover': '#ffb143','text': ('black','white')},
    'orange-highlight':{'fg': 'white','hover': 'white','text': ('black','#FF9500')}
}

TITLE_BAR_HEX_COLORS = {
    'dark':0x00000000,
    'light':0x00EEEEEE
}

BLACK = '#000000'
WHITE = '#EEEEEE'