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
