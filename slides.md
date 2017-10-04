%title: Building awesome (command line) tools in Python!
%author: github.com/snth/numismatic
%date: 2017-10-05


      ______________________________________
    / You suck at shell scripting:           \
    | Building awesome command line tools in |
    \ Python for fun and profit!             /
      --------------------------------------
             \   ^__^ 
              \  (oo)\_______
                 (__)\       )\/\
                     ||----w |
                     ||     ||
    

-------------------------------------------------------------------------------

# Background

<br>
  * Found myself spending a lot of time looking up bash syntax:

  <br>
      * Why do I need to use `[[ condition ]]` instead of 
        `[ condition ]` again?

  <br>
  * Conclusion?

  <br>
      * I suck at shell scripting!
    
  <br>
> Python is a good scripting language

  <br>
  * So why am I not using it for shell scripting?

  <br>
  * Decided to investigate what's available.

  <br>
  * Found that: 
  
  <br>
      * *Python (3) is awesome for shell scripting!*

-------------------------------------------------------------------------------

# Objectives

Highlight

  * *Python 3 features*

      <br>
      * _f-strings_

      <br>
      * _pathlib_

  <br>
  * The *click* library

      <br>
      * A replacement for `argparse`, `optparse` and more

  <br>
  * *Build a CLI* for collecting *cryptocurrency* data for fun and profit!

-------------------------------------------------------------------------------

# Python 3 features

<br>
*f-strings*

  <br>
  * Let's look at bash snipped I use in my deployments:
    <br> 

    LATEST_RELEASE=$(curl -s -X GET http://$(REGISTRY_URL)/v2/$(IMAGE)/tags/list \
        | jq -r ".tags[]" \
        | grep -E $(REGEXP_RELEASE) \
        | sort -V \
        | tail -n )

      <br>
      * Gets the job done but not very reusable.

      <br>
      * However one advantage is that the URL is more readable than
        `'http://{}/v2/{}/tags/list'.format(REGISTRY_URL, IMAGE)`

      <br>
      * With *f-strings* this becomes much better:

    from subprocess import call
    call(f'curl -s -X GET http://{REGISTRY_URL}/v2/{IMAGE}/tags/list')

