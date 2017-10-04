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

-> # Background

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

-> # Objectives

<br>
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

-> # Python 3 features

<br>
*f-strings*

  <br>
  * Let's look at bash snippet I use in my deployments:
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

-------------------------------------------------------------------------------

-> # Python 3 features

<br>
*pathlib*

  <br>
  * `os.path` is dead! Long live *pathlib*!

    <br>
    * `os.path`\`s procedural API had long felt clunky to me.

    <br>
    * *pathlib* is awesome!

-------------------------------------------------------------------------------

-> # Python 3 features

<br>
*pathlib* examples (1)

<br>
## paths

    from pathlib import Path
    p = Path('.')
    p

    <br>
    str(p)
    str(p.absolute())

    <br>
    p = p.absolute()
    p.as_posix()

    <br>
    p.as_uri()

    <br>
    p.parent

    <br>
    p.relative_to(p.parent)

-------------------------------------------------------------------------------

-> # Python 3 features

<br>
*pathlib* examples (2)

<br>
## testing

    <br>
    p.exists()

    <br>
    p.is_dir()

    <br>
    p.is_file()
 
-------------------------------------------------------------------------------

-> # Python 3 features

<br>
*pathlib* examples (3)

<br>
## navigation

  <br>
  * subdirectories

    [x for x in p.iterdir() if x.is_dir()]

  <br>
  * files

    [x for x in p.iterdir() if x.is_file()]

  <br>
  * finding files by glob and recursively

    list(p.rglob('*'))

-------------------------------------------------------------------------------

-> # Python 3 features

<br>
*pathlib* examples (4)

## object creation

    <br>
    q = p / 'newdir'
    q

    <br>
    q.exists()

    <br>
    q.mkdir()

    <br>
    q.exists()

    <br>
    fp = n / 'newfile.txt'
    fp

    <br>
    with fp.open('wt') as f:
        f.write('The quick brown fox jumped over the lazy dog.')

    <br>
    fp.exists() and fp.is_file()

    <br>
    fp.read_text()

-------------------------------------------------------------------------------

-> # Python 3 features

<br>
*pathlib* examples (5)

## object removal

    <br>
    fp.unlink()

    <br>
    fp.exists()

    <br>
    q.rmdir()

    <br>
    q.exists()
