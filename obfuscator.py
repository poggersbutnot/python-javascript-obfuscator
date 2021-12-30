import random
hexchars = [chr(i) for i in range(97,103)]
numers = [chr(i) for i in range(49,58)]
def randomComplexHex():
    return '0x' + random.choice(hexchars) + str(random.randint(10,15))
def randomHHex():
    return '0x' + random.choice(numers)+ random.choice(numers)+ random.choice(numers)
def randomHex():
    return '0x' + random.choice(numers)+ random.choice(numers)
class Py:
    def charToExp(letter):
        exp= randomComplexHex() + '+-' + randomHHex() + '+' + randomHex()+'*'+randomHex()+'-'+randomHex()+'*0x'+random.choice(numers)
        return 'chr('+exp+'+-'+str(hex(eval(exp)-ord(letter)))+')'
    def sentToExp(string):
        return '+'.join(Py.charToExp(i) for i in string)
    def codeToExp(code):
        return 'exec('+Py.sentToExp(code)+')'
    def ezObfuscate(code):
        return "exec('{}')".format("".join("\\x{:02x}".format(ord(c)) for c in code))
    def obfuscate(code):
        return Py.codeToExp(Py.ezObfuscate(code))
    def deobfuscate(code):
        dcode=[]
        [dcode.append(chr(eval(x))) for x in code[:-2].replace(')+','')[9:].split('chr(')]
        breakLayer1 = ''
        for i in range(len(dcode)):
            breakLayer1+=dcode[i]
        return eval("'"+__import__('re').search("\\\\x.*",breakLayer1).group()[:-1])
class Js:
    def charToExp(letter):
        exp= randomComplexHex() + '+-' + randomHHex() + '+' + randomHex()+'*'+randomHex()+'-'+randomHex()+'*0x'+random.choice(numers)
        return exp+'+-'+str(hex(eval(exp)-ord(letter)))
    def sentToExp(string):
        return ','.join(Js.charToExp(i) for i in string)
    def codeToExp(code):
        return 'window["\\x65\\x76\\x61\\x6C"](window["\\x65\\x76\\x61\\x6C"]("\\x74\\x68\\x69\\x73\\x5b\\x22\\x53\\x74\\x72\\x69\\x6e\\x67\\x22\\x5d\\x5b\\x22\x66\\x72\\x6f\\x6d\\x43\\x68\\x61\\x72\\x43\\x6f\\x64\\x65\\x22\\x5d")('+Js.sentToExp(code)+'))'
    def ezObfuscate(code):
        return "window['\\x65\x76\\x61\\x6C']('{}')".format("".join("\\x{:02x}".format(ord(c)) for c in code))
    def obfuscate(code):
        return Js.codeToExp(Js.ezObfuscate(code))
    def deobfuscate(code):
        code = code.replace('window["\\x65\\x76\\x61\\x6C"](window["\\x65\\x76\\x61\\x6C"]("\\x74\\x68\\x69\\x73\\x5b\\x22\\x53\\x74\\x72\\x69\\x6e\\x67\\x22\\x5d\\x5b\\x22\x66\\x72\\x6f\\x6d\\x43\\x68\\x61\\x72\\x43\\x6f\\x64\\x65\\x22\\x5d")','eval(String.fromCharCode')
        code = code.replace('eval(String.fromCharCode(','');code = code.replace('))','')
        res = ''
        split = code.split(',')
        for i in range(len(split)):
            res += chr(eval(split[i]))
        return eval(res.replace("window['\\x65v\\x61\\x6C'](",'').replace(')',''))
