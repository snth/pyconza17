%title: Building awesome (command line) tools in Python!
%author: github.com/snth/pyconza17
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

  * Found myself spending a lot of time looking up bash syntax:

      * Why do I need to use `[[ condition ]]` instead of 
        `[ condition ]` again?

  * Conclusion?

  <br>
      * I suck at shell scripting!
    
  <br>
> Python is a good scripting language

  * So why am I not using it for shell scripting?

      <br>
      * Impedance mismatch

  <br>
  * Decided to investigate current shell scripting/CLI support:

  * Found that: 
  
  <br>
      * *Python (3) is awesome for shell scripting!*

-------------------------------------------------------------------------------

-> # Objectives

Highlight

  * *Python 3 features*

      * `f-strings`

      * `pathlib`

  <br>
  * The *click* library

      * Makes writing a CLI easy and fun!

      * A replacement for `argparse`, `optparse` and more

  <br>
  * *Build a CLI* for collecting *cryptocurrency* data for fun and profit!

      * Learn about

          * *asyncio*

          * *attrs*

          * *streamz*

-------------------------------------------------------------------------------

-> # Python 3 features

*f-strings*

  <br>
  * Let's look at bash snippet I use in my deployments:

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

*pathlib*

  <br>
  * `os.path` is dead! Long live *pathlib*!

    <br>
    * `os.path`\`s procedural API had long felt clunky to me.

    * *pathlib* is awesome!

-------------------------------------------------------------------------------

-> # Python 3 features

*pathlib* examples (1)

## paths

    <br>
    from pathlib import Path
    p = Path('.')
    p

    <br>
    str(p)
    str(p.absolute())

    p = p.absolute()
    p.as_posix()

    p.as_uri()

    p.parent

    p.relative_to(p.parent)

-------------------------------------------------------------------------------

-> # Python 3 features

*pathlib* examples (2)

## interrogating paths

    q = p / 'newdir'
    q

    <br>
    p.exists()

    q.exists()

    p.is_dir()

    p.is_file()
 
-------------------------------------------------------------------------------

-> # Python 3 features

*pathlib* examples (3)

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

*pathlib* examples (4)

## object creation

  <br>
  * directories

    q.exists()

    q.mkdir()

    q.exists()

  <br>
  * files

    fp = n / 'newfile.txt'
    fp

    with fp.open('wt') as f:
        f.write('The quick brown fox jumped over the lazy dog.')

    fp.exists() and fp.is_file()

    fp.read_text()

-------------------------------------------------------------------------------

-> # Python 3 features

*pathlib* examples (5)

## object removal

  <br>
  * files

    fp.unlink()

    fp.exists()

    * My only bugbear: why is there no

        fp.rm()

        fp.remove()
    
        fp.delete()

  <br>
  * directories

    q.rmdir()

    q.exists()

-------------------------------------------------------------------------------

-> # CLIs

## Command Line Interfaces

  <br>
  * Reputation as `arcane` and `difficult`

  <br>
  * --> 40 years of bad branding

  <br>
  * Rebrand these in line with current trends as *Chatbot Like Interface*!

      <br>
      * Only half joking: use text to interact with your application!

<br>
## I like them!

  * Encourage compositional/functional thinking

  * Do one thing well

  * Great for automating non-regular tasks

-------------------------------------------------------------------------------

-> # Click

## Command Line Interface Creation Kit

  <br>
  * Lots of features for quickly creating useful interfaces

      * automatic help page generation
      * parameter validation
      * arbitrary nesting of commands
      * supports lazy loading of subcommands at runtime

-------------------------------------------------------------------------------

-> # Click

## Basic Example

    <br>
    import click

    @click.command()
    @click.option('--count', default=1, help='Number of greetings.')
    @click.option('--name', prompt='Your name', help='The person to greet.')
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            click.echo('Hello {}!'.format(name))

    if __name__=='__main__':
        hello()

<br>
Then run it

    python examples/greet.py

    python examples/greet.py --name 'PyconZA 2017' --count 3

-------------------------------------------------------------------------------

-> # Click

## Setuptools integration

See [http://github.com/snth/numismatic/setup.py](github.com/snth/numismatic.py)

<br>
Then easily install with

    pip install -e .

-------------------------------------------------------------------------------

-> # Numismatic

## Motivation

  * Collect *cryptocurrency* prices

  <br>
  * Try out

      * *asyncio*

      * *attrs*

      * *streamz*

      * *websockets*

-------------------------------------------------------------------------------

-> # Numismatic

*streamz*

  * Small library by Mathew Rocklin (creator of `dask`) for trying out
    stream based/reactive event processing in pure Python.

  * Self-contained with few dependencies

  * Test stream based dataflow before deploying `Kafka`, `Flink`, ...

    <br>
    from streamz import Stream
    source = Stream()

    source.emit('hello')
    source.emit('world')

    <br>
    printer = source.map(print)
    for event in ['hello', 'world']:
        source.emit(event)
 
    <br>
    L = []
    collector = source.map(L.append) j
    for event in ['hello', 'world']:
        source.emit(event)

-------------------------------------------------------------------------------

-> # Numismatic

*attrs*

  * I think of it as better *namedtuples*

  * Classes without the boilerplate

  <br>
  * Look at `numismatic/events.py`
    
    <br>
    @attr.s(slots=True)
    class Heartbeat:
        exchange = attr.ib()
        symbol = attr.ib()
        timestamp = attr.ib(default=attr.Factory(time.time))

  <br>
  * Use it as

    from numismatic.events import Heartbeat
    Heartbeat('bitfinex', 'BTCUSD')

    <br>
    import attr
    attr.asdict(Heartbeat('bitfinex', 'BTCUSD'))

-------------------------------------------------------------------------------

-> # Numismatic

*asyncio*

  * Good tutorials out there.

  * I found these helpful:

      * [asyncio — Asynchronous I/O, event loop, and concurrency tools](https://pymotw.com/3/asyncio/)

      * [AsyncIO for the Working Python Developer](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e)

-------------------------------------------------------------------------------

-> # Numismatic

*Example*

  <br>
  * Set up our streams

    from streamz import Stream
    source = Stream()
    printer = source.map(print)
    L = []
    collector = source.map(L.append)

  <br>
  * Prepare our connection

    from numismatic.exchanges import BitfinexExchange
    bfx = BitfinexExchange(source)
    subscription = bfx.listen('BTCUSD', 'trades')

  <br>
  * Run the event loop

    import asyncio
    loop = asyncio.get_event_loop()
    future = asyncio.wait([subscription], timeout=10)
    loop.run_until_complete(future)

-------------------------------------------------------------------------------

-> # Numismatic

## *coin* CLI

  * Install

    git clone https://github.com/snth/numismatic.git
    cd numismatic
    pip install -e .

  * Run without arguments for help (or with `--help`)

    coin

-------------------------------------------------------------------------------

-> # Closing

## We're hiring!

  * Go to *https://bitbucket.org/argonasset/opportunities*

## Contact

  * I'm *snth* on `github` and `zatech` slack.

  * Presentation: *github.com/snth/pyconza17*
  * Numismatic: *github.com/snth/numismatic*

    <br>
      __________
    < Questions? >
      ----------
            \   ^__^ 
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
