# Advanced Class Relationships

## Previous Activities

[Part I - Class Attributes and Methods](https://github.com/mjpalarcon-max/9siliconcs3/blob/main/q1/My%20OOP%20Seed%20System/classAttributesMethods.md)

[Part II - Class Relationships](https://github.com/mjpalarcon-max/9siliconcs3/blob/main/q1/My%20OOP%20Seed%20System/classRelationships.md)


## Existing System Description:

### 1. What classes currently exist in your system?

Class 1: StudySession

Class 2: StudyPlan

### 2. What problem or limitation exists in your current design?

The previous design works, but the StudySession class contains both general study-activity information and information specific to a study session. This could lead to repeated code if other types of study activities are added in the future. A better design is to place the common information in a general StudyActivity parent class and let StudySession inherit from it.

## Inheritance Relationship
Parent: StudyActivity
Child: StudySession
Explanation: A StudySession is a type of StudyActivity because every study session has a subject and a planned duration. The StudySession class adds more specific information such as priority level and completion status. Therefore, StudySession is a specialized form of StudyActivity.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation

Relationship:
Explanation: The relationship is aggregation because a StudyPlan contains StudySession objects, but those study sessions can exist independently of the study plan. The sessions are created separately and then added to the plan. Therefore, the study plan does not completely control the lifetime of the study-session objects.


## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
1. I chose StudyActivity as the parent class because it contains information that is generally useful for different study-related activities. StudySession is a type of StudyActivity because every study session has a subject and a planned duration. The child class then adds specific features such as priority level and completion status. This makes the IS-A relationship between StudySession and StudyActivity logical.

2. Inheritance moved the common subject and durationMinutes attributes into StudyActivity. The displayBasicInfo() method was also placed in the parent class and reused by StudySession. The child constructor uses super().__init__(subject, durationMinutes) instead of rewriting the parent initialization code. This reduces repeated code and makes the system easier to expand.

3. The HAS-A relationship between StudyPlan and StudySession is aggregation because the study sessions can exist independently from the study plan. The StudySession objects are created separately before they are added to the StudyPlan. The plan only stores references to those existing objects. Therefore, removing the plan does not require the individual study-session objects to be removed from the system.

4. In Part III, the relationship between StudyPlan and StudySession was represented as a general association with a one-to-many connection. In Part IV, that relationship is given a more specific meaning as aggregation because the sessions can exist independently of the plan. Aggregation is represented by a hollow diamond in UML. The system also includes inheritance, which is an IS-A relationship rather than a HAS-A relationship.

5. The design follows the DRY principle by placing common study-related information in one parent class, StudyActivity. StudySession inherits the subject, durationMinutes, and displayBasicInfo() functionality instead of redefining the same code. The use of super().__init__() also reuses the parent initialization code. This reduces unnecessary repetition and makes the system easier to maintain and expand.
