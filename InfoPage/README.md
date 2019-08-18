# Info Page
>Use this tutorial to learn how to use HTML and CSS    
>[See the Original Guidelines](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects/build-a-tribute-page)

We're going to create a webpage telling visitors all about our favorite superhero. This tutorial is perfect for getting started with website development.

## Set-Up

Hyper Text Markup Language (HTML) and Cascading Style Sheets (CSS) are easy to work with and involve little advanced set-up. 

1) Open a new file in your text editor. Save it to a location where you can find it later by clicking 'File -> Save,' renaming the file as 'index.html', and changing the save location to the file where your Github Repository is located, or your Desktop, or etc... 
2) Repeat this process with a second file, but save it as 'style.css'.


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
</head>
</html>
```





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
