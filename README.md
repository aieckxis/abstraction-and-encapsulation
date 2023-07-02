# OOP Concepts: Abstraction and Encapsulation
This repository demonstrates the fundamental concepts of **abstraction and encapsulation** in **object-oriented programming (OOP)**. It contains script files that create three classes: **Fan, Car, and Pet**. Each class showcases different aspects of abstraction and encapsulation. These classes serve as examples to illustrate how abstraction and encapsulation can be applied in OOP. They show how properties and behaviors of objects can be enclosed within classes, promoting modular design and hiding implementation details from users of the class.

## Fan Class:
The **Fan class** represents a fan object with various properties such as **speed, radius, color, and on/off state.** It provides methods to get and set these properties. The class defines three constants for fan speeds: **SLOW, MEDIUM, and FAST**. The constructor initializes the fan object with default values or the values provided by the user. The class also includes methods to check if the fan is on and to turn it on or off. Overall, the Fan class encapsulates the behavior and attributes of a fan.

### How abstraction and encapsulation are used in the Fan class:
**Abstraction**: Abstraction means hiding unnecessary details and showing only the important parts. In the **Fan class**, abstraction is used by providing simple methods for users to get and set properties like the **fan's speed, radius, color, and on/off state**. Users don't need to know how these properties are stored or manipulated inside the class. They can just use the provided methods to interact with the fan object.

**Encapsulation**: Encapsulation means bundling data and related actions together and controlling access to them. In the **Fan class**, encapsulation is used by keeping the data fields **(speed, radius, color, on/off state)** private. This means they can only be accessed or modified using special methods provided within the class. By doing this, we can ensure that the internal state of a Fan object is managed in a controlled way, preventing unwanted changes and maintaining the integrity of the object.

In simpler terms, abstraction helps to simplify the way users interact with the fan object by providing easy-to-use methods, while encapsulation helps to protect the internal workings of the fan object and ensure that it is used correctly.

## Car Class:
The **Car class** represents a car object and encapsulates its **year model, make, and current speed.** It provides methods to accelerate the **car, brake it, and retrieve the current speed.** The class utilizes encapsulation by making the **year model, make, and speed attributes** private, which means they can only be accessed or modified through the class methods. The class serves as a blueprint for creating car objects and allows for easy manipulation of their speeds.

### How abstraction and encapsulation are used in the Car class:
**Abstraction:** Abstraction means simplifying complex things by breaking them down into smaller, easier-to-understand parts. In the **Car class**, abstraction is used to hide the inner workings of how the car's speed is managed. Instead of dealing with complicated details, users of the class can simply interact with the car by using methods like **accelerate, brake,** and **get_speed.** These methods provide a simpler and more understandable way to control and access the car's speed.

**Encapsulation:** Encapsulation is the practice of keeping related data and functions together in a single unit, called a class. It helps in organizing code and protecting data from unauthorized access. In the **Car class**, encapsulation is used by marking certain attributes as private (using double underscores). Private attributes cannot be directly accessed or modified from outside the class. Instead, users of the class interact with the car object through the public methods provided, such as **accelerate,** **brake,** and **get_speed.** This way, the internal workings of the car are hidden, and the class provides a controlled and secure way to interact with the car's speed.

By using abstraction and encapsulation, the **Car class** simplifies how the car's speed is managed and provides a clear interface for users to control and access the speed. Users don't need to worry about the inner details of the class, allowing for easier understanding and maintenance of the code.

## Pet Class:
The Pet class represents a pet with attributes such as **name, animal type, and age.** It provides methods to set and retrieve these attributes, allowing for interaction with pet data. The class encapsulates the **pet's information**, ensuring data privacy by using name mangling to make the attributes private. The class promotes abstraction by separating the implementation details from the user interface, making it easy to create and manage pet objects in a structured manner.

### How abstraction and encapsulation are used in the Pet class:
**Abstraction:** Abstraction in the **Pet class** means that we hide unnecessary details and provide a simplified way to interact with a pet's information. Instead of directly accessing the pet's attributes like **name, animal type, and age**, we use methods like **set_name(), set_animal_type(), set_age(), get_name(), get_animal_type(), get_age().** These methods provide an abstraction layer, allowing users of the class to easily set and retrieve the pet's information without needing to know the inner workings of how the data is stored or handled.

**Encapsulation:** Encapsulation in the **Pet class** means that we bundle together the pet's data and the methods that operate on that data within the class. The attributes **__name, __animal_type, and __age** are made private by using double underscores, which means they cannot be accessed directly from outside the class. This protects the data from accidental modifications or unauthorized access. Instead, users interact with the attributes through the public methods provided by the class, ensuring controlled and proper handling of the pet's information.

By using abstraction and encapsulation, the **Pet class** provides a simplified and secure way to work with pet data. Users of the class don't need to worry about the internal details or risk modifying the data incorrectly. They can simply use the provided methods to set and retrieve the pet's attributes, making the code easier to understand, maintain, and reuse.

