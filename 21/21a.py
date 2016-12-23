import numpy as np

# INITIAL_PASSWORD = list('abcde')
INITIAL_PASSWORD = list('abcdefgh')

def replace(s,d):
    return [d.get(x,x) for x in s]

with open('input.txt') as f:
    password = INITIAL_PASSWORD
    for l in f:
        cmd = l.strip().split(' ')
        print cmd

        if cmd[0] == 'swap':
            x,y = (cmd[2],cmd[5])
            if cmd[1] == 'position':
                x,y = map(int,(x,y))
                tmp = password[x]
                password[x]=password[y]
                password[y]=tmp
            if cmd[1] == 'letter':
                d={x:y,y:x}
                password = replace(password,d)

        if cmd[0] == 'reverse':
            s,e = int(cmd[2]),int(cmd[4])+1
            rev = password[s:e]
            rev.reverse()
            password[s:e] = rev

        if cmd[0] == 'rotate':
            dirdict = {'right' : 1, 'left' : -1}
            rotdist = 0
            if cmd[1] in dirdict.keys():
                d = dirdict[cmd[1]]
                amt = int(cmd[2])
                rotdist = d*amt
            if cmd[1] == 'based':
                letterind = password.index(cmd[6])
                rotdist = 1 + letterind
                if letterind >= 4:
                    rotdist += 1
            password = list(np.roll(password,rotdist))

        if cmd[0] == 'move':
            s,d = int(cmd[2]),int(cmd[5])
            c = password.pop(s)
            password.insert(d,c)
        print "".join(password)

    print "DONE"
    print "".join(password)