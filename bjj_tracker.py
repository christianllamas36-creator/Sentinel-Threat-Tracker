sessions = []

name = input("what is your name? ")
print("Welcome to your BJJ tracker, " + name + "!")

another = "yes"
while another == "yes":
    technique = input("what technique did you drill? ")
    duration = input("How many minutes did you train? ")
    notes = input("Any notes from session? ")

    session = {
        "technique": technique,
        "duration": duration,
        "notes": notes
    }
    
    sessions.append(session)
    another = input("log another session? (yes/no) ")

print("--- Your sessions ---")
for session in sessions:
    print("Technique: " + session["technique"])
    print("Duration: " + session["duration"] + " minutes")
    print("Notes: " + session["notes"])
    print("---")

print("Total sessions: " + str(len(sessions)))
