# OlympicsMedals
This is a semester long project for my Artificial Intelligence Class taught by Professor Haiushai Wang. 
I wanted a user to be able to input their own measurables (height, weight, sex, age, country, sport), and then my application would tell them what medal they'd win.
My project is in three distinct "phases", for lack of a better word. 

The first phase:
  The first objective that I had to do was to obtain data, and then subsequently clean and tweak that data to make it usable in my Neural Network Model. 
  The data I obtained was from Kaggle https://www.kaggle.com/rio2016/olympic-games. This data set contains the measurables of all 11k+ athletes and their medal count. 
  The data set was saved under athletes.csv, which I have attached in this repo.
  
  I had to first clean the data, which involved making sure that there were no empty values and accounting for them. 
  Several nations such as Somalia, Yemen, did not have Date of Birth Data, but their numbers were small. The date of birth was saved via a standrad date format:
   month/day/year. However, this was undesirable as I did not know how to quantify that into a "trainable" model. So I converted the date of birth into age. I did 
   this by using excel to convert their date of birth to days and then divided by 365. 
   
   The second aspect of the data I had to change was the medals. The medals was the key section of the model, without it nothing would work. However there were three columns of data related to medals. One column for bronze, one for silver, and one for gold. There was a number in each column for each athlete related to the medals. This organization of the data was not ideal to make a model off of. So I had to figure out a way to convert three columns of medals into one. 
   
   With code in Jupyter notebook, I parsed through each line in the CSV file and created a new column called medals. This column had 4 possible inputs: 0,1,2,3, with each number corresponding to a medal that they won. 1 for bronze, 2 for silver, 3 for gold, and 0 for no medals won. I did this by parsing through the columns with some code in python and using a series of if statements created column medals. 
   
   Now that I had my data all set, I had to convert the categorical data to numerical numbers. This I did with some simple python code. 
   Then I created the model using a simple keras neural network. I did a bunch of combinations of nodes and layers and this combination resulted in best accuracy of 49%. 
   
   
   The Second Phase:
    Now that I had my model created I decided to create the basic HTML and CSS framework of my website. I created the basic layout that you see on the website where the user manually inputs the height, weight, age. Then for their gender, nationality, and sport, I created a dropdown menu for the user to select the correct variable that they wanted. Eventually this became a problem, because, when I was training the model, has turned all categorical data into numerical data for example: "United States" became "27". I obviously didn't want a user too have to manually input a number instead of the name of the country. So for the value of the input of a country I had to match up each number and to each name of the nationallity, sport, and gender. The process was painstaking, but I did not know what else to do. Now that I had my framework done, I decided to make the CSS section. Due to time constraints, I did not have enough time to make everything pretty, but I am going to do an update. 
    
  
  
  
 The Third Phase:
     The third phase was the actual Flask Application, which itself, was actually not a lot of code, but was actually a pretty confusing topic at first. Flask has two main parts of it called Get and Post. The Get part recieves user data, and then the Post uses the model to quantify the data and then Post the results. This took a little while for me to understand, but eventually I got the hang of it. 
     
     
     
     
How to run the applicaiton:
    You will have to download all the files, and then you run the application through the application.py
   
