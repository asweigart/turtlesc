import turtle, time, re

ALL_SHORTCUTS = 'f b l r h c g x y st u pd pu ps pc fc bc sh cir undo bf ef sleep n s e w nw ne sw se' + \
    'forward backward left right home clear goto setx sety stamp update pendown penup pensize pencolor fillcolor bgcolor setheading circle undo begin_fill end_fill north south east west northwest northeast southwest southeast reset bye done exitonclick'

_MAP_FULL_TO_SHORT_NAMES = {'forward': 'f', 'backward': 'b', 'right': 'r', 'left': 'l', 'home': 'h', 'clear': 'c', 
        'goto': 'g', 'setx': 'x', 'sety': 'y', 'stamp': 'st', 'update': 'u', 'pendown': 'pd', 'penup': 'pu', 'pensize': 'ps', 
        'pencolor': 'pc', 'fillcolor': 'fc', 'bgcolor': 'bc', 'setheading': 'sh', 'circle': 'cir', 
        'begin_fill': 'bf', 'end_fill': 'ef', 'north': 'n', 'south': 's', 'east': 'e', 'west': 'w',
        'northwest': 'nw', 'northeast': 'ne', 'southwest': 'sw', 'southeast': 'se'}

class TurtleShortcutException(Exception):
    pass

def sc(*args, turtle_obj=None): # type: () -> int
    """Supported commands:

    f N - forward(N)
    b N - backward(N)
    l N - left(N)
    r N - right(N)
    h - home()
    c - clear()
    g X Y - goto(X, Y)
    x X - setx(X)
    y Y - sety(Y)
    st - stamp()
    pd - pendown()
    pu - penup()
    ps N - pensize(N)
    pc RGB - pencolor(RGB) (RGB value can either be a single string like `red` or three dec/hex numbers `1.0 0.0 0.5` or `FF FF 00`
    fc RGB - fillcolor(RGB)
    bc RGB - bgcolor(RGB)
    sh N - setheading(N)
    cir N - circle(N)
    undo - undo()
    bf - begin_fill()
    ef - end_fill()
    to X Y - towards(X, Y)
    reset - reset()

    sleep N - time.sleep(N)

    n N - setheading(90);forward(N)
    s N - setheading(270);forward(N)
    w N - setheading(180);forward(N)
    e N - setheading(0);forward(N)
    nw N - setheading(135);forward(N)
    ne N - setheading(45);forward(N)
    sw N - setheading(225);forward(N)
    se N - setheading(315);forward(N)
    north N - setheading(90);forward(N)
    south N - setheading(270);forward(N)
    west N - setheading(180);forward(N)
    east N - setheading(0);forward(N)
    northwest N - setheading(135);forward(N)
    northeast N - setheading(45);forward(N)
    southwest N - setheading(225);forward(N)
    southeast N - setheading(315);forward(N)

    done - done()
    bye - bye()
    exitonclick - exitonclick()

    Note: 


    Furthermore, you can also use the full names: forward N translates to forward(N).
    Note: None of these functions can take string args that have spaces in them, since spaces are the arg delimiter here.
    Note: You also can't use variables here, only static values. But you can use f-strings.

    Return value is the number of commands executed.
    Whitespace is insignificant. '   f     100   ' is the same as 'f 100'
    """


    # Join multiple arg strings into one, separated by commas:
    shortcuts = ','.join(args)

    # Newlines become commas as well:
    shortcuts = shortcuts.replace('\n', ',')

    if shortcuts == '' or len(shortcuts.split(',')) == 0:
        return 0
    
    count_of_shortcuts_run = 0

    # Go through and check that all shortcuts are syntactically correct:
    for shortcut in shortcuts.split(','):
        count_of_shortcuts_run += _run_shortcut(shortcut, turtle_obj=turtle_obj, dry_run=True)

    # Go through and actually run all the shortcuts:
    count_of_shortcuts_run = 0
    for shortcut in shortcuts.split(','):
        count_of_shortcuts_run += _run_shortcut(shortcut, turtle_obj=turtle_obj)
         
    return count_of_shortcuts_run


def _run_shortcut(shortcut, turtle_obj=None, dry_run=False):
    # NOTE: The nsew shortcuts only work properly in degrees mode, not radians mode.
    
    if turtle_obj is None:
        turtle_obj = turtle  # Use the main turtle given by the module.

    # Clean up shortcut name from "  FOrWARD " to "f", for example.
    shortcut_parts = shortcut.strip().split()
    if len(shortcut_parts) == 0:
        return 0
    _sc = shortcut_parts[0].lower()
    _sc = _MAP_FULL_TO_SHORT_NAMES.get(_sc, _sc)

    # Check that the shortcut's syntax is valid:

    if _sc not in ALL_SHORTCUTS:
        raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[0] + '` is not a turtle shortcut.')

    raise_exception = False
    count_of_shortcuts_run = 0
    
    if _sc in ('f', 'b', 'r', 'l', 'x', 'y', 'ps', 'sh', 'cir', 'sleep', 'n', 's', 'e', 'w', 'nw', 'ne', 'sw', 'se'):
        # These shortcuts take a single numeric argument.
        if len(shortcut_parts) < 2:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: Missing the required numeric argument.')
        if len(shortcut_parts) > 2:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: Too many arguments.')

        try:
            float(shortcut_parts[1])
        except ValueError:
            raise_exception = True  # We don't raise here so we can hide the original ValueError and make the stack trace a bit neater.
        if raise_exception:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[1] + '` is not a number.')

        if not dry_run:
            # Run the shortcut that has exactly one numeric argument:
            if _sc == 'f':
                turtle_obj.forward(float(shortcut_parts[1]))
            elif _sc == 'b':
                turtle_obj.backward(float(shortcut_parts[1]))    
            elif _sc == 'r':
                turtle_obj.right(float(shortcut_parts[1]))    
            elif _sc == 'l':
                turtle_obj.left(float(shortcut_parts[1]))    
            elif _sc == 'x':
                turtle_obj.setx(float(shortcut_parts[1]))    
            elif _sc == 'y':
                turtle_obj.sety(float(shortcut_parts[1]))    
            elif _sc == 'ps':
                turtle_obj.pensize(float(shortcut_parts[1]))    
            elif _sc == 'sh':
                turtle_obj.setheading(float(shortcut_parts[1]))
            elif _sc == 'cir':
                turtle_obj.circle(float(shortcut_parts[1]))    
            elif _sc == 'sleep':
                time.sleep(float(shortcut_parts[1]))
            elif _sc in ('n', 's', 'e', 'w', 'nw', 'ne', 'sw', 'se'):
                originally_in_radians_mode = in_radians_mode()
                turtle.degrees()
                if _sc == 'n':
                    turtle.setheading(90)
                elif _sc == 's':
                    turtle.setheading(270)
                elif _sc == 'e':
                    turtle.setheading(0)
                elif _sc == 'w':
                    turtle.setheading(180)
                elif _sc == 'nw':
                    turtle.setheading(135)
                elif _sc == 'ne':
                    turtle.setheading(45)
                elif _sc == 'sw':
                    turtle.setheading(225)
                elif _sc == 'se':
                    turtle.setheading(315)
                else:  # pragma: no cover
                    assert False, 'Unhandled shortcut: ' + _sc
                turtle_obj.forward(float(shortcut_parts[1]))
                if originally_in_radians_mode:
                    turtle.radians()
            else:  # pragma: no cover
                assert False, 'Unhandled shortcut: ' + _sc
            count_of_shortcuts_run += 1

    elif _sc in ('g',):
        # These shortcuts take exactly two numeric arguments.
        if len(shortcut_parts) < 3:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: Missing two required numeric argument.')
        elif len(shortcut_parts) > 3:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: Too many arguments.')

        try:
            float(shortcut_parts[1])
        except ValueError:
            raise_exception = True  # We don't raise here so we can hide the original ValueError and make the stack trace a bit neater.
        if raise_exception:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[1] + '` is not a number.')
        try:
            float(shortcut_parts[2])
        except ValueError:
            raise_exception = True  # We don't raise here so we can hide the original ValueError and make the stack trace a bit neater.
        if raise_exception:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[2] + '` is not a number.')

        if not dry_run:
            # Run the shortcut that has exactly two numeric arguments:
            x = float(shortcut_parts[1])
            y = float(shortcut_parts[2])

            # Run the shortcut:
            if _sc == 'g':
                turtle_obj.goto(x, y)
            else:  # pragma: no cover
                assert False, 'Unhandled shortcut: ' + _sc 
            count_of_shortcuts_run += 1

    elif _sc in ('h', 'c', 'st', 'pd', 'pu', 'undo', 'bf', 'ef', 'reset', 'bye', 'done', 'exitonclick'):
        # These shortcuts take exactly zero numeric arguments.
        if len(shortcut_parts) > 1:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: This shortcut does not have arguments.')

        if not dry_run:
            # Run the shortcut that has exactly zero arguments:
            if _sc == 'h':
                turtle_obj.home()
            elif _sc == 'c':
                turtle_obj.clear()
            elif _sc == 'st':
                turtle_obj.stamp()
            elif _sc == 'pd':
                turtle_obj.pendown()
            elif _sc == 'pu':
                turtle_obj.penup()
            elif _sc == 'undo':
                turtle_obj.undo()
            elif _sc == 'bf':
                turtle_obj.begin_fill()
            elif _sc == 'ef':
                turtle_obj.end_fill()
            elif _sc == 'reset':
                turtle_obj.reset()
            elif _sc == 'bye':  # pragma: no cover
                turtle_obj.bye()
            elif _sc == 'done':  # pragma: no cover
                turtle_obj.done()
            elif _sc == 'exitonclick':  # pragma: no cover
                turtle_obj.exitonclick()
            else:  # pragma: no cover
                assert False, 'Unhandled shortcut: ' + _sc
            count_of_shortcuts_run += 1

    elif _sc in ('pc', 'fc', 'bc'):
        # These shortcuts take one RGB argument:
        if len(shortcut_parts) < 2:
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: Missing required RGB argument.')
        elif len(shortcut_parts) not in (2, 4):
            raise TurtleShortcutException('Syntax error in `' + shortcut + '`: Invalid RGB argument. It must either be a color name like `red` or three numbers like `1.0 0.5 0.0` or `255 0 255` or `FF 00 FF`.')

        if len(shortcut_parts) == 4:
            # We expect the color arg to either be something like (255, 0, 0) or (1.0, 0.0, 0.0):
            raise_exception = False

            try:
                float(shortcut_parts[1])
            except ValueError:
                raise_exception = True  # We don't raise here so we can hide the original ValueError and make the stack trace a bit neater.
            if raise_exception:
                raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[1] + '` is not a number.')

            try:
                float(shortcut_parts[2])
            except ValueError:
                raise_exception = True  # We don't raise here so we can hide the original ValueError and make the stack trace a bit neater.
            if raise_exception:
                raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[2] + '` is not a number.')

            try:
                float(shortcut_parts[3])
            except ValueError:
                raise_exception = True  # We don't raise here so we can hide the original ValueError and make the stack trace a bit neater.
            if raise_exception:
                raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[3] + '` is not a number.')

            color_arg = (float(shortcut_parts[1]), float(shortcut_parts[2]), float(shortcut_parts[3]))
        elif len(shortcut_parts) == 2:
            # We expect the color arg to be a string like 'blue' or 'ff0000' or '#FF0000:
            raise_exception = False

            # If the argument is an RGB value, convert to numbers:
            shortcut_parts[1] = shortcut_parts[1].strip('#')
            
            # Lowercase possible color names:
            shortcut_parts[1] = shortcut_parts[1].lower()

            if re.match(r'^[0-9a-f]{6}$', shortcut_parts[1]):
                # Convert hex color to decimal color:
                if turtle_obj.colormode() == 255:
                    color_arg = (int(shortcut_parts[1][0:2], 16), int(shortcut_parts[1][2:4], 16), int(shortcut_parts[1][4:6], 16))
                elif turtle_obj.colormode() == 1.0:
                    color_arg = (int(shortcut_parts[1][0:2], 16) / 255.0, int(shortcut_parts[1][2:4], 16) / 255.0, int(shortcut_parts[1][4:6], 16) / 255.0)
                else:  # pragma: no cover
                    assert False, 'Unknown return value from turtle.colormode(): ' + str(turtle_obj.colormode())
            else:
                # shortcut_parts[1] must be a color name like 'blue'
                color_arg = shortcut_parts[1]

            try:
                turtle_obj.pencolor(color_arg)
            except turtle.TurtleGraphicsError:
                raise_exception = True  # We don't raise here so we can hide the original TurtleGraphicsError and make the stack trace a bit neater.

            if raise_exception:
                raise TurtleShortcutException('Syntax error in `' + shortcut + '`: `' + shortcut_parts[1] + '` is not a valid color.')


        if not dry_run:
            if isinstance(color_arg, tuple):
                temp_switch_to_mode_255 = len(color_arg) == 3 and turtle_obj.colormode() == 1.0 and (color_arg[0] > 1.0 or color_arg[1] > 1.0 or color_arg[2] > 1.0)
                temp_switch_to_mode_1 = len(color_arg) == 3 and turtle_obj.colormode() == 255 and (0.0 <= color_arg[0] <= 1.0 and 0.0 <= color_arg[1] <= 1.0 and 0.0 <= color_arg[2] <= 1.0)
                assert not (temp_switch_to_mode_255 and temp_switch_to_mode_1)
            else:
                temp_switch_to_mode_255 = False
                temp_switch_to_mode_1 = False

            if temp_switch_to_mode_255:
                turtle_obj.colormode(255)
                color_arg = (int(color_arg[0]), int(color_arg[1]), int(color_arg[2]))
            elif temp_switch_to_mode_1:
                turtle_obj.colormode(1.0)
            
            # Run the shortcut that has an RGB color argument:
            if _sc == 'pc':
                turtle_obj.pencolor(color_arg)
            elif _sc == 'fc':
                turtle_obj.fillcolor(color_arg)
            elif _sc == 'bc':
                turtle_obj.bgcolor(color_arg)
            else:  # pragma: no cover
                assert False, 'Unhandled shortcut: ' + _sc  
            count_of_shortcuts_run += 1

            if temp_switch_to_mode_255:
                turtle_obj.colormode(1.0)
            elif temp_switch_to_mode_1:
                turtle_obj.colormode(255)

    return count_of_shortcuts_run

def in_radians_mode():
    """Returns True if turtle is in radians mode, False if in degrees mode."""
    original_heading = turtle.heading()
    turtle.left(1)
    turtle.radians()  # Switch to radians mode.
    turtle.right(1)
    if turtle.heading() == original_heading:
        return True
    else:
        turtle.degrees()  # Switch back to degrees mode.
        return False

def in_degrees_mode():
    """Returns True if turtle is in degrees mode, False if in radians mode."""
    return not in_radians_mode()

sc('pc FF0000')