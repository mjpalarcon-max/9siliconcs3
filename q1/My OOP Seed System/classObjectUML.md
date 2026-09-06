# SG4 - Understanding Classes and Objects
## Class Name: StudySession
## Class Description

The `StudySession` class represents a scheduled study session that a student can use to organize and track their studying. It stores important information about the session and provides actions for managing its progress.

## Properties

| Property        | Data Type | Description                                            |
| --------------- | --------- | ------------------------------------------------------ |
| subject         | string    | The subject that the student will study                |
| durationMinutes | int       | The planned length of the study session in minutes     |
| priorityLevel   | int       | The importance of the study session, from 1 to 5       |
| completed       | boolean   | Indicates whether the study session has been completed |

## Methods

| Method                                 | Description                                       |
| -------------------------------------- | ------------------------------------------------- |
| startSession()                         | Starts the study session and marks it as active.  |
| markCompleted()                        | Marks the study session as completed.             |
| extendDuration(additionalMinutes: int) | Adds extra minutes to the planned study duration. |