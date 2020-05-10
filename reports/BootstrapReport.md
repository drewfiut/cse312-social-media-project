# Bootstrap Report

## Overview
Bootstrap is an HTML, CSS, and JavaScript library our group used to simplify the styling of our website.
Bootstrap allows us to easily implement complex well designed features into our project.
Bootstrap accomplishes this by having several premade CSS classes that we can assign to our html tags.
The classes are also easily edited so we were able to customize them to meet our needs.

Some of the major bootstrap classes we utilized were
    -.navbar: Used to style our navbar on every page of our website
    -.container: Used on most of our content organize page layout and keep the content width responsive
    -.card: Used for our signin page, and for displaing all projects on main feed and project page.
    -.jumbotron: Used for displaying the main heading of a page in our profile and selected project page
    -.list-group: Used to improve the appearence of our list data


## Code
To add bootstrap to our website we inclided the following line on all of our html pages
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
This loads the online version of the bootstrap css page to be referenced in our project


All pages are rendered using [base.html](../templates/base.html), which has the link to the online stylesheet we included via the url listed above.


## License
Bootstrap is licensed under the MIT license. This license grants permission to anyone to use this product free of charge with the ability to
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software. 
The only conditions we must follow are:
    "The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE."

## Citations
Bootstrap.com:
    Otto, Mark, and Jacob Thornton. “The Most Popular HTML, CSS, and JS Library in the World.” Bootstrap, getbootstrap.com/.
Bootstrap on Github.com:
    Twbs. “Twbs/Bootstrap/License.” GitHub, github.com/twbs/bootstrap/blob/master/LICENSE.