
#Vocab
vocab_set = {}
vocab_set["3-letter"] = []
vocab_set["6-letter"] = []
vocab_set["8-letter"] = []
vocab_set["unknown"] = []

s1 = ['ACE', 'AID', 'ALL', 'BUG', 'BOX', 'CAT', 'COW', 'DIG', 'ELF', 'FOE', 'BOOK', 'CURE',
      'CARD', 'DOCK', 'EGG', 'FARM', 'FIRE', 'GOLD', 'ICE', 'JAW', 'KING', 'KITE', 'LOVE', 'LOST',
      'MOON', 'MAP', 'JAZZ', 'LIE', 'NICE', 'NEW', 'OAT', 'ODD', 'PIG', 'POUR', 'RAT', 'RUSH', 'STAR',
      'SIT', 'TOUR', 'TOY', 'TEN', 'UNIT', 'VAN', 'WIN', 'ZAP']

s2 = ['AURORA', 'BOUGHT', 'BRIGHT', 'CATCH', 'DROUGHT', 'EVOLVE', 'EIGHT', 'FLOWER',
      'GHOST', 'HAUNTED', 'GLOBAL', 'GOVERN', 'HAVOCS', 'INDEED', 'INSERT', 'JUNGLE',
      'KRAKEN', 'KITTEN', 'LABORS', 'MARGIN', 'NORMAL', 'NUMBER', 'ORDERS', 'OUTFIT',
      'PASSED', 'QUOTES', 'QUIVER', 'RANDOM', 'RISKED', 'SEIZES', 'SHAMAN', 'TATTOO',
      'UNPLUG', 'VALVED', 'WAFFLE', 'WHIRLS', 'XYLEM', 'YOGURT', 'ZIPPER', 'PYTHON']


s3 = ['ASHGABAT', 'BRASILIA', 'BUDAPEST', 'CANBERRA', 'DAMASCUS', 'KINGSTON', 'PRISTINA',
      'TIRASPOL', 'VICTORIA', 'ETHIOPIA', 'MONGOLIA', 'SCOTLAND', 'THAILAND', 'ZIMBABWE',
      'ILLINOIS', 'MICHIGAN', 'CHINESE', 'STARLORD', 'JAMESTOWN', 'SINGAPORE', 'STOCKHOLM',
      'KINGSTOWN', 'JERUSALEM', 'BANGALORE', 'HIROSHIMA', 'ARGENTINA', 'VENEZUELA',
      'LITHUANIA', 'GLASGOW', 'ORANJESTAD', 'BRATISLAVA']

s4 = ['AP', 'FF' ,'BA', 'PM', 'RT', 'HG', 'FD', 'BP', 'PL', 'CX', 'ZM', 'PZ', 'LA',
      'BV', 'PK', 'QJ', 'JQ', 'DC', 'ZA', 'TY', 'HJ', 'CR']

try :
    for i in s1 :
        vocab_set["3-letter"].append(i)
    for i in s2 :
        vocab_set["6-letter"].append(i)
    for i in s3 :
        vocab_set["8-letter"].append(i)
    for i in s4 :
        vocab_set["unknown"].append(i)
except :
    print("Error Occured")
    running = False
    
