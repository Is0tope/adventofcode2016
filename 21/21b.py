import numpy as np

# INITIAL_PASSWORD = list('decab')
INITIAL_PASSWORD = list('fbgdceah')

def replace(s,d):
    return [d.get(x,x) for x in s]

def findValidRotationIndicies(s,c):
    valid = []
    L = len(s)
    pos = s.index(c)
    for i in xrange(L):
        rotdist = 1 + i
        if i >= 4:
            rotdist += 1
        if (i+rotdist) % L == pos:
            valid.append(i)
    return valid


with open('input.txt') as f:
    # just awful
    PASSWORDS = []
    PASSWORDS.append(INITIAL_PASSWORD)
    instructions = f.readlines()
    instructions.reverse()
    for l in instructions:
        cmd = l.strip().split(' ')
        print "COMMAND: ",cmd
        EXTRA_PASSWORDS = []
        TO_DELETE = []      
        for pass_num,password in enumerate(PASSWORDS):
            EXTRA_PASSWORDS = []
            TO_DELETE = []
            print "Trying: ",password
            if cmd[0] == 'swap':
                x,y = (cmd[2],cmd[5])
                if cmd[1] == 'position':
                    x,y = map(int,(x,y))
                    tmp = password[x]
                    password[x]=password[y]
                    password[y]=tmp
                    PASSWORDS[pass_num] = password
                if cmd[1] == 'letter':
                    d={x:y,y:x}
                    password = replace(password,d)
                    PASSWORDS[pass_num] = password

            if cmd[0] == 'reverse':
                s,e = int(cmd[2]),int(cmd[4])+1
                rev = password[s:e]
                rev.reverse()
                password[s:e] = rev
                PASSWORDS[pass_num] = password

            if cmd[0] == 'rotate':
                dirdict = {'right' : -1, 'left' : 1}
                rotdist = 0
                if cmd[1] in dirdict.keys():
                    d = dirdict[cmd[1]]
                    amt = int(cmd[2])
                    rotdist = d*amt
                    password = list(np.roll(password,rotdist))
                    PASSWORDS[pass_num] = password
                if cmd[1] == 'based':
                    valid = findValidRotationIndicies(password,cmd[6])
                    print valid
                    # raw_input('press any key...')
                    # delete/fork the current password
                    TO_DELETE.append(pass_num)

                    for v in valid:
                        print "Forking index ",v
                        rotdist = v - password.index(cmd[6])
                        EXTRA_PASSWORDS.append(list(np.roll(password,rotdist)))
                    print "EXTRA_PASSWORDS: ",EXTRA_PASSWORDS

            if cmd[0] == 'move':
                d,s = int(cmd[2]),int(cmd[5])
                c = password.pop(s)
                password.insert(d,c)
                PASSWORDS[pass_num] = password

        PASSWORDS = [x for i,x in enumerate(PASSWORDS) if not i in TO_DELETE]
        PASSWORDS += EXTRA_PASSWORDS
        print "PASSWORDS: ",["".join(p) for p in PASSWORDS]

    print "DONE"
    print ["".join(p) for p in PASSWORDS]