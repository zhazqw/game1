print('''                                               _
                 ___                          (_)
               _/XXX\
_             /XXXXXX\_                                    __
X\__    __   /X XXXX XX\                          _       /XX\__      ___
    \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\
  \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \
 ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____/
/  __    \  /     \ \_   _//_\___    __/    //           \___/  \/     __/
__/_______\________\__\_/________\__/_/____/_____________/_______\____/____
                                  ___
                                 /L|0\
                                /  |  \
                               /       \
                              /    |    \
                             /           \
                            /  __  | __   \
                           /  __/    \__   \
                          /  /__   |  __\   \
                         /___________________\
                         /          |         \
                              /   _|_   \
                      /      ____/___\____     \
                      ___________[o0o]___________
''')
print("Welcome to THE MISERY OF THE OLD.")
print("Your choices make you.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
wait=input("do u want to wait for her? WAIT OR KEEP WALKING\n")
if wait== "WAIT":
    print("she starts talking to you and you guys get know that  you are a match made in heaven")
    home=input("Do you want to go with her or go your own way?\n")
    if home ==  "go with her":
      print("Months pass , you guys get close to each other ")
      choice=input("She tell you that she is pregnant.\n what do you do ? support her finanicially, marry her, leave her\n")
      choiceA= choice.lower()
      if choiceA == "financially support her":
        print("You drift apart like the fallen leaves on the river euprates")
      elif choiceA== "leave her":
        print("She found true love else where . you lost yours")
      else:
        print("married but then came the coffin and the grave to take her away from you")
    else:
      print("you carried on with a story of your life that was different")
else:
  print("the wind of life took you towards a new adventure")