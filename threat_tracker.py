import os

def read_threats():
    if os.path.exists("threat_log.txt"):
        print("--- LOADING PREVIOUS THREAT LOG ---")
        file = open("threat_log.txt", "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            print(line.strip())
        print(str(len(lines)) + " threats loaded")
        print("-----------------------------------")
    else:
        print("No previous log found. Starting fresh.")

def classify_threat(speed, altitude):
    if speed > 200 and altitude < 1000:
        return "HIGH"
    elif speed > 100:
        return "MEDIUM"
    else:
        return "LOW"

def save_threats(threats):
    file = open("threat_log.txt", "a")
    for threat in threats:
        file.write(threat["id"] + " | " + threat["type"] + " | " + str(threat["altitude"]) + " ft | " + str(threat["speed"]) + " mph | LEVEL: " + threat["threat_level"] + "\n")
    file.close()
    print("Threats saved to threat_log.txt")

threats = []
operator = input("Operator name: ")
print("SENTINEL THREAT TRACKER - Operator: " + operator)
read_threats()
print("--------------------------------")

another = "yes"
while another == "yes":
    threat_id = input("Threat ID: ")
    threat_type = input("Threat type (drone/aircraft/missile): ")

    while True:
        try:
            altitude = int(input("Altitude (ft): "))
            break
        except ValueError:
            print("Invalid input. Numbers only. Try again.")

    while True:
        try:
            speed = int(input("Speed (mph): "))
            break
        except ValueError:
            print("Invalid input. Numbers only. Try again.")

    level = classify_threat(speed, altitude)
    threat = {
        "id": threat_id,
        "type": threat_type,
        "altitude": altitude,
        "speed": speed,
        "threat_level": level
    }
    threats.append(threat)
    another = input("Log another threat? (yes/no): ")

print("\n--- THREAT LOG ---")
for threat in threats:
    print(threat["id"] + " | " + threat["type"] + " | " + str(threat["altitude"]) + " ft | " + str(threat["speed"]) + " mph | LEVEL: " + threat["threat_level"])

print("Total threats logged: " + str(len(threats)))
save_threats(threats)

print("\n--- HIGH PRIORITY THREATS ---")
for threat in threats:
    if threat["threat_level"] == "HIGH":
        print(threat["id"] + " | " + threat["type"] + " | " + str(threat["altitude"]) + " ft | " + str(threat["speed"]) + " mph")