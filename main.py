# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":  
            opening_brackets_stack.append((next, i)) # tiek pievienota atverošā iekava un attiecīgais kārtas numurs
            

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1][0], next): 
                # pārbauda, vai steks ir tukšs, vai arī aizverošā iekava nesakrīt ar pēdējo atverošo iekavu stekā
                return i+1 # atgriež pašreizējo indeksu "i" +1, tādā veidā norādot pirmās nesakrītošās iekavas pozīciju
            
            opening_brackets_stack.pop() # tiek noņemta pēdējā atverošā iekava no steka, jo tā sakrīt ar pašreizējo aizverošo iekavu
        
    if opening_brackets_stack: # pārbauda, vai steks nav tukšs
        return opening_brackets_stack[0][1] #atgriež pirmās nesakrītošās atverošās iekavas pozīciju stekā
    
    return "Success" # izvada "Success", ja visas iekavas ir vienāda skaita ( katrai atverošajai iekavai ir attiecīgā aizverošā iekava)
            
                
def main():
    # I un F ievade jāpievieno main
    while True:
        text = input() #lietotājs ievada virkni, kas tiek saglabāts mainīgajā "text"
        if "I" in text: # tiek pārbaudīts, vai virknē tika ievadīts burts "I"
            text = input() # tālāk lietotājs atkal ievada citu virkni, kas tiek saglabāts mainīgajā "text"
            mismatch = find_mismatch(text)
            print(mismatch) #izvada mainīgā "mismatch" vērtību
            
        elif "F" in text:
            fname = input("Ievadiet faila nosaukumu: ")
            try:
                with open(fname, 'r') as file:
                    dati = file.read()
                mismatch = find_mismatch(dati)
                print(mismatch) 
            except FileNotFoundError:
                print("Fails netika atrasts.")
        else:
            # text = input() # tālāk lietotājs atkal ievada citu virkni, kas tiek saglabāts mainīgajā "text"
            mismatch = find_mismatch(text)
            print(mismatch) #izvada mainīgā "mismatch" vērtību
            
        

if __name__ == "__main__":
    main()
