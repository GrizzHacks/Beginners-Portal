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

Hit the “Add Component” button again, and scroll to the bottom to find the “New script” option. Name it something like “MovementScript” and press “Create and Add.”
> Don’t use a space in the script’s name; it will cause a compilation error.

Find the new script in the 'Inspector' panel, click the gear icon to the right of its name, and click “Edit Script”. The script will open in a text editor. We can begin to program the actions of the cube now!

#### What We've Learned
- [`GameObjects`](https://docs.unity3d.com/Manual/class-GameObject.html) are the basic building blocks of a Unity game.
- We can change what `GameObjects` do by adding [`Components`](https://docs.unity3d.com/Manual/Components.html)
- We can keep track of all of our `GameObjects` with the 'Hierarchy' panel, and view properties of `GameObjects` in the 'Inspector' panel.
- The RigidBody Component allows us to use [Unity’s physics engine](https://docs.unity3d.com/2018.1/Documentation/Manual/PhysicsOverview.html)
- We can run our game from inside the Unity editor

### Beginning Our Movement Script
