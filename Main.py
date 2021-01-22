import pyttsx3 #Importing the Module

Engine = pyttsx3.init() #Defining the Engine
x = input("Enter the Text: ") #Taking the text input.
Engine.say(x) # Giving the Output.
Engine.runAndWait()