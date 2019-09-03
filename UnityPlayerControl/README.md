# Unity Player Controller Tutorial
> Use this tutorial to learn some C# and the Unity platform.    
> Created by [James Lynott](https://www.linkedin.com/in/james-lynott/)

We'll be programming a third-person controller for a video game character using C# and the Unity platform. Use this tutorial as a stepping-off point for making your own video game!

## Set-Up

1. You'll want to begin by downloading the [Unity Hub](https://unity3d.com/get-unity/download), a new program used to manage Unity projects.
2. From the Hub, you'll want to install the latest version of Unity. This can be done during the initial Unity Hub set-up, or from the 'Installs' menu.
3. Create a new Unity project by going to the 'Projects' menu tab, clicking 'New', then giving your project a unique name. Be sure to save it to a location that can be accessed by yourself and/or is easily referenced by your Github account. Be sure to leave the template as '3D', then click 'Create Project.'    
> Note that the choice between a 2D and 3D template only affects starting configurations and doesn’t limit what options are available in the editor.
> By default, Unity will use Visual Studio for script editing, but if you wish to use another text editor, this can be changed in Edit -> Preferences -> External Tools from within any Unity project.

## Coding our Third-Person Player Controller

### Setting Up the Landscape

Before we get right into the coding, it’s worth covering a few basic Unity concepts. You should find a 'Hierarchy' panel to the left of your editor, with "Main Camera and "Directional Light" listed inside. This panel shows all of the `GameObjects` present in your game, and their relationship to each other.
> `GameObjects` are bundles of `Components`, or properties. We attach `Components` to a `GameObject` - such as a light component - to allow them to do different things in our game.     

Right click in an empty spot in the hierarchy and select '3D Object -> Plane.' This will create a new `GameObject` with a few components that represents a geometric plane surface in the world. This will be our simple ground to test our controller on. 
> Feel free to rename this plane object by selecting it in the Hierarchy and editing the name field at the very top of the Inspector panel (by default to the right of the screen).

Now, we’ll create a cube to represent the player character by right clicking in the heirarchy and selecting '3D Object -> Cube'. If you look at the game in the 'Scene' view at the center of the screen, you’ll see the cube bisects the plane. Either click and drag the cube up, or change the position from the 'Inspector' panel so that it sits above the plane. Rename the cube.

We now need to add a couple of extra components to this player object. Scroll down to the bottom of the 'Inspector' panel and click the “Add Component” button. Search for “RigidBody” in the new menu. This will allow us to use Unity’s physics engine on this object. Press the play button above the 'Scene' view to see a runtime demonstration of your project. The cube should fall onto the “ground”.

Hit the “Add Component” button again, and scroll to the bottom to find the “New script” option. Name it “MovementScript” and press “Create and Add.”
> Don’t use a space in the script’s name; it will cause a compilation error.

Find the new script in the 'Inspector' panel, click the gear icon to the right of its name, and click “Edit Script”. The script will open in a text editor. We can begin to program the actions of the cube now!

#### What We've Learned
- [`GameObjects`](https://docs.unity3d.com/Manual/class-GameObject.html) are the basic building blocks of a Unity game.
- We can change what `GameObjects` do by adding [`Components`](https://docs.unity3d.com/Manual/Components.html)
- We can keep track of all of our `GameObjects` with the 'Hierarchy' panel, and view properties of `GameObjects` in the 'Inspector' panel.
- The RigidBody Component allows us to use [Unity’s physics engine](https://docs.unity3d.com/2018.1/Documentation/Manual/PhysicsOverview.html)
- We can run our game from inside the Unity editor

### Beginning Our Movement Script

Delete the information that already exists within the file so that we have a blank slate. 

Begin by importing the `UnityEngine` namespace and setting up the class: 

```C#
using UnityEngine;

public class MovementScript : MonoBehaviour
{
	//Our code will go here
}
```
This will give us access to all of the basic Unity methods and should be the only namespace we need for the time being
> It's important that the name of the class is the same as the name of the script you created (which is why spaces will not work) and that it inherits from [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html)

Now we're going to write a function called `FixedUpdate`. Make sure your code now looks like this:

```C#
using UnityEngine;

public class MovementScript : MonoBehaviour
{
private void FixedUpdate()
{
//Movement controls
}
}
```
This is very similar to one of the default functions shown in the original template: [the `Update` function.](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) The advantage to using `FixedUpdate` in our situation is that it is called at a fixed rate rather than once per game frame, as is done with the traditional `Update` function.
> This is advantageous in cases where regularity is vital, such as in physics calculations. 

We'll now create a series of [if-statements](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/if-else) to handle the different inputs we need to check for inside of our `FixedUpdate` function.

```C#
private void FixedUpdate()
    {
        if (Input.GetKey(KeyCode.W))
        {
            //move upscreen
        }
        if (Input.GetKey(KeyCode.S))
        {
            //move downscreen
        }
        if (Input.GetKey(KeyCode.A))
        {
            //move left
        }
        if (Input.GetKey(KeyCode.D))
        {
            //move right
        }
    }
```
The [`GetKey` method](https://docs.unity3d.com/ScriptReference/Input.GetKey.html) returns true each frame the specified input button is down - in this case the A, W, S, and D keys. All we need to do is increment the position by some amount for as long as the button is held down.

There are several ways to do this, but the simplest is to probably directly translate the `GameObject` with the [`Translate` method.](https://docs.unity3d.com/ScriptReference/Transform.Translate.html)

Write the following in place of the comments (signified by the backslashes):
```C#
if (Input.GetKey(KeyCode.W))
{
    gameObject.transform.Translate(Vector3.forward);
}
if (Input.GetKey(KeyCode.S))
{
    gameObject.transform.Translate(-Vector3.forward);
}
if (Input.GetKey(KeyCode.A))
{
    gameObject.transform.Translate(-Vector3.right);
}
if (Input.GetKey(KeyCode.D))
{
    gameObject.transform.Translate(Vector3.right);
}
```
> “gameObject” is already predefined as the `GameObject` that this script is attached to.

Save your file, then return to the Unity editor and press the play button. You'll see that the cube moves far too fast. 
> If your cube doesn't move at all, or you notice an error notification in the Unity editor, make sure that the name of the class is the same as the name of the script you created. 

We can fix this by creating a speed variable that allows the cube to move at a more reasonable pace. 

Under our class declaration (`public class MovementScript : MonoBehaviour`), write:    `float speed = xf;`,    
where x is any value that you decide. For this tutorial, I recommend setting it as `float speed = 0.05f;`.
> We need to include the "f" at the end of our 0.05 because otherwise the value is treated as a `double`. [Read more about C# variable types here](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/value-types)

Back at our `FixedUpdate` function, integrate the `speed` variable like this:
```C#
if (Input.GetKey(KeyCode.W))
{
    gameObject.transform.Translate(Vector3.forward * speed);
}
if (Input.GetKey(KeyCode.S))
{
    gameObject.transform.Translate(-Vector3.forward * speed);
}
if (Input.GetKey(KeyCode.A))
{
    gameObject.transform.Translate(-Vector3.right * speed);
}
if (Input.GetKey(KeyCode.D))
{
    gameObject.transform.Translate(Vector3.right * speed);
}
```
You can play around with different speed settings until your character moves at a pace you like.

#### What We've Learned
- Unity comes with many helpful methods, accessible by inheriting from the MonoBehaviour class.    
- The `Update` method allows us to run some code almost continuously during runtime.
- We can use `FixedUpdate` when applying physics interactions.
- We can directly modify a `GameObject’s` transform values.
- What the `GameObject` script is attached to is represented by the variable “gameObject”.

### Programming a Jump Button

With the horizontal movement taken care of, we now need to move on to vertical movement. Let's program a jump button! Unlike with walking, if you hold down the jump button the player shouldn’t rise indefinitely. Therefore, we’ll use the [`GetKeyDown` method](https://docs.unity3d.com/ScriptReference/Input.GetKeyDown.html) so that it will only execute on the frame that the button is pressed.

Editing the position directly would also be challenging with a jump feature, so instead we can take advantage of the RigidBody and use the physics method of [`AddForce`.](https://docs.unity3d.com/ScriptReference/Rigidbody.AddForce.html) 
> We'll set the [`velocity`](https://docs.unity3d.com/ScriptReference/Rigidbody-velocity.html) to zero before initiating the force to prevent outside interactions from affecting the jump height.    
> Horizontal movement does not qualify as RigidBody velocity, so we can still control the character mid-jump.

We need to use a method associated with the RigidBody component. We can access such a method by typing:

```C#
private void Start()
    {
        rigidBody = gameObject.GetComponent<Rigidbody>();
    }
```

above `private void FixedUpdate()`.

[`Start()`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) is a common MonoBehavior function which executes just once at the start of a scene (I'll explain this later on). We use `Start()` due to the computational resources required by the [`GetComponent` method](https://docs.unity3d.com/ScriptReference/GameObject.GetComponent.html).    
> By doing the above, we are storing the RigidBody in a variable, which we can access via the variable name "rigidBody".    

Under our `speed` variable declaration, create a new variable called `jumpHeight`. Your code for this should look like:    
`int jumpHeight = x;`    
where x is any numerical value. For this example, I set x equal to 200.

-----

We are mostly there, but there remains one problem: the player can simply tap the jump button mid-air and jump again, allowing them to go as high as they want! Many games may employ double or triple jumping as a gameplay mechanic, but for the sake of this tutorial, we will limit the player to a single jump.  

One way of checking to see if we are currently in the air is by reading the RigidBody’s velocity in the y direction. Normal movement across the plane will actually affect the vertical velocity very slightly, so we’ll check to see if it’s in some reasonable rounding error. 

We'll add the following variables to the class in order accomplish this task, as well as see if we are actually falling:

```C#
bool isFalling = false;
float fallRounding = 0.01f;
```
> A `bool` is short for [boolean](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/bool), which is simply a true or false variable.    
> You'll notice that in my code, I wrote the `speed` and `fallRounding` variables on one line. You can do that as well, if it makes sense, or leave it as how I have described above.

Place the following code in-line with the rest of your if-statements within the `FixedUpdate()` function:

```C#
if (!isFalling) //If we aren't falling and we've pressed space, jump
{
    if (Input.GetKeyDown(KeyCode.Space))
    {
        rigidBody.velocity = Vector3.zero;
        rigidBody.AddForce(Vector3.up * jumpHeight);
    }
}

if (Mathf.Abs(rigidBody.velocity.y) > fallRounding) //If the absolute value of the y velocity is less than the rounding variable, we aren't falling
    isFalling = true;
else
    isFalling = false;

```
 
#### What We've Learned
- The `GetKeyDown` method returns true only on the first frame a key is pressed
- To use physics interactions, we need to interact with a `GameObject’s` RigidBody component
- Code that should only be executed once at the start should be put within the `Start` method body

### Having the camera follow the player.

Congratulations, you’ve now built a functional third-person controller for your game! Let’s try making one more modification: having the cameral follow the player.    

Go back to the Unity editor, and select  "Main Camera" in the hierarchy. Click and drag the camera onto the player object in the hierarchy. The camera should show up below the player in the hierarchy and shifted over to the right.     
We have made the camera a child of the player (which is now the parent). The child object will inherit any changes to the basic `GameObject` properties (position, activity, etc.), so now the camera will move the same amount as the player. 

#### What We've Learned
- We can have certain objects inherit the properties of other objects by allowing for [object parenting](https://www.tutorialspoint.com/unity/unity_transforms_and_object_parenting.htm)

## Running the Game

In running the game, we can better understand what a [scene](https://docs.unity3d.com/Manual/CreatingScenes.html) is.

Scenes can be thought of as isolated sub-games, which can share as many assets with other scenes as you’d like. Different levels, cutscenes, and menus are generally each given their own scene. Right now, we only have one scene, which you can find in the "Assets" folder (viewable from the Projects tab near the bottom of the screen).
> If you save and close your project, and come back to it later to find a blank editor, don’t panic! You just need to reopen the scene you were working on.

To actually build a standalone executable version of our game, we’ll need to check that our scene is listed as part of the build. Go to 'File -> Build Settings' and click 'Add Open Scenes'. Then, if you want to create a build of this game, click 'Build and Run.' Select a location to save the build. 
> Generally, it’s wise to create a new folder for this.

After a moment, you should be able to play a version of your third-person game.


## Difficulties

If you encounter any errors, they should show up near the bottom of the screen or in the 'Console' tab (next to the 'Projects' tab).    
If code is behaving in a way you don’t expect, printing a message to the console to see when a certain line is run or what value a variable has at any given point can be very helpful. > Print a message with the [`Debug.Log()` method.](https://docs.unity3d.com/ScriptReference/Debug.Log.html)

## Next Steps
From here, you’ll need to think of how you’d like your game to take shape.    
Here are some things to consider:
- How would you program in projectile avoidance? (Hint: look into `collision` detection and the `SetActive` method.)
- How would you create a double jump?
- Can you expand your game to include more characters? What about more players?
- If you want less of an arcade feel to your controller, one thing you want to try is reducing the amount of control the player has while jumping. How might you do this?
- If the cube is knocked over, our controls will no longer be accurate. Try to come up with another way to program the directions and motions of the cube. 

# Good Luck Hackers!
 -----

 This code comes from the author listed at the top of the page, and is edited by a member of the GrizzHacks 4 team. No commercial gain is sought from using the code, and is instead intended for educational purposes.