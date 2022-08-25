from os import system as os_system
from platform import system as platform_system
from time import sleep as time_sleep

def clear():
    user_system = str(platform_system()).upper()
    if user_system == 'WINDOWS':
        return os_system('cls')
    else:
        return os_system('clear')


def enter_to_continue():
    input('\n[ - ] Enter to continue\n')


def loading_text(text, cycles = 3):
    symbols = ['|', '\\', '-', '/']
    for i in range(cycles):
        for symbol in symbols:
            clear()
            print(f'[ {symbol} ] {text}')
            time_sleep(0.1)
    clear()


def main_menu():
    print('[ 1 ] Resolve logical expression\n' + 
    '[ 2 ] Important informations\n' + 
    '[ 3 ] Exit')


def important_informations():
    print('[ - ] List of logic symbols:\n' +
    '[ \u2192 ] use "->"\n' +
    '[ \u2194 ] use "<->"\n' +
    '[ \u00AC ] use "!"\n' +
    '[ \u2227 ] use "&"\n' +
    '[ \u2228 ] use "|"\n' +
    '\n' +
    '[ - ] Example:\n' +
    '(P \u2192 Q) \u2228 (R \u2194 S) use (P -> Q) | (R <-> S)' + 
    '\n',
    '[ - ] Warning:\n' + 
    'Use space between elements')


def resolve_logical_expression():
    dictionary_symbols = {
        '<->' : '==',
        '->' : '->',
        '!' : 'not ', # Warning space
        '&' : 'and',
        '|' : 'or',
        '(' : '(',
        ')' : ')'
    }
    dictionary_values = {
        'T' : True,
        'F' : False
    }
    dictionary_variables = {}

    # Checking for invalid characters
    # Not finished
    while True:
        clear()
        verify = True
        logical_expression_unformatted = input('[ - ] Enter logical expression\n[ > ] ').strip().upper()
        
        for caracter in logical_expression_unformatted.split():
            if not caracter.isalpha() and caracter not in dictionary_symbols.keys():
                for i in caracter:
                    if not i.isalpha() and i not in dictionary_symbols.keys():
                        verify = False
                        loading_text('Invalid expression, try again.')
                        break
        if verify:
            break

    # Checking if the expression is valid
    # Coming soon

    # Getting values of the variables
    for variable in logical_expression_unformatted:
        if variable.isalpha() and variable not in dictionary_variables.keys():
            while True:
                clear()
                variable_value = input(f'[ - ] Enter the value of the variable {variable}\n[ T ] True\n[ F ] False\n[ > ] ').strip().upper().replace(' ', '')
                if variable_value in ['T', 'F']:
                    dictionary_variables[variable] = dictionary_values[variable_value]
                    break
                else:
                    loading_text('Invalid value, try again.')
    
    # Formatting expression
    logical_expression_formatted = logical_expression_unformatted
    for symbol, value in dictionary_symbols.items():
        logical_expression_formatted = logical_expression_formatted.replace(symbol, value)

    for variables, value in dictionary_variables.items():
        logical_expression_formatted = logical_expression_formatted.replace(variables, str(value))
    
    logical_expression_formatted = logical_expression_formatted.split()
    if logical_expression_formatted.count('->') > 0:
        index = logical_expression_formatted.index('->')
        if logical_expression_formatted[index - 1] == 'True' and logical_expression_formatted[index + 1] == 'False':
            logical_expression_formatted[index] = 'False'
        else:
            logical_expression_formatted[index] = 'True'
        del logical_expression_formatted[index + 1]
        del logical_expression_formatted[index - 1]
    logical_expression_formatted = ' '.join(logical_expression_formatted)

    clear()
    print(f'[ - ] Result:\n[ > ] {eval(logical_expression_formatted)}')

def main():
    while True:
        clear()
        main_menu()
        option = input('[ > ] ').strip()

        if option in ['1', '2', '3']:
            if option == '1':
                clear()
                resolve_logical_expression()
            elif option == '2':
                clear()
                important_informations()
            else:
                clear()
                exit()
            enter_to_continue()
        else:
            loading_text('Invalid option, try again.')


main()
