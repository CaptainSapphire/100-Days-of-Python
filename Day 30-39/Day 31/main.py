## COLOR REFERENCES
#white: \033[1;37m
#blue: \033[0;34m
#yellow: \033[1;33m
#pink: \033[1;35m
#green: \033[1;32m
#red: \033[0;31m

###INTERFACE #1
#check!
print(" ",end="\t")
print("\033[31m=","\033[1;37m=","\033[0;34m=","\033[1;33m Music App ", "\033[0;34m=","\033[1;37m=","\033[31m=", sep="")
print("🔥▶️",end="\t")
print(" ",end="")
print("\033[1;37mRadio Gaga", end="\n")
print(" ",end="\t")
print("\033[1;33m Queen")
for i in range(1,4):
  if i == 1:
    print("\033[1;37mPREV", end="\v")
  if i == 2:
    print("\033[1;32mNEXT", end ="\v")
  if i==3:
    print("\033[1;35mPAUSE", end="\v")

###INTERFACE #2
print(" ",end="")
print(" ",end="\t")
print("\033[1;37mWELCOME TO", end ="\n")
print(" ",end="\t")
print(" ",end="\t")
print(" ",end="\t")
print("\033[1;34m--   ARMBOOK    --", end="\n")
print(" ")
#to work on
print(" "," "," "," "," "," "," "," ",end="\t")
print("\033[1;33mDefinitely not a rip off of", end="\n")
print(" "," ", end="\t")
print(" "," "," "," "," "," "," "," ",end="\t")
print(" a certain other social", end="\n")
print(" "," "," "," "," "," "," "," ",end="\t")
print("           networking site.", end="\n")
##seperatation thingy
print(" ")
print(" "," "," "," "," "," "," "," ",end="\t")
print("\033[1;31mHonest.")
print(" ")
print(" "," "," "," "," "," "," ",end="\t")
print("\033[1;37mUsername:")
print(" "," "," "," "," "," "," ",end="\t")
print("Password:")

##NOTES FROM THE CREATOR
# this is not the most ideal way to do this, however, this is how I worked it out. The solution is very different, but this is the one I made. Overall, I did do a good job. 
#Also, the colors are very different from the desired, however, from the looks of it, the colors in the example have a different background, so it is possible we are running different versions. 
#When I archive this to Github, make sure to add the interfaces (from the directions) as reference points
