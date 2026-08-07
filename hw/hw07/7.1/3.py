def symbol_frequency(text:str)-> dict:
    res = {}
    for sym in text:
        if sym in res.keys():
            res[sym] +=1
            continue
        res[sym] = 1
    return res


print(symbol_frequency("abracadabra!@!"))
