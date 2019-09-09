# Pokedex Tutorial
> Use this tutorial to learn some of the basics of Java

We'll be creating a way to generate entries for different Pokemon in a Pokedex (a dictionary of Pokemon). Use this tutorial to learn about object-oriented programming and generate ideas for web applications.

## Set-Up

1. The best way (up for some debate) to develop Java applications is by using an IDE called NetBeans. [Please download NetBeans](https://netbeans.org) for this tutorial.
> I'll be using Netbeans v8.2. There are newer versions available, and all the code should follow.    
> You'll be fine if you download Java SE    
> You're more than welcome to see if your chosen text editor can write Java files, but Netbeans is generally the easiest system to work with. I'll be using this program, and the tutorial will reflect that.  
2. Upon opening NetBeans, click "File -> New Project". Leave the selections as "Java" and "Java Application". Save the project name as "PokedexEntries" and save it to a location accessable by your Github connection, DevPost, etc... Finally, click "Finish".
3. When the file first opens, you'll see a whole bunch of confusing text. Under the gray text that reads `// TODO code application logic here`, write `System.out.println("Hello World!")`.
> Make sure this new line is in between the curly braces (`{}`).
4. Press the green play arrow at the top of the page, and see what happens! You should now see "Hello World!" printed in the built-in terminal. Pretty cool, right? We'll be doing some more awesome stuff later on.

If you want to see you file in context, you can click on the "Projects" tab along the left side of the screen. Feel free to explore more of the IDE before getting started.

## Coding Our Application

### Let's go over some basic concepts of object-oriented programming first.

Object-oriented programming (OOP) is a way of writing code that allows us to create *objects* which interact with one another. What is great about OOP is that it gives us the ability to model real-world entities in a simple and speedy fashion. 

Consider the following example: We run a bank, and want to have a way of keeping track of all of our employees. We know that each employee has a name, age, rank within the company, salary, and vacation time. We can certainly type each label and information for every employee into a database. But what if we had 10,000 employees? Wouldn't it be great if all of those labels were already set-up, and all we had to do was insert the information? 

That's were OOP comes in! Using OOP, we are able to create those labels so that our secretary can easily insert a new employee's information when they are hired in. 

OOP can get a bit complex, but here are the basic concepts you should know for this tutorial:

[Object](https://docs.oracle.com/javase/tutorial/java/concepts/object.html): An object is a fundemental element in a program. It is an individual employee in our banking example, of a Pokemon in this tutorial.       
[Attribute](http://www.dmc.fmph.uniba.sk/public_html/doc/Java/ch2.htm#Attributes): An attribute is a piece of information about the object (e.g. the salary of an employee, or the name of the Pokemon.)    
[State](https://www.quora.com/What-is-an-object-state-in-programming): An object's state is closely tied to its attributes. The state is an object is defined by its attributes.    
[Methods/Operations](https://brilliant.org/wiki/methods-oop/): Methods are actions we can take to modify an object. For example, we can increase the salary of an employee. For a Pokemon, a potential method would be the ability to raise or lower its HP.   
[Behavior](http://www.informit.com/articles/article.aspx?p=25856&seqNum=6): The behavior of an object is closely tied to its methods. It is defined by the methods/operations associated with an object.    
[Class](https://docs.oracle.com/javase/tutorial/java/concepts/class.html): A class is the way in which we create objects. Think of a class as a blueprint for a building. It tells us *how* to build an object, but is not the object itself.

> Some of the reference pages may be a bit confusing based on your knowledge level, but that's okay. Try to understand as much as you can, and also feel free to look some stuff up. We're performing a very basic version of OOP, and likely won't get into the meat of what it is.    
> If you are interested in reading a basic explaination of the finer points of OOP, [freeCodeCamp has an excellent article.](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/)

You'll also want to understand what a [variable](https://www.kidscodecs.com/variables/) is.

#### What We've Learned
- Object-Oriented Programming (OOP) is a programming technique that comes from defining classes which represent object(s). 
- Objects are defined by their state and behavior, which themselves are defined by their attributes and methods, respectively. 
- Variables are names used to represent values or objects in code.    
> [Here is an explaination of variables in Java](https://www.geeksforgeeks.org/variables-in-java/). I'll also go over specific ones later on in the code. 

### Using what we know, let's try and come up with a name for our class, its attributes, and its methods.

If you've every played a Pokemon game, you know that an entry in the National Pokedex can hold the following data for each Pokemon:
- Its National Number
- Its Name
- Its Type(s)
- Its Species/Nickname
- Its Height
- Its Weight
- A Short Description
- An Image of the Pokemon
- An Image of its Footprint
- Its Habitat
- Its Evolutions

This data gives us the different attributes we want to include in our class! In fact, it can also help us come up with variable names for that information! 

Choose 5 of the items given above to use as attributes within our class, and try to come up with a variable name to represent the data it will hold. I'll be using:

- Attribute: National Number; Variable Name: `nationalNumber`
- Attribute: Pokemon Name; Variable Name: `pokemonName`
- Attribute: A Short Description; Variable Name: `shortDescription`
- Attribute: Height; Variable Name: `height`
- Attribute: Evolutions; Variable Name: `evolutions`

Now that we know our attributes, let's think of some methods we could use to change our attributes. 

- The National Number will always stay the same, but maybe I'll want to know what its number is specifically. I'll need a method called `getNationalNumber()`.
- The Pokemon's name will never change, but maybe I'll want to call its name specifically. I'll need a method called `getPokemonName()`.
- The description of the Pokemon can change depending on how much we know about the Pokemon. I'll create a method to change its informaton called `changeDescription()`.
- The height of a Pokemon could change, depending on how many we've caught. I'll create a method called `alterHeight()`.
- What if we discover a new evolution for a Pokemon? I'll create a method called `addEvolution()`. 

Finally, we need a class that will act as the blueprint for each Pokemon entry that we create.  Each Pokemon entry represents a unique Pokemon. So let's decide to call our class `Pokemon`.


#### What We've Learned
- Characteristics of an object are usually great at telling us what its attributes are, and can serve as a guideline for variable names.
- Methods are typically used to alter attributes.

### Let's start writing some meaningful code!

The page we are currently on (with `public class PokedexEntries`) will help us with creating new entries in our Pokedex, but it is not ultimately what *makes* the entries themselves. 

Go over to your "Projects" tab, and right click on "pokedexentries". Select "New -> Java Class" and set the class name as "Pokemon". Hit "Finish"

You should now see a page with a lot of grey text, `package pokedexentries`, more grey text, and `public class Pokemon` on it. Feel free to delete the grey text.

This page will serve as our class - our blueprint for each Pokemon entry in the Pokedex. 

Classes will very often have methods called constructors, which help us to initialize the variables associated with each object. In order to write a contructor, it must have the following two properties:
1. The name of the constructor must be the same as the name of the class
2. The constructor cannot have a return type, or return a value.
> We'll explore this second point later on. 

Let's write our constructor! In between the curly braces of our class, write the following:

```Java
public Pokemon(String name, int num, String description, double height, String evolutions)
{
    pokemonName = name;
    nationalNumber = num;
    shortDescription = description;
    this.height = height;
    this.evolutions = evolutions;
}
```
If you've done it correctly, you should be seeing an error message of "cannot find symbol" in Netbeans. We'll fix that in one second.    

What we've done here is create a constructor. When we create a new Pokemon entry, we'll be supplying the name of the Pokemon, its national number, a description, its height, and its evolutions. That information is passed in as parameters, those values in between the parenthesis. The information in the parameters are now called arguements, and are then assigned to the data within the class (shown via `pokemonName = name`). `pokemonName` is data that exists within the class - called instance data - while `name` is an arguement. 

> As an example, say we want to create an entry for Pikachu. When we create our object, we'll be passing it in like this:    
> `Pokemon("Pikachu", 25, "Mouse Pokemon", 0.4, "Pichu, Raichu")`.    
> That information is sent to our constructor, where our variable `pokemonName` becomes equal to "Pikachu". 

Let's get rid of those error messages. Underneath `public class Pokemon` but above `public Pokemon()` (in between the curly braces), write

```Java
private String pokemonName;
private int nationalNumber;
private String shortDescription;
private double height;
private String evolutions;
```
What we've done is create instance data, or instance variables. These variables can be accessed anywhere within the class, making them easily manipulable. They are also representative of our attributes.

#### What We've Learned
- A [constructor](https://www.w3schools.com/java/java_constructors.asp) is a special method used to instantiate objects. It will serve to assign data that is passed in to our attributes.
- The [`this` keyword](https://www.guru99.com/java-this-keyword.html) is used to distinguish the parameters of the constructor from the instance data when both have the same name. If they don't have the same name, we don't need the `this` keyword.
- [Parameters](https://www.quora.com/In-Java-what-are-parameters) are the list of variables in a method decleration. 
> A method decleration is where we write out the name of our method with parenthesis next to it. E.g. `public Pokemon()`.
- [Arguements](https://www.geeksforgeeks.org/argument-vs-parameter-in-java/) are the values passed into a method.
- [Instance data](https://www.programmerinterview.com/c-cplusplus/whats-the-difference-betwe    en-a-class-variable-and-an-instance-variable/) are any variables/attributes which are written at the class-level, i.e. underneath the class heading (`public class`). These variables can be accessed in any class method.
> These attributes are also unique for each object that is created from the class. This ensures that each object can have its own state.
- [`private`](https://www.geeksforgeeks.org/access-modifiers-java/) is a visibility modifier, and is important to the concept of [encapsulation](https://www.tutorialspoint.com/java/java_encapsulation.htm). We won't cover encapsulation here, but just know that `private` ensures an attribute cannot be referenced from outside an object.
- `String`, `int`, and `double` all represent different Java [data types](https://www.w3schools.com/java/java_data_types.asp).
> A `String` is actually an object, but here we'll just view it as a collection of alphanumeric characters.    
> An `int` is any number that does not use a decimal point.    
> A `double` is any number that can have a fractional component.

### 