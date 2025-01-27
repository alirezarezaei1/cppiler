from hashlib import sha256
from rich.table import Table
from rich.console import Console

def grammer():
    grammer_dict = {
    'Start': [['S', 'N', 'M']],
    'S': [['#include','S'], ['ϵ']],
    'N': [['using name space std;'], ['ϵ']],
    'M': [['int' , 'main' , '(' , ')' , '{' , 'T' , 'V' , '}' ]],
    'T': [['Id','T'], ['L','T'], ['Loop','T'], ['Input','T'], ['Output','T'], ['ϵ']],
    'V': [['return','0', ';'], ['ϵ']],
    'Id': [['int','L'], ['float','L']],
    'L': [['identifier','Assign','Z']],
    'Z': [[',','identifier','Assign','Z'], [';']],
    'Operation': [['number','P'], ['identifier','P']],
    'P': [['O','W','P'], ['ϵ']],
    'O': [['+'],['-'], ['*']],
    'W': [['number'], ['identifier']],
    'Assign': [['=','Operation'], ['ϵ']],
    'Expression': [['Operation','K','Operation']],
    'K': [['=='], ['>='], ['<='], ['!=']],
    'Loop': [['while','(','Expression',')','{','T','}']],
    'Input': [['cin','>>','identifier','F'],[';']],
    'F': [['>>','identifier','F'], ['ϵ']],
    'Output': [['cout','<<','C','H',';']],
    'H': [['<<','C','H'], ['ϵ']],
    'C': [['number'], ['string'], ['identifier']],
}
    
def parse_table():
    console = Console()
    table = Table()
    table_row = ["","#include","using",")","}","return","int","float",";","number","identifer","+","-","*",",","==",">=","<=","!=","while","cin",">>","cout","<<","string","$"] 
    for i in table_row:
        table.add_column(i)

    parse_table_dict = dict()
    parse_table_dict["Start"] = ["Start" , "Start -> SNM" ]
    table.add_row("Start" , "Start -> SNM" )
    table.add_row("S" , "S -> #include" , "S -> ϵ" )
    table.add_row("N" ,'', "N -> using namespace std;" , "", "" , "","N -> ϵ" )
    table.add_row("M" ,'','','','','','M -> int main () {T V}' )
    table.add_row("T" ,'','','', "T -> ϵ" , "T -> ϵ", "T -> Id T" , "T -> Id T","", "T -> Operation",'T -> LT','','','','','','','',"",'T -> Loop T', "T -> Input" , "", "T -> Output","","","T -> ϵ")
    table.add_row("Id" ,'','','','','','Id -> int T', 'Id -> float L' )
    table.add_row("Assign" ,'','','','','','','','','', 'Assign ->identifier = Operation Q' )
    table.add_row("Operation" ,'','','','','','','','','Operation -> number P' , "Operation -> identifier P")
    table.add_row("Expression" ,'','','','','','','','','Expresion -> Operation K Operation' , 'Expresion -> Operation K Operation' )
    table.add_row("Loop" ,'','','','','','','','','','','','','','','','','','', 'Loop -> while(Expression){T}' )
    table.add_row("Input",'','','','','','','','','','','','','','','','','','','','Input -> cin >> identifier F;' )
    table.add_row("Output" ,'','','','','','','','','','','','','','','','','','','','','','Ouutput -> cout << CH;')
    table.add_row("V" ,'','','', "V -> ϵ" , "V -> return 0;" )
    table.add_row("L" ,'','','','','','','','','','L -> icentifier Assign Z')
    table.add_row("Z" ,'','','','','','','','Z -> ;','','','','','','Z -> , identifier Assign Z' )
    table.add_row("P" ,'','','P -> ϵ','','','','','','','','P -> OWP','P -> OWP','P -> OWP','P -> ϵ','P -> ϵ','P -> ϵ','P -> ϵ','P -> ϵ')
    table.add_row("O" ,'','','','','','','','','','','O -> +','O -> -','O ->*')
    table.add_row("W" ,'','','','','','','','', "W -> number" , "W -> identifier", "" , "")
    table.add_row("K" ,'','','','','','','','','','','','','','', "K -> ==" , "K -> >=", "K -> <=" , "K -> !=")
    table.add_row("F" ,'','','','','', "F -> ϵ" ,"F -> ϵ",'','' ,"F -> ϵ",'','','','','','','','' ,"F -> ϵ" ,"F -> ϵ" ,'F -> >> identifier F',"F -> ϵ" ,'','',"F -> ϵ" )
    table.add_row("H" ,'','','','','',"H -> ϵ" ,"H -> ϵ",'','' ,"H -> ϵ" ,"" ,'','','','','','','',"H -> ϵ" ,"H -> ϵ",'',"H -> ϵ" ,"H -> << CH" ,'',"H -> ϵ" )
    table.add_row("C" ,'','','','','','','','', "C -> numver" , "C -> identifier",'','','','','','','','','','','','','', "C -> string" , "" )
    console.print(table)
    parse_table_dict["Start"] = ["Start" , "Start -> SNM" ]
    parse_table_dict["S"] = ["S" , "S -> #include" , "S -> ϵ" ]
    parse_table_dict["N"] = ["N" ,'', "N -> using namespace std;" , "", "" , "","N -> ϵ" ]
    parse_table_dict["M"] = ["M" ,'','','','','','M -> int main () {T V}' ]
    parse_table_dict["T"] = ["T" ,'','','', "T -> ϵ" , "T -> ϵ", "T -> Id T" , "T -> Id T","", "T -> Operation",'T -> LT','','','','','','','',"",'T -> Loop T', "T -> Input" , "", "T -> Output","","","T -> ϵ"]
    parse_table_dict["Id"] = ["Id" ,'','','','','','Id -> int T', 'Id -> float L' ]
    parse_table_dict["Assign"] = ["Assign" ,'','','','','','','','','', 'Assign ->identifier = Operation Q' ]
    parse_table_dict["Operation"] = ["Operation" ,'','','','','','','','','Operation -> number P' , "Operation -> identifier P"]
    parse_table_dict["Expression"] = ["Expression" ,'','','','','','','','','Expresion -> Operation K Operation' , 'Expresion -> Operation K Operation' ]
    parse_table_dict["Loop"] = ["Loop" ,'','','','','','','','','','','','','','','','','','', 'Loop -> while(Expression){T}' ]
    parse_table_dict["Input"] = ["Input",'','','','','','','','','','','','','','','','','','','','Input -> cin >> identifier F;' ]
    parse_table_dict["Output"] = ["Output" ,'','','','','','','','','','','','','','','','','','','','','','Ouutput -> cout << CH;']
    parse_table_dict["V"] = ["V" ,'','','', "V -> ϵ" , "V -> return 0;" ]
    parse_table_dict["L"] = ["L" ,'','','','','','','','','','L -> icentifier Assign Z']
    parse_table_dict["Z"] = ["Z" ,'','','','','','','','Z -> ;','','','','','','Z -> , identifier Assign Z' ]
    parse_table_dict["P"] = ["P" ,'','','P -> ϵ','','','','','','','','P -> OWP','P -> OWP','P -> OWP','P -> ϵ','P -> ϵ','P -> ϵ','P -> ϵ','P -> ϵ']
    parse_table_dict["O"] = ["O" ,'','','','','','','','','','','O -> +','O -> -','O ->*']
    parse_table_dict["W"] = ["W" ,'','','','','','','','', "W -> number" , "W -> identifier", "" , ""]
    parse_table_dict["K"] = ["K" ,'','','','','','','','','','','','','','', "K -> ==" , "K -> >=", "K -> <=" , "K -> !="]
    parse_table_dict["F"] = ["F" ,'','','','','', "F -> ϵ" ,"F -> ϵ",'','' ,"F -> ϵ",'','','','','','','','' ,"F -> ϵ" ,"F -> ϵ" ,'F -> >> identifier F',"F -> ϵ" ,'','',"F -> ϵ" ]
    parse_table_dict["H"] = ["H" ,'','','','','',"H -> ϵ" ,"H -> ϵ",'','' ,"H -> ϵ" ,"" ,'','','','','','','',"H -> ϵ" ,"H -> ϵ",'',"H -> ϵ" ,"H -> << CH" ,'',"H -> ϵ" ]
    parse_table_dict["C"] = ["C" ,'','','','','','','','', "C -> numver" , "C -> identifier",'','','','','','','','','','','','','', "C -> string" , "" ]

    for i in parse_table_dict:
        for j in range(25-len(parse_table_dict[i])):
            parse_table_dict[i].append("")
    for i in parse_table_dict:
        print(parse_table_dict[i])
    return parse_table_dict
    
    

def sort_pairs(pairs):
    devided = {"string":list() ,"number":list() ,"symbol":list() ,"identifier":list() ,"reservedword":list()}
    for pair in pairs:
        devided[pair[0]].append(pair[1])
    
    for i in devided:
        # devided[i] = list(set(devided[i]))
        devided[i].sort()
    print(devided)
    return devided
    

def create_hash_table(pairs):

    sorted_pairs = sort_pairs(pairs)
    console = Console()
    table = Table(title="Hash Table")
    table.add_column("string", style="blue", justify="center")
    table.add_column("number", style="blue", justify="center")
    table.add_column("symbol", style="blue", justify="center")
    table.add_column("identifier", style="blue", justify="center")
    table.add_column("reservedword", style="blue", justify="center")
    max_h = 0
    for i in sorted_pairs:
        max_h = max(max_h,len(sorted_pairs[i]))
    
    for i in range(max_h):
        table.add_row(f"{sha256(sorted_pairs["string"][i].encode()).hexdigest() if i < len(sorted_pairs["string"]) else ""}",
                      f"{sha256(sorted_pairs["number"][i].encode()).hexdigest() if i < len(sorted_pairs["number"]) else ""}",
                       f"{sha256(sorted_pairs["symbol"][i].encode()).hexdigest() if i < len(sorted_pairs["symbol"]) else ""}",
                        f"{sha256(sorted_pairs["identifier"][i].encode()).hexdigest() if i < len(sorted_pairs["identifier"]) else ""}",
                         f"{sha256(sorted_pairs["reservedword"][i].encode()).hexdigest() if i < len(sorted_pairs["reservedword"]) else ""}" )
        

    console.print(table)

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
    create_hash_table(pairs)

# main()
parse_table()