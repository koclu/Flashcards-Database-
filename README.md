# Flashcards-Database-

This project is new version of [Flashcard with Json](https://github.com/omarfaruk305/Flashcards)

## Differences : 
- Used Postre Sql Database instead of Json files.
- Added statistic section on the menu and game screen.
- Added level options .
- Added to add custom level.
- Added password to login menu.

## About Project
- This project was done in [Pycoders Bootcamp](https://github.com/pycoders-nl) as a challenge after Sql module finished.
- Worked with 4 people as a team.
- Main goal is the project try to people learn words by cards. Dutch-Eng
- Created in 2 weeks.


## Tools
- PyQt5 for interface
- OOP
- PostreSql

## ERD Diagram
Database Model : 

![erd](https://user-images.githubusercontent.com/70334899/150153965-118b79fc-dc03-4900-909f-76e1204d5682.PNG)


*Note : Before running the program create database in postresql and run query code where in flashcard.sql in your database query.Then change information in db.py file according to your db information.*


## About Game
### Information
There is a 250 level and each level has 20 word. It ordered by easy to hard.

The user is also able to add level that only can access his/him self.

### Game Play
- You have to have username which is unique . The system check whether have your username in database.

![welcome](https://user-images.githubusercontent.com/70334899/150160423-63972d3b-5c2f-4305-a595-b6c2b46290df.PNG)


-After sign in you  pass to menu screen.

![menu](https://user-images.githubusercontent.com/70334899/150162568-8f7543b8-16d7-4cfe-9342-89741783111f.PNG)

- Statistics menu : 

![statistics](https://user-images.githubusercontent.com/70334899/150162731-1ec0c277-86a6-4f3f-bb18-1b8988a79fac.PNG)

- Add levels : 

![addlevels](https://user-images.githubusercontent.com/70334899/150162810-51fa6520-7d97-496c-8c4e-feb72529fb65.PNG)


### Inside the game 

Firstable you will see a word which is dutch then 3 second later it turn to english word.


You try to guess meaning of word that you see. According to whether your know after 3 seconds you select the true or false button. (You can't press the button while counting down from 3 )

- You see your current level and your statistics data that you are in the level

![insidegame](https://user-images.githubusercontent.com/70334899/150163201-ef4ca8b1-101e-4a8d-9fc4-70d37793bc3f.PNG)



You should finish all words before pass to next level . If you press red button the word shows itself after all words pass in that level.


*Note :  while you exit game you must use Quit button , otherwise program doesn't close.* 





