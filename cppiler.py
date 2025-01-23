def type_ide(text):
    is_int = True
    is_float = 0
    for i in text:
        if i in "0123456789":
            pass
        elif i ==".":
            is_float= is_float +1
            is_int = False
        else:
            is_int = False
            is_float = 0
            break
        
    if is_int :
        return "number"
    if is_float ==1 :
        return "floatNumber"
    if text in ['int' , 'float' , 'void' , 'return' , 'if' , 'while' , 'cin' , 'cout' ,
                 'continue' , 'break' , '#include' , 'using', 'iostream' , 'namespace' , 'std' , 'main']:
        return "reservedword"
    return "identifier"
def analys(term):
    lis = list()
    st = ""
    i=0
    even = True
    while i in range(len(term)):
        if term[i] in ["(" , ")", "[", "]", "," ,";", "+", "-", "*", "/", "=" , "!" , ">", "<" , "|", "{" , "}" ] and even :
            if st != "":
                lis.append(["unknow" , st])
            st = ""
            st = st + term[i]
            if i+1 != len(term):
                if term[i+1] in ["=" , '<' , '>' , '|']:
                    st = st + term[i+1]
                    i = i+1
            lis.append(["symbol" , st])
            st = ""
        else:
            st = st + term[i]
            if (term[i] == "\'" or term[i] == "\"") :
                if not even:
                    lis.append(["string", st])
                    even = True
                    st = ""
                else:
                    even = False
        i = i+1
    if len(lis) != 0 :
        if lis[-1][0] == "symbol"and lis[-1][1] != st:
            if st != "":
                lis.append(["unknow" , st])
    else:
            lis.append(["unknow" , st])

    for i in lis :
        if i[0] == "unknow":
            i[0] = type_ide(i[1])
    return lis      

str_line  = ""
pairs = list()
while True:
    str_line = input()
    if str_line == "end":
        break
    temp_list = str_line.split()
    for i in temp_list:
        pairs = pairs + analys(i)
for i in pairs:
    print(f"[{i[0]}, {i[1]}]")