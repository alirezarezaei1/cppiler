
from hashlib import sha256
from rich.table import Table
from rich.console import Console
import anytree
from collections import defaultdict

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
    table_row = ["","#include","usingnamespacestd",")","}","return","int","float",";","number","identifier","+","-","*",",","==",">=","<=","!=","while","cin",">>","cout","<<","string","$" ] 
    for i in table_row:
        table.add_column(i)

    parse_table_dict = dict()
    parse_table_dict["Start"] = ["Start" , "Start -> SNM" ]
    table.add_row("Start" , "Start -> SNM" , "Start -> SNM" ,"", '' , '' ,"Start -> S N M")
    table.add_row("S" , "S -> #include S" , "S -> ϵ" ,"",'','',"S -> ϵ")
    table.add_row("N" ,'', "N -> using namespace std;" , "", "" , "","N -> ϵ" )
    table.add_row("M" ,'','','','','','M -> int main () {T V}' )
    table.add_row("T" ,'','','', "T -> ϵ" , "T -> ϵ", "T -> Id T" , "T -> Id T","", "T -> Operation",'T -> LT','','','','','','','',"",'T -> Loop T', "T -> Input" , "", "T -> Output","","","T -> ϵ")
    table.add_row("Id" ,'','','','','','Id -> int L', 'Id -> float L' )
    table.add_row("Assign" ,'','','','','','','','Assign -> ϵ','', 'Assign ->identifier = Operation Q' )
    table.add_row("Operation" ,'','','','','','','','','Operation -> number P' , "Operation -> identifier P")
    table.add_row("Expression" ,'','','','','','','','','Expresion -> Operation K Operation' , 'Expresion -> Operation K Operation' )
    table.add_row("Loop" ,'','','','','','','','','','','','','','','','','','', 'Loop -> while(Expression){T}' )
    table.add_row("Input",'','','','','','','','','','','','','','','','','','','','Input -> cin >> identifier F;' )
    table.add_row("Output" ,'','','','','','','','','','','','','','','','','','','','','','Output -> cout << CH;')
    table.add_row("V" ,'','','', "V -> ϵ" , "V -> return 0;" )
    table.add_row("L" ,'','','','','','','','','','L -> identifier Assign Z')
    table.add_row("Z" ,'','','','','','','','Z -> ;','','','','','','Z -> , identifier Assign Z' )
    table.add_row("P" ,'','','P -> ϵ','','','','','P -> ϵ','','','P -> OWP','P -> OWP','P -> OWP','P -> ϵ','P -> ϵ','P -> ϵ','P -> ϵ','P -> ϵ')
    table.add_row("O" ,'','','','','','','','','','','O -> +','O -> -','O ->*')
    table.add_row("W" ,'','','','','','','','', "W -> number" , "W -> identifier", "" , "")
    table.add_row("K" ,'','','','','','','','','','','','','','', "K -> ==" , "K -> >=", "K -> <=" , "K -> !=")
    table.add_row("F" ,'','','','','', "F -> ϵ" ,"F -> ϵ",'','' ,"F -> ϵ",'','','','','','','','' ,"F -> ϵ" ,"F -> ϵ" ,'F -> >> identifier F',"F -> ϵ" ,'','',"F -> ϵ" )
    table.add_row("H" ,'','','','','',"H -> ϵ" ,"H -> ϵ",'','' ,"H -> ϵ" ,"" ,'','','','','','','',"H -> ϵ" ,"H -> ϵ",'',"H -> ϵ" ,"H -> << CH" ,'',"H -> ϵ" )
    table.add_row("C" ,'','','','','','','','', "C -> number" , "C -> identifier",'','','','','','','','','','','','','', "C -> string" , "" )
    console.print(table)
    parse_table_dict["Start"] = [{"Start" : ['S', 'N', 'M']} , {"Start" : ['S', 'N', 'M']} , '','','', {"Start" : ['S', 'N', 'M']}]
    parse_table_dict["S"] = [{'S': ['#include' , "S"] }, {"S" : ["ϵ"]}, '','','', {"S" : ['ϵ']} ]
    parse_table_dict["N"] = ['', {"N" : ["usingnamespacestd"]} , "", "" , "",{"N" : ["ϵ"]} ]
    parse_table_dict["M"] = ['','','','','',{"M" :["int", "main" , "(" ,")" ,"{","T" ,"V","}"]} ]
    parse_table_dict["T"] = ['','','', {"T": ['ϵ']} , {"T": ['ϵ']}, {"T": ['Id', 'T']} , {"T": ['Id', 'T']},"","",{"T": ['L','T']},'','','','','','','',"",{"T": ['Loop', 'T']}, {"T": ['Input',"T"]} , "", {"T": ['Output',"T"]},"",""]
    parse_table_dict["Id"] = ['','','','','',{"Id": ['int', 'L']}, {"Id": ['float', 'L']}]
    parse_table_dict["Assign"] = ['','','','','','','',{"Assign": ['ϵ']},'', '','','','', {"Assign": ['ϵ']}]
    parse_table_dict["Operation"] = ['','','','','','','','',{"Operation": ['number', 'P']}, {"Operation": ['identifier', 'P']}]
    parse_table_dict["Expression"] = ['','','','','','','','',{"Expression": ['Operation', 'K', 'Operation']}, {"Expression": ['Operation', 'K', 'Operation']} ]
    parse_table_dict["Loop"] = ['','','','','','','','','','','','','','','','','','', {"Loop": ['while', '(', 'Expression', ')', '{', 'T', '}']}]
    parse_table_dict["Input"] = ['','','','','','','','','','','','','','','','','','','',{"Input": ['cin', '>>', 'identifier', 'F', ';']}]
    parse_table_dict["Output"] = ['','','','','','','','','','','','','','','','','','','','','',{"Output": ['cout', '<<', 'C','H',";"]}]
    parse_table_dict["V"] = ['','','', {"V": ['ϵ']}, {"V": ['return' , "0" , ";"]} ]
    parse_table_dict["L"] = ['','','','','','','','','',{"L": ["identifier", 'Assign', 'Z']}]
    parse_table_dict["Z"] = ['','','','','','','',{"Z": [';']},'','','','','',{"Z": [',', 'identifier', 'Assign', 'Z']}]
    parse_table_dict["P"] = ['','',{"P": ['ϵ']},'','','','',{"P":"ϵ"},'','',{"P": ['O','W','P']},{"P": ['O','W','P']},{"P": ['O','W','P']},{"P": ['ϵ']},{"P": ['ϵ']},{"P": ['ϵ']},{"P": ['ϵ']},{"P": ['ϵ']}]
    parse_table_dict["O"] = ['','','','','','','','','','',{"O": ['+']}, {"O": ['-']}, {"O": ['*']}]
    parse_table_dict["W"] = ['','','','','','','','', {"W": ['number']}, {"W": ['identifier']}, "" , ""]
    parse_table_dict["K"] = ['','','','','','','','','','','','','','', {"K": ['==']}, {"K": ['>=']}, {"K": ['<=']}, {"K": ['!=']}]
    parse_table_dict["F"] = ['','','','','', {"F": ['ϵ']}, {"F": ['ϵ']},{"F": ['ϵ']},'' ,{"F": ['ϵ']} ,'','','','','','','','' ,{"F": ['ϵ']}, {"F": ['ϵ']} ,{"F": ['>>', 'identifier', 'F']},{"F": ['ϵ']}  ,'','',{"F": ['ϵ']}  ]
    parse_table_dict["H"] = ['','','','','',{"H": ['ϵ']} ,{"H": ['ϵ']},{"H": ['ϵ']},'' ,{"H": ['ϵ']} ,"" ,'','','','','','','',{"H": ['ϵ']} ,{"H": ['ϵ']},'',{"H": ['ϵ']} ,{"H": ['<<', 'C','H']} ,'',{"H": ['ϵ']} ]
    parse_table_dict["C"] = ['','','','','','','','', {"C": ['number']}, {"C": ['identifier']},'','','','','','','','','','','','','', {"C": ['string']} , "" ]








    for i in parse_table_dict:
        for j in range(25-len(parse_table_dict[i])):
            parse_table_dict[i].append("")
    for i in parse_table_dict:
        print(parse_table_dict[i])
    parse_table_dict["Assign"].append({"Assign" : ['=', 'Operation']})
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
                 'continue' , 'break' , '#include' , 'using', 'iostream' , 'namespace' , 'std' , 'main',"usingnamespacestd"]:
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


def compile(pairs, grammer):
    table_row = ["#include","usingnamespacestd",")","}","return","int","float",";","number","identifier","+","-","*",",","==",">=","<=","!=","while","cin",">>","cout","<<","string","$","="] 
    stack = list()
    lis = list()
    all_grammer = list()
    stack.append('$')
    stack.append("Start")
    head = stack.pop()
    count = 0
    while head != "$":
        print("stack:" , stack, "  head:" , head, "  pair:", pairs[count])
        if head =="ϵ":
            print("epsilon pop :" , head)
            head = stack.pop()
        elif pairs[count][1] == head or (head =="identifier" and pairs[count][0] == "identifier") or (head == "number" and pairs[count][0] == "number")or (pairs[count][0] == "string" and head == "string"):
            
            # if not  (head =="identifier" and pairs[count][0] == "identifier") and stack[-1] !="Assign":
            if head in ["identifier" , "number", "string"]:
                lis.append(pairs[count][1])
                print("????????????????????????????????????????????????????????????????????????????????????",pairs[count][1])
            count =  count +1
            print("normal pop :" , head)
            head = stack.pop()
        else:

            temp = grammer.get(head)
            num = -1
            for i in range(len(table_row)):
                if pairs[count][1] == table_row[i] or( pairs[count][0] == "identifier" and table_row[i] =="identifier") or (pairs[count][0] == "number" and table_row[i] == "number")or (pairs[count][0] == "string" and table_row[i] == "string"):
                    if temp[i] !="":
                        num = i
                        break
            temp_head = head
            if (temp_head != "ϵ"or temp_head != "") and (temp[num] !=""):
                # head = stack.pop()
                all_grammer.append(temp[num])
                print("transition: ", temp[num])
                for i in range(len(temp[num][temp_head])-1 ,-1, -1):
                    stack.append(temp[num][temp_head][i])
                head = stack.pop()
    output_tree(all_grammer,lis)
    # return all_grammer

def spliter(str):
    lis = list()
    temp_lis =list()
    flag = False
    for i in str:
        if flag and i == " ":
            temp_lis.append(i)
        elif flag and (i=="\'" or i == "\""):
            temp_lis.append(i)
            lis.append("".join(temp_lis))
            temp_lis = list()
            flag = False
        elif (i=="\'" or i == "\""):
            temp_lis.append(i)
            flag = True
        elif i ==" ":
            lis.append("".join(temp_lis))
            temp_lis = list()
        else:
            temp_lis.append(i)
    if len(lis) >0:
        if "".join(temp_lis) != lis[-1]:
            lis.append("".join(temp_lis))
    elif "".join(temp_lis) != "":
            lis.append("".join(temp_lis))
    print(lis)
    return lis

def output_tree (all_grammer , lis) :
    console = Console()
    root = anytree.Node("Start", color = "blue")
    stack = list()
    stack.append(root)
    grammer_count = 0
    k=0
    while len(stack) > 0 :
        head = stack.pop()
        temp = list(all_grammer[grammer_count].values())
        temp2 = list()
        print(temp[0])
        for j in temp[0]:
            if j  in ["Start" , "S" , "N" , "M" , "T" , "Loop","Id" , "Assign" , "Operation" , "Expression" , "Input" , "Output" , "V" , "L" , "Z" , "P", "O","W", "K", "F" , "H" , 'C','ϵ',"identifier" , "number", "string"]:
                i = anytree.Node(name = j, parent=head, color = "blue")
            else:
                i = anytree.Node(name = j, parent=head, color = "black")
            temp2.append(i)
        temp2.reverse()
        for j in temp2:
            # print(j)
            if j.name in["identifier" , "number", "string"]:
                i = anytree.Node(name = lis[k], parent=j, color = "black")
                k = k+1
            if j.name  in ["Start" , "S" , "N" , "M" , "T" , "Id" , "Assign" , "Operation" , "Expression" , "Input" , "Output" , "V" , "Loop","L" , "Z" , "P", "O","W", "K", "F" , "H" , "C"]:
                # print("done ")
                stack.append(j)
        grammer_count += 1     
        if(grammer_count) == len(all_grammer):
            break           
    for pre, fill, node in anytree.RenderTree(root):
        if node.color =="blue":
            console.print(f"{pre}{node.name} ")
        else:
            console.print(f"{pre}[bold red]{node.name}[/bold red] ")
        # console.print(root)



        
    



def main():
    str_line  = ""
    line_count = 0
    corosheh  = 0
    is_main_called = False
    pairs = list()
    while True:
        line_count = line_count + 1 
        str_line = input()
        temp_list = spliter(str_line)
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
    final_pairs = list()
    flag = False
    for pair in pairs:
        if flag:
            flag= False
        elif pair[1] == "using":
            final_pairs.append([pair[0],"usingnamespacestd"])
        elif pair[1] not in["namespace" , "<" , ">" , "std" ,"iostream"]:
            final_pairs.append(pair)

        if pair[1] == "std":
            flag = True
    return final_pairs


m = main()
p = parse_table()
compile(m , p)


####   #include usingnamespacestd int main(){ }   ###

"""
#include <iostream>
using namespace std;
int main(){
int x;
int s=0, t=10;
while (t >= 0){
cin>>x;
t = t - 1;
s = s + x;
}
cout<<"sfdsfsdf dsf  um="<<s;
return 0;
}
"""