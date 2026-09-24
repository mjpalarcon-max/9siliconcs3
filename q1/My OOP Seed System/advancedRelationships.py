class StudyActivity:
    def __init__(self, subject, durationMinutes):
        self.subject = subject
        self.durationMinutes = durationMinutes

    def displayBasicInfo(self):
        print(f"Subject: {self.subject}")
        print(f"Duration: {self.durationMinutes} minutes")


class StudySession(StudyActivity):
    def __init__(self, subject, durationMinutes, priorityLevel, completed=False):
        super().__init__(subject, durationMinutes)
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
        self.displayBasicInfo()
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


if __name__ == "__main__":
    studyPlan = StudyPlan("Quarter 1 Study Plan", "Student")

    session1 = StudySession("Physics", 90, 5, False)
    session2 = StudySession("Mathematics", 60, 5, False)
    session3 = StudySession("English", 45, 3, False)

    print("--- TEST 1: INHERITANCE ---")
    print(f"Child object: session1 : {type(session1).__name__}")
    print(f"Inherited subject: {session1.subject}")
    print(f"Inherited duration: {session1.durationMinutes} minutes")
    print("Calling inherited parent method:")
    session1.displayBasicInfo()

    print("\n--- TEST 2: AGGREGATION ---")
    print("Before relationship:")
    print(f"Number of sessions in StudyPlan: {len(studyPlan.sessions)}")

    print("\nBuilding aggregation relationship...")
    studyPlan.addSession(session1)
    studyPlan.addSession(session2)
    studyPlan.addSession(session3)

    print("\nAfter relationship:")
    studyPlan.displaySessions()

    print("\n--- TEST 3: ACCESS THROUGH RELATIONSHIP ---")
    for session in studyPlan.sessions:
        print(
            f"{studyPlan.planName} -> {session.subject} "
            f"({session.durationMinutes} minutes)"
        )

    print("\n--- AGGREGATION INDEPENDENCE CHECK ---")
    print("Session1 still exists independently:")
    print(session1.startSession())
