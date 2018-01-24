## So the essence of this game will be that your
## character is in a castle that is under siege from
## a zombie hoard. The castle walls and gate are
## holding the hoard off with no difficulty but the
## castle is running out of food. At the back of the
## castle is a drawbridge that can be used to cross a
## deep chasam that runs behind the castle. This
## chasam cannot be crossed by the zombie hoard and
## so it is by way of this drawbridge that you and
## your people will make your escape. There is just
## one problem: the drawbridge has not been used in
## decades. It is in disrepair and cannot be lowerd.
## The wooden gears have rotted and the chain has
## rusted. You need to construct a new chain and
## new gears before you can make your escape.

## Note: So I didn't do the best job of sticking to the format that Z. Shaw
## recommends for work flow on the first half of this project. Having gone
## through about half of the thing now I really see the importance of that now.
## The second half of the projcect really involves a separate system that
## opperates within the game (The carpenter creating gears), independent of the
## first one (the blacsmith creating a chain). The workflow is important because
## on bigger projects it would be impossible to keep track of all the moving
## parts that the programmer has to manage and develope to say nothing of keeping
## a team on the same page. I'm going to try to do a better job of this for
## this half of the project.

## THE Z. SHAW CODING PROCESS:
#1 Write a to do list.
#2 Pick the easiest thing from your list.
#3 Describe the thing in your source code in English comments.
#4 Write code under the comments.
#5 run the code to see if it works.
#5 stay in the cycle of writing code, running it to test it, and fixing it untill
## it works.
#6 cross the task off your list, go to the next task, repeat.


## TO DO LIST:

#A) find a way to use a for-loop in this game.

#1 ---DONE---
## Create the 'carpenter' function. It will work the same way as the 'blacksmith'
## function in that "talking" to the carpenter will become accessable after
## the 'drawbridge_gaurdtower' is accessed for the first time and the nature of
## the gears and the carpenter's relationship to them is made clear. The carpenter
## will then explain that he needs wood to make the new gears and the "rotten
## gears" string will be removed from var 'pully'. It will be up to the player
## to explore the keep, barricks, and stables inorder to accertain where the
## wood is and how to get it to the blacksmith. Once the gears are made the player
## will need the strings 'men', 'horses', and 'wagon' to be in var 'crew' inorder
## for the blacksmith to get the new gears to the drawbridge_gaurdtower.

#2 ---DONE--- 
## Create the 'keep' function. This will be where the wood for the gears can be
## found in the form of furnature in the great hall. It will become clear that
## is what the furnature is for after talking to the carpenter. However, the
## player will need 'men' to be in var 'crew' inorder to get the furnature out
## of the keep and to the carpenter. The great hall of the keep will have a
## passage that leads down to function 'mausoleum' where the story of the king
## and his family falling prey to disease, becoming zombies and eating eachother
## will be told.

#3 Create the 'barricks' function. This is where the player can get the men
## needed to move the furnature from the keep to the carpenter's workshop and
## to harness the horses to the wagon at the stables.

#4 Create the 'stables' function. This is where the player can get horses and a
## wagon to move the carpenters newly made gears to the drawbridge gaurdtower.
## They will become accessable after the carpenter has made the gears (after the
## furnature has been brought to the carpenter) and after the player has talked
## to the carpenter.

#5 You will need to build a system of functions, once the drawbridge is repaired,
## to move the story over the bridge and out of the castle, and then end the game.
## Somewhere, in here might be a good place to use a for loop, possibly while
## listing the repaires that have been made and all the people and supples that
## are ready to go.




## PROBLEMS TO SOLVE:

#1


## QUESTIONS THAT NEED ANSWERING:

#1
