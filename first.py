def log_session(technique, duration):
    print("Logged: " + technique + " for " + duration + " minutes")

def check_goal(duration, goal):
    if int(duration) >= int(goal):
        print("Goal reached! Great session.")
    else:
        print("Keep pushing. You need " + str(int(goal) - int(duration)) + " more minutes.")
    
name = input("What is your name? ")
goal = input("What is your minute goal per session? ")
print("Welcome to your BJJ tracker, " + name + "!")

count=1
while count <= 3:
    print("--- session " + str(count) + "---")
    technique = input("What technique did you drill? ")
    duration = input("How many minutes did you train? ")
    log_session(technique, duration)
    check_goal(duration, goal)
    count = count + 1
    
print("Training log complete. Stay on the mats, " + name + "!")