#Functions
def colorRed(a):
  print("\033[31m",a,"\033[1;33m",sep="", end="")
def colorYellow(a):
  print("\033[1;33m",a,"\033[1;33m",sep="", end="")
def colorPink(a):
  print("\033[1;35m",a,"\033[1;33m",sep="", end="")
def colorAqua(a):
    print("\033[1;36m",a,"\033[1;33m",sep="", end="")
#START
#no use in using function when I can just insert the yellow
print("\033[1;33mSuper Subroutine")
print()
#actual nightmare
print("With my " , end=""), colorPink("new program ") , print("I can just call red" , "(\"and\") " , sep ="") , colorRed("and ") , print("that word will appear in the color I set it to. ", sep ="")
print()
#Aqua and yellow
print("With no ", end="") , colorAqua("weird gaps"), print("." )
#epic indeed
print()
print("Epic.")
