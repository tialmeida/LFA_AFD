class Transtion:
    def __init__(self, origin_state, destiny_state, symbol):
        self.origin_state = origin_state
        self.destiny_state = destiny_state
        self.symbol = symbol


def inputLineBreak(text):
    if PRINT_QUESTIONS:
        return input(f'{text}\n')
    else:
        return input()


def printNot():
    print("N")


def printYes():
    print("S")


def ifNotContainsRaiseException(array, object_to_validate):
    if not any(array_object for array_object in array if array_object == object_to_validate):
        raise Exception()


def validateSymbol(symbol_to_validate):
    ifNotContainsRaiseException(alphabet, symbol_to_validate)


def validateState(state_to_validation):
    ifNotContainsRaiseException(states, state_to_validation)


ERROR_STATE = 'ERROR'
PRINT_QUESTIONS = False

states = inputLineBreak("Digite os estados")
states = states.split()

alphabet = inputLineBreak("Digite o alfabeto")
alphabet = alphabet.split()

transtionsNumber = int(inputLineBreak("Digite o número total de transições"))
transtions = []

for index in range(0, transtionsNumber):
    transtion = inputLineBreak("Digite a transição").split()
    validateState(transtion[0])
    validateState(transtion[2])
    validateSymbol(transtion[1])
    transtions.append(Transtion(transtion[0], transtion[2], transtion[1]))

start_state = inputLineBreak("Digite o estado incial")
if len(states) > 0:
    validateState(start_state)

end_states = inputLineBreak("Digite os estados finais").split()
for end_state in end_states:
    validateState(end_state)

words = inputLineBreak("Digite as palavras").split()

for word in words:
    current_state = start_state

    for symbol in word:
        found = False

        for transtion in transtions:
            if transtion.symbol == symbol and current_state == transtion.origin_state:
                current_state = transtion.destiny_state
                found = True
                break

        if not found:
            current_state = ERROR_STATE
            break

    if any(state for state in states if state == current_state):
        printYes()
    else:
        printNot()
