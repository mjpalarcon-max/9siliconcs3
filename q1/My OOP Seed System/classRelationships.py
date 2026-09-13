class StudySession:
    def __init__(self, subject, durationMinutes, priorityLevel, completed=False):
        self.subject = subject
        self.durationMinutes = durationMinutes
        self.priorityLevel = priorityLevel
        self.__completed = completed

    def startSession(self):
        return f"Study session for {self.subject} started."

    def markCompleted(self):
        self.__completed = True

    def extendDuration(self, additionalMinutes):
        if additionalMinutes > 0:
            self.durationMinutes += additionalMinutes

    def getStatus(self):
        return "Completed" if self.__completed else "Not completed"

    def displayInfo(self):
        print(f"Subject: {self.subject}")
        print(f"Duration: {self.durationMinutes} minutes")
        print(f"Priority: {self.priorityLevel}/5")
        print(f"Status: {self.getStatus()}")


class StudyPlan:
    def __init__(self, planName, owner):
        self.planName = planName
        self.owner = owner
        self.sessions = []

    def addSession(self, session):
        self.sessions.append(session)

    def displaySessions(self):
        print(f"Study Plan: {self.planName}")
        print(f"Owner: {self.owner}")
        print("Sessions:")

        for session in self.sessions:
            print(
                f"- {session.subject}: {session.durationMinutes} minutes "
                f"(Priority {session.priorityLevel}/5, {session.getStatus()})"
            )


# Create one StudyPlan object
studyPlan = StudyPlan("Quarter 1 Study Plan", "Student")

# Create three StudySession objects
session1 = StudySession("Physics", 90, 5, True)
session2 = StudySession("Mathematics", 60, 5, False)
session3 = StudySession("English", 45, 3, False)

print("--- BEFORE RELATIONSHIP ---")
print("StudyPlan object created:", studyPlan.planName)
print("Number of sessions:", len(studyPlan.sessions))

print("StudySession objects created:")
print("-", session1.subject)
print("-", session2.subject)
print("-", session3.subject)

print("\n--- BUILDING RELATIONSHIP ---")
print("Adding StudySession objects to StudyPlan...")

studyPlan.addSession(session1)
studyPlan.addSession(session2)
studyPlan.addSession(session3)

print("\n--- AFTER RELATIONSHIP ---")
studyPlan.displaySessions()

print("\nAccessing data through the relationship:")

for session in studyPlan.sessions:
    print(
        f"{studyPlan.planName} -> "
        f"{session.subject} ({session.durationMinutes} minutes)"
    )
    