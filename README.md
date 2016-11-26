# monty_hall_statistics

This python program simulates the unintuitive "Monty Hall" (named after "Let's Make a Deal" game show host).  
Traditionally it is shown with Three Doors.

A prize is behind one of the doors.  
The other two doors are empty (or contain dud "prizes" as in the game show).  

When a user picks one of the three doors, he has 33% chance of being correct.  
Then "Monty" opens one of the other doors to show it is empty.  

Now, the user has an option of keeping his choice, or switching to choose the other door.  

The facinating result is that if the user sticks with his original choice,  
his chance of winning is still 33%.  

However, if the user now switches to choose the other door,  
his chance of winning increases to 66%.  

This app simulates (and "proves") this effect by using a random number generator to pick  
  - prize door  
  - chosen door  
Then counts the number of times the   
  - winning door was matched initially,  
  - winning door was matched after the switch.  
  
This process is repeated 1000 times, and percentage of each is displayed at the end.  

## This app then goes one step further..
by changing num_doors from 3 to another number, you can see how your odds stack up given a greater initial number of doors.  
No matter how many doors, only 1 door is revealed, and only 1 switch is made.  
In the case of 3 doors, there is only 1 other door to choose from.  
In the case of more than 3 doors, the user switches to another door, via     
     random (number) selection of the remaining doors   
     (shown door is never chosen, and the first door chosen is also not eligible).  
     
### TODO
**Let the user input the number of doors** (default to 3 if nothing input)  
Vary the number of iterations from 1000 (not important)  
Let the user indicate   
  - how many doors to show  
  - how many times allowed to switch  
When number of doors is greater than 3. (limit shown doors to num_doors - 2, similar with number of switches)  

#### sources
Udacity.com Intro to Statistics Course: 31 Monty Hall Problem  
  
Intro to the Concept and Explanation of why this is so:  
https://classroom.udacity.com/courses/st101/lessons/48744119/concepts/484806120923#  
  
The posed programming challenge for the Monty Hall Problem  
https://classroom.udacity.com/courses/st101/lessons/48744119/concepts/487043480923#  
  



