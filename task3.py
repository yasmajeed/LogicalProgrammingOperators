'''
please ignore these notes -I have left them to show you any problems I came accross and how i resolved 
them
Ive been working on this code (TO4) and was happy with it, until my total triathlon time = 106 minutes and 
it keeps executing at the first elif statement when it should execute the second elif statement. 
Im struggling to figure out what I'm doing wrong! 
ok so i re watched the T04 video then resolved this by changing my 'or' condition to 'and' 
Removed f-string from print comments as was better to create a new print statement to summarise
the total time taken for triathlon prior to if statements. Here i used the format method.   
'''

print("Triathlon Competition Award")

swimming_time = int(input("Swimming time taken in minutes: "))
cycling_time = int(input("Cycling time taken in minutes: "))
running_time = int(input("Running time taken in minutes: "))
total_time = swimming_time + cycling_time + running_time
 
print("Your total triathlon time is: {} minutes".format(total_time))

if total_time <= 100 and total_time >= 40:
    print("You have completed within the qualifying time, you're award is Provincial Colours, Well done!")

elif total_time >=100 and total_time <=105:
    print("You completed within 5 minutes of qualifying time, you get the provincial half colours award!")

elif total_time >105 and total_time <= 110:
    print("You completed within 10 minutes of qualifying time, you get the provincial scroll award!")

elif total_time >110:
    print("Sorry you took too long in the triathlon, no award this time.")

else:
    print("OOps looks like something went wrong, you can't possibly complete a triathlon in such short time.")





 

