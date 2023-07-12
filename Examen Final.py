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
    nList = {}

    for element in iList:
        order_element = ''.join(sorted(iList))

    if order_element in nList:
        nList[order_element].append()


  
iList = ["apa", "oso", "paa", "soo"] #List of objects that we want to tuple with
tList = [tuple(iList) ] #Return the tuples list 
print(tList) #print

#Ejercicio 3
#dado una lista de entero y en un entero x, generar una funcion que 
#regrese los indices de dos elementos de la lista curya suma
#sea igual a x.

def encPuesto(vrts, index):
    obj = {}

    #genera una lista para enumerar los indices.
    for i, vrt in enumerate(vrts):
        #variable que almacena el ciclo de las ubicaciones.
        move = index - vrt
        if move in obj:
            return [obj[move], i]
        obj[move] = i
    return None

dig = [1,2,3,4,5]
tot = 7

res = encPuesto(dig, tot)
print(res)

#Ejercicio 4
'''
Paso 1: Capture network package.
Paso 2: Store the package.
Paso 3: Analice the package. 
Paso 4: Detect any aberrations. 
Paso 5: Generate Alerts.
Paso 6: Evaluate and generate solutions.

'''


