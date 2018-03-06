CSS Notes
=========

10.27
-----
+ css: cascading style sheets
    + a style sheet language used for describing look and 
        formatting of a document in a markup language
    + control how web pages look without changing html
+ style element
    + put <style> ---- </style> in <head>s content
    + <style> 
        h1, h2 (name of element tag in html){
            backgroud-color: purple; (please noting colon and semicolon)
            border_bottom: 1px solid black;
        }
        p  {
            color: red;
            font-size: 25px;
            font-family: Helvetica;
            border: 1px solid black;
        }
      </style>
+ inheritance and overide
    + child element will inherit the style of parent element
    + unless it is overrided
+ style for certain elements
    + class="classname"
        + e.g. <p class="blue"> --</p>
        + <style> p.blue {color:blue;} </style>
        + e.ge. <h1 class="blue underline"> -- </p>
        + <style> .blue {color:blue;} </style>
        + note
            + an element can belong to several class
            + ".classname" apply to all elements of this class 
                regardless of their tags
            + "tagname.classname" could be specified to a 
                certain element type of a class
+ type of style sheet
    + internal style sheet
    + external style sheet
        + <head> 
            <link rel="stylesheet" type="text/css" href="filename.css">
          </head>
    + inline
        + <p style="color:red; font-size:25px;"> -- </p>
        + generally we do not use inline sheet, 
            but if we are not going to change it anymore (which is 
            usually not the case), it is okay to use inline style.
+ property
    + font-family
        + could list several fonts, then the browser will try
            to apply these fonts in order, if the previous one
            is not installed.
    + font-weight
        + lighter, normal, bold, bolder
    + text-decoration
        + underline, line-through, overline
    + font-style
        + italic
        + html italic is usually for some words, not the whole elements
    + background
        + backgroud-color
            + specify the color name: pink
            + rgb form: rgb(255,0,255)
            + hexcode: #fcf79
        + backgroud-imgae: url(picname.gif);
    + font-size
        + 25px
        + 150% or 1.5em: relative to the parent font size
            + very nice, avoiding changing every font size 
                when making changes
        + keywords: xx-small, x-small, small, medium, 
            large, x-large, xx-large
    + line-height
        + 25px; 150%; 1.5em
    + text-align
        + center, left, right
    + overflow
        + overflow: scroll(hidden);
        + when we set a height for an element
+ css box model
    + __every html element have 4 boxes around them:__
        __content, padding, border, margin__
    + padding: 20px
        + left, right, top, bottom
    + border: color, width, style
        + border.radius: 10px;
    + margin: the browser add some margins automatically
        + 20px
        + center the img: margin-left: auto; margin-right: auto;
        + margin-top, margin-bottom, margin-left, margin-right
            + could be set seperately or together
            + e.g. margin: 2px 3px 4px 5px
    + note
        + html place every element in a top-down order
        + backgroud-color only applies to content and padding
+ id attribute
    + a specific css style applies to a __specific__ element
    + in html: <p id="idname"> -- </p>
    + in css: #idname{ ---- }
        + "#" tag!
+ some html elements
    + div
        + divides web page into logical sections
        + includes several elements
        + div tag do not do anything by themselves, they just
            identify a particular section
        + id="divname"
        + in css: #divname{ --- }
    + span
        + like div
        + works inside an element
        + <span id="--"> -- </span>
        + or inline style
            + <span style="--"> -- <span>
+ special effects of link
    + a:link{ color:blue; }
    + a:visited{ color:#8c8c9D; }
    + a:hover {color: #F15A51; }
    + note:
        + why we seperate them is because they do not show at the same time
        + the order of these 3 states should be changed
            + ? __I do not understand this senctence now...__
        + pseudo class
            + we do not need to declare it in html, but they 
                are treated as a class
            + colon ":" means we are treating a pseudo class
+ how to position element
    + block element
        + span from left to right of browser if 'width' is not set
        + <h#> <p> <div>
    + inline element
        + side by side
        + <span> <img --> <a>
            + img has 'margin' on 4 sides
            + span has 'margin' only on left and right
        + convert an inline element into a block element
            + add attribute "display: block;"
    + float an element
        + float: left;
        + allow us to place block elements side by side
        + we need to give the element a __width__
        + if we float an element, it is no longer part of 
            the flow of the system
    + absolute position of an element
        + absolute position in the web page
        + position by first non-static element it touches in the 
            specificed direction
        + position: absolute;
        + top, left, height, width
        + absolute position is absolutely outside the flow of the system
    + fixed position
        + position: fixed
        + does not move when scrolling, e.g. advertisment in some web pages
    + relative position
        + relative to
            + first static elements it touches in the specified direction;
                relative to the static elements around it
        + usually we do not use it, except in the following cases
            + as a support when using absolute position
    + static position
        + default
        + everthing is in the flow
            + block elements are top-down 
            + inline elements are inline
+ commment for css
    + double back slash "//"
    + /* --- */
+ modification of list of menu
    + ul{
        list-style:none;
        padding: 0;
        margin: 0;
        }
    + ul li a{
        text-decoration: none;
        font-family: Geogia, "Times New Roman";
        background-color: #5x755e;
        color: white; 
        display: block;
        margin: 5px;
        padding: 10 px;
        }
+ form element
    + action attribute; method attribute;
    + an input element is an inline element
    + form{d isplay: table;}
    + .row{ display:table-row; }
    + .row lable{ display:table-cell; }
    + .row input{ display:table-cell; }
+ selector
    + select by type: h1
    + select by id: #para1
    + select by class: .para
    + select by combining selectors
        + h2, h3, #para1 { -- }
            + using comma
    + select by descendent selector
        + select element within another element
        + div p { -- }
    + select by child selector
        + select direct child by ">"
        + .test>b { -- }
    + sibling selector
        + adjacent sibling 
            + h2+p: select 'p' element right after 'h2'
        + general sibling
            + h2~o: select 'p' element after 'h2'
    + attribute selector
        + p[lang] { color: red;}
        + p[lang="fr"] { color: red;}
        + p[lang^="fr"] { color: red;}
            + begining with 'fr'
        + p[lang$="o"] { color: red;}
            + ending with 'o'
         + p[lang$="o"] { color: red;}
            + ending with 'o'
          + p[lang*="us"] { color: red;}
            + having 'us'
    + pseudo selector
        + for pattern select
        + need a colon ":" sign
        + p:nth-child(condition) { --- }
            + condition can be
                + even, odd, 3, 3n, 3n+4
    + not selector
        + belong to pseudo selector, so ':' is needed
        + :not(p) { -- }
            + 'p' in '()' must be a selctor in css file
    + first selector
        + p::first-letter { -- }
            + double colon is needed.
        + p:first-line { -- }
+ NOTE
    + if there is differnet rules for same attributes,
        the last rule will be applied.
    + latest version: CSS 3

10.30
-----
+ properties
    + opacity: 0.4
        + means transparency
        + could use "#box:hover" to change opacity
    + gradient
        + backgroud: blue;
            + in case browser do not support gradient
        + backgroud: linear-gradient(blue, yellow);
            + default gradient direction is top-down order
            + backgroud: linear-gradient(to right, blue, yellow);
            + backgroud: linear-gradient(to top right, blue, yellow);
            + backgroud: linear-gradient(30deg, blue, yellow);
            + backgroud: linear-gradient(green, blue, yellow);
            + backgroud: linear-gradient(blue, yellow 20%);
                + after cross 20% line, it becomes totally yellow
            + backgroud: linear-gradient(rgba(,,,), rgba(,,,));
                + a means 'opacity'
    + text-shadow: 3px 3px orange;
        + 1st value: horizontal shadow
        + 2nd value: vertical shadow
    + box-shadow

### Layout
+ the browser construct the web page based on the order in the 
    html file
+ how to make css file tidy?
    + using comment: /* === LAYOUT SECTION === */
+ difference between flexible and fixed layout
    + fixed layout does not span the whole browser window
        + need to calculate the width very accurately
