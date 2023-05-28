import eel ,subprocess
print("Hello, Jadir")

@eel.expose
def infix_to_postfix(infix):
        # print ("jkjbk")
        # Dictionnaire pour stocker les priorités des opérateurs
        priorite = {'+':1, '-':1, '*':2, '/':2, '^':3}

        
        # delete any space in a string input 
        infix=infix.replace(" ", "")

        # Initialisation des piles pour les opérateurs et les opérandes
        operateurs = []
        postfix = []
        i = 0

        while i < len(infix):
            char = infix[i]

            # Si le caractère est une lettre, on détermine si c'est une variable ou une fonction
            if char.isalpha():
                function = ''
                while i < len(infix) and infix[i].isalpha():
                    function += infix[i]
                    i += 1

                # Si c'est une variable, on l'ajoute directement à la liste postfixe
                if infix[i] != '(':
                    postfix.append(function)
                # Sinon, c'est une fonction et on l'ajoute à la pile des opérateurs
                else:
                    operateurs.append(function)

            # Si le caractère est un chiffre, on ajoute l'opérande à la liste postfixe
            elif char.isnumeric():
                operand = ''
                while i < len(infix) and (infix[i].isnumeric() or infix[i] == '.'):
                    operand += infix[i]
                    i += 1
                postfix.append(operand)

            # Si le caractère est une virgule, on pousse tous les opérateurs jusqu'à la première parenthèse ou virgule dans la liste postfixe
            elif char == ',':
                while operateurs and operateurs[-1] not in ('(', ','):
                    postfix.append(operateurs.pop())
                i += 1

            # Si le caractère est un opérateur, on pousse les opérateurs ayant une priorité supérieure ou égale à celui-ci dans la liste postfixe
            elif char in '+-*/^':
                while operateurs and operateurs[-1] in priorite and priorite[operateurs[-1]] >= priorite[char]:
                    postfix.append(operateurs.pop())
                operateurs.append(char)
                i += 1

            # Si le caractère est une parenthèse ouvrante, on l'ajoute à la pile des opérateurs
            elif char == '(':
                operateurs.append(char)
                i += 1

            # Si le caractère est une parenthèse fermante, on pousse tous les opérateurs jusqu'à la première parenthèse ouvrante dans la liste postfixe
            elif char == ')':
                while operateurs and operateurs[-1] != '(':
                    postfix.append(operateurs.pop())
                if operateurs and operateurs[-1] == '(':
                    operateurs.pop()
                    # If the previous operator was a function, add it to the postfix expression
                    if operateurs and operateurs[-1] not in ('(', ','):
                        postfix.append(operateurs.pop())
                i += 1

        # Pousse tous les opérateurs restants dans la liste postfixe
        while operateurs:
            postfix.append(operateurs.pop())

        # Retourne la liste postfixe sous forme de chaîne de caractères
        return ' '.join(postfix)

@eel.expose
def postfix_postscript(postfixe):


    
    postfixe = postfixe.split()
    print(postfixe)

    
    # Open the JSON file for reading
    f= open('functions.txt', 'r') 
    
    # Read the file contents into a string
    contents = f.read()
    
    # Define the dictionary of operations
    operations = eval(contents)
    

# Convert the postfix expression to PostScript
    postscript = []
    for char in postfixe:
        if char in operations:
            postscript.append(operations[char])
        else:
            postscript.append(char)
    return ' '.join(postscript)



# function pour difier le fichier des functions 
@eel.expose
def add_function(key,value):

    # Read the test into a string
    with open('functions.txt', 'r') as f:
        s = f.read()

    # Define the new key-value pair
    

    # Find the index of the last } character in the string
    last_bracket_index = s.rfind('}')

    # Add the new line before the last } character
    new_line = ",\n    '" + key + "' : '" + value + "'\n}"
    s = s[:last_bracket_index] + new_line

    # Write the modified string back to the test
    with open('functions.txt', 'w') as f:
        f.write(s)
        f.close()
    return "succes"

# open and edit functions 
@eel.expose
def open_functions():
    filename = "functions.txt"
    subprocess.call(["notepad.exe", filename])
    return 1


eel.init('web')
eel.start('/html/index.html')
