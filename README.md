# TurtleSC

TurtleSC provides a mini-language of shortcut instructions to carry out turtle.py function calls, like `'f 100'` instead of `forward(100)`. These two examples do the same thing:


| Original Turtle Code | TurtleSC Code |
| -------------------- | ------------- |
| `from turtle import *`<br>`from random import *`<br><br>`colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']`<br><br>`speed('fastest')`<br>`pensize(3)`<br>`bgcolor('black')`<br>`for i in range(300):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`pencolor(choice(colors))`<br>&nbsp;&nbsp;&nbsp;&nbsp;`forward(i)`<br>&nbsp;&nbsp;&nbsp;&nbsp;`left(91)`<br>`hideturtle()`<br>`done()` | `from turtlesc import *`<br>`from random import *`<br><br>`colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']`<br><br>`sc('spd fastest, ps 3, bc black')`<br>`for i in range(300):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`sc(f'pc {choice(colors)}, f {i}, l 91')`<br>`sc('hide,done')` |



These shortcuts are quicker to type, making them ideal for experimenting from the interactive shell. TurtleSC takes the idea of the existing `fd()` and `rt()` aliases for `forward()` and `right()` to the next level. All shortcuts are run from a string passed to the `turtlesc.sc()` function.

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

Some less-common shortcuts (such as `'done'`) only have their full function name. All shortcuts have their full function name as a shortcut name: you can use either `'f'` or `'forward'`.

TurtleSC also adds cardinal movement shortcuts that move the turtle independent of it's current heading (and does not change the heading): `'n 100'`, `'s 100'`, `'e 100'`, `'w 100'` will move the turtle up, down, right, and left 100 steps, respectively. There are also full name shortcuts (`'north'`, `'south'`, `'east'`, `'west'`) and diagonal shortcuts (`'nw'`, `'ne'`, `'sw'`, `'se'`, `'northwest'`, `'northeast'`, `'southwest'`, `'southeast'`).

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


If you want to get the original code for a shortcuts string (which can be helpful to print the shortcuts), pass it to the `scs()` function:

```python
>>> from turtlesc import *
>>> scs('f 100, r 45, f 100')
'forward(100)\nright(45)\nforward(100)'
```

Note that the return value of `scs()` is a string. If there are multiple shortcuts, they are separated by a newline and all lack the `turtle.` prefix in case you want to add your own (either the `turtle` module or a variable containing a `Turtle` object.)

To easily print out this shortcut string, call `psc()`:

```python
>>> from turtlesc import *
>>> psc('f 100, r 45, f 100')
forward(100)
right(45)
forward(100)
```





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
| `sc('eoc')` | [`exitonclick()`](https://docs.python.org/3/library/turtle.html#turtle.exitonclick) |
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
| `sc('# this is a comment')` | `# this is a comment` |

**Notes**

The `sc(skip=True)` keyword argument skips all the shortcuts. Consider this the same as commenting out the `sc()` call.

The `sc('sleep 5')` shortcut exists to call the `time.sleep()` function.

You can pass multiple strings to `sc()`. For example, `sc('f 100', 'r 45', 'f 100')` is equivalent to `sc('f 100, r 45, f 100')`.

The `'pc'`, `'fc'`, and `'bc'` shortcuts for pen color, fill color, and background color can take a color argument as:

* A color name, such as `'red'`
* Three 0 to 255 integer values, such as `'255 0 0` (turtle.py's [color mode](https://docs.python.org/3/library/turtle.html#turtle.colormode) must be set to 255)
* Three 0.0 to 1.0 float values, such as `'1.0 0.0 0.0` (turtle.py's [color mode](https://docs.python.org/3/library/turtle.html#turtle.colormode) must be set to 255)
* A hexadecimal RGB code, such as `'#FF0000'` (the leading # hashtag is required)

The cardinal directions shortcuts change *both* the heading and position of the turtle.

## scs (shortcut strings) and psc (print shortcuts)

If you pass the shortcut string to `scs()`, instead of carrying out the turtle instructions, it will return a string of the original turtle.py function calls the `sc()` function would make. For example:

```python
>>> from turtlesc import *
>>> scs('bf, f 100, r 90, f 100, r 90, ef')
'begin_fill()\nforward(100)\nright(90)\nforward(100)\nright(90)\nend_fill()\n'
```

If you'd like to print these out for debugging purposes, you can call `psc()`:

```python
>>> from turtlesc import *
>>> psc('bf, f 100, r 90, f 100, r 90, ef')
begin_fill()
forward(100)
right(90)
forward(100)
right(90)
end_fill()
```

## Comments

You can put comments inside the shortcut string. This is especially helpful when passing multi-line strings to `sc()`. Comments begin with a # hashtag character and go up to the next comma (which marks the start of the next shortcut). For example:

```python
>>> from turtlesc import *
>>> sc('''f 100
          r 100
          f 100, # This is a comment
          # Another comment
          r 100, f 100''')
```

## Skipping Shortcuts

If you want to temporarily disable a call to `sc()`, you could comment it out like any other Python instruction. However, this is difficult for `sc()` calls that have multi-line string arguments. Instead, add the `skip=True` keyword argument to the call. For example, this instruction does absolutely nothing:

```python
from turtlesc import *
sc('''f 100
      r 100
      f 100,
      r 100, f 100''', skip=True)
```

When you want to add these shortcuts back in, remove the `skip=True` text.

## Recording Turtle Function Calls

If you want to collect the turtle.py function calls for all your `sc()` calls, add a call to `begin_recording()` to the start of your program. When you call `end_recording()` at the end, it returns a list of strings of turtle.py function calls. For example:

```python
>>> from turtlesc import *
>>> begin_recording()
>>> sc('f 100, r 90, f 100')
3
>>> sc(' r 90,f 100, r 90, f 100')
4
>>> end_recording()
['f 100', ' r 90', ' f 100', ' r 90', 'f 100', ' r 90', ' f 100']
```

## Interactive Drawing Mode

You can draw with the turtle like an [etch a sketch](https://en.wikipedia.org/wiki/Etch_A_Sketch) by using TurtleSC's interactive mode. Make one of the following function calls:

```python
>>> from turtlesc import *
>>> interactive()  # Use cardinal direction style (the default): WASD moves up/down, left/right
>>> interactive('turn')  # WASD moves forward/backward, turn counterclockwise/clockwise
>>> interactive('isometric')  # WASD moves up/down, and the AD, QE keys move along a 30 degree isometric plane
```

For all styles, the O and L key move the pen up and down, respectively. The H key moves the cursor home (to 0, 0) and clears the window. The U key is an undo. A mouse click moves the turtle with the pen up (and puts the pen back down if it had been down before.)

Details of each movement style:

* **'cardinal'** style has the WASD and arrow keys move up/down/left/right. The QE, ZC keys also move diagonally. Pass the `length` argument for how long each movement should be. Diagonal movements are shortened so that a diagonal up-right movement goes to the same position as an up movement and a right movement.

* **'turn'** style has the WASD and arrow keys move forward/backward and *turn* left and right relative to its current heading. Each turn is 90 degrees. However, you can also add a number like **'turn45'** or **'turn30'** to have it turn by a different amount for each key press.

* **'isometric'** style has the WA keys move up/down, but the QE, AD keys move [diagonally along an isometric plane](https://duckduckgo.com/?q=isometric+tile+game&t=ffab&iar=images).


Cardinal:

<img src="https://raw.githubusercontent.com/asweigart/turtlesc/refs/heads/main/style-cardinal.png" />

Turn:

<img src="https://raw.githubusercontent.com/asweigart/turtlesc/refs/heads/main/style-turn.png" />

Isometric:

<img src="https://raw.githubusercontent.com/asweigart/turtlesc/refs/heads/main/style-isometric.png" />


## Contribute

If you'd like to contribute, send emails to [al@inventwithpython.com](mailto:al@inventwithpython.com)

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon.](https://www.patreon.com/AlSweigart)

