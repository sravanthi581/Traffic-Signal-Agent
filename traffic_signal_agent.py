import requests
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change if you have a different username
    password="venkataganesh",  # Add your MySQL password here
    database="TrafficDB"
)
cursor = db.cursor()

# Subagent API endpoints
subagents = {
    "Central Traffic Controller": "http://localhost:5001/control_traffic",
    "Public Transport Optimization": "http://localhost:5002/optimize_transport",
    "Emergency Vehicle Priority": "http://localhost:5003/priority_emergency",
    "Congestion Detection": "http://localhost:5004/detect_congestion",
}

# Tasks for subagents
tasks = {
    "Central Traffic Controller": {"action": "Adjust signals for peak hours"},
    "Public Transport Optimization": {"action": "Give priority to buses"},
    "Emergency Vehicle Priority": {"action": "Clear path for ambulance"},
    "Congestion Detection": {"action": "Monitor real-time traffic"},
}

# Send requests and store responses
for agent, url in subagents.items():
    response = requests.post(url, json=tasks[agent]).json()
    print(f"Task sent to {agent}, Response: {response}")

    # Insert into database
    cursor.execute("INSERT INTO TrafficLogs (agent_name, task, response) VALUES (%s, %s, %s)", 
                   (agent, tasks[agent]["action"], response["message"]))
    db.commit()

cursor.close()
db.close()
