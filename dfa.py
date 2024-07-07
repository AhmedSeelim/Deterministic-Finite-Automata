num_states=int(input("enter number of states : "))
states=[input("enter states : ") for i in range(0,num_states)]
print("states : " , states)
num_keys=int(input("enter number of alphabet : "))
alphabet=[input("enter alphabet : ") for i in range(0,num_keys)]
print("alphabet : ",alphabet)
final_state=input("final state : ")

#Building transition table
transitions=[0 for i in range(len(states))]

for state in range(len(states)):
    transitions[state] = [0 for j in range(len(alphabet))]
    for sympol in range(len(alphabet)):
        transitions[state][sympol] =input("from state "+states[state]+" if "+alphabet[sympol]+" go to state  : ")
print("transitions of ",states,"is : ",transitions)


def transition (state,sympol) :
    result.append((transitions[states.index(state)][alphabet.index(sympol)]))
    print(result)
    return transitions[states.index(state)][alphabet.index(sympol)]


while True :
    result=[]
    start = states[0]
    string=input("enter string to check : ")
    print("result of each transition in string")
    for sympol in string :
        start=transition(start,sympol)
    if (result[-1] == final_state):
        print("yes")
    else:
        print("no")