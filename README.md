# RedditStreakSaver:
A python program that saves your reddit streak by making a post every day. Build to run on Debain-based linux systems. Written in python with the playwright library.
The point of the program is to save your reddit streak by making a post to your account every day. So far, it only works on Debain, which is the system I use.

## Config:
To get streak saver working, you need to change 4 config values:

```DAY```: This value is only for fun. the point is to tell you what day of your reddit streak you are on when you are done running the program, and it is sucessful
<br> ```DAYS_LEFT```: This is also only for fun, telling you how many days left until you hit your goal, also set by you. The default value is 20.
<br> ```USERNAME```: This is required. The program uses this to log into your account to make a post.
<br> ```PASSWORD```: This is also reqired for the program to run.
