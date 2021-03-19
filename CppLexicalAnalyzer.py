import re

def delimiters_dict():
    delimiters_dict = {
    "\t": "TAB",
    "\n": "NEWLINE",
    "(": "LPAR",
    ")": "RPAR",
    "[": "LBRACE",
    "]": "RBRACE",
    "{": "LCBRACE",
    "}": "RCBRACE",
    "=": "ASSIGN",
    ":": "COLON",
    ",": "COMMA",
    ";": "SEMICOL",
    "<<": "OUT",
    ">>": "IN",
    }
    return delimiters_dict


def keywords_list():
    keywords_list = [
                        "auto","break","case","char","const","continue","default",
                        "do","double","else","enum","extern","float","for","goto",
                        "if","int","long","register","return","short","signed",
						"sizeof","static","struct","switch","typedef","union",
						"unsigned","void","volatile","while",
                      ]
    return keywords_list

def operators_dict():
    operators_dict = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "MUL",
    "/": "DIV",
    "%": "MOD",
    "+=": "PLUSEQ",
    "-=": "MINUSEQ",
    "*=": "MULEQ",
    "/=": "DIVEQ",
    "++": "INC",
    "--": "DEC",
    "|": "OR",
    "&&": "AND",
    }
    return operators_dict


def tokenTest(token):
    isVariable = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
    isDigit = re.compile(r'\d')
    isFloat = re.compile(r'\d+[.]\d+')

    if token in keywords_list():
        print(token + " : " + " KEYWORD")
    elif token in operators_dict().keys():
        print(token + " : ", operators_dict()[token])
    elif token in delimiters_dict():
        tokenName = delimiters_dict()[token]
        if tokenName == 'NEWLINE' or tokenName == 'TAB':
            print(tokenName)
        else:
            print(token + " : ", tokenName)
    elif re.match(isVariable, token) or "'" in token or '"' in token:
        print(token + " : " + " IDENTIFIER" )
    elif re.match(isDigit, token):
        if re.match(isFloat, token):
            print(token + " : " + " FLOAT")
        else:
            print(token + " : " + " INT")
    elif token == '':
        pass
    else:
         print(token + " : error")
    return True

def delimiterCorrection(line):
    tokens = line.split(" ")
    for delimiter in delimiters_dict().keys():
        for token in tokens:
            if token == delimiter:
                pass
            elif delimiter in token:
                pos = token.find(delimiter)
                tokens.remove(token)
                token = token.replace(delimiter, " ")
                extra = token[:pos]
                token = token[pos + 1 :]
                tokens.append(delimiter)
                tokens.append(extra)
                tokens.append(token)
            else:
                pass
    for token in tokens:
        if testSpace(token):
            tokens.remove(token)
        elif ' ' in token:
            tokens.remove(token)
            token = token.split(' ')
            for d in token:
                tokens.append(d)
    return tokens

def testSpace(string):
    redundant_list = [ " ", "\t", "\n"]
    for element in redundant_list:
        if string == element:
            return True
        else:
            return False


def tokenize_function(path):
    try:
        f = open(path).read()
        lines = f.split("\n")
        counter = 0
        for line in lines:
            counter = counter + 1
            tokens = delimiterCorrection(line)
            print("\nLine: ", counter)
            print("Tokens: ", tokens)
            for token in tokens:
                tokenTest(token)
        return True
    except FileNotFoundError:
        print("\nTry another file-path")

def main():
    tokenize_function('D:/ddd/ANUL III/SEM2/Tehnici Compilare/test.txt')

if __name__ == "__main__":
    main()
