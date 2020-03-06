import math
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline uncomment for use in jupyter notebook

# functions #############################################################################################

# Calculates the amount of substance remaining given half_life, initial amount and time
def amount_left(tau, p_nought, time):
    return p_nought*np.exp(-math.log(2)*time/tau)

# Calculates the amount of substance needed for 5 grams to be left after 30 seconds given the half_life
def amount_needed(tau):
    return 5*np.exp(math.log(2)*30/tau)

# Returns a tuple of numpy arrays for the x and y values to use in drawing graphs
def build_time_series(isotope,single,max_time=10):
    name, half_life, p_nought, time = isotope #
    ar = np.linspace(0,max_time)
    return (ar, amount_left(half_life, p_nought, ar)) #(x,y)

#Builds a graph for decay of isotope over time.  
#Trinket doesn't seem to allow legends which is a pain. Also y-axis labelling dowsnt work properly in trinket
def do_graph(isotope, single=True, max_time=10):
    x, y = build_time_series(isotope,single,max_time)
    plt.plot(x, y, label=isotope[0])
    if single:
        plt.title("Decay of " + isotope[0]+" over time", fontweight="bold") #fontweight crashes trinket
    else:
        plt.title("Decay of all isotopes studied over time", fontweight="bold") #fontweight crashes trinket
    plt.xlabel("time /s")
    plt.ylabel("Amount remaining /g")#doesn't work properly in trinket

# Helper function to return a list of inputted isotope data
def get_input(isotopes):
    isotope = input("Please enter the name of the isotope ")
    half_life = float(
        input("Please enter the half-life of the isotope in seconds "))
    p_nought = float(input("Please enter the initial amount in grams "))
    time = float(input("Please enter a time in seconds "))
    isotopes.append([isotope, half_life, p_nought, time])
    return isotopes

####################################################################################################

# Initialise list to keep isotope data in
isotopes = []

# Loop to process each isotope
while True:
    data = get_input(isotopes)[-1]  # Gets the last inputted item from the list
    isotope, half_life, p_nought, time = data  # Pulls out the pieces from teh list
    p = amount_left(half_life, p_nought, time) # Calculates the amount left at the given time
    print("")
    print("Starting with ", p_nought, "grams of",isotope, "after", time, "seconds there will be", round(
        p, 2), "grams remaining")
    start_amount = amount_needed(half_life)  # Calculates the starting amount.
    print("In order to have 5 grams left after 30 seconds you should start with", round(start_amount, 2), "grams")
    print("")
    do_graph(isotopes[-1]) #builds a graph using current isotope data
    plt.show()
    if input("Do you want to do another isotope y/n") == "n":
        print("")
        break
    else:
        print("")
        
#Processes the final list and does the graphs
#max_time=(max([x[1] for x in isotopes]))*10#returns a value used in teh x-axis of the graph based on the largest hl
max_time=10  #using the time specified in the exercise
for isotope in isotopes:
    do_graph(isotope, False,max_time) #False is a flag that this is a graph of multiple isotopes
plt.legend()
plt.show()


# Output list of isotopes studied, tweak to get commas right (yes I am that sad).
iso_string = ""
for n in range(len(isotopes)):
    if n < len(isotopes)-2:
        iso_string += isotopes[n][0]+", "
    elif n==len(isotopes)-2:
        iso_string+=isotopes[n][0]+" and "
    else:
        iso_string += isotopes[n][0]


print(f"Isotopes studied : {iso_string}")
