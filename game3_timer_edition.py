import random
from time import sleep
import threading as th
def timer():
    global my_timer
    my_timer = 3
    for x in range(3):
        my_timer = my_timer - 1
        sleep(1)
def timer2():
    global my_timer2
    my_timer2 = 3
    for x in range(3):
        my_timer2 = my_timer2 - 1
        sleep(1)
timer_thread = th.Thread(target=timer)
timer_thread2 = th.Thread(target=timer2)
print("Let's play a driving game. Type help for assistance.")

#user decided action
action = input("> ").lower()
#the state of car at the beginning and for when it stops and starts by the users action
car_stopped = True
car_started = False
car_crashed = False
#how far the user has travelled
mile_counter = 0
#an event counter for collisions
rand_encounter = random.randint(1,4)
rand_encounter2 = 9
#commences the game and get inputs from the user and relevant actions
while True:
    #prints guide for user
    if action == 'help':
        print("""
type 'start' to start the car.
type 'drive' once the car has started.
type 'stop' to stop the car.   
type 'quit' to quit the game.\n""")
        action = input("> ")
    #if user types start
    elif action == 'start' and not car_started:
        print("The car has started. Let's go!")
        car_started = True
        car_stopped = False
        action = input("> ")
    #if the user types start and the car is running
    elif action == 'start' and car_started:
        print("The car has ALREADY STARTED!!!!")
        action = input("> ")
    #when the user types drive
    elif action == 'drive' and car_started:
        mile_counter += 1
        print(f"You have driven {mile_counter} miles.")
        #end goal if statement
        if mile_counter == 10 and car_crashed == False:
            print("Congratulations! You have reached the end. Have a gold star.")    
            break
        #collision event
        if mile_counter == rand_encounter:
                    #begins the countdown
                    timer_thread.start()
                    print("STOP THE CAR! (you have 3 seconds)")
                    decision = input("> ").lower()
                #stop decision from user
                    if decision == 'stop' and my_timer > 0:
                        print("You avoided a crash, type start to continue.")
                        car_stopped = True
                        car_started = False
                        action = 'stop'
                        action = input("> ")
                    #when the user doesnt type stop
                    elif decision != 'stop' or my_timer == 0:
                        print('BANG!! You have crashed! Game over.')
                        break
        if mile_counter == rand_encounter2:
                    timer_thread2.start()
                    print("STOP THE CAR! (you have 3 seconds)")
                    decision = input("> ").lower()
                #stop decision from user
                    if decision == 'stop' and my_timer2 > 0:
                        print("You avoided a crash, type start to continue.")
                        car_stopped = True
                        car_started = False
                        action = 'stop'
                        action = input("> ")
                    #when the user doesnt type stop
                    elif decision != 'stop' or my_timer == 0:
                        car_crashed = True
                        print('BANG!! You have crashed! Game over.')
                        break
        elif not mile_counter == rand_encounter and not mile_counter == rand_encounter2 :
            action = input("> ")
    #car isnt started and the user tries to drive                
    elif action == 'drive' and not car_started:
        print("You need to start the car silly! :P")    
        action = input("> ")
    #stop car action
    elif action == 'stop' and not car_stopped:
        print("The car has stopped.")
        car_stopped = True
        car_started = False
        action = input("> ")
    #user repeats stop and car stopped
    elif action == 'stop' and car_stopped:
        print("The car has ALREADY STOPPED!!!!")
        action = input("> ")
        
    #user quits :(
    elif action == 'quit':
        print('goodbye. :)')
        break
    #no understand
    else:
        print("Sorry, I don't understand that")
        action = input("> ")

