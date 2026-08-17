Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: 9-Silicon
Score:____________
C# / Name: Myrla Janiela P. Alarcon   Date: August 16, 2026

Step 1: Identify the Big Problem
Main Problem: 
The PSHS school canteen faces operational inefficiencies during peak lunch hours. The limited space combined with a high volume of students results in prolonged waiting times. The inefficiency stems from three primary factors: delayed order placement due to indecision, time-consuming manual payment processing, and the lack of a system to monitor food availability. These issues contribute to congestion,reduced time for consumption, and overall dissatisfaction with the canteen services.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Students are only able to view and decide on food selections upon reaching the counter. The absence of prior exposure to menu options and prices leads to hesitation, which accumulates and significantly increases total service time per student.

2.The cashier manually adds item prices and computes changes for each transaction. This process is prone to arithmetic errors and requires additional time per customer, thereby creating a bottleneck in the payment stage.

3. There is no mechanism to record and monitor the quantity of food items sold. As a result, canteen staff are unable to determine when supplies are running low. Students may queue for items that are already unavailable, leading to wasted time and frustration.

4. The first -come-first-served-single-line system does not regulate the flow of the students. It results in overcrowding at the ordering and payment areas, making it difficult for students to move and staff to operate efficiently.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Prolonged Decision-Making by Students	| Decomposition and Pattern Recognition | Decompose the menu into logical categories: Main Meals, Snacks, and Beverages. Deploy a digital menu board outside the outside the canteen and/or a mobile pre-order application |

| Manual Computation of Transactions | Abstraction and Algorithm Design | Implement an automated Point-of-Sale system with barcode or RFID scanning. The system will abstract the details of pricing and automatically execute an algorithm to compute totals and change |

| Lack of Real-Time Inventory Tracking	| Data Collection and Data Analysis | Integrate an inventory database linked to the POS system. Each sale decrements stock count. The system will analyze sales data and trigger alerts when stock falls below a threshold |

| Inefficient Queue Management	| Algorithm Design and Simulation | Develop a digital queuing system that assigns sequential numbers and estimates waiting time based on average service rate. Students may receive notifications via a display screen or app |

---

 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
 
BEGIN PROGRAM Automated_Cashier
    DECLARE item_price[1..n], total, cash_tendered, change AS REAL
    DECLARE item_count AS INTEGER


    OUTPUT "Welcome to PSHS Canteen POS System"
    INPUT item_count


    total ← 0
    FOR i ← 1 TO item_count DO
        INPUT item_price[i]
        total ← total + item_price[i]
    END FOR


    OUTPUT "Total Amount Due: P", total


    REPEAT
        INPUT cash_tendered
        IF cash_tendered < total THEN
            OUTPUT "Insufficient Payment. Please add: P", total - cash_tendered
        END IF
    UNTIL cash_tendered ≥ total


    change ← cash_tendered - total
    OUTPUT "Payment Accepted"
    OUTPUT "Change: P", change
    OUTPUT "Thank you. Please get your receipt."
END PROGRAM





