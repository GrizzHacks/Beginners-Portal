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
> Each time we use this class, we are creating a `Pokemon` object.


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
- [Instance data](https://www.programmerinterview.com/c-cplusplus/whats-the-difference-between-a-class-variable-and-an-instance-variable/) are any variables/attributes which are written at the class-level, i.e. underneath the class heading (`public class`). These variables can be accessed in any class method.
> These attributes are also unique for each object that is created from the class. This ensures that each object can have its own state.
- [`private`](https://www.geeksforgeeks.org/access-modifiers-java/) is a visibility modifier, and is important to the concept of [encapsulation](https://www.tutorialspoint.com/java/java_encapsulation.htm). We won't cover encapsulation here, but just know that `private` ensures an attribute cannot be referenced from outside an object.
- `String`, `int`, and `double` all represent different Java [data types](https://www.w3schools.com/java/java_data_types.asp).
> A `String` is actually an object, but here we'll just view it as a collection of alphanumeric characters.    
> An `int` is any number that does not use a decimal point.    
> A `double` is any number that can have a fractional component.

### Let's go ahead and define the methods we want to use in our class

Remember earlier when we were discussing methods to alter our attributes? Now that we have our attributes, let's define our methods.

Let's take a look at the first method we discussed: `getNationalNumber()`. Outside of the curly braces that wrap the statements in our constructor, but within the curly braces that wrap our class, write the following:

```Java
public int getNationalNumber()
{
    return nationalNumber;
}
```

Method are constructed in a certain way. First, we write the method decleration. The method decleration is made of four parts:
- Optional modifiers (in this case the visibility modifier `public`),
- The return value (in this case `int`),
- The method name (`getNationalNumber`), and
- The parameter list (left blank here).

The purpose of our method is to *return* the number associated with our Pokemon. 

We should reason that the method `getPokemonName` will behave in the same way as `getNationalNumber`, so try to write it by yourself, underneath `getNationalNumber`. 
> Hint: The return type will be different. Look at how we defined `name` for a hint.
------

Figure it out? My code for the method looks like this:

```Java
public String getPokemonName()
{
    return pokemonName;
}
```

#### What We've Learned
- [Methods](https://www.w3schools.com/java/java_methods.asp) are defined by optional modifiers, a return type, a method name, and a list of parameters. 
- What the method actually does is contained within the method body. The method body is contained within curly braces (`{}`).
- [`public`](https://www.w3schools.com/java/java_modifiers.asp) is a visibility modifier which allows us to use a method by referencing a `Pokemon` object. 
- `int` and `String` are examples of the [return type](https://www.decodejava.com/java-method-return-types.htm), i.e. what type of variable is given back to the user.
- If we have a return type, we MUST use the `return` keyword. This makes sure that the result of our method's process is given back to the larger program.
- Have you noticed how each of our methods start with the word "get"? Programmers will often refer to these types of methods as ["getters"](https://www.codejava.net/coding/java-getter-and-setter-tutorial-from-basics-to-best-practices), since they retrieve - or get - the value of an attribute from our object. You'll also see reference to "setter" methods. 

### You know what's great? We have everything we need to get our code to run! Let's try this.

Going back to `PokedexEntries.java`, under where we have written `System.out.println("Hello World!");`, let's create an actual `Pokemon` object. 

In order to do that, we first have to declare the type of object we are creating. Think of this as deciding the data type for a standard variable. Because we want to create a `Pokemon` object, our type of object is `Pokemon`. 

Now we need a name for our `Pokemon` type. This will be our variable name. I'm going to call my `Pokemon` object `Pikachu`. Write `Pokemon Pikachu` underneath the `System.out` statement.
> This is the exact same procedure as writing `int nationalNumber`, just without the visibility modifier.

In order to give our `Pikachu` variable value, we need to create a new `Pokemon` object. To do this, write the following line of code:    
```Java
Pikachu = new Pokemon("Pikachu", 25, "Mouse Pokemon", 0.4, "Pichu, Raichu");
```
The `new` keyword instantiates a `Pokemon` object. We need to include the various strings and numbers in our parameter list because that is what is required by the constructor method in `Pokemon.java`.
> Take a look back at `Pokemon.java` if you are confused.

Underneath this, we'll test the methods that we wrote. In order to do this, write out:
```Java
System.out.println(Pikachu.getNationalNumber());
System.out.println(Pikachu.getPokemonName());
```
Hit the green "Play" button and see what happens! You should see 
`Hello World!`    
`25`    
`Pikachu`    
in the output terminal.
> If not, use the error given to try and fix your code. You can reference my code through the Beginners Portal by clicking "Beginners-Portal -> Pokedex -> PokedexEntries -> src/pokedexentries" and then clicking on either file.

#### What We've Learned
- We are able to create objects based on classes that we have created by declaring a variable as the name of our class. 
- Using the [`new` keyword](https://www.geeksforgeeks.org/new-operator-java/) allows us to instantiate a new object from a class.
- Variables written in the parameter list of our constructor method must be filled in by values when we create a new object.
- [`System.out.println()`](https://javapapers.com/core-java/system-out-println/) allows us to write information to the output terminal/console.
- We can call public methods from a class by typing the object's name, a period, and then the name of the method.
> Be sure to include the parenthesis at the end!

### Let's clean up our PokedexEntries.java page, then go back to writing more methods for our Pokemon class.

Feel free to get rid of all the grey text that exists, as well as the `"Hello World!"` execution statement. 

I'm also going to rewrite the section of code which creates our `Pikachu object`. Instead of declaring the `Pikachu` variable, then creating a new object, I can do it all in one line of code:

```Java
Pokemon Pikachu = new Pokemon("Pikachu", 25, "Mouse Pokemon", 0.4, "Pichu, Raichu");
```
This makes the code cleaner and shorter. It isn't necessary, and you can certainly leave it as how we originally wrote it.

----

Perfect! Now, let's go back to `Pokemon.java` and continue to write more methods.

Let's add in our `changeDescription()` method. We know it should be called through the object's name, and it has the name `changeDescription()`. But it won't return anything to the user who called the method. So our return type will be `void` Go ahead and write all of that out yourself under the `getPokemonName()` method. Be sure to include your curly braces!

Now, in order to change a description, we need to get the original description and a new one. We're able to directly reference the original description via its variable name ` shortDescription`, but how can we get a new one? 

It needs to be provided by the user, of course! And how can we use that new description to change the old one? We need to pass it in as an arguement! That means we need to add a parameter to our `changeDescription()` method. Once you've done that, try to figure out how to actually change the description. 

-----
 
Figure it out? If not, that's okay! We're all still learning. Here's what my method looks like:

```Java
public void changeDescription(String shortDescription)
{
    this.shortDescription = shortDescription;
}
```

#### What We've Learned
- We are able to declare and instantiate objects in the same line of code. 
- [`void`](https://www.w3schools.com/java/ref_keyword_void.asp) is used when a method does not return anything. 
- Remember when I talked about getters and setters? `changeDescription()` would be considered a setter method, since we are changing - or setting - the description for our Pokemon to something else. We could very easily have called this method `setDescription()` to follow standard conventions.

### Let's add in our final two methods

Using what you know, go ahead and try to add in `alterHeight()` and `addEvolution`. 
 
My code for those two methods ends up looking like this:

```Java
public void alterHeight(double newHeight)
{
    height = newHeight;
}

public void addEvolution(String evolve)
{
    evolutions += ", " + evolve;
}
```

That final method body looks weird, right? What we're performing is string concatination. If we had just done `this.evolutions = evolutions`, we would have gotten rid of the evolutions already in place. By using the `+=` symbol, we tell the computer to add on the value(s) passed in through `evolve` to the value(s) that already exists in `evolutions`. 
`", " + evolve` is another form of string concatination, in that we are adding a comma and a space to the front of the value of `evolve`. 

> Example: Say `evolutions` = "Pichu" only. I realize that I forgot to add Raichu. I will call the `addEvolution` method by writing `Pikachu.addEvolution("Raichu");` "Raichu" will be the value of the variable `evolve`. In the body of `addEvolutions()`, we append `, ` to the front of "Raichu" (so it now looks like ", Raichu"), then add that to the value of `evolutions`. `evolutions` is now equal to "Pichu, Raichu". 

#### What We've Learned
- [String concatination](https://www.techiedelight.com/concatenate-two-strings-java/) is the process of combining two Strings together using the `+` symbol.
- [+=](https://www.geeksforgeeks.org/compound-assignment-operators-java/) is shorthand notation for the following type of structure: `x+=y` is equivalent to `x = x + y`. This also works for numerical values. 

### With our code all set, go ahead and try out these last few methods that we have added on.

As you're doing this, you may notice errors popping up if you want to display the results of `changeDescription()`, `alterHeight()`, or `addEvolution()` via `System.out.println()`. You can change how the methods work by altering the return type, but that defeats the purpose of those methods in the first place. Instead, what we can do is add a `toString()` method which will display all of the attributes of our Pokemon entry. 

Go back to `Pokemon.java` and write the following code:

```Java
public String toString(){
    String result = "Pokemon Name: " + pokemonName + "\n";
    result += "National Number: " + nationalNumber + "\n";
    result += "Description: " + shortDescription + "\n";
    result += "Height (in meters): " + height + "\n";
    result += "Evolutions: " + evolutions;

    return result;
}
```
Now, go to `PokedexEntries.java` and called the methods like so:    
`Pikachu.*methodname*(*parameters if required*);`    
Finally, to see everything in action, do `System.out.println(Pikachu);`

This will give us all the details of our `Pokemon` object, with all the changes made to it via our methods. If you want to see how `Pikachu` looked before all of the changes, just put `System.out.println(Pikachu);` below where we created our `Pikachu` object.

#### What We've Learned
- [`"\n"`](https://docs.oracle.com/javase/tutorial/java/data/characters.html) stands for "newline", and adds a newline character to the end of a sentence so the next sentence starts on a new line.
> Look at "Escape Sequences" in the link.
- A [`toString()` method](https://www.javatpoint.com/understanding-toString()-method) makes sure that we are properly able to view attributes without having to redo entire sections of code
> In other examples, you'll see that it provides meaningful information where we normally get a confusing line of code. 

## Running the Code

In order to appreciate the fruits of your labor, all you need to do is hit the big green "Run Project" arrow.

### Difficulties 
If your code does not work for some reason, make sure:
- your method bodies are surrounded by their own set of curly braces
- your methods are within the class curly braces
- each line of code that isn't a method decleration ends in a semicolon (;)

Compare your code to mine by going to "Beginners Portal -> Pokedex -> PokedexEntries -> src/pokedexentries" and then selecting either file. 

If you are still getting errors, use the internet! It is often times your best resource.

## Next Steps

