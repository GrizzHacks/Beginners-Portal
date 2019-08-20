# Info Page
>Use this tutorial to learn how to use HTML and CSS    
>[See the Original Guidelines](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects/build-a-tribute-page)

We're going to create a webpage telling visitors all about our favorite superhero. This tutorial is perfect for getting started with website development.

## Set-Up

1) I recommend using Google Chrome for devloping and troubleshooting web elements. Feel free to download Google Chrome before starting this tutorial and setting it as your default browser.
> -- NOTE -- An unfortunate fact of web design is that not all web browsers are created equal. While most things will work across different browsers, there may be specific syntax you have to use in order get things to work on Safari, Firefox, etc... 

2) Hyper Text Markup Language (HTML) and Cascading Style Sheets (CSS) are easy to work with and involve little advanced set-up. 

    1) Open a new file in your text editor. Save it to a location where you can find it later by clicking 'File -> Save,' renaming the file as 'index.html', and changing the save location to the file where your Github Repository is located, or your Desktop, or etc... 
    2) Repeat this process with a second file, but save it as 'style.css'.

3) If you are using Visual Studio Code, go to the "Extensions" menu along the left-hand side of the text editor and search for "Live Server" in the Marketplace. Download and install it for later use.

## Coding Our Webpage

Our goal is to tell a visitor to our site all about our favorite superhero. For this tutorial, I'm going to be using She-Ra, but feel free to use whoever you want. 

### Let's consider the basic outline of what we want our page to have, as well as what we want our code to look like.

We can use small snippets of text called 'User Stories' to tell programmers what we want a site to do/have on it, or how we want to identify certain features. 
>For this project, we'll have 8 user stories, some of which come from the reference source.

#### User Stories
- User Story 1: The HTML code should have an element with the corresponding `id="main"` and which contains all other elements. 
>Don't worry if you don't understand what that means. We'll learn about elements and ids later on
- User Story 2: The HTML code should have an element with the corresponding `id="title"`. This should display our superhero's name at the top of the webpage.
- User Story 3: The HTML code should have a section that will hold an image under the `id="img-div"`.
- User Story 4: The HTML code should have an img tag with `id="image"`. This will show an image of our superhero underneath their name.
- User Story 5: We want to describe our image with an element that has `id="img-caption"`.
- User Story 6: We want to give our reader some information about the superhero using an element with `id="tribute-info"`.
- User Story 7: The page shouldn't be too long or large, so be sure to include a link to an auxilory site that gives more superhero information. Use the `id="tribute-link"`.
- User Story 8: Our page should include some kind of animated element that the user can interact with. Use the `id="flip-card"`.

Looks like a lot of info, right? The good thing is is that we don't have to tackle each of these stories all at once. In fact, they're made to be addressed one at a time. You can use this approach in other projects you may work on.

### Let's go to our index.html page and write some code.

Type the following at the top of index.html:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Superhero Info Page</title>
</head>

<body>
    <h1>Superheros Rule!</h1>
</body>
</html>
```

Copy the code exactly as shown in the grey box. Make sure to do the same whenever you see a grey box.

#### What We've Learned
- See those words inside of the angle brackets? Those are known as HTML elements, and the angle brackets denote an HTML tag. 
    - HTML tags usually come in pairs: the opening tag (`<element>`) and the closing tag (`</element>`)
- `<!DOCTYPE  html>` tells a web browswer that the it is looking at an HTML document
- `<html>` is the root element of an HTML page.
- `<head>` contains meta information about the webpage we'll see.
> -- NOTE -- Meta data won't be displayed on the webpage itself, but rather tells the web browser what the page is about, where to get styling information from, etc...
- `<title>` is the title of the document and is used for the page when it is added to favorites or in search-engine results. 
- `<body>` contains the content that a viewer can actually see
- `<h1>` defines one of six styles of heading, ranging from h1-h6. h1 is the largest.

Go ahead and navigate to where your index.html file is saved on your computer. Click on it, and it should open in your default browser. You should see "Superheros Rule!" in bold lettering across the top of your screen. Notice how our title text (Superhero Info Page) is displayed in the tab.
> This same task can be accomplished with the Live Server extension in VS Code. In the "Explorer" tab, where you see all of your open files, right click on index.html and click "Open with Live Server". You should see the same result.

### We're able to address User Story (US) #2 using what we know from above. 

Remember, US 2 tells us to display the name of our superhero at the top of the page. Underneath the opening `<body>` tag, make another `<h1></h1>` pair and write the name of your superhero between the two tags, just like you see with "Superheros Rule!".

Change the `<h1>` tags around "Superheros Rule" to say `<h2>`. Remember, both the opening and closing tag need to be changed, and the closing tag must contain a "/".

Now, in the opening tag (`<h1>`), write `id="title"` next to `h1`. Your code should look like this:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Superhero Info Page</title>
</head>

<body>
    <h1 id="title"> She-Ra: Princess of Power </h1>
    <h2>Superheros Rule!</h2>
</body>
</html>
```

If you'd like, make more content appear on your page by using `<hX> </hX>`, where X can be any value between 1 and 6.    
Check to make sure the name of your hero is now on the webpage. If not, make sure your code looks exactly like mine, save for the names 

#### What We've Learned
- `<h1>` represents a heading element. Each subsequent heading value represents the importance of a heading and is useful not just for styling purposes, but also for those who use assistive technologies. There is typically only one `<h1>` tag per page. 
> [Learn more about headings](https://www.w3schools.com/tags/tag_hn.asp)
- The text in between tags is the content displayed on the page. The tags themselves are used for assignment and styling purposes.
- `id=""` is used to identify a specific element. You may not use the same id for different elements. 
> For example, we could not put `id="title"` in the `<h2>` tag, as it represents a unique element.    
> [ids are used for CSS and Javascript purposes](https://www.w3schools.com/html/html_id.asp).

### Now that we know more about ids, let's address US #1.

Since our `<body>` tag contains all other elements on the page, let's add `id="main"`. Our opening `<body>` tag should now look like this:    
`<body id="main">`

#### What We've Learned
- `<body>` contains the visual page elements and surrounds all other page elements. 
> W3 Schools gives us a [great example](https://www.w3schools.com/html/html_intro.asp) of how to visualize the HTML page structure. Here you can see just what `<body>` does.

### Let's start to style our page by centering the name of our superhero

Let's open up style.css and type the following:

```CSS
#main {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;

}

#title {
    text-align: center;
    width: 100%;
    height: 50px;
}
```
In index.html, under `<head>`, write:    
`<link rel="stylesheet" href="style.css">`

Save both files, then open index.html in your web browser and ensure the name of your superhero is centered at the top of the page.
> If it is not, make sure your code looks like the example code. Otherwise, use Google and your friends to try and figure out what is going on. Make use of the browser-specific developer tools as well.    
> To use Chrome Developer Tools, you can right-click anywhere on the page and select "Inspect" or go to "View > Developer". Explore what you're seeing. 

#### What We've Learned
- Remember when we added the `id="name"` to our HTML tags? Here we see them finally at work! 
    - "#name" is an id selector, and styles the element with the specific id name. Because each HTML page should only have one specific id name, it is easy to identify just what on the page is changing.
- We style each id using the CSS properties that are inside of the curly braces ({}).
    - [`display: x`](https://www.w3schools.com/cssref/pr_class_display.asp): Specifies how an element renders. In this example we are using a flex container.
    > By specifying the display as flex, we are using the flexbox layout. [Read more about the Flexbox layout](https://internetingishard.com/html-and-css/flexbox/).
    - [`flex-direction: x`](https://www.w3schools.com/cssref/css3_pr_flex-direction.asp): Flex-direction is best used in the Flexbox layout, and specifies the direction of flexible items (in this case the `<h1>` and `<h2>` elements)
    - [`width: x`](https://www.w3schools.com/cssref/pr_dim_width.asp): Sets the width (length) of an element. 
    > By setting width equal to 100%, we ensure that the width of each element is as wide as the screen someone is working on.
    - [`height: x`](https://www.w3schools.com/cssref/pr_dim_height.asp): Sets the height on an element, but does not include padding, borders, or margins.
    > -- NOTE -- See how I use two different types of units for height? They each control the length of an element in slightly different ways. '%' is relative to the size of the screen, while `px` is absolute. [Read about CSS units](https://www.w3schools.com/cssref/css_units.asp)
    > width and height play into the [CSS Box Model](https://www.w3schools.com/css/css_boxmodel.asp).    
    > Read about the box model above to understand padding, border, and margin. 
    - [`text-align: x`](https://www.w3schools.com/cssref/pr_text_text-align.asp): Specifies the horizontal placement of text in an element. 
    > -- NOTE -- Text (i.e. "Superheros Rule") is NOT equivalent to element. While CSS controls an element (i.e. h1 or h2), we use CSS attributes to control objects like text, images, etc...
- `<link>` is an example of a meta element. It tells the HTML page where to find the styling information for the webpage. [Read about `<link>` and its attributes](https://www.w3schools.com/tags/tag_link.asp)
> -- NOTE -- `href=x` points to the location on your computer where style.css is located. If you find you are unable to style your webpage, make sure this attribute is pointing to the correct location on your computer. You can move up a "level" from where index.html is located by typing "../".

There a ton of attributes we can apply to `main` and `title`. [This website](https://www.w3schools.com/cssref/default.asp) gives you a complete list of all the CSS properties we can apply to our id selectors. 

We will continue to utilize the [CSS Box Model](https://www.w3schools.com/css/css_boxmodel.asp) and [Flexbox layout](https://internetingishard.com/html-and-css/flexbox/) to style our info page. If you haven't already, please acquaint yourself with these items.

### Let's get back on track and tackle US #3 







<!-- Project Title

Summary
Citations
Include a brief one or two sentence summary of what the project is/does/accomplishes.

Set-Up

Include any languages people may need to install and how to install them.

Include any packages that people will use, as well as a short summary of what they do

Explain how a person may need to download/install a package
Coding Our ___

Include step-by-step instructions on what a programmer should type.

If necessary, discuss some of the planning steps that programmers may need to go through.
Include a 'What We've Learned' section to discuss new information, or clarify code that may be difficult to understand.

Break the code process up into different sections

Running the __

Include how to run the program.

Difficulties

Explain any difficulties that may appear when you run the program.

Next Steps

Describe improvements people could make on the existing code. Give ideas on what they can do with their new-found knowledge.

Don't tell people exactly what to do, give them ideas. This is the final section people should see

If you feel it's necessary, include the following in a footer at the bottom of the page:

This code comes from the source listed at the top of the page. No commercial gain is sought from using the code, and is instead intended for educational purposes. -->

---

<!-- User Story #1: My tribute page should have an element with a corresponding id="main", which contains all other elements.
User Story #2: I should see an element with a corresponding id="title", which contains a string (i.e. text) that describes the subject of the tribute page (e.g. "Dr. Norman Borlaug").
User Story #3: I should see a div element with a corresponding id="img-div".
User Story #4: Within the img-div element, I should see an img element with a corresponding id="image".
User Story #5: Within the img-div element, I should see an element with a corresponding id="img-caption" that contains textual content describing the image shown in img-div.
User Story #6: I should see an element with a corresponding id="tribute-info", which contains textual content describing the subject of the tribute page.
User Story #7: I should see an a element with a corresponding id="tribute-link", which links to an outside site that contains additional information about the subject of the tribute page. HINT: You must give your element an attribute of target and set it to _blank in order for your link to open in a new tab (i.e. target="_blank").
User Story #8: The img element should responsively resize, relative to the width of its parent element, without exceeding its original size.
User Story #9: The img element should be centered within its parent element. -->
