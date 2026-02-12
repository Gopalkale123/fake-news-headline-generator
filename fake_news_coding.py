'''
step description
step 1 : import the random module

step 2: create lists of subjects, action, and places - all with indian examples.

step 3 : use random. choice() to pick one worc from each list

step 4: combine the words into a headline using string formatting

step 5: print the headline to the user

step 6: ask the user if they want another headline 
step 7: if yes, repeat, if no, stop the program.
lets start
'''
'''
1. start the program
2. import the random module
3. create a list of indian subject
ex: ["shahrukh kahn", " virat kohli", " nirmala sitaram", " a mumbai cat", " a group of monkey"]
4. create a list of indian actions
ex: ["launches", "cancel", dance with", " eats", declares war on"]
5. create a list of indian places or things
ex: ["at red for", "in mumbai local train", " a plate of samosas", " inside parliment", "at ganga ghat"]
6. start a loop (use while loop) that keeps running until the user says "no"
    a. randomly chose one item from each list (subject, action, Place)
    b. combine the three chosen words into one sentence using string formatting 
    ex: format: "breaking: {subject}{action} {place}!"
    c. print the final fake news healine
    d. ask the user if they want to generate another headline (yes/no)
    e. if user says "no", END the loop
    7. PRINT a goodbye message
    8. End the program
'''

#import the random module
import random

# 2- create subjects

subjects= [
    "shahrukh khan",
    " virat kohli",
    "nirmala sitharaman",
    " a mumbai  cat",
    " A group of monkeys",
    "prime minister modi",
    "auto rickshaw driver from delhi"
]

actions= [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things= [
    "at red fort",
    "in mumbai locan train",
    "a plate of samosa",
    "at ganga ghat",
    "during ipl match",
    "on the road"

]

# start the headline generation loop

while True:
    subject=random.choice(subjects)
    action= random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline= f" BREAKING NEWS: {subject} {action} {place_or_thing}"

    print("\n" + headline)

    user_input = input("\n do you want generate another headline? (yes/no)").strip().lower()
    if user_input== "no":
        break
    #print goodbye message
    print("\n thanks for using the fake news headlines generator. have a fun day")



