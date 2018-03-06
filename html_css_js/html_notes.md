HTML Notes
==========

10.26
-----
+ html: hyper text markup language
    + document contains text
    + web browser can open html
+ component
    + <> : angle brackets contain tag
    + markup element
        + <body> ---- </body>
    + empty element: no infomation inside
        + <br> line break
+ browser can open many types of files, like html, xml
    + in order to tell browser this is a html file, we add
        "<!doctype html>" at the begin of the file.
        + could add version number, like <!doctype html 4.01>
        + if no version number, the latest version will be used
            + which is good, we don't need to change it now
        + Latest version is html5
+ some markup sign
    + <html> </html>
    + <head> </head>
        + <title> ---- </title>
        + language
        + metatags, javascripyt reference
    + <body> </body>
        + <h1> -- </h1>
            + name of section
            + style: bold, big font
            + <h2> -- </h2>
                + name of subsection
        + <p> -- </p>
            + create a paragraph
    + <br>
        + there is automatic line break after each tag
    + &nbsp;
        + add space
        + semicolon is important
    + comment
        + starts with "<!--", and ends with "--"
    + list
        + <ul> </ul> : unordered list
        + <ol> </ol> : ordered list
        + <li> </li> : list item for both ordered and unordered list
    + table
        + <table>
        + <tr>: row
        + <th>: name of column
        + <td>: data
    + link
        + outside url
            + <a href="https://www.youtube.com"> --- </a>
        + link within the same page
            + <a href="#name"> -- </a>
            + <a name="name"> -- </a>
    + image
        + image in the same directory
        + <img src='--/--/image.jpg>
            + this is an empty markup element
            + so no </img>
            + usually, jpg file for important pic; gif and png
                for low quality pic
        + resize: <img src="--/--/image.jpg" width="200" height="100">
            + the resize function is done when the browser open html file,
                this is a pain
    + form
        + The HTML <form> element defines a form that is used to 
            collect user input.
        + Form elements are different types of input elements, 
            like text fields, checkboxes, radio buttons, 
            submit buttons, and more.
        + <form action="--" method="--"> </form>
            + the form element by itself does not do anything
        + <input type="text" name="--">
            + no closing tag
            + size="50"
            + id="name"
        + label for input box
            + <label for="name"> NAME </label>
            + name needs to match id of input box
            + label will be shown in the same line of input box
            + one cool thing is that when click on the label text,
                the input box will be highlighted
        + multi-line text box
            + <textarea rows="30" cols="40"></textarea>
            + weird enogh, there is a closing tag
        + radio button
        + <input type="submit" value="name of this button">

10.27
-----
+ form
    + <input type="radio" name="name" value="">
        + value would be sent to the server
        + for 'radio' type having the same name, 
            only one choice for radio boxes 
    + <input type="checkbox" name="">
        + checked="checked"
            + predefined choice
    + <input type="number">
        + min="10" max="20"
    + <select>
        <option value="a"> a </option>
        <option value="b"> b </option>
      </select>
    + <input type="data">
    + <fieldset> </fieldset>
        + a nice box around the form
    + <legend> --- </legend>
        + the name for fieldset, looks very nice
+ attributes
    + give more information about an attribute
        + like <p class="name">, <lable for="name">
+ meta tag
    + inside <head> </head>
    + <meta name="description" content="-----" >
    + <meta http-equiv="author" content="Jonh">
    + "name" can be description, keywords
    + "http-equiv" can be author, content-language
+ style
    + bold element <b> </b>
    + strong element <strong> </strong>
        + visually looks the same like bold element
        + strong element have some special use, but not very useful now
    + italic element <i> </i>
    + em element <em> </em>
        + like strong version of italic element
    + super element <sup> </sup>
    + sub element <sub> </sub>
+ iframe element
    + <iframe frameborder="1" width="200" height="199"
        src="" name="---" id="--"></iframe>
    + no content inside <frame --> and </iframe>; 
        if there is, it will not be shown.
    + another use method: <a href="a.html" 
        target="id of iframe element above"> some text </a>
+ title attributes
    + almost for all html elemenets
    + for example, when put the cursor on one pic, the title will be shown
+ alt attributes
    + when an img is not shown for some reasons, the text will be 
        shown on the screen
    + <img src="11.jgp" title="aa" alt="bb">
+ audio element 
    <audio control autoplay loop> <source src="test1.mp3> </audio>
    + html5 provides easy way to include audios and videos
    + standard audio format is .mp3, .wav, .ogg
+ video element
    + <video width="--" height="--" controls> 
        <source src="--.mp4"> 
        <source src="--.ogg"> 
      </video>
    + we put several source inside, which are actually the same,
        to avoid missing files
+ draggable element
    + draggable="True"
    + apply to alomost every element
+ <!doctype html>
    + 'doctype' is not a html tag, but a instruction for the browser
