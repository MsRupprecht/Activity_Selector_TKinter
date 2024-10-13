#import tkinter library
from tkinter import *
from random import randint


#basic functions for lists
def pick_random(list):
  n=len(list)
  i=randint(2,n-1)
  return list[i]

def pick_random_final(list):
  n=len(list)
  i=randint(0,n-1)
  return list[i]

def clear_result():
  results_label.config(text="")



#rescue result
def choice_rescue():
  activity_rescue=pick_random(rescue)
  activity_passive_rest=pick_random(passive_rest)
  results_label.config(text="First you should {}. \nThen just {}.\nLater, if you're feeling up to something a bit more active, come back here for more advice.".format(activity_rescue,activity_passive_rest))



#functions for buttons
    #level 2 how much influence
def influence():
  clear_result()
  anxiety_buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]
  for button in anxiety_buttons:
    button["state"]=DISABLED
  level2_label.config(text="How involved in the decision do you want to be?")

  global lots
  global some
  global none
  
  lots=Button(frame_level2,text="I'll pick the categories",width=20,background="#BAA8ED",command=select_categories)
  lots.grid(row=1,column=0)

  some=Button(frame_level2,text="Just a few choices",width=20,background="#A7B2EE",command=location)
  some.grid(row=1,column=1)

  none=Button(frame_level2,text="Pick for me, please",width=20,background="#93BBEF",command=choice_easy)
  none.grid(row=1,column=2)

def choice_easy():
  today_list=easy_list
  for i in range (0,len(today_list)):
    options.extend(today_list[i][2:])
  results_label.config(text="Today you should {}.".format(pick_random_final(options)))

#functions for buttons
    #level 3 location
def location():
    clear_result()

    influence_buttons=[lots,some,none]
    for button in influence_buttons:
      button["state"]=DISABLED
    
    level3_label.config(text="Where do you want to be?")

    global inside
    global outside
    global in_or_out
    
    inside=Button(frame_level3,text="Inside",width=15,background="#50B3AF",command=choice_inside)
    inside.grid(row=1,column=0)

    outside=Button(frame_level3,text="Outside",width=15,background="#7FD2C4",command=choice_outside)
    outside.grid(row=1,column=1)

    in_or_out=Button(frame_level3,text="Either",width=15,background="#AFF2D8",command=choice_either_location)
    in_or_out.grid(row=2,columnspan=2)

def choice_inside():
    for index in range(len(master_list)):
        if master_list[index][0]=="i":
            today_list.append(master_list[index])
    energy()

def choice_outside():
    for index in range(len(master_list)):
        if master_list[index][0]=="o":
            today_list.append(master_list[index])
    energy()


def choice_either_location():
    today_list.extend(master_list)
    energy()


#functions for buttons
    #level 4 energy
def energy():
    clear_result()
    
    location_buttons=[inside,outside,in_or_out]
    for button in location_buttons:
      button["state"]=DISABLED
    
    level4_label.config(text="How much energy and focus do you want to use?")

    global passive
    global relaxed
    global goals
    global any_energy

    passive=Button(frame_level4,text="Passive",width=12,background="#FCD9C5",command=choice_passive)
    passive.grid(row=1,column=0)

    relaxed=Button(frame_level4,text="Relaxed",width=12,background="#FACAC3",command=choice_relaxed)
    relaxed.grid(row=1,column=1)

    goals=Button(frame_level4,text="Goal-oriented",width=12,background="#F7BAC1",command=choice_goals)
    goals.grid(row=1,column=2)

    any_energy=Button(frame_level4,text="Any option",width=16,background="#F4AABF",command=choice_any_effort)
    any_energy.grid(row=2,columnspan=3)

def choice_final_list():
    for i in range (0,len(today_list)):
        options.extend(today_list[i][2:])
    final_choice=pick_random_final(options)
    results_label.config(text="Today you should {}.".format(final_choice))

    reroll=Button(frame_reroll,text="Do you want to reroll?",width=30,background="#EF8BBB",command=choice_reroll)
    reroll.grid(row=0,column=0)

def choice_reroll():
    final_choice=pick_random_final(options)
    results_label.config(text="Today you should {}.".format(final_choice))

def choice_passive():
    energy_buttons=[passive,relaxed,goals,any_energy]
    for button in energy_buttons:
      button["state"]=DISABLED
    
    for index in range(len(today_list)):
        if today_list[index][1]=="r" or today_list[index][1]=="g":
            to_remove.append(today_list[index])
    for list in to_remove:
        today_list.remove(list)    
    choice_final_list()
    

def choice_relaxed():
    energy_buttons=[passive,relaxed,goals,any_energy]
    for button in energy_buttons:
      button["state"]=DISABLED 
    for index in range(len(today_list)):
        if today_list[index][1]=="p" or today_list[index][1]=="g":
            to_remove.append(today_list[index])
    for list in to_remove:
        today_list.remove(list)
    choice_final_list()

def choice_goals():
    energy_buttons=[passive,relaxed,goals,any_energy]
    for button in energy_buttons:
      button["state"]=DISABLED
    for index in range(len(today_list)):
        if today_list[index][1]=="p" or today_list[index][1]=="r":
            to_remove.append(today_list[index])
    for list in to_remove:
        today_list.remove(list)
    choice_final_list()

def choice_any_effort():
    energy_buttons=[passive,relaxed,goals,any_energy]
    for button in energy_buttons:
      button["state"]=DISABLED 
    choice_final_list()

#functions for full category control
def select_categories():
  influence_buttons=[lots,some,none]
  for button in influence_buttons:
    button["state"]=DISABLED

  
  level3_label.config(text="Which categories do you want to include?")

  creative=Button(frame_level3,text="Creative",width=20,background="#50B3AF",command=add_creative)
  creative.grid(row=1,column=0)

  thinking=Button(frame_level3,text="Reading and learning",width=20,background="#7FD2C4",command=add_thinking)
  thinking.grid(row=1,column=1)

  work_fun=Button(frame_level3,text="Work fun",width=20,background="#AFF2D8",command=add_work_fun)
  work_fun.grid(row=1,column=2)

  chores=Button(frame_level3,text="Chores",width=20,background="#FCD9C5",command=add_chores)
  chores.grid(row=2,column=0)

  outside_sit=Button(frame_level3,text="Outside relaxed",width=20,background="#FACAC3",command=add_outside_sit)
  outside_sit.grid(row=2,column=1)

  outside_active=Button(frame_level3,text="Outside active",width=20,background="#F7BAC1",command=add_outside_active)
  outside_active.grid(row=2,column=2)

  level3_secondlabel=Label(frame_level3,text=" ",background="#edf2fb")
  level3_secondlabel.grid(row=3,columnspan=3)

  roll=Button(frame_level3,text="That's enough for now",width=40,background="#F4AABF",command=choice_final_list)
  roll.grid(row=4,columnspan=3)

def add_creative():
  today_list.append(creative_relaxed)
  today_list.append(creative_goal)
  today_list.append(bujo)
  today_list.append(computing)
  

def add_thinking():
  today_list.append(read)
  today_list.append(learn)
  today_list.append(computing)

def add_work_fun():
  today_list.append(work_fun)

def add_chores():
  today_list.append(routine_chores)
  today_list.append(household_chores)

def add_outside_sit():
  today_list.append(outside_sitspot)
  today_list.append(outside_rest)

def add_outside_active():
  today_list.append(outside_adventure)
  today_list.append(outside_walk)



#activity lists
rescue=["i", "p", "do 5 minutes of restorative breathing",\
        "wrap up in a cosy blanket", "write to Apricot",\
        "talk to Deryk","make a hot chocolate",\
        "do a grounding activity", "write in your bujo",\
        "use Autumn/Christmas visualisation distraction",\
        "listen to Christmas music", "take a nap"]

passive_rest=["i","p","watch Thor Ragnarok", "watch Loki",\
              "watch Ant-Man", "watch Spiderman",\
              "watch The Good Place", "watch Parks and Rec",\
              "watch Brooklyn 99", "watch a new series",\
              "watch a new movie", "watch She Hulk",\
              "listen to a programming podcast", "listen to Magic Tavern",\
              "listen to Sawbones", "take a nap"\
              "scroll through Netflix and make a to-watch list",\
              "watch Harry Potter", "make a Sugar and Sloth wishlist",\
              "scroll through Instagram for project ideas",\
              "do a guided meditation in the office"]

routine_chores=["i","g","wash the dishes", "clean the bathroom","hoover",\
                "tidy the office", "complete one step of laundry",\
                "change the sheets", "change the towels", "dust"]

household_chores=["i", "g", "organise paperwork in the office",\
                  "deep clean the kitchen", "organise the bookshelf",\
                  "go through my wardrobe for donations",\
                  "go through the kitchen cabinets and fridge",\
                  "clean the windows", "tidy the medicine shelf",\
                  "deep clean the bathroom", "defrost the fridge"]

creative_relaxed=["i", "r", "mend something","work on your granny squares",\
                  "work on an embroidery project", "get out a colouring book",\
                  "organise your craft resources", "make a craft project and craft supply wishlist"]

creative_goal=["i", "g", "work on your miniature library",\
               "create something miniature from polymer clay",\
               "create earrings from polymer clay", "code something",\
               "plan Instagram posts"]

computing=["i", "g", "work on seating plan spreadsheet", "tinker with the micro:bit",\
           "learn something new in RoboMaster", "link micro:bit to Python textbook",\
           "make displays for 4207", "get this selector online using Flask"]

bujo=["i", "r", "make a holiday activity wishlist",\
      "make a do more/less list", "revisit your resolutions and goals",\
      "make a calendar for the upcoming season",\
      "make pages for your work planner",\
      "make pages for your lesson palnner",\
      "make a weekly bujo layout to encourage daily journalling"]

read=["i", "r", "read my current book", "re-read a Harry Potter book",\
      "read a new book from Mieke", "read a new book from Deryk",\
      "read a new Rick Riordan book"]

learn=["i","g","meet your three daily goals on Duolingo",\
       "work on 'Python the Hard Way'", "work on your French books"\
       "use your BSL learning app", "work through a programming challenge"]

work_fun=["i", "g", "make Mathematician posters", "work on data analysis",\
          "work through a week of lesson in the Y10 computing course",\
          "read Computer Science pedagogy resources", "make creative HW activities"\
          "automate worksheet creation", "make a spreadsheet for an upcoming task"]

inside_movement=["i", "g", "do Beyonce sit-ups", "do a Zumba class",\
                 "do a Nike workout program", "do a Nike yoga class"]

outside_sitspot=["o", "r", "read at Pinch",\
                 "do an embroidery project at Pinch", "bujo at Pinch",\
                 "read at Dee Light", "do an embroidery project at Dee Light",\
                 "bujo at Dee Light", "read at Taste", "bujo at Taste",\
                 "sit in the garden with a book", "do some embroidery in the garden",\
                 "read at Tooting Common", "read at Furzedown Park"]

outside_adventure=["o", "g", "go to the V&A", "go to the Science Museum",\
                   "go into Chinatown and find a new ingredient",\
                   "go to Chelsea and walk around",\
                   "find day tickets to the theatre","visit Kew Gardens",\
                   "visit Chiswick House", "take the train somewhere new",\
                   "walk along the South Bank"]

outside_rest=["o", "p", "listen to a podcast in the park",\
              "lay outside and soak up the sun",\
              "listen to a podcast in the garden",\
              "do a guided meditation in the garden"]

outside_walk=["o", "r", "walk to pick up boba",\
              "pick up groceries for a nice meal today",\
              "pick up pastries from Cut the Mustard",\
              "go for a walk around Tooting Common",\
              "go for a walk around Furzedown Park"]

master_list=[passive_rest, outside_walk, outside_adventure, outside_sitspot,\
             inside_movement, work_fun,learn, read,bujo, creative_goal, creative_relaxed,\
             household_chores, routine_chores, outside_rest, computing]

easy_list=[outside_sitspot, learn, read, bujo, creative_relaxed,\
           routine_chores, passive_rest]

today_list=[]
to_remove=[]
options=[]


#create the welcome window
window=Tk()
window.configure(background="#edf2fb")
window.title("Activity Selector")



#create frame structure

frame_welcome=Frame(window,background="#edf2fb")
frame_welcome.grid(row=0,columnspan=9)
welcome_label=Label(frame_welcome,text="Hello there, Sunshine.",font="bold",background="#edf2fb")
welcome_label.grid(row=0,columnspan=9)

frame_level1=Frame(window,background="#edf2fb")
frame_level1.grid(row=1)
level1_label=Label(frame_level1,text="",background="#edf2fb")
level1_label.grid(row=0,columnspan=9)

frame_level2=Frame(window,background="#edf2fb")
frame_level2.grid(row=2)
level2_label=Label(frame_level2,text=" ",background="#edf2fb")
level2_label.grid(row=0,columnspan=9)

frame_level3=Frame(window,background="#edf2fb")
frame_level3.grid(row=3)
level3_label=Label(frame_level3,text=" ",background="#edf2fb")
level3_label.grid(row=0,columnspan=9)

frame_level4=Frame(window,background="#edf2fb")
frame_level4.grid(row=4)
level4_label=Label(frame_level4,text=" ",background="#edf2fb")
level4_label.grid(row=0,columnspan=9)

frame_result=Frame(window,background="#edf2fb")
frame_result.grid(row=5)
results_label=Label(frame_result,background="#edf2fb")
results_label.grid(row=0,columnspan=9)

frame_reroll=Frame(window,background="#edf2fb")
frame_reroll.grid(row=6)
reroll_label=Label(frame_reroll,text=" ",background="#edf2fb")
reroll_label.grid(row=0,columnspan=9)


#Welcome Frame
Label(frame_welcome,text="I'm proud of you for reaching out and I'm here to help.\
    \nHow are you feeling today?",background="#edf2fb").grid(row=1,columnspan=9)


#Level 1 Choice - Anxiety Rating

button1=Button(frame_level1,text="1",width=7,command=choice_rescue)
button1.configure(background="#FF7480")
button1.grid(row=0,column=1,pady=5)

button2=Button(frame_level1,text="2",width=7,command=choice_rescue)
button2.configure(background="#FF8C8E")
button2.grid(row=0,column=2,pady=5)

button3=Button(frame_level1,text="3",width=7,command=influence)
button3.configure(background="#FFA49B")
button3.grid(row=0,column=3,pady=5)

button4=Button(frame_level1,text="4",width=7,command=influence)
button4.configure(background="#FFBBA9")
button4.grid(row=0,column=4,pady=5)

button5=Button(frame_level1,text="5",width=7,command=influence)
button5.configure(background="#FFD3B6")
button5.grid(row=0,column=5,pady=5)

button6=Button(frame_level1,text="6",width=7,command=influence)
button6.configure(background="#EFE9AE")
button6.grid(row=0,column=6,pady=5)

button7=Button(frame_level1,text="7",width=7,command=influence)
button7.configure(background="#DCEDC1")
button7.grid(row=0,column=7,pady=5)

button8=Button(frame_level1,text="8",width=7,command=influence)
button8.configure(background="#C0E7C4")
button8.grid(row=0,column=8,pady=5)

button9=Button(frame_level1,text="9",width=7,command=influence)
button9.configure(background="#A8E6CF")
button9.grid(row=0,column=9,pady=5)


label1=Label(frame_level1,text="super anxious",wraplength=52,background="#edf2fb")
label1.grid(row=1,column=1)

label5=Label(frame_level1,text="a bit stuck",wraplength=52,background="#edf2fb")
label5.grid(row=1,column=5)

label9=Label(frame_level1,text="just indecisive",wraplength=52,background="#edf2fb")
label9.grid(row=1,column=9)

