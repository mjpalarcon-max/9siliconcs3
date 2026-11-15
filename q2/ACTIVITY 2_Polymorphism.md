# Polymorphism and Duck Typing

## 1. Answer the following questions

### a. What is duck typing, as explained in the video?
Duck typing is a concept in Python where an object can be used based on the methods it has rather than the class it belongs to. This means that different classes can perform the same action as long as they have the required method.

### b. What did the `Car` class need to have so it could work inside the same loop as `Dog` and `Cat`, even if it does not inherit from the `Animal` class?
The `Car` class needed to have the same method that the loop calls in the `Dog` and `Cat` classes. It did not need to inherit from the `Animal` class because Python only checks whether the object has the required method.

---

## 2. * [View Source Code](https://github.com/mjpalarcon-max/9siliconcs3/blob/main/q2/ACTIVITY%202_Polymorphism.py)

---

## 3. How does the code in 2.2 demonstrate polymorphism?
The code demonstrates polymorphism because the same `move()` method produces different results depending on the object being used. The `Car`, `Boat`, and `Drone` classes have the same method name, but each performs a different action. This shows duck typing because the classes do not need to inherit from one another to use the same function.
