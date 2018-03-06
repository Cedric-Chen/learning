Boodstrap Notes
===============

11.1
----
+ bootstrap
    + open source framework that allows me to build websites
        + what is framework: a lot tools
        + e.g. jQuery is framework of javascript
    + a framework for html, css, javascript
    + offer many components
        + label, button, navbar, etc.
    + a mobile-first framework
+ grid layout
    + advantages
        + provides structures for our web
        + bootstrap provides majorities of css to handle
            all different types of browsers and devices
        + easy to maintain
    + bootstrap - max # of column: 12
    + predefinde class
        + container
        + row
            + inside 'container'
        + col-md-2
            + indide 'row'
            + xs-phones; sm-tablets, md-desktops, lg-larger desktops 
            + '2' at the last furthre specifies the size; 
                could pick from 1 thorugh 12 
            + attribute
                + offset from left
                    + col-md-offset-5
                + hide in small screen
                    + visible-md visible-lg
                    + means visible in middle and large screen
                + push to right, pull to left
                    + col-md-push-3
                    + when push some column right, usually
                        we need to push other column left
                + hidden
                    + hide the element
                    + hidden-xs: only hide on extra small screen
    + custom class: we also need to define our own class
        + we usually do not define 'width', the bootstrap takes 
            care of that for us
        + we define "min-height", rether than "height", to 
            accomodate more situations
+ topography
    + bootstrap automatically select font and font-size for users
    + attribute
        + text-hide
        + lead
            + highlight some content
        + align
            + text-center
            + text-right
        + font-size
            + small
+ button
    + for 3 thml tag: <button> <a> <input>
    + button type
        + btn-default, btn-primary, btn-secondary, btn-success,
            btn-info, btn-warning, btn-danger, btn-link
        + class = "btn btn-default"
    + button size
        + class = "btn-lg btn-default"
    + create a button as block
        + by default, html button is an inline element
        + class = "btn-lg btn-default btn-block"
    + create a button group
        + <div class="btn-group" role="group">
            <button type="button" class="btn btn-primary"> button1 </button>
            <button type="button" class="btn btn-info"> button2 </button>
          </div>
    + create a toolbar: group of button group
        + <div class="btn-toobar" role="toolbar">
+ drop-down menu
    + <div class="dropdown">
        <button type="button" class="btn btn-primary dropdown-toggle"> 
            button1 </button>
            <ul class="dropdown-menu" role="menu">
                <li class="dropdown-header"> text </li>
                <li> <a href="#"> text </a> </li>
                <li> <a href="#"> text </a> </li>
                <li class="divider"> </li>
                <li class="dropdown-header"> text </li>
                <li> <a href="#"> text </a> </li>
                <li> <a href="#"> text </a> </li>
                </ul>
          </div>
+ navigation bar
    + <nav class="navbar navbar-default">
        <div class="container-fluid">
            + logo
            <div class="navbar-header">
                <a class="navbar-brand" href="#"> Name </a>
            </div>
            + contents
            <ul class="nav navbar-nav">
                <li class="active"><a href="#"> Home </a></li>
                <li><a href="#"> News </a></li>
            </ul>
            + search bar
            <form class="navbar-form">
                <div class="form-group">
                    <input type="text" class="form-control" 
                        placeholder="serarch">
                </div>
                <button type="submit" class="btn btn-danger"> submit </button>
            </form>
        </div>
      </nav>
    + nav-default, nav-inverse

