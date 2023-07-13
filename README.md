# Calculating Pi
This repo contains 6 different ways to calculate pi, all of them are in the `methods/` directory. If you want a new method to be implemented, have a new method you want to add, or have any questions, just leave an issue (and/or a pull request) and I will respond/review it.

## `generate.py`
This script uses the .js files in `methods/` to generate the .html files, I made it because I don't want to edit a bunch of files every time I need to make a change.

## Writing your own methods
New methods must implement the `calcPi()` function with preferably one argument (by default `runner.js` will only provide one argument). They should also have some data about them, written in comments somewhere in the file, these comments can include HTML elements in them as they are directly pasted into the HTML file.  
Example:
```js
// name: [Method name]
// desc: [Short description]
// url: [Optional link to an external resource, eg. a Wikipedia article
/* longdesc:
[Optional multi-line long description of the method, not shown on the home page]

*/

function calcPi(arg) {
  // Do something
  return pi;
}
```
