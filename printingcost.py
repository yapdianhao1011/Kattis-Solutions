import sys

def main():
    d = dict()
    d[" "] = 0
    d["!"] = 9
    d["\""] = 6
    d["#"] = 24
    d["$"] = 29
    d['%'] = 22
    d['&'] = 24
    d['\''] = 3
    d['('] = 12
    d[')'] = 12
    d['*'] = 17
    d['+'] = 13
    d[','] = 7
    d['-'] = 7
    d['.'] = 4
    d['/'] = 10
    d['0'] = 22
    d['1'] = 19
    d['2'] = 22
    d['3'] = 23
    d['4'] = 21
    d['5'] = 27
    d['6'] = 26
    d['7'] = 16
    d['8'] = 23
    d['9'] = 26
    d[':'] = 8
    d[';'] = 11
    d['<'] = 10
    d['='] = 14
    d['>'] = 10
    d['?'] = 15
    d['@'] = 32
    d['A'] = 24
    d['B'] = 29
    d['C'] = 20
    d['D'] = 26
    d['E'] = 26
    d['F'] = 20
    d['G'] = 25
    d['H'] = 25
    d['I'] = 18
    d['J'] = 18
    d['K'] = 21
    d['L'] = 16
    d['M'] = 28
    d['N'] = 25
    d['O'] = 26
    d['P'] = 23
    d['Q'] = 31
    d['R'] = 28
    d['S'] = 25
    d['T'] = 16
    d['U'] = 23
    d['V'] = 19
    d['W'] = 26
    d['X'] = 18
    d['Y'] = 14
    d['Z'] = 22
    d['['] = 18
    d['\\'] = 10
    d[']'] = 18
    d['^'] = 7
    d['_'] = 8
    d['`'] = 3
    d['a'] = 23
    d['b'] = 25
    d['c'] = 17
    d['d'] = 25
    d['e'] = 23
    d['f'] = 18
    d['g'] = 30
    d['h'] = 21
    d['i'] = 15
    d['j'] = 20
    d['k'] = 21
    d['l'] = 16
    d['m'] = 22
    d['n'] = 18
    d['o'] = 20
    d['p'] = 25
    d['q'] = 25
    d['r'] = 13
    d['s'] = 21
    d['t'] = 17
    d['u'] = 17
    d['v'] = 13
    d['w'] = 19
    d['x'] = 13
    d['y'] = 24
    d['z'] = 19
    d['{'] = 18
    d['|'] = 12
    d['}'] = 18
    d['~'] = 9
    d['\n'] = 0
    for line in sys.stdin:
        count = 0
        for c in line:
            count += d[c]
        print(count)

main()
