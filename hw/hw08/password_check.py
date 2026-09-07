import re
def passwordcheck(passwd:str,special_symbols:str="$#@",minlen:int=6, maxlen:int=16):
    #i've used the lookaheads that basically say whether the pattern occurs in text
    #independently of the position
    l = len(passwd)
    return l>=minlen and l<=maxlen and len(re.findall(f"(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[{special_symbols}])",passwd))>0
    #also, i've used the so called 'short-circuit logic' -- if boolean statement consists of ANDs
    #and the Nth AND is FALSE, then the others will not evaluate, so checking len condition puts
    #less stress on the processor (not saying that the password check task is hardware heavy, but prioritising execution of the conditions is good programming practice i guess)