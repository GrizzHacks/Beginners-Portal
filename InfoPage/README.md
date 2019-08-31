# Info Page
>Use this tutorial to learn how to use HTML and CSS    
>[See the Original Guidelines](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects/build-a-tribute-page)

We're going to create a webpage telling visitors all about our favorite superhero. This tutorial is perfect for getting started with website design.

## Set-Up

1) I recommend using Google Chrome for developing and troubleshooting web elements. Feel free to download Google Chrome before starting this tutorial and setting it as your default browser.
> An unfortunate fact of web design is that not all web browsers are created equal. While most things will work across different browsers, there may be specific syntax you have to use in order get things to work on Safari, Firefox, etc... 

2) Hyper Text Markup Language (HTML) and Cascading Style Sheets (CSS) are easy to work with and involve little advanced set-up. 

    1) Open a new file in your text editor. Save it to a location where you can find it later by clicking 'File -> Save,' renaming the file as 'index.html', and changing the save location to the where it can be added to either your Github Repository, Desktop, etc... 
    2) Repeat this process with a second file, but save it as 'style.css'.

3) If you are using Visual Studio Code, go to the "Extensions" menu along the left-hand side of the text editor and search for "Live Server" in the Marketplace. Download and install it for later use. 
> Confused? [Click this link to find it directly.](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## Coding Our Webpage

Our goal is to show and tell an internet user all about our favorite superhero. For this tutorial, I am going to be using She-Ra, but feel free to use whomever you want.

### Let's consider the basic outline of what we want our page to have, as well as what we want our code to look like.

We can use small snippets of text called User Stories to tell programmers what we want a site to do/have on it, or how we want to identify certain features.    
For this project, we'll have 8 user stories, some of which come from the reference source.

#### User Stories
- User Story 1: The HTML code should have an element with corresponding `id="main"` and contain all other elements. 
- User Story 2: The HTML code should have an element with corresponding `id="title"`. This should display our superhero's name at the top of the webpage.
- User Story 3: The HTML code should have a section that will hold an image with `id="img-div"`.
- User Story 4: The HTML code should have an img tag with `id="image"`. This will show an image of our superhero underneath their name.
- User Story 5: We want to describe our image with an element that has `id="img-caption"`.
- User Story 6: We want to give our reader some information about the superhero using an element with `id="tribute-info"`.
- User Story 7: The page should not be too long or large, so be sure to include a link to an auxiliary site that gives more information on your superhero. Use the `id="tribute-link"`.
- User Story 8: Our page should include some kind of animated element that the user can interact with. Use`id="flip-card"`.

Looks like a lot of info, right? The good thing is that we do not have to tackle each of these stories all at once. In fact, they are made to be addressed one at a time. You can use this approach in any other projects you may work on.

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
- [`<!DOCTYPE  html>`](https://www.w3schools.com/tags/tag_doctype.asp): Tells a web browswer that it is looking at an HTML document
- [`<html>`](https://www.w3schools.com/tags/tag_html.asp): Exists as the root element of an HTML page.
- [`<head>`](https://www.w3schools.com/tags/tag_head.asp): Contains meta information about the webpage we will see.
> Metadata will not be displayed on the webpage itself, but rather tells the web browser what the page is about, where to get styling information from, etc...
- [`<title>`](https://www.w3schools.com/tags/tag_title.asp): Defines the title of the document and is used for the page when it is added to "Favorites" or in search-engine results. 
- [`<body>`](https://www.w3schools.com/tags/tag_body.asp): Contains the content that a viewer can actually see
- [`<h1>`](https://www.w3schools.com/tags/tag_hn.asp): Defines one of six styles of heading, ranging from h1-h6. h1 is the largest.

Go ahead and navigate to where your index.html file is saved on your computer. Click on it, and it should open in your default browser. You should see "Superheros Rule!" in bold lettering across the top of your screen. Notice how our title text ("Superhero Info Page") is displayed in the tab.
> This same task can be accomplished with the Live Server extension in VS Code. In the "Explorer" tab, where you see all of your open files, right click on index.html and click "Open with Live Server". You should see the same result.

### We are able to address User Story (US) #2 using what we know from above. 

Remember, US 2 tells us to display the name of our superhero at the top of the page. Underneath the opening `<body>` tag, make another `<h1></h1>` pair and write the name of your superhero between the two tags, just like you see with "Superheros Rule!".

Change the `<h1>` tags around "Superheros Rule!" to say `<h2>`. Remember, both the opening and closing tag need to be changed, and the closing tag must contain a "/".

Now, in the opening h1 tag (`<h1>`), write `id="title"` next to `h1`. Your code should look like this:

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

If you wouldd like, make more content appear on your page by using `<hX> </hX>`, where X can be any value between 1 and 6.    
Check to make sure the name of your hero is now on the webpage. If not, make sure your code looks exactly like mine, save for the names 

#### What We've Learned
- [`<h2>`](https://www.tutorialrepublic.com/html-tutorial/html-headings.php): Represents a heading element. Each heading value represents the importance of a heading and is useful not just for styling purposes, but also for those who use assistive technologies. There is typically only one `<h1>` tag per page. 
- The text in-between tags is the content displayed on the page. The tags themselves are used for assignment and styling purposes.
- [`id=""`](https://www.w3schools.com/html/html_id.asp): Used to identify a specific element. You may not use the same id for different elements, nor may we use the id for multiple of the same element.
> For example: we could not put `id="title"` in the `<h2>` tag, as it represents a unique element. 

### Now that we know more about ids, let us address US #1.

Since our `<body>` tag contains all other elements on the page, let us add `id="main"`. Our opening `<body>` tag should now look like this:    
`<body id="main">`

#### What We've Learned
- W3 Schools gives us a [great example](https://www.w3schools.com/html/html_intro.asp) of how to visualize the HTML page structure. Here you can see just what `<body>` does.

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
    height: fit-content;
    box-sizing: border-box;
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
    > See how I use two different types of units for height? They each control the length of an element in slightly different ways. '%' is relative to the size of the screen, while `px` is absolute.    
    [Read about CSS units.](https://www.w3schools.com/cssref/css_units.asp)    
    > Width and height play into the [CSS Box Model](https://www.w3schools.com/css/css_boxmodel.asp). Read about the box model to understand padding, border, and margin. 
    - [`text-align: x`](https://www.w3schools.com/cssref/pr_text_text-align.asp): Specifies the horizontal placement of text in an element. 
    > Text (i.e. "Superheros Rule!") is NOT equivalent to an element. While CSS controls an element (i.e. h1 or h2), we use CSS properties to control objects like text, images, etc...
    - ['box-sizing: x'](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing): Determines how the width and height are calculated.
    > Typically CSS does not consider padding, border, and margin values to be included in width and height measurements. By specifying box-sizing as `border-box`, we are able to including the padding and border measurements into the entire value of the width and height.
- [`<link>`](https://www.w3schools.com/tags/tag_link.asp): A meta element. It tells the HTML page where to find the styling information for the webpage.
> `href=x` points to the location on your computer where style.css is located. If you find you are unable to style your webpage, make sure this attribute is pointing to the correct location on your computer. You can move up a "level" from where index.html is located by typing the following: ../

There a ton of properties we can apply to `main` and `title`. [This website](https://www.w3schools.com/cssref/default.asp) gives you a complete list of all the CSS properties we can apply to our id selectors. 

We will continue to utilize the [CSS Box Model](https://www.w3schools.com/css/css_boxmodel.asp) and [Flexbox layout](https://internetingishard.com/html-and-css/flexbox/) to style our info page. If you haven't already, please acquaint yourself with these items.

### Let's get back on track and tackle US #3 

We'll be using the `<figure>` tag to define a section that will hold an image. [Go ahead and read about `<figure`>](https://www.w3schools.com/tags/tag_figure.asp). Try to include it into the HTML document with the id "img-div" (don't worry about adding the `<img>` tag just yet).

Your code should now have the following section underneath the `<h1>` and `<h2>` tags:

```HTML
<figure id="img-div">
</figure>
```

#### What We've Learned
- [`<figure>`](https://www.w3schools.com/tags/tag_figure.asp): Used to denote self-contained content; aka content that is not dependent upon the main "flow" of the webpage.[This website gives a good explaination under "Usage Notes".](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) 
    - `<figure>` typically contains visual imagery of some sort.
> The flow of a webpage is how developers talk about how different elements interact with one another. If we were to move our `<figure>` element to another point on the HTML document - say, above `<h1>` and `<h2>` - we would not affect how the elements interact with one another and with the rest of the webpage.    
> [Reading about semantic HTML](https://www.lifewire.com/why-use-semantic-html-3468271) and [HTML sections](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines#Sectioning_roots) may aid in understanding.

### With that done, let's handle US #4 and #5

Within the `<figure>` tags, let's add `<img>` with id "image" and `<figcaption></figcaption>` with id "img-caption". 

You should now see

```HTML
<figure id="img-div">
    <img id="image"/>
    <figcaption id="img-caption"></figcaption>
</figure>
```

If we look at our HTML page in a web browser, we don't see an image or any description. Why? 

[Look at this documentation](https://www.w3schools.com/tags/tag_figcaption.asp) and compare it to our code. What are we missing? Based on what you know, try to add an image of your superhero and a caption to the webpage. 

------

Figure it out? If not, that's okay! You're learning something brand new. 

My code now looks like this:

```HTML
<figure id="img-div">
    <img id="image" src="shera.jpeg" alt="She-Ra stands strong"/>
    <figcaption id="img-caption">She-Ra (center) stands alongside her friends and allies</figcaption>
</figure>
```

#### What We've Learned
-  [`<img/>`](https://www.w3schools.com/tags/tag_img.asp): This tag is unique in that we do not require a traditional closing tag. We do, however, require two attributes: "src" and "alt".
    - The backslash is not technically required, but it does encourage proper syntax. We could have just as easily have written our tag as `<img id="image" src="shera.jpeg" alt="She-Ra stands strong">`
    - "src" specifies where to find an image (its URL). I saved my image to where I stored my HTML and CSS documents, but I could have also used its URL on Google Images.
    - "alt" is displayed when the webpage is unable to find or render an image. For users who use screen readers, this is used to describe what the image shows (since `<figcaption>` is not always used).
    > `<img>` CANNOT have the traditional closing tag (i.e. `</img>`). A quick Google search can explain why this is if you are interested.
- [`<figcaption>`](https://www.w3schools.com/tags/tag_figcaption.asp): Gives our image a caption to describe what a user sees.

Take a look at your webpage. You should now see an image of your superhero, as well as a caption describing the image. 

### Go ahead and try to style these new elements using what you have discovered. 

I'll explain what I've done:

```CSS
#img-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 25%;
    margin: 20px 0px;
}

#image {
    max-width: 100%;
    max-height: 500px; 
}

#img-caption {
    font: bold 20px sans-serif;
    color: #1C7C54;
}
```
#### What We've Learned
We've seen some of these items before, but others are brand new.
- [`justify-content`](https://www.w3schools.com/cssref/css3_pr_justify-content.asp): Determines the position of items within the flexbox (in this case our `figure`) along the horizontal line.
- [`align-items`](https://www.w3schools.com/cssref/css3_pr_align-items.asp): Decides the position of items along the vertical axis.
> Both of the above properties tie into the [flexbox layout](https://internetingishard.com/html-and-css/flexbox/) I mentioned earlier. 
- [`margin: x`](https://www.w3schools.com/cssref/pr_margin.asp): The attribute for setting up the spacing that surrounds an object on the page. It is actually shorthand for four individual properties, which you can read about in the reference article. 
> By writing `margin: 20px 0px`, I tell the webpage to render my item with a top and bottom margin of 20px, and a right and left margin of 10px. 
> There are multiple ways to use the `margin` attribute as a shortcut for specifying item spacing. [This website provides additional information about the number of values you can apply to `margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin).
- [`max-width: x`](https://www.w3schools.com/cssref/pr_dim_max-width.asp): Sets the maximum width of an element.
- [`max-height: x`](https://www.w3schools.com/cssref/pr_dim_max-height.asp): Sets the maximum height of an element.
- [`font: x`](https://www.w3schools.com/cssref/pr_font_font.asp): Font is another property that serves as a shortcut for five indivual properties. 
> You are able to specify as many or as few of the properties as you want. In my example, I am defining the [`font-weight`](https://www.w3schools.com/cssref/pr_font_weight.asp), [`font-size`](https://www.w3schools.com/cssref/pr_font_font-size.asp), and [`font-family`](https://www.w3schools.com/cssref/pr_font_font-family.asp) properties.
- [`color: x`](https://www.w3schools.com/cssref/pr_text_color.asp): This attribute sets the text-color of an element.
> `color` can be defined via HEX, RGB, RGBA, HSL, HSLA, or an internal color palette. 

### Not too much more to go! Let's do US #6

It's important that visitors to our website know who our superhero is! Let's write about who and what our superhero has done using the `<p>` and `<ul>` tags.

Under our closing `<figure>` tag (`</figure>`), let's write the following:

```HTML
<div id="tribute-info">
    <p id="tribute-paragraph">
        XXX
    </p>
    <ul id="tribute-list">
        <li class="tribute-item">X</li>
        <li class="tribute-item">X</li>
        <li class="tribute-item">X</li>
    </ul>
    <p>
        XXX
    </p>
</div>
```
Where you see X's, type in some information about your superhero. Once you've finished, launch your page on a web browser and see what the result is.

#### What We've Learned
- [`<div>`](https://www.w3schools.com/tags/tag_div.asp): This tag defines a division or section of an HTML page. We typically wrap this around other HTML elements in order them to style on the page.
- [`<p>`](https://www.w3schools.com/tags/tag_p.asp): The `<p>` tag defines a paragraph. It is able to display any amount of text.
- [`<ul>`](https://www.w3schools.com/tags/tag_ul.asp): This tag represents an unordered list. It must be used with `<li>` tags in order to display items as bullet points.
> If you want a list of items that is ordered, use the [`<ol>`](https://www.w3schools.com/tags/tag_ol.asp) tag.
- [`<li>`](https://www.w3schools.com/tags/tag_li.asp): Use the `<li>` tag to define a list item. These are the elements that actually render items onto an ordered or unordered list. 
> You may include as many or as few `<li>` tags as you wish
- [`class=""`](https://www.w3schools.com/html/html_classes.asp): Used among multiple elements to assign the same style to each element. In the case of our `<li>` tags, we want to make sure that each `li` element is styled the same way. 

Go ahead and style these elements using CSS. In order to style the elements defined by a class, you'll need to write `.classname {}` in the CSS sheet.

### We're moving on to US #7 and #8

If you're interested in how I styled my paragraph and list elements, check out the [style.css page](https://github.com/GrizzHacks/Beginners-Portal/blob/master/InfoPage/style.css) attached to this tutorial. The only new attribute used is [list-style-type](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type).

We're going to place our link to an auxiliary page in a flip-card! This is a bit more complicated, but I'll take things slow. 

First, write the following under your final `</p>` tag:

```HTML
 <div id="flip-card">
    <a id="tribute-link" href="YY">
        <h1 id="flip-card-front">XX</h1>
        <h1 id="flip-card-back">XX</h1>
    </a>
</div>
```
Write what you would want to see on the front of a flip-card between the `<h1>` tags (where the X's are) with id "flip-card-front". 

Do the same thing for the back of the card between the `<h1>` tags with id "flip-card-back".

Go ahead and launch your page on the web browser. Notice something weird about our front and back text? Go ahead and click on the text. 

#### What We've Learned
- What you're seeing is the results of the `<a>` tag, known as the [anchor tag](https://www.w3schools.com/tags/tag_a.asp). The anchor tag defines a hyperlink, aka a link from one webpage to another. In order to link to another webpage, you need to put the destination web address where you see the Y's in `href="YY"`. If you look at my HTML code, you'll see that I linked to She-Ra's Wikipedia page.
> Notice something else in my code? I've included `target="_blank"`. When you clicked on the front and back text, did you see how you were sent to the top of your webpage (if the webpage was large enough), or to your destination webpage in the same tab? By including the attribute `target="_blank"`, I'm able to view to my destination webpage in a new tab. 

### Nothing is animated yet. Let's change that by moving to CSS.

Write out the declaration blocks for each id in style.css as follows:

``` CSS
#flip-card {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 200px;
    perspective: 1020px;
}

#tribute-link {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    width: 50%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s;
    transform-style: preserve-3d;
}

#flip-card-front, #flip-card-back {
    position: absolute;
    backface-visibility: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    margin: 0;
}

#flip-card-back {
    transform: rotateX(180deg);
}

#flip-card:hover #tribute-link {
    transform: rotateX(180deg);
}
```

That's a lot, and probably pretty confusing, right? Let's break it down block by block.

#### What We've Learned
- "flip-card" is our overarching container, and is mainly used for styling purposes.
> Consider `perspective: x;` for a minute. It is used to determine how an object looks in 3d space. [MDN gives a great explaination and uses imagery to explain this concept](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective).    
- "tribute-link" is an anchor tag. We can use this to style our text, but also ensure that by clicking anywhere on the flip-card, we are sent to the external website. 
> If we wanted text alone to link to an external site, we could place an anchor tag around our various text elements.    
    For example, I've added anchor tags around the elements in my unsorted list. It now looks like this:

```HTML
    <ul id="tribute-list">
        <li class="tribute-item"><a href="https://en.wikipedia.org/wiki/Swift_Wind" target="_blank">Swift Wind, a talking unicorn</a></li>
        <li class="tribute-item"><a href="https://he-man.fandom.com/wiki/Glimmer_(She-Ra_and_the_Princesses_of_Power)" target="_blank">Princess Gimmer, commander of the Great Rebellion</a></li>
        <li class="tribute-item"><a href="https://he-man.fandom.com/wiki/Bow_(She-Ra_and_the_Princesses_of_Power)" target="_blank">Bow, a master archer</a></li>
    </ul>
```
> I've also chosen to style my tags using an element selector, shown here:
```CSS
a {
    color: inherit;
    text-decoration: none;
}
```
- [`transition: x`](https://www.w3schools.com/css/css3_transitions.asp): The first attribute we see that allows us to change another attribute over a fixed period of time. 
> By specifying `transform 0.8s`, we say "perform a 3D transformation over the course of 0.8s".
- [`transform-style: x`](https://www.w3schools.com/cssref/css3_pr_transform-style.asp): This attribute specifies how nested elements (in this case the h1 elements) are rendered in 3D space. Check out the associated link for a demo.
> transform-style MUST be used with the transform property.
- [`position: x`](https://www.w3schools.com/cssref/pr_class_position.asp): This attribute is a bit complex. Position doesn't position things in the terms of left or right, but rather in terms of page flow. [This website gives an auxiliary explaination](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
- What does it mean when we see two id selectors seperate by a comma? By doing this, we are able to apply all properties within the block to elements possessing either id (i.e. the properties are shared among both ids).
> Later on, you'll see two ids not seperated by a comma. This means that the second id will only be styled by the properties when it is nested under the first id.(If you hover over the text `#flip-card:hover #tribute-link`, you'll see what I mean).
- [`backface-visibility:x`](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility): This property is applicable when an element is rotated in 3D space. What we consider to be the back of the flip-card can be either hidden or visible, depending on what the attribute is set to.
- [`transform: x`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform): Setting this property a certain way allows us to rotate, scale, skew, or translate an element. 
> In our version, we tell the webpage to rotate our element around the X-axis 180 degrees.
- See where we write `#flip-card:hover`? `:hover` is known as a selector, and makes sure that certain properties are only triggered when an element is moused over. [There are a number of other selectors, detailed here.](https://www.w3schools.com/cssref/css_selectors.asp)


It's a bit hard to see this as a flip-card, so do your best and style your flip card. If you get stuck, or want to see how I did it, look at my style.css file.

## That's it! Go ahead and look at what your efforts have wrought. Wonderful job!

## Next steps

What's next? Quite a bit! Here are some ideas to get you started:
- Create a new webpage in the same project for another superhero, and link to it from your first webpage
- Make sure your webpage works on a variety of web browsers and see how to design for multi-browser support.
- Try integrating Javascript into your webpage. 
- Turn this static webpage into a dynamic one. Check out programs like Django or Ruby on Rails to help you with this.
- Come up with an idea for another project? Use this tutorial to create a promotions page.

# Good luck Hackers!    

----

##### No commercial gain is sought from using the code, and is instead intended for educational purposes.
