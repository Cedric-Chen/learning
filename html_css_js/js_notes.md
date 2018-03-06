JavaScript Notes
================

11.1
----
+ javascript adds programming to our web pages; 
    making our web sites interactive.
+ how js different from other programming language
    + we do not need to compile our code
    + the browser execute it
+ <script> tag in <head>
    + <head>
        <script>
            document.write("Hello World!");
        </script>
      </head>
        + this output "Hello World!" in the html page
        + ";" at the end of statement
    + <head>
        <script src="jsname.js"> </script>
      </head>
+ Actually, it is not recommended to put script tag
    inside element tag.
    + it is recommended to put script tag right before
        the end of body element.
    + because js file works on the DOM, and DOM does
        not exist until we load whole html and css files.

+ js basics
    + declare a variable
        + var varname; var varname2 = 1;
        + no need to specify the type: loosely typed language
            + c++, java are strongly typed language
        + varaible type
            + numerical, string, boolean
            + array: var arrayname = [1, 2, 3]
                + arrayname[0], arrayname[1]
            + object: var objname = {
                            a: 1,
                            b: 2
                            c: function(){---}
                        }
                + delete properties: delete a;
        + we even can omit "var" keyword, but this is strongly not 
            recommended
    + declare a function
        + function fnname(paraname1, paraname2) {
            some statements;
            }
        + return result;
        + __local and global variables for a function__
            + if 'var' keyword is not used for declaring a variable,
                the variable has the possibility to be a global 
                variable.
            + this also tells me that add 'var' when decalring new
                variables; thus I can tell apart local variables
                and global variables
            + local variables is done when the function is done
    + operators
        + shorthand
            + num += 1;
            + num++;
    + condition
        + if(condition) {
            some statements;
            }
          else if(condition) {
            some statements;
            }
          else{
            some statements;
            }
    + loop
        + while(condition){
            some statements;
            }
        + for(var i=1; i<5; i++) {
            some statements;
            }
    + global objects
        + string
            + toUpperCase(), toLowerCase()
            + length()
            + replace('--'.'--')
        + Date object
            + var todayDate = new Date()
                + keyword 'new' give us a copy of the object
            + toDateString()
        + class
            + function classname(para1, para2) {
                this.attr1 = para1;
                this.attr2 = para2;
                }
            + var varname = new classname(para1, para2);
    + useful debug functions
        + alert( something );
        + document.write( something );
            + write to html page
        + comment
            + /* some things */
            + // some things
        + confirm("something");

+ DOM - document object model
    + Dom allows us to use our js code to access 
        parts of the web page
    + nodes: how we reference html in our js codes
        + element node
        + attribte node: id, class
        + text node
    + select
        + document.getElementById("para").style.color = "blue";
        + document.getElementByTagName("p")
            + return a node list; thus we may access
                entries by index
        + document.getElementByClassName("p")
            + return a node list
    + change
        + css styles
            + document.getElementById("para").style.color = "blue";
        + change text, images
            + var paragraph = document.getElementById("para");
            + var changeText = paragraph.innerHTML = "new text";
            + content is a property of the object
                + "innerHTML" attribute
        + validation
            + document.getElementById("images").src = "some.jpg";
            + "src" attribute
        + create new elements
            + var element = document.createElement("p");
              var main = document.getElementById("main");
              main.appendChild(element);
              var text = document.createTextNode("some texts");
              element.appendChild(text);
        + remove elements
            + var element = document.getElementByTagName("h2")[2];
              var parent = element.parentNode;
              parent.removeChild(element);
        + create attribute
            + var attribute = document.createAttribute("id");
              attribute.value = "test";
              element.setAttributeNode(attribute); 
              //element is variable we created before.
    + event
        + pick the element we want to place our event;
            then choose the event we want to use
        + onclick
            + <button onclick="fnname()"> buttonname </button>
        + onmouseover
            + works on almost all html elements
            + the effects is permanant
        + onmouseout
            + clear the effects of "onmouseover"
    + traverse the DOM
        + parent.childNodes
        + parent.firstElementChild
        + child.parentNode
        + elem.nextElementSibling
        + elem.previousElementSibling
+ form validation
    + web side check; server side check is still needed
    + action = "someweb.html"
        + next step
    + method
        + post
    + onsubmit = "return validateTextbox()"
+ window object
    + window.location="index.html";
        + change url
        + not part of html, so cannot use 'document' object
    
+ restriction of js
    + do not display errors?
