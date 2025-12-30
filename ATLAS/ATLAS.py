import math
import turtle
import random
import datetime
import sys
import subprocess
import os
import asyncio
import tempfile
import platform
from playsound import playsound
import edge_tts
import re
sys.path.append("F:\ATLAS\Data") # Change every time for each computer (directory) #
sys.stderr = open(os.devnull, 'w')

(pi)=math.pi
(sqrt)=math.sqrt
(cos)=math.cos
(sin)=math.sin
(tan)=math.tan
(c)=299792458
(g)=9.807
(G)=6.674*10**-11
(fact)=math.factorial
(e)=math.e
(log)=math.log

blockedwords=("import","_","os","delete")
blockedwordsmath=("import","os","delete")

locktrig=("Lockdown mode","Lockdown mode","Lockdown","lockdown","lockdown mode","Lock","lock")
mathtrig=("Math","math","Maths","maths")
calctrig=("calc","Calc","Calculator","calculator")
drawtrig=("Draw a shape","Draw","draw a shape","draw","Shapedraw","shapedraw")
drawyeahtrig=("Yeah","yeah","yes","Yes","Ok","ok","Sure","sure","Ye","ye")
surecalctrig=("Yeah","yeah","Yes","yes","Ye","ye","Sure","sure")
randomtrig=("Random","random","Open random","open random")
currentdaytrig=("Current day","current day","Day","day","What day is it","what day is it")
scitrig=("Science","science","Sci mod","sci mod")
periodictrig=("Periodic Table","periodic table","Periodic table","periodic Table")
PULGtrig=("PULG","pulg","Pan Universal Liquid Gravity")
optionstrig=("Options","options","Help","help")
AtlasChat=("Chat","Atlas","chat","atlas","Atlas")

# Math defs for input #

def gamma(n):
    return fact(n-1)
def fib(n):
    (ph1)=(((1+sqrt(5))/2)**n)
    (ph2)=(((1-sqrt(5))/2)**n)
    (fx)=round(((ph1-ph2)/sqrt(5)),0)
    return fx
def area_circle(radius, dp):
    return round(pi*(radius**2),d_p)
def pyth_tri_hyp(side1, side2):
    return sqrt((side1**2)+(side2**2))
def pyth_tri_si(hypotenuse, side):
    return sqrt((h**2)-(s**2))
def area_RA_tri(base, height):
    return ((base*height)/2)
def vol_sphere(radius, dp):
    return round((4/3*pi*(radius**3)),dp)
def vol_cylinder(radius, height):
    return ((pi*(radius**2))*height)
def LTD(LSP_FTR, Y):
    (LTDANs)=1/sqrt(1-((LSP_FTR)**2))
    (LTDans)=(Y)/(LTDANs)
    (LTD)=round(LTDans,2)
    return LTD
def UG(m1,m2,r):
    return (G*(m1*m2))/r**2
def Emc2(m):
    return m*(c**2)
def fma(m,a):
    return m*a
def speed(d,t):
    return d/t
def RNG(x,y):
    return random.randint(x,y)
    

def Talk(txt, rate="+100%"):
    async def _talk_async():
          voice = "en-US-GuyNeural"
          print(txt)
          temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
          temp_audio.close()
          tts = edge_tts.Communicate(txt, voice)
          await tts.save(temp_audio.name)
          system = platform.system()
          playsound(temp_audio.name)
    asyncio.run(_talk_async())
    return ""
def Speak(txt):
    async def _speak_async():
          voice = "en-US-GuyNeural"
          temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
          temp_audio.close()
          tts = edge_tts.Communicate(txt, voice)
          await tts.save(temp_audio.name)
          system = platform.system()
          playsound(temp_audio.name)
    asyncio.run(_speak_async())
    
          


 
def calc():
 while True:
      print("-"*25,"CALCULATIONS","-"*25)
      (calc)=input(Talk("What would you like to calculate? "))
      if (calc)=="Back" or (calc)=="back":
         Speak("Going back to main menu!")
         DevModSel()
         break
      else:
         if any(trigger in calc for trigger in("import","os","delete")):
             Talk("Malicious intent detected!!! Locking down...")
             Lock()
         else:
            (calcans)=eval(calc)
            Talk(f"{calc} = {calcans}")
            (ans)=(calcans)
    
def math():
 while True:


   print("="*25,"MATH SELECTION","="*25)
   Speak("Math Selection")
   print("1. Calculations")
   print("2. Maths")
   print("3. Science")
   print("4. Calculus")
   (mode)=input(Talk("Choose mode: "))

   if (mode)=="1":
     Speak("Calculations")
     while True:
      print("-"*25,"CALCULATIONS","-"*25)
      (calc)=input("What would you like to calculate? ")
      if (calc)=="Back" or (calc)=="back":
         print("-"*25,"BACK","-"*25)
         Speak("Going back to math menu!")
         math()
         break
      else:
         if any(trigger in calc for trigger in blockedwordsmath):
             Talk("Malicious intent detected!!! Locking down...")
             Lock()
         else:
            (calcans)=eval(calc)
            print(f"{calc}={calcans}")
            (ans)=(calcans)


         
         


   if (mode)=="2":
     
    while True:
     print("="*25,"MATHS","="*25)
     Speak("Math")
     Talk("Which would you like to do?")
     print("1. Maths Formulas")
     print("2. Binet's Fibonacci Formula")
     print("3. Functions")
     (MC1)=input(Talk("Choose: "))

     if (MC1)=="Back" or (MC1)=="back":
        print("="*25,"BACK","="*25)
        Talk("Going back to main menu!")
        math()
        break
    
     elif (MC1)=="1":
          print("="*25,"MATHS FORMULAS","="*25)
          Talk("Choose a formula")
          Talk("1. Area of a Circle")
          Talk("2. Pythagorean Theorem")
          Talk("3. Area of a Triangle")
          Talk("4. Volume of a Sphere")
          Talk("5. Volume of a Cylinder")
          (MF1)=input("Choose a formula: ")
          if (MF1)=="1":
              print("-"*25,"AREA OF A CIRCLE","-"*25)
              (Cradius)=float(input(Talk("What is the radius in cm? ")))
              (AreaCircans)=(pi*((Cradius)**2))
              print(">"*25,"ANSWER","<"*25)
              Talk(f"The area to your circle is {round(AreaCircans,3)} cm^2")
          elif (MF1)=="2":
              print("-"*25,"PYTHAGOREAN THEOREM","-"*25)
              print("Which version?")
              print("1. A+B=C")
              print("2. C-A=B")
              (PythagorChoose)=input("Which one? ")
              if (PythagorChoose)=="1":
                  print("-"*25,"A+B=C","-"*25)
                  (PythA)=float(input("What is side A in cm? "))
                  (PythB)=float(input("What is side B in cm? "))
                  (PythAans)=(PythA)**2
                  (PythBans)=(PythB)**2
                  (PythCans)=sqrt((PythAans)+(PythBans))
                  print(">"*25,"ANSWER","<"*25)
                  print("The length of side C is",(PythCans),"cm")
              if (PythagorChoose)=="2":
                  print("-"*25,"C-B=A","-"*25)
                  (PythC)=float(input("What is the length of side C in cm? "))
                  (PythB)=float(input("What is the length of side B in cm? "))
                  (PythCsq)=(PythC)**2
                  (PythBsq)=(PythB)**2
                  (PythAsq)=(PythCsq)-(PythBsq)
                  (PythAAns)=sqrt(PythAsq)
                  print(">"*25,"ANSWER","<"*25)
                  print("The length of side A is",(PythAAns),"cm")
          
          elif (MF1)=="3":
              print("-"*25,"AREA OF A TRIANGLE","-"*25)
              (BASEt)=float(input("What is the length of the triangle in cm? "))
              (HeighTT)=float(input("What is the perpendicular height in cm? "))
              (tAREA)=((BASEt)*(HeighTT))/2
              print(">"*25,"ANSWER","<"*25)
              print("The triangle has an area of",(tAREA),"cm^2")
          elif (MF1)=="4":
              print("-"*25,"VOLUME OF A SPHERE","-"*25)
              (Rspherearea)=float(input("What is the radius in cm? "))
              (Sphereans)=4/3*pi*((Rspherearea)**3)
              print(">"*25,"ANSWER","<"*25)
              print("The volume of the sphere is",(round(Sphereans,3)),"cm^3")
          elif (MF1)=="5":
              print("-"*25,"VOLUME OF A CYLINDER","-"*25)
              (Rcylinder)=float(input("What is the radius of the cylinder in cm? "))
              (Hcylinder)=float(input("What is the height of the cylinder in cm?"))
              (Cylinans)=pi*((Rcylinder)**2)*(Hcylinder)
              print(">"*25,"ANSWER","<"*25)
              print("The volume of the cylinder is",(round(Cylinans,3)),"cm^3")
          elif (MF1)=="Back" or (MF1)=="back":
              print("="*25,"BACK","="*25)
              print("Going back to main menu!")
              math()
              break
     elif (MC1)=="2":
         print("-"*25,"BINET'S FIBONACCI FORMULA","-"*25)
         (n)=int(input("nth term of the Fibonacci Sequence? "))
         (ph1)=(((1+sqrt(5))/2)**n)
         (ph2)=(((1-sqrt(5))/2)**n)
         (fx)=round(((ph1-ph2)/sqrt(5)),0)
         print(f"The {n}th term of the Fibonacci Sequence is {fx}")
         (ans)=(fx)
     elif (MC1)=="3":
         print("1. Gamma Function")
         (fc)=input("Choose: ")
         if fc=="1":
             print("-"*25,"GAMMA","-"*25)
             (n)=int(input("What positive integer? "))
             (gn)=fact(n-1)
             print(f"Gamma({n})={gn}")
             (ans)=(gn)
         
   if (mode)== "3":
    while True:
      print("="*25,"Science","="*25)
      print("Choose formula:")
      print("1. Lorentz Time Dilation")
      print("2. E=mc^2")
      print("3. F=MA")
      print("4. Universal Gravitation")
      print("5. Speed")
      (M2)=input("Choose formula: ")
      
      if (M2)=="1":
         print("-"*25,"LORENTZ TIME DILATION","-"*25)
         (E1)=float(input("What is the amount of earth years? "))
         (LSPDF)=float(input("What is the light speed factor? Must be 0 < X <= 1?  "))
         (LTDANs)=1/sqrt(1-((LSPDF)**2))
         (LTDans)=(E1)/(LTDANs)
         (LTD)=round(LTDans,2)
         print(">"*25,"ANSWER","<"*25)
         print("For every",(E1),"years spent on earth",(LTD),"years would be spent travelling at that speed, or around",((LTD)*365),"days")
      elif (M2)=="2":
         print("-"*25,"E=MC^2","-"*25)
         (Massemc)=float(input("What is the mass of the object (Kg)? "))
         (EMC2ans)=(Massemc)*((c)**2)
         (expoemc)=int(math.floor(math.log10(abs(EMC2ans))))
         (Basemc)=(EMC2ans)/(10**(expoemc))
         (BASEMC)=round((Basemc),3)
         print(">"*25,"ANSWER","<"*25)
         print("Your object contains around",(BASEMC),"*10^",(expoemc),"joules of energy")
      elif (M2)=="3":
         print("-"*25,"F=MA","-"*25)
         (MassFMA)=float(input("What is the mass of the object (Kg)? "))
         (accelFMA)=float(input("What is the acceleration of the object (M/S)? "))
         (AnsFMA)=((MassFMA)*(accelFMA))
         print(">"*25,"ANSWER","<"*25)
         print("The force of your object is",(AnsFMA),"newtons")
      elif (M2)=="4":
         print("-"*25,"UNIVERSAL GRAVITATION","-"*25)
         (Mass1UG)=float(input("What is the mass of the first object (Kg)? "))
         (Mass2UG)=float(input("What is the mass of the second object (Kg)? "))
         (distanceUG)=float(input("What is the distance between the objects (M)? "))
         (G)=(6.674*10**-11)
         (ForceUG)=(G)*((Mass1UG)*(Mass2UG))/((distanceUG)**2)
         (expoUG)=int(math.floor(math.log10(abs(ForceUG))))
         (BaseUG)=(ForceUG)/(10**(expoUG))
         (BASEUG)=round((BaseUG),3)
         print(">"*25,"ANSWER","<"*25)
         print("The force of gravity on these 2 objects is",(BASEUG),"*10^",(expoUG),"newtons")
      elif (M2)=="5":
         print("-"*25,"SPEED","-"*25)
         (DISTSDT)=float(input("What is the distance (M)? "))
         (TIMESDT)=float(input("What is the time taken (s)? "))
         (SPEEDSDT)=((DISTSDT)/(TIMESDT))
         print(">"*25,"ANSWER","<"*25)
         print("The average speed of the object is",(round(SPEEDSDT,3)),"m/S")
      if (M2)=="Back" or (M2)=="back":
          print("="*25,"BACK","="*25)
          print("Going back to selection screen!")
          math()
   if (mode)=="Back" or (mode)=="back":
       (surecalc)=input("Are you sure? ")
       if any(trigger in surecalc for trigger in surecalctrig):
           DevModSel()
       elif (surecalc)=="Dev43":
           DevModSel()
       else:
           DevModSel()
           

def RANDFIN():
              print("Shape generated!")
              (randnewshape)=input("Like your shape? Want to make a new one? ")
              if any(trigger in randnewshape for trigger in ("Yeah","yeah","Ye","ye","Yes","yes")):
                  print("YAY MORE SHAPES!!!")
                  ShapeTD()
              if any(trigger in randnewshape for trigger in ("No","no","Nah","nah")):
                  (aysrand)=input("Are you sure? ")
                  if (aysrand)=="Dev43":
                      DevModSel()
                  if any(trigger in aysrand for trigger in ("No","no","Nah","nah")):
                      print("Phew! More shapes ahead ")
                      ShapeTD()
                  else:
                      DevModSel()
                      
def TURTLEDRAW():
    equilatrig=("Equilateral Triangle","equal triangle","Equal triangle","equilateral triangle","Equilateral triangle")
    print("="*25,"DRAW","="*25)
    (TurtDrawSinp)=("Yeah","yeah","Okay","okay","Sure","sure","Why not")
    def ShapeTD():
     (userinput)=input("Wanna draw a shape? ")
     if any(trigger in userinput for trigger in drawyeahtrig):
        (ShapeSel)=input("Cool! What shape? Or type choose to choose and random for a random shape. ")
        if any(trigger in ShapeSel for trigger in equilatrig):
            (EquiltriSides)=int(input("Nice! Length of sides? "))
            for i in range(3):
                turtle.forward(EquiltriSides)
                turtle.left(120)
            (enjdraw)=input("Hope you enjoyed your triangle. Want to make another shape? ")
            if (enjdraw) in ("Yeah","yeah","ye","Ye","Yes","yes"):
                print("Yay!")
                ShapeTD()
            if (enjdraw) in ("No","no","Nah","nah"):
                (ayseqtri)=input("Are you sure? ")
                if (ayseqtri) in ("No","no","Nah","nah"):
                   print("YAY more shapes!")
                   ShapeTD()
                if (ayseqtri)=="Dev43":
                    DevModSel()
                else:
                    DevModSel()
                
        if any(trigger in ShapeSel for trigger in ("Choose","choose")):
            (sideshapesel)=int(input("Cool! A custom shape! Choose amount of sides here: "))
            (angcusTD)=360/sideshapesel
            (lengthcus)=int(input("Nice! Now choose side length: "))
            print("Your shape is being made now!")
            for i in range(sideshapesel):
                turtle.forward(lengthcus)
                turtle.right(angcusTD)
            (newshapeTD)=input("Enjoy your shape? Wanna make a new one? ")
            if (newshapeTD) in ("Yes","yes","Yeah","yeah","ok","Ok","Okay","okay","Sure","sure"):
                ShapeTD()
            else:
                (aysTD)=input("Are you sure? ")
                if (aysTD)=="Dev43":
                    DevModSel()
                if any(trigger in aysTD for trigger in ("No","no","Nah","nah")):
                    ShapeTD()
                else:
                    DevModSel()
                    
     if any(trigger in ShapeSel for trigger in ("Random","random")):
            print("Ooh random huh! Okay, generating shape now ")
            sidesRD=random.randint(3,360)
            lengthRD=random.randint(1,20)
            colorlistRD=["red","blue","green","orange","pink"]
            colorlistRD2=["red","blue","green","orange","pink"]
            if sidesRD>150:
                lengthRD2=lengthRD/2
                colorRD=random.choice(colorlistRD)
                colorRD2=random.choice(colorlistRD2)
                turtle.pencolor(colorRD)
                turtle.fillcolor(colorRD2)
                turtle.begin_fill()
                for i in range(sidesRD):
                   turtle.forward(lengthRD2)
                   turtle.right(360/sidesRD)
                turtle.end_fill()
                RANDFIN()
            else:
             colorRD=random.choice(colorlistRD)
             colorRD2=random.choice(colorlistRD2)
             turtle.pencolor(colorRD)
             turtle.fillcolor(colorRD2)
             turtle.begin_fill()
             for i in range(sidesRD):
                turtle.forward(lengthRD)
                turtle.right(360/sidesRD)
               
             turtle.end_fill()
             RANDFIN()
            
    ShapeTD()

    


def Random():
    print("="*25,"RANDOM","="*25)
    print("Which random thing do you want to do? ")
    print("1. Random Number Generator")
    print("2. Random Shape Generator")
    print("3. Random Module")
    (randchoose)=input("Which one? ")
    if randchoose=="1":
        def RNG():
          (xrand)=int(input("What is the X value? "))
          (zrand)=int(input("What is the Z value? "))
          (RandY)=random.randint(xrand,zrand)
          print("The random number generated was",(RandY))
          (reroll)=input("")
          if any(trigger in reroll for trigger in("Change","change")):
               RNG()
          if any(trigger in reroll for trigger in("Back","back")):
              Random()
          if any(trigger in reroll for trigger in("Reroll","reroll","Keep","keep","same","Same")):
              def SameRNG():
                  (RandY)=random.randint(xrand,zrand)
                  print("The random number generated was",(RandY))
                  (reroll)=input("")
                  if any(trigger in reroll for trigger in("Change","change")):
                       RNG()
                  if any(trigger in reroll for trigger in("Back","back")):
                       Random()
                  if any(trigger in reroll for trigger in("Reroll","reroll","Keep","keep","same","Same")):
                       SameRNG()
                  if any(trigger in reroll for trigger in("Back","back")):
                       Random()
          SameRNG()
        RNG()
            
    if any(trigger in randchoose for trigger in("Back","back")):
        DevModSel()
    if randchoose=="Dev43":
        DevModSel()
    else:
        Random()
    
        
    if randchoose=="2":
        print("Ooh random shape! Okay, generating now ")
        sidesRD=random.randint(3,360)
        lengthRD=random.randint(1,20)
        colorlistRD=["red","blue","green","orange","pink"]
        colorlistRD2=["red","blue","green","orange","pink"]
        if sidesRD>150:
            lengthRD2=lengthRD/2
            colorRD=random.choice(colorlistRD)
            colorRD2=random.choice(colorlistRD2)
            turtle.pencolor(colorRD)
            turtle.fillcolor(colorRD2)
            turtle.begin_fill()
            for i in range(sidesRD):
                turtle.forward(lengthRD2)
                turtle.right(360/sidesRD)
            turtle.end_fill()
            Random()
        else:
            colorRD=random.choice(colorlistRD)
            colorRD2=random.choice(colorlistRD2)
            turtle.pencolor(colorRD)
            turtle.fillcolor(colorRD2)
            turtle.begin_fill()
            for i in range(sidesRD):
               turtle.forward(lengthRD)
               turtle.right(360/sidesRD)
               
            turtle.end_fill()
            Random()
        

        
def mstrkey():
    print("="*25,"MASTER ACCESS","="*25)
    (MSTRCODE)=input("Which code? ")
    if (MSTRCODE)=="42":
        print("="*25,"ACCESS GRANTED","="*25)
        print("Master Access Granted. Welcome creator.")
        print("There are many different modules you can choose from: ")
        print("1. Projects")
        print("2. User Checking")
        print("3. Faraday Shutdown")
        print("4. Logs + Diaries")
        (mstrchoose)=input("Which one? ")

def Lock():
 while True:
    (fstpass)=("A")
    (scndpass)=("B")
    (thrdpass)=("C")
    print("="*25,"LOCK","="*25)
    (passlock)=input("Enter 1st password: ")
    if (passlock)==(fstpass):
        (twopasslock)=input("Enter 2nd password: ")
        if (twopasslock)==(scndpass):
            (threepasslock)=input("Enter 3rd password: ")
            if (threepasslock)==(thrdpass):
                print("Welcome to ATLAS")
                DevModSel()
            else:
                print("Wrong! You are locked out of ATLAS")

       
        else:
            print("Wrong! You are locked out of ATLAS")

    if (passlock)=="Passoverride43":
        DevModSel()
    else:
        print("Wrong! You are locked out of ATLAS")



def mstrkeytrig():
    return ("Master Access Key","Master Key","master access key","master key","Master Code","master code","Key43")


def Alfie():
    print("Welcome, Creator. How may I assist you? ")
    print("You have PRIME access level, meaning you can call any function")
    DevModSel()

def DevModSel():
  while True:
    print("="*25,"DEV MODULE SELECT","="*25)
    (userinput)=input(Talk("What would you like me to do? "))
    if any(trigger in userinput for trigger in locktrig):
        print("Atlas is locking down")
        Lock()
    if any(trigger in userinput for trigger in mathtrig):
        math()
    if any(trigger in userinput for trigger in calctrig):
        calc()
    if any(trigger in userinput for trigger in drawtrig):
        TURTLEDRAW()
    if (userinput) in mstrkeytrig():
        mstrkey()
    if any(trigger in userinput for trigger in randomtrig):
        Random()
    if any(trigger in userinput for trigger in currentdaytrig):
        Currentday()
    if any(trigger in userinput for trigger in scitrig):
        sciencemod()
    if any(trigger in userinput for trigger in periodictrig):
        periodictable()
    if any(trigger in userinput for trigger in PULGtrig):
        PULG()
        DevModSel()
    if any(trigger in userinput for trigger in optionstrig):
        options()
    if any(trigger in userinput for trigger in blockedwords):
        print("Malicious intent!")
        Lock()
    if any(trigger in userinput for trigger in AtlasChat):
        chat()
  
    try:
        (a)=eval(userinput)
        Talk(f"{userinput} = {a}")
    finally:
        DevModSel()

def options():
    print("-"*25,"OPTIONS","-"*25)
    print("""Welcome to the Atlas Options Menu.
Here you can ask for help or select the desired module.
The modules are as follows:""")
    print("1. Calculator")
    print("2. Shape Drawing")
    print("3. Random")
    print("4. Day Schedule")
    print("5. Science")
    print("6. Periodic Table")
    print("7. Pan-Universal Liquid Gravity")
    print("8. Lock")
    (opchoose)=input("Choose: ")
    if opchoose=="1":
        CALCMOD()
    if opchoose=="2":
        TURTLEDRAW()
    if opchoose=="3":
        Random()
    if opchoose=="4":
        Currentday()
    if opchoose=="5":
        sciencemod()
    if opchoose=="6":
        periodictable()
    if opchoose=="7":
        PULG()
    if opchoose=="8":
        Lock()
    
        
       
def chat():
    while True:
        import atlas_chat
        atlas_chat.start_chat()
        
def periodictable():
       while True:
        import Periodic_Table
        print("-"*25,"PERIODIC TABLE","-"*25)
        Talk("Welcome to the ATLAS Periodic Table Module!")
        Talk("Please note: All elements will be in the IUPAC format")
        (element)=input("Enter the name of your element: ")
        if any(trigger in element for trigger in("Hydrogen","hydrogen")) or element=="H" or element=="h":
                 Talk(Periodic_Table.H)
        if any(trigger in element for trigger in("Helium","helium")) or element=="He" or element=="he":
                 Talk(Periodic_Table.He)
        if any(trigger in element for trigger in("Lithium","lithium")) or element=="Li" or element=="li":
                 Talk(Periodic_Table.Li)
        if any(trigger in element for trigger in("Beryllium","beryllium")) or element=="Be" or element=="be":
                 Talk(Periodic_Table.Be)
        if any(trigger in element for trigger in("Boron","boron")) or element=="B" or element=="b":
                 Talk(Periodic_Table.B)
        if any(trigger in element for trigger in("Carbon","carbon")) or element=="C" or element=="c":
                 Talk(Periodic_Table.C)
        if any(trigger in element for trigger in("Nitrogen","nitrogen")) or element=="N" or element=="n":
                 Talk(Periodic_Table.N)
        if any(trigger in element for trigger in("Oxygen","oxygen")) or element=="O" or element=="o":
                 Talk(Periodic_Table.O)
        if any(trigger in element for trigger in("Flourine","flourine")) or element=="F" or element=="f":
                 Talk(Periodic_Table.F)
        if any(trigger in element for trigger in("Neon","neon")) or element=="Ne" or element=="ne":
                 Talk(Periodic_Table.Ne)
        if any(trigger in element for trigger in("Sodium","sodium")) or element=="Na" or element=="na":
                 Talk(Periodic_Table.Na)
        if any(trigger in element for trigger in("Magnesium","magnesium")) or element=="Mg" or element=="mg":
                 Talk(Periodic_Table.Mg)
                 











        if element=="Back" or element=="back":
            sciencemod()
                  
def sciencemod():
    print("="*25,"SCIENCE","="*25)
    print("Welcome to the Atlas science module. Here you can choose between different science functions: ")
    print("1. Science Formulas")
    print("2. Periodic Table")
    print("3. Suit Specific")
    print("4. Theories / Ideas")
    (scimodc)=input("Choose: ")
    if scimodc=="1":
     def sciform():
      while True:
        print("="*25,"Science","="*25)
        print("Choose formula:")
        print("1. Lorentz Time Dilation")
        print("2. E=mc^2")
        print("3. F=MA")
        print("4. Universal Gravitation")
        print("5. Speed")
        (sciform)=input("Choose formula: ")
        if (sciform)=="1":
               print("-"*25,"LORENTZ TIME DILATION","-"*25)
               (E1)=float(input("What is the amount of earth years? "))
               (LSPDF)=float(input("What is the light speed factor? Must be 0 < X <= 1?  "))
               (LTDANs)=1/sqrt(1-((LSPDF)**2))
               (LTDans)=(E1)/(LTDANs)
               (LTD)=round(LTDans,2)
               print(">"*25,"ANSWER","<"*25)
               print("For every",(E1),"years spent on earth",(LTD),"years would be spent travelling at that speed, or around",((LTD)*365),"days")
        elif (sciform)=="2":
               print("-"*25,"E=MC^2","-"*25)
               (Massemc)=float(input("What is the mass of the object (Kg)? "))
               (EMC2ans)=(Massemc)*((c)**2)
               (expoemc)=int(math.floor(math.log10(abs(EMC2ans))))
               (Basemc)=(EMC2ans)/(10**(expoemc))
               (BASEMC)=round((Basemc),3)
               print(">"*25,"ANSWER","<"*25)
               print("Your object contains around",(BASEMC),"*10^",(expoemc),"joules of energy")
        elif (sciform)=="3":
               print("-"*25,"F=MA","-"*25)
               (MassFMA)=float(input("What is the mass of the object (Kg)? "))
               (accelFMA)=float(input("What is the acceleration of the object (M/S)? "))
               (AnsFMA)=((MassFMA)*(accelFMA))
               print(">"*25,"ANSWER","<"*25)
               print("The force of your object is",(AnsFMA),"newtons")
        elif (sciform)=="4":
               print("-"*25,"UNIVERSAL GRAVITATION","-"*25)
               (Mass1UG)=float(input("What is the mass of the first object (Kg)? "))
               (Mass2UG)=float(input("What is the mass of the second object (Kg)? "))
               (distanceUG)=float(input("What is the distance between the objects (M)? "))
               (G)=(6.674*10**-11)
               (ForceUG)=(G)*((Mass1UG)*(Mass2UG))/((distanceUG)**2)
               (expoUG)=int(math.floor(math.log10(abs(ForceUG))))
               (BaseUG)=(ForceUG)/(10**(expoUG))
               (BASEUG)=round((BaseUG),3)
               print(">"*25,"ANSWER","<"*25)
               print("The force of gravity on these 2 objects is",(BASEUG),"*10^",(expoUG),"newtons")
        elif (sciform)=="5":
               print("-"*25,"SPEED","-"*25)
               (DISTSDT)=float(input("What is the distance (M)? "))
               (TIMESDT)=float(input("What is the time taken (s)? "))
               (SPEEDSDT)=((DISTSDT)/(TIMESDT))
               print(">"*25,"ANSWER","<"*25)
               print("The average speed of your object is",(SPEEDSDT))
        if (sciform)=="Back" or sciform=="back":
            sciencemod()
     sciform()
    if scimodc=="2":
        periodictable()
    if scimodc=="4":
            print("Which theory?")
            print("1. Pan-Universal Liquid Gravity")
            (theory)=input("Choose: ")
            if theory=="1":
              PULG()
              sciencemod()
    if scimodc=="Back" or scimodc=="back":
        DevModSel()
def PULG():
     import Theories
     Talk(Theories.PULG)
def Currentday():
    import Timetable
    now=datetime.datetime.now()
    dayname=now.strftime("%A")
    datestr=now.strftime("%d-%m-%Y")
    timestr=now.strftime("%H:%M")
    (Y)=2024
    (M)=9
    (D)=9
    weekAstart=datetime.datetime(Y,M,D)
    today=datetime.datetime.today()
    weekspassed=(today-weekAstart).days // 7
    Talk(f"Today is {dayname}, {datestr}. The time is {timestr}")
    if weekspassed%2==0:
        Talk("It's Week A")
        if dayname=="Saturday":
            print("")
            Talk("The one day of true peace. I'll be here when monday rolls around and you want to gauge your eyes out")
            print("")
        if dayname=="Sunday":
            print("")
            Talk("Ughhh sunday. The prequel to suffering")
            print("")
        else:
            if dayname=="Monday":
                print(Timetable.MondayA)
            if dayname=="Tuesday":
                print(Timetable.TuesdayA)
            if dayname=="Wednesday":
                print(Timetable.WednesdayA)
            if dayname=="Thursday":
                print(Timetable.ThursdayA)
            if dayname=="Friday":
                print(Timetable.FridayA)
    else:
        print("It's Week B")
        if dayname=="Saturday":
            print("")
            Talk("The one day of true peace. I'll be here when monday rolls around and you want to gauge your eyes out")
            print("")   
        if dayname=="Sunday":
            print("")
            Talk("Ughhh sunday. The prequel to suffering")
            print("")
        else:
            if dayname=="Monday":
                print(Timetable.MondayB)
            if dayname=="Tuesday":
                print(Timetable.TuesdayB)
            if dayname=="Wednesday":
                print(Timetable.WednesdayB)
            if dayname=="Thursday":
                print(Timetable.ThursdayB)
            if dayname=="Friday":
                print(Timetable.FridayB)
    DevModSel()

DevModSel()
        
