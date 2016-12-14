class Bot(object):
    def __init__(self,id,exec_chain):
        self.id = id
        self.chips = []
        self.givelo = None
        self.givehi = None
        self.responsibility = []
        self.exec_chain = exec_chain
    def addChip(self,c):
        if len(self.chips) < 2:
            self.chips.append(c)
        if len(self.chips) == 2:
            self.exec_chain.append(self.id)
    def removeChip(self,c):
        if len(self.chips) > 0:
            ind = self.chips.index(c)
            del self.chips[ind]
    def clear(self):
        self.chips = []
        self.givelo = None
        self.givehi = None
    def hi(self):
        return max(self.chips)
    def lo(self):
        return min(self.chips)
    def giveHi(self,b):
        self.givehi = b
    def giveLo(self,b):
        self.givelo = b
    def execute(self):
        print 'executing'
        self.responsibility = self.chips[:]
        self.givelo.addChip(self.lo())
        self.givehi.addChip(self.hi())
        self.clear()


BOTS = {}
OUTPUTS = {}
EXECUTION = []
file = 'input.txt'
def checkCollection(col,id,exec_chain):
    if not id in col:
        col[id] = Bot(id,exec_chain)

def retId(b):
    if b:
        return b.id
    return None

def dispBots(bots):
    for b in bots:
        print b,bots[b].chips,bots[b].responsibility,retId(bots[b].givelo),retId(bots[b].givehi)

with open(file) as f:
    for l in f:
        l = l.strip()
        data = l.split(' ')
        if data[0] == 'value':
            print l
            c = int(data[1])
            b = int(data[5])
            # check if there is a bot
            checkCollection(BOTS,b,EXECUTION)
            BOTS[b].addChip(c)
        if data[0] == 'bot':
            print l
            b = int(data[1])
            lo = data[5]
            lb = int(data[6])
            ho = data[10]
            hb = int(data[11])
            print b,lo,lb,ho,hb
            # does bot even exist
            checkCollection(BOTS,b,EXECUTION)
            # check if there is a bot
            if lo == 'bot':
                checkCollection(BOTS,lb,EXECUTION)
                BOTS[b].giveLo(BOTS[lb])
            else:
                checkCollection(OUTPUTS,lb,EXECUTION)
                BOTS[b].giveLo(OUTPUTS[lb])
            if ho == 'bot':
                checkCollection(BOTS,hb,EXECUTION)
                BOTS[b].giveHi(BOTS[hb])
            else:
                checkCollection(OUTPUTS,hb,EXECUTION)
                BOTS[b].giveHi(OUTPUTS[hb])
                
for b in EXECUTION:
    BOTS[b].execute()   

dispBots(BOTS)
dispBots(OUTPUTS)