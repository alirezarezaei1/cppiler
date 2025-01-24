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
                lis.append(["unknown" , st])
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
                lis.append(["unknown" , st])
    else:
            lis.append(["unknown" , st])

    for i in lis :
        if i[0] == "unknown":
            i[0] = type_ide(i[1])
    return lis      
def corosheh_count(list):
    count = 0
    for i in list:
        for j in i:
            if j == "{":
                count = count +1
            elif j == "}":
                count = count -1
    return count
def check_error(lis):
    pass

def main():
    str_line  = ""
    line_count = 0
    corosheh  = 0
    is_main_called = False
    pairs = list()
    while True:
        line_count = line_count + 1 
        str_line = input()
        temp_list = str_line.split()
        line_pairs = list()
        for i in temp_list:
            pair = analys(i)
            if ["reservedword" , "main"] in pair :
                is_main_called = True
            pairs = pairs + pair
            line_pairs = line_pairs + pair
        corosheh = corosheh_count(temp_list) + corosheh
        if check_error(line_pairs):
            print("syntax error on types")
        if len(line_pairs) > 0 :
            if line_pairs[-1] not in [["symbol", ">"],["symbol", ";"],["symbol", "}"], ["symbol" , "{"]]:
                print("missing ;")
                break
        if corosheh < 0 :
            print("syntax error unexpected \"}\"")
            break 
        if is_main_called and corosheh == 0:
            break
    for i in pairs:
        print(f"[{i[0]}, {i[1]}]")


main()