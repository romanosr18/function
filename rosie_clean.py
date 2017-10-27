first_term = str(input("Set term one "))
second_term = str(input("Set term two "))
third_term = str(input("Set term three "))
equation = first_term +"+"+ second_term +"+"+ str(third_term)
print(equation)
 

#term_three
component = third_term.split('x')

#new_exponent = exponent-1
#new_multiplier = multiplier*exponent
def fofx(term):
    component = term.split('x')
    if len(component) == 1:  #there was no x; just constant
        return str(0)

    if len(component) == 2:
        multiplier = (component[0])
        exponent = (component[1])
        if multiplier == "" and exponent == "":  #just x
            return str(1)
        elif exponent == "":  #poly+x
            return (multiplier)
        elif multiplier == "":  #^x
            exponent = exponent[1:] #strip leading ^
            if int(exponent) > 2:
                return (exponent + 'x^' + str(int(exponent)-1))
            else:
                return (exponent + 'x')
        else:  #polyx^exp
            exponent = exponent[1:] #strip leading ^
            if int(exponent) > 2:
                return (str(int(multiplier)*int(exponent)) + 'x^' + str(int(exponent)-1))
            else:
                return (str(int(multiplier)*int(exponent)) + 'x')

answer=''
d1 = fofx(first_term)
if d1 != '0':
    answer = d1
d2 = fofx(second_term)
if d2 != '0':
    if answer == '':
        answer = d2
    else:
        answer = answer +'+'+ d2
d3 = fofx(third_term)
if d3 != '0':
    if answer == '':
        answer = d3
    else:
        answer = answer +'+'+ d3
if answer == '':
    answer = '0'
answer = answer.replace ('+-', '-')

print (answer)


#figure out how to make them the derivatives of given numbers ex. 10x^2=20x
#take all derivatives and print them in string
