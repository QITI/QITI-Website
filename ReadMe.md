New Hugo website for QITI lab.

[![github pages](https://github.com/QITI/QITI-Website/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/QITI/QITI-Website/actions/workflows/gh-pages.yml)

To run a local copy:
* Install hugo:
* Next clone this repo into any directory
* Navigate to themes/ananke
* run $ git submodule init
* run $ git submodule update
* navigate back to the root of the repo
* run $ hugo server -D
* Open any browser and navigate to the address in the output from hugo



Colour palette:

The colour palette of the website is derived from the ion images ('inferno' theme). The primary colours are shown in "QITI_ions_color_palette.PNG". 



TO DO:

1. Change default background color of the webpages.
2. Remove space at the bottom of home page (after the recent publications section) - done, options in baseof.html
3. Bottom padding for short pages, such as individual members without much content. 
4. "Top of the page button", e.g. in Publication-sections. A floating button would be ideal. 
5. Page highlighting co-op work
6. Resources page - Ion spectrum, collection of important papers, list of other groups



TIPS:

1. Repeating-linear-gradient in background: 

   ! <div style="background: repeating-linear-gradient(45deg,
     rgb(80,76,85) 0%, rgb(80,76,85) 10%, rgb(225,217,187) 100%)">

2. 

   <div style="background: repeating-linear-gradient(45deg,
     rgb(80,76,85) 0%, rgb(80,76,85) 10%, rgb(225,217,187) 100%)">

