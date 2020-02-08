# cobra-crawler
Python Snake Dungeon Crawler

## TODO List
* Prevent snake from moving directly back on itself
  * i.e. if moving left, cannot immedieatly move right and kill self (no action)
* Add walls
  * Add special wall for door
    * Door will open after snake reaches a certain length.
* Add length counter
* Get board drawn so that characters are as tall as they are wide 
  * i.e. a board made of squares
* Use inhertiance to put all the drawing functions outside of main.py (e.g. in draw.py)
  * This will make things scalable, as we will make a new python file for each room and call it as the player progresses.
