#Ejercicio 1
def vtxt(regTxt): #Function will use with it variable.
    #First check if all elements in the words have been done and therefore are equal to 0;
    if len(regTxt) == 0:
        return regTxt #Variable that we are returning. 
    else:
        return regTxt[len(regTxt)::-1] #slicing of the string that was imputed
    
regTxt = "Cambiar este texto" #Enter text that we want to invert
invTxt = vtxt(regTxt) #Add to variable the function for the string that we want to invert
print(invTxt) #print

#Ejercicio 2
def fList(iList): #Function will use with it variable.
    nList = []
    if len(iList) == 0: #First check if all elements in the words have been done and therefore are equal to 0;
        return fList #Variable that we are returning. 
    else:
        return nList

  
iList = ["apa", "oso", "paa", "soo"] #List of objects that we want to tuple with
tList = [tuple(iList) ] #Return the tuples list 
print(tList) #print

#Ejercicio 3


#Ejercicio 4
'''
Paso 1: Capture network package.
Paso 2: Store the package.
Paso 3: Analice the package. 
Paso 4: Detect any aberrations. 
Paso 5: Generate Alerts.
Paso 6: Evaluate and generate solutions.

'''


