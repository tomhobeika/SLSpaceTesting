from tkinter.messagebox import RETRY


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ', '\n']
swears = ['arse\n', 'arsehole\n', 'balls\n', 'bastard\n', 'beef curtains\n', 'bellend\n','berk\n', 'bint\n', 'bitch\n', 'blighter\n', 'blimey\n', "blimey o'reilly\n", 'bloodclaat\n', 'bloody\n', 'bloody hell\n', 'blooming\n', 'bollocks\n', 'bonk\n', 'bugger\n', 'bugger me\n', 'bugger off\n', 'bukkake\n', 'bullshit\n', 'cack\n', 'cad\n', 'chav\n', 'choad\n', 'chuffer\n', 'clunge\n', 'cobblers\n', 'cock\n', 'cock cheese\n', 'cock jockey\n', 'cock-up\n', 'cock\n', 'cockwomble\n', 'codger\n', 'cor blimey\n', 'corey\n', 'crap\n', 'crikey\n', 'cunt\n', 'damn\n', 'dick\n', 'dickhead\n', 'dildo\n', 'duffer\n', 'fanny\n', 'feck\n','fuck\n', 'fucking cunt\n', 'fucktard\n', 'git\n', 'gob shite\n', 'goddam\n', 'gorblimey\n', 'gordon bennett\n', 'gormless\n', 'hell\n', 'jesus christ\n', 'jizz\n', 'ligger\n', 'manky\n', 'minge\n', 'minger\n', 'minging\n', 'motherfucker\n', 'munter\n', 'muppet\n', 'naff\n', 'nitwit\n', 'nonce\n', 'numpty\n', 'nutter\n', 'penguin\n', 'pillock\n', 'pish\n', 'piss off\n', 'pissed\n', 'piss\n', 'plonker\n', 'ponce\n', 'poof\n', 'pouf\n', 'poxy\n', 'prat\n', 'prick\n', 'prick\n', 'prickteaser\n', 'punani\n', 'punny\n', 'pussy\n', 'randy\n', 'rapey\n', 'rape\n', 'nigger\n','nigga\n', 'rotter\n', 'shag\n', 'shit\n', 'shite\n', 'shitfaced\n', 'skank\n', 'slag\n', 'slut\n', 'snatch\n', 'sod\n', 'sod-off\n','spunk\n', 'tart\n', 'tits\n', 'toff\n', 'tosser\n', 'trollop\n', 'tuss\n', 'twat\n', 'twonk\n', 'wally\n', 'wanker\n', 'wank\n', 'wazzack\n', 'whore\n']

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def has_special(inputString):
    return any(char not in letters for char in inputString)

def is_swear(inputString):
    return any(inputString in word for word in swears)

words = open("MIT_Wordlist.txt", "r")
lines = words.readlines()
lines.sort()

print("Initial Lines: "+str(len(lines)))

revisedWords = []

w = open("playerWordlist.txt", "w")

out = ""
for x in lines:
    if has_numbers(x):
        continue
    if has_special(x):
        continue
    if is_swear(x):
        continue
    out=out+x
#out = out.replace('\n','')+']'
w.write(out)
w.close

revised = open("revisedWordsMIT.txt", "r")
lines = revised.readlines()

print("After Processing: "+str(len(lines)))



