# TurtleSC

TurtleSC provides a mini-language of shortcut instructions to carry out turtle.py function calls.

These shortcuts are quicker to type, making them ideal for experimenting from the interactive shell. Turtlesc takes the idea of the existing `fd()` and `rt()` aliases for `forward()` and `right()` to the next level. All shortcuts are run from a string passed to the `turtlesc.sc()` function.

TurtleSC was created by Al Sweigart, author of [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) and [other programming books](https://inventwithpython.com/). All of his books are available for free online under a [Creative Commons license](https://creativecommons.org/share-your-work/cclicenses/). If you'd like a tutorial specifically about Python's `turtle` module, check out [The Simple Turtle Tutorial](https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md).

You can also write (less readable) turtle programs using shortcuts. For example, this program:

```python
from turtle import *
from random import *

tracer(4, 0)

for i in range(50):
    fillcolor((random(), random(), random()))

    # Set a random heading and draw several short lines with changing direction:
    setheading(randint(0, 360))
    begin_fill()
    for j in range(randint(200, 600)):
        forward(1)
        left(randint(-4, 4))
    home()
    end_fill()

update()
done()
```

...could be written as:

```python
from turtlesc import *
from random import *

sc('t 4 0')

for i in range(50):
    sc(f'fc {random()} {random()} {random()}, sh {randint(0, 360)}, bf')
    for j in range(randint(200, 600)):
        sc(f'''f 1
               l {randint(-4, 4)}''')
    sc('h,ef')

sc('u,done')
```

This code isn't very readable, but it's quick to type. This is useful if you are making rapid prototypes of ideas.

Shortcuts in the `sc()` string argument are separated by a comma, with any shortcut arguments separated by spaces. Whitespace is insignificant (you can have one more spaces, and it's the same as a single space). Shortcut names and arguments are case-insensitive: `'f'` and `'F'` work the same. Newlines in the string argument are treated as shortcut-separating commas.

Some less-common shortcuts (such as `'done'`, `'bye'`, and `'exitonclick'`) only have their full function name. All shortcuts have their full function name as a shortcut name: you can use either `'f'` or `'forward'`.

TurtleSC also adds cardinal movement shortcuts that move the turtle independent of it's current heading (and does not change the heading): `'n 100'`, `'s 100'`, `'e 100'`, `'w 100'` will move the turtle up, down, right, and left 100 steps, respectively. There are also full name shortcuts (`'north'`, `'south'`, `'east'`, `'west'`) and diagnoal shortcuts (`'nw'`, `'ne'`, `'sw'`, `'se'`, `'northwest'`, `'northeast'`, `'southwest'`, `'southeast'`).

By default, the `sc()` function operates on the single, global turtle. You can also pass the `turtle_obj` keyword argument to operate on different `Turtle` objects:

```python
from turtlesc import *
from turtle import *

t1 = Turtle()
t2 = Turtle()

# Make turtle 1 red and move up-right:
sc('pc red, l 45, f 100', turtle_obj=t1)

# Make turtle 2 blue and move down-right:
sc('pc blue, r 45, f 100', turtle_obj=t2)

sc('done')
```

The `turtlesc` module also provides new `in_radians_mode()` or `in_degrees_mode()` functions that return a Boolean `True` or `False` value depending on which mode the turtle is in. These features are missing in the original `turtle` module.


If you want to get the original code for a shortcuts string, pass it to the `get_turtle_code()` function:

```python
>>> from turtlesc import *
>>> get_turtle_code('f 100, r 45, f 100')
('forward(100)', 'right(45)', 'forward(100)')
```

Note that the return value of `get_turtle_code()` is a tuple of strings, all of which lack the `turtle.` prefix in case you want to add your own (either the `turtle` module or a variable containing a `Turtle` object.)




## Reference

Here is a complete reference of supported shortcuts:

| **Shortcut Call** | **Turtle.py Equivalent** |
| ------------- | -------------------- |
| `sc('f 100')` | [`forward(100)`](https://docs.python.org/3/library/turtle.html#turtle.forward) |
| `sc('b -100.5')` | [`backward(-100.5)`](https://docs.python.org/3/library/turtle.html#turtle.backward) |
| `sc('l 45')` | [`left(45)`](https://docs.python.org/3/library/turtle.html#turtle.left) |
| `sc('r 90')` | [`right(90)`](https://docs.python.org/3/library/turtle.html#turtle.right) |
| `sc('h')` | [`home()`](https://docs.python.org/3/library/turtle.html#turtle.home) |
| `sc('c')` | [`clear()`](https://docs.python.org/3/library/turtle.html#turtle.clear) |
| `sc('g 15 40')` | [`goto(15 40)`](https://docs.python.org/3/library/turtle.html#turtle.goto) |
| `sc('x 10')` | [`setx(10)`](https://docs.python.org/3/library/turtle.html#turtle.setx) |
| `sc('y -20')` | [`sety(-20)`](https://docs.python.org/3/library/turtle.html#turtle.sety) |
| `sc('st')` | [`stamp()`](https://docs.python.org/3/library/turtle.html#turtle.stamp) |
| `sc('pd')` | [`pendown()`](https://docs.python.org/3/library/turtle.html#turtle.pendown) |
| `sc('pu')` | [`penup()`](https://docs.python.org/3/library/turtle.html#turtle.penup) |
| `sc('ps 4')` | [`pensize(4)`](https://docs.python.org/3/library/turtle.html#turtle.pensize) |
| `sc('pc 1.0 0.0 0.5')` | [`pencolor(1.0, 0.0, 0.5)`](https://docs.python.org/3/library/turtle.html#turtle.pencolor) |
| `sc('fc 255 0 128')` | [`fillcolor(255, 0, 128)`](https://docs.python.org/3/library/turtle.html#turtle.fillcolor) |
| `sc('bc #FF00FF')` | [`bgcolor('#FF00FF')`](https://docs.python.org/3/library/turtle.html#turtle.bgcolor) |
| `sc('sh 90')` | [`setheading(90)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) |
| `sc('cir 10')` | [`circle(10)`](https://docs.python.org/3/library/turtle.html#turtle.circle) |
| `sc('undo')` | [`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo) |
| `sc('bf')` | [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill) |
| `sc('ef')` | [`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill) |
| `sc('reset')` | [`reset()`](https://docs.python.org/3/library/turtle.html#turtle.reset) |
| `sc('sleep 5')` | [`time.sleep(5)`](https://docs.python.org/3/library/time.html#time.sleep) |
| `sc('n 10')` | [`setheading(90)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('s 10')` | [`setheading(270)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('e 10')` | [`setheading(180)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('w 10')` | [`setheading(0)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('nw 10')` | [`setheading(135)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('ne 10')` | [`setheading(45)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('sw 10')` | [`setheading(225)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('se 10')` | [`setheading(315)`](https://docs.python.org/3/library/turtle.html#turtle.setheading) `; ` [`forward(10)`](https://docs.python.org/3/library/turtle.html#turtle.forward)|
| `sc('done')` | [`done()`](https://docs.python.org/3/library/turtle.html#turtle.done) |
| `sc('bye')` | [`bye()`](https://docs.python.org/3/library/turtle.html#turtle.bye) |
| `sc('exitonelick')` | [`exitonclick()`](https://docs.python.org/3/library/turtle.html#turtle.exitonclick) |
| `sc('t 100 0')` | [`tracer(100, 0)`](https://docs.python.org/3/library/turtle.html#turtle.tracer) |
| `sc('u')` | [`update()`](https://docs.python.org/3/library/turtle.html#turtle.update) |
| `sc('hide')` | [`hide()`](https://docs.python.org/3/library/turtle.html#turtle.hideturtle) |
| `sc('show')` | [`show()`](https://docs.python.org/3/library/turtle.html#turtle.showturtle) |
| `sc('dot 5')` | [`dot(5)`](https://docs.python.org/3/library/turtle.html#turtle.dot) |
| `sc('cs 42')` | [`clearstamp(42)`](https://docs.python.org/3/library/turtle.html#turtle.clearstamp) |
| `sc('css')` | [`clearstamps()`](https://docs.python.org/3/library/turtle.html#turtle.clearstamps) |
| `sc('css 10')` | [`clearstamps(10)`](https://docs.python.org/3/library/turtle.html#turtle.clearstamps) |
| `sc('degrees')` | [`degrees()`](https://docs.python.org/3/library/turtle.html#turtle.degrees) |
| `sc('radians')` | [`radians()`](https://docs.python.org/3/library/turtle.html#turtle.radians) |
| `sc('spd 5')` | [`speed(5)`](https://docs.python.org/3/library/turtle.html#turtle.speed) |
| `sc('spd fastest')` | [`speed('fastest')`](https://docs.python.org/3/library/turtle.html#turtle.speed) |

**Notes**

The `sc('sleep 5')` shortcut exists to call the `time.sleep()` function.

You can pass multiple strings to `sc()`. For example, `sc('f 100', 'r 45', 'f 100')` is equivalent to `sc('f 100, r 45, f 100')`.

The `'pc'`, `'fc'`, and `'bc'` shortcuts for pen color, fill color, and background color can take a color argument as:

* A color name, such as `'red'`
* Three 0 to 255 integer values, such as `'255 0 0` (turtle.py's [color mode](https://docs.python.org/3/library/turtle.html#turtle.colormode) must be set to 255)
* Three 0.0 to 1.0 float values, such as `'1.0 0.0 0.0` (turtle.py's [color mode](https://docs.python.org/3/library/turtle.html#turtle.colormode) must be set to 255)
* A hexadecimal RGB code, such as `'#FF0000'` (the leading # hashtag is required)

The cardinal directions shortcuts change *both* the heading and position of the turtle.

## Contribute

If you'd like to contribute, send emails to [al@inventwithpython.com](mailto:al@inventwithpython.com)

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon.](https://www.patreon.com/AlSweigart)

