#print(What transformer character are you?)

##Each Character holds a different value each question adds up to the user score. At the end the user should be assigned to their correspondign character depending on the score they got
#Optimus Prime
#Megatron
#Bumblebee
#Elita-1
#Starscream
#Soundwave
#Shockwave
import time
import os

optimusprime = 0
megatron = 0
bumblebee = 0
elita = 0
starscream = 0
soundwave = 0
shockwave = 0
print("kind, loyal, cunning, ambitious, optimistic, hardworking, intelligent")

positive_trait = input("Choose A Positive Trait You Identify With")
if positive_trait == ("kind"):
    optimusprime +=1
elif positive_trait == ("ambitous"):
    megatron +=1
elif positive_trait == ("optimistic"):
    bumblebee +=1
elif positive_trait == ("hardworking"):
    elita +=1
elif positive_trait == ("cunning"):
    starscream +=1
elif positive_trait == ("loyal"):
    soundwave +=1
elif positive_trait == ("intelligent"):
    shockwave +=1

##Apply and exception if the user does not type in one of the options listedkind


time.sleep(2)
os.system('clear')

print("Naive, Cowardly, Cruel, Stubborn, Unattentive")

negative_trait = input("Choose A Negative Trait You Identify With")
if negative_trait == ("Cruel"):
    megatron +=1
    starscream +=1
    shockwave +=1
    soundwave +=1
elif negative_trait == ("Naive"):
    optimusprime +=1
    bumblebee +=1
elif negative_trait == ("Stubborn"):
    elita +=1
    megatron +=1

## what is your favorite color?
#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave

##what flavor best describes you
#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave



##Night or day?
#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave


#Autobots or decepticons
#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave



##Do you see yourself 
#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave



#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave



#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave



#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave


#option counting towards Optimus Prime
#option counting towards Megatron
#option counting towards Bumblebee
#option counting towards Elita-1
#option counting towards Starscream
#option counting towards Soundwave
#option counting towards Shockwave


#receive score - character 

if (optimusprime < megatron) and (bumblebee > megatron):
    print("ypu are not a deception ")
elif (optimusprime > megatron) and (bumblebee > megatron):
    print("you are not a deception")
elif (optimusprime > megatron):
    print("weeee")
