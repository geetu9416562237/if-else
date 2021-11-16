
# strong=input("enter something for strong password: ")
# if len(strong)>=6 and len(strong)<=12:
#     if ('a' in strong or 'b' in strong or 'c' in strong or 'd' in strong or 'e' in strong or 'f' in strong or 'g' in strong or 'h' in strong or 'i' in strong or 'j' in strong or 'k' in strong or 'l' in strong or 'm' in strong or 'n' in strong or 'o' in strong or 'p' in strong or 'q' in strong or 'r' in strong or 's' in strong or 't' in strong or 'u' in strong or 'v' in strong or 'w' in strong or 'x' in strong or 'y' in strong or 'z' in strong) and ('A' in strong or 'B' in strong or 'C' in strong or 'D' in strong or 'E' in strong or 'F' in strong or 'G' in strong or 'H' in strong or 'I' in strong or 'J' in strong or 'K' in strong or 'L' in strong or 'M' in strong or 'N'in strong or 'O' in strong or 'P' in strong or 'Q' in strong or 'R' in strong or 'S' in strong or 'T' in strong or 'U' in strong or 'V' in strong or 'W' in strong or 'X' in strong or 'Y' in strong or 'Z' in strong) and ('0' in strong or '1' in strong or '2' in strong or '3' in strong or '4' in strong or '5' in strong or '6' in strong or '7' in strong or '8' in strong or '9' in strong) and ('@' in strong or '$' in strong or '#' in strong):
#         print("strong password")
#     else:
#         print("wrong password")
# else:
#     print("invalid lenth")
    


def calculator():
    a=int(input("enter a value"))
    b=int(input("enter a vlaue"))
    selection=input("enter a value")
    def add(selection):
        print(a+b)
    add("+")
    def sub(selection):
        print(a-b)
        
    sub("-")
    def multi(selection):
        print(a*b)
    multi("*")
    def div(selcetion):
        print(a%b)
    div("%")
calculator()