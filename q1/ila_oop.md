# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be applied by creating a Product class that contains the product’s data such as its name, price, and quantity, together with methods that manage this data. For example, the quantity property can be protected from direct changes and updated through methods such as add_stock() and self_product(). This keeps the data and the operations related to it together, making the inventory system more organized and helping prevent incorrect changes to product information.

### 2. Abstraction
Abstraction can be used by hiding the complex details of inventory operations and showing only the necessary functions to the user. For example , the store system can provide methods such as add_product(), update_stock(), and display_inventory() without requiring the user to know how the system internally stores or processes data. This makes the program easier to use and reduces unnecessary complexity.

### 3. Inheritance
Inheritance can be applied when different types of products share common properties and behaviors. A general Product class can contain properties such as name, price, and quantity while classes such as FoodProduct, and HouseholdProduct can inherit these properties and their own specific characteristics or methods. This reduces repeated code and makes the program easier to expand when new product categories are added.

### 4. Polymorphism
Polymorphism can be used when different product types need to perform the same operation in different ways. For example, display_info() method can exist in the Product class, while FoodProduct() and HouseholdProduct() can each provide their own version of the method to display information specific to that product type. This allows the inventory system to use the same method name for different objects while still producing behavior appropriate to each product.

## Reflection
Among the four pillars, encapsulation would be the most useful for improving the sari-sari store inventory system. It allows the product information, such as price and quantity, to be kept together with the methods that control how the data is changed. Thai can help prevent errors, such as accidentally assigning an incorrect stock quantity or price. Encapsulation also makes the program easier to maintain because the data and its related operations are organized within the same object.

                Product
        ------------------------
        - name
        - price
        - quantity
        ------------------------
        + add_stock()
        + sell_product()
        + display_info()
              /       \
             /         \
     FoodProduct   HouseholdProduct
