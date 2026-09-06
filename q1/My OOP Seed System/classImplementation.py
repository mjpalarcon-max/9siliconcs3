### `classImplementation.py`

```python
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


# Two independent objects
object1 = StudySession("Physics", 60, 5)
object2 = StudySession("English", 45, 3)

print("--- BEFORE ---")
print("Object 1:")
object1.displayInfo()
print()

print("Object 2:")
object2.displayInfo()

print("\nPerforming actions on Object 1...")
print(object1.startSession())
object1.extendDuration(30)
object1.markCompleted()

print("\n--- AFTER ---")
print("Object 1:")
object1.displayInfo()
print()

print("Object 2:")
object2.displayInfo()
```