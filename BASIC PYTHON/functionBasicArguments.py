def function(name, id):
    print(name+" OK ",id)
   
def args(*joy):
    print("I am ",joy[2])
    
def args2(joy3,joy2,joy1):
    print("I am now ",joy2)
    
def args3(**joy):
    print("I am "+joy["name"]+" and "+joy["name2"])
    
def defaultParameter(country="Canada"):
    print("I am from "+country)\
        
def arrayPrint(food):
    for c in food:
        print(c)
        
def ret(x):
    return 5*x

#main()    
function("Joy",45390)
function("Badhon",9354)
args("joy","badhon","Joy again")
args2(joy1="Joy",joy2="Badhon",joy3="Joy again")
args3(name="Badhon",name2="joy")
defaultParameter("Bangladesh")
defaultParameter("America")
defaultParameter()

fruits=["apple","banana","cherry"]
arrayPrint(fruits)

print(ret(5))
