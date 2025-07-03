import pytest
from turtle import *
from turtlesc import *
from random import *

seed(42)  # Keep at 42 for reproducible tests (dependent on which tests are run and in what order, anyway)
tracer(10000, 0)

def test_basic_sc_calls():
    # Blanks are no-ops and fine:
    assert sc('') == 0
    assert sc('', '') == 0
    assert sc(' ') == 0
    assert sc(' ', ' ') == 0
    assert sc('f 1, ') == 1
    assert sc('f -1, ', '\n', ' ') == 1

    # Invalid commands raise exceptions:
    with pytest.raises(TurtleShortcutException):
        sc('invalid')
    with pytest.raises(TurtleShortcutException):
        sc('f')
    with pytest.raises(TurtleShortcutException):
        sc('f 1 2')
    with pytest.raises(TurtleShortcutException):
        sc('f invalid')

    assert sc('f 1, f -1') == 2

def test_in_radians_mode():
    radians()
    assert in_radians_mode()
    degrees()
    assert not in_radians_mode()


def test_in_degrees_mode():
    degrees()
    assert in_degrees_mode()
    radians()
    assert not in_degrees_mode()
    degrees()  # These tests always use degrees mode.


def test_forward():
    turtle.reset()

    for name in ('f', 'forward', 'F', 'FORWARD', 'fOrWaRd'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        assert sc(f'{name} 1') == 1
        assert pos() == (1, 0)
        assert sc(f'{name} -1') == 1
        assert pos() == (0, 0)
        assert sc(f'{name} 0') == 1
        assert pos() == (0, 0)
        assert sc(f'{name} 0.5') == 1
        assert pos() == (0.5, 0)
        assert sc(f'{name} -0.5') == 1
        assert pos() == (0, 0)


def test_backward():
    turtle.reset()

    for name in ('b', 'backward', 'B', 'BACKWARD', 'bAcKwArD'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument

        assert sc(f'{name} 1') == 1
        assert pos() == (-1, 0)
        assert sc(f'{name} -1') == 1
        assert pos() == (0, 0)
        assert sc(f'{name} 0') == 1
        assert pos() == (0, 0)
        assert sc(f'{name} 0.5') == 1
        assert pos() == (-0.5, 0)
        assert sc(f'{name} -0.5') == 1
        assert pos() == (0, 0)


def test_right():
    turtle.reset()

    for name in ('r', 'right', 'R', 'RIGHT', 'rIgHt'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        assert sc(f'{name} 1') == 1
        assert heading() == 359
        assert sc(f'{name} -1') == 1
        assert heading() == 0
        assert sc(f'{name} 0') == 1
        assert heading() == 0
        assert sc(f'{name} 0.5') == 1
        assert heading() == 359.5
        assert sc(f'{name} -0.5') == 1
        assert heading() == 0


def test_left():
    turtle.reset()

    for name in ('l', 'left', 'L', 'LEFT', 'lEfT'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        assert sc(f'{name} 1') == 1
        assert heading() == 1
        assert sc(f'{name} -1') == 1
        assert heading() == 0
        assert sc(f'{name} 0') == 1
        assert heading() == 0
        assert sc(f'{name} 0.5') == 1
        assert heading() == 0.5
        assert sc(f'{name} -0.5') == 1
        assert heading() == 0


def test_setheading():
    for name in ('sh', 'setheading', 'SH', 'SETHEADING', 'sEtHeAdInG'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        assert sc(f'{name} 1') == 1
        assert heading() == 1
        assert sc(f'{name} 0') == 1
        assert heading() == 0
        assert sc(f'{name} 360') == 1
        assert heading() == 0
        assert sc(f'{name} 720') == 1
        assert heading() == 0
        assert sc(f'{name} -360') == 1
        assert heading() == 0


def test_home():
    for name in ('h', 'home', 'H', 'HOME', 'hOmE'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')   # Too many arguments
        
        assert sc(f'{name}') == 1
        assert pos() == (0, 0)
        assert heading() == 0


def test_clear():
    for name in ('c', 'clear', 'C', 'CLEAR', 'cLeAr'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')   # Too many arguments

        assert sc(f'{name}') == 1


def test_goto():
    for name in ('g', 'goto', 'G', 'GOTO', 'gOtO'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):   
            sc(f'{name} 1')  # Missing second argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2 3')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 invalid')
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid 2')
    
        assert sc(f'{name} 1 2') == 1
        assert pos() == (1, 2)
        assert sc(f'{name} -3 -4') == 1
        assert pos() == (-3, -4)
        assert sc(f'{name} 0 0') == 1
        assert pos() == (0, 0)
        assert sc(f'{name} 0.5 0.5') == 1   
        assert pos() == (0.5, 0.5)
        assert sc(f'{name} -0.5 -0.5') == 1
        assert pos() == (-0.5, -0.5)


def test_tele():
    for name in ('tele', 'TELE', 'tElE', 'teleport', 'TELEPORT', 'tElEpOrT'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):   
            sc(f'{name} 1')  # Missing second argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2 3')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 invalid')
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid 2')
    
        assert sc(f'{name} 1 2') == 1
        assert pos() == (1, 2)
        assert sc(f'{name} -3 -4') == 1
        assert pos() == (-3, -4)
        assert sc(f'{name} 0 0') == 1
        assert pos() == (0, 0)
        assert sc(f'{name} 0.5 0.5') == 1   
        assert pos() == (0.5, 0.5)
        assert sc(f'{name} -0.5 -0.5') == 1
        assert pos() == (-0.5, -0.5)


def test_setx():
    for name in ('x', 'setx', 'X', 'SETX', 'sEtX'):
        reset()

        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument

        assert sc(f'{name} 1') == 1
        assert pos() == (1, 0)
        assert sc(f'{name} -2') == 1
        assert pos() == (-2, 0)
        assert sc(f'{name} 0.5') == 1
        assert pos() == (0.5, 0)
        assert sc(f'{name} -0.5') == 1
        assert pos() == (-0.5, 0)

        sety(10)
        assert sc(f'{name} 1') == 1
        assert pos() == (1, 10)


def test_sety():
    for name in ('y', 'sety', 'Y', 'SETY', 'sEtY'):
        reset()

        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument

        assert sc(f'{name} 1') == 1
        assert pos() == (0, 1)
        assert sc(f'{name} -2') == 1
        assert pos() == (0, -2)
        assert sc(f'{name} 0.5') == 1
        assert pos() == (0, 0.5)
        assert sc(f'{name} -0.5') == 1
        assert pos() == (0, -0.5)

        setx(10)
        assert sc(f'{name} 1') == 1
        assert pos() == (10, 1)  
        


def test_pendown():
    for name in ('pd', 'pendown', 'PD', 'PENDOWN', 'pEnDoWn'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments
        
        penup()
        assert sc(f'{name}') == 1
        assert isdown()
        
        
def test_penup():
    for name in ('pu', 'penup', 'PU', 'PENUP', 'pEnUp'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments
        
        pendown()
        assert sc(f'{name}') == 1
        assert not isdown()


def test_pensize():
    for name in ('ps', 'pensize', 'PS', 'PENSIZE', 'pEnSiZe'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        assert sc(f'{name} 10') == 1
        assert pensize() == 10

        assert sc(f'{name} 1.5') == 1
        assert pensize() == 1.5

        pensize(1)


def test_stamp():
    for name in ('st', 'stamp', 'ST', 'STAMP', 'sTaMp'):
        reset()

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments

        assert sc(f'{name}') == 1


def test_pencolor_fillcolor_bgcolor():
    for name in ('pc', 'pencolor', 'PC', 'PENCOLOR', 'pEnCoLoR', 'fc', 'fillcolor', 'FC', 'FILLCOLOR', 'fIlLcOlOr', 'bc', 'bgcolor', 'BC', 'BGCOLOR', 'bGcOlOr'):
        function_to_test = None
        if name.lower().startswith('p'):
            function_to_test = pencolor
        elif name.lower().startswith('f'):
            function_to_test = fillcolor
        elif name.lower().startswith('b'):
            function_to_test = bgcolor
            
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} FF0000')  # Missing the leading # for hex colors

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid 0 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 invalid 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 0 invalid')  # Invalid argument


        colormode(1.0)  # Set to 1.0 for testing

        function_to_test('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert function_to_test() == 'red'

        function_to_test('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert function_to_test() == 'red'

        function_to_test('black')  # Reset to black
        assert sc(f'{name} 1 0 0') == 1
        assert function_to_test() == (1.0, 0.0, 0.0)

        function_to_test('black')  # Reset to black
        assert sc(f'{name} 1.0 0.0 0.0') == 1
        assert function_to_test() == (1.0, 0.0, 0.0)

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 255 0 0')

        colormode(1.0)
        assert function_to_test() != (0, 255, 0)  # Make sure it's not returning a 255 mode value.

        for color_mode_setting in (255, 1.0):
            colormode(color_mode_setting)
            for color_name in 'black blue brown orange gray grey green purple violet pink yellow white red magenta cyan'.split():
                assert sc(f'{name} {color_name}') == 1  # Set the color
                assert function_to_test() == color_name  # Test that the color was set
        
        colormode(255)
        assert sc(f'{name} #FF0000') == 1
        assert function_to_test() == (255, 0, 0.0)

        colormode(1)
        assert sc(f'{name} #FF0000') == 1
        assert function_to_test() == (1, 0, 0.0)

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} xxyyzz')  # Invalid color name



def test_circle():
    for name in ('cir', 'circle', 'CIR', 'CIRCLE', 'cIrClE'):
        reset()

        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument

        # The (int(pos()[0]), int(pos()[1])) stuff is because Vec2D objects 
        # returned from pos() consider (-0.00, -0.00) as not equal to (0, 0).

        assert sc(f'{name} 1') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        assert sc(f'{name} 10') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        assert sc(f'{name} 10.5') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        assert sc(f'{name} -1') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        assert sc(f'{name} -10') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        assert sc(f'{name} -10.5') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        assert sc(f'{name} 0') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)
        

def test_undo():
    for name in ('undo', 'UNDO', 'uNdO'):
        reset()

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments

        assert sc(f'{name}') == 1


def test_begin_fill_end():
    for name in ('bf', 'begin_fill', 'BF', 'BEGIN_FILL', 'bEgIn_FiLl'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments

        assert sc(f'{name}') == 1
        end_fill()


def test_end_fill():
    for name in ('ef', 'end_fill', 'EF', 'END_FILL', 'eNd_FiLl'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments
        
        begin_fill()
        assert sc(f'{name}') == 1


def test_reset():
    for name in ('reset', 'RESET', 'rEsEt'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments
        
        assert sc(f'{name}') == 1


def test_sleep_sc():
    for name in ('sleep', 'SLEEP', 'sLeEp'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')




def test_move_turn():
    # Test the move and turn commands:

    # Test home/h:
    goto(1, 0)
    assert sc('h') == 1
    assert (int(pos()[0]), int(pos()[1])) == (0, 0)

    goto(1, 0)
    assert sc('home') == 1
    assert (int(pos()[0]), int(pos()[1])) == (0, 0)

    with pytest.raises(TurtleShortcutException):
        sc('h 1')

    # Test f/b forward/backward l/r left/right:
    assert sc('f 1') == 1
    assert (int(pos()[0]), int(pos()[1])) == (1, 0)

    assert sc('forward 1') == 1
    assert (int(pos()[0]), int(pos()[1])) == (2, 0)

    assert sc('b 1') == 1
    assert (int(pos()[0]), int(pos()[1])) == (1, 0)

    assert sc('backward 1') == 1
    assert (int(pos()[0]), int(pos()[1])) == (0, 0)

    assert sc('l 90') == 1
    assert heading() == 90

    assert sc('left 90') == 1
    assert heading() == 180

    assert sc('r 90') == 1
    assert heading() == 90

    assert sc('right 90') == 1
    assert heading() == 0

    assert sc('sh 42') == 1
    assert heading() == 42
    assert sc('sh 0') == 1
    assert heading() == 0

    assert sc('f -1') == 1
    assert (int(pos()[0]), int(pos()[1])) == (-1, 0)

    assert sc('b -1') == 1
    assert (int(pos()[0]), int(pos()[1])) == (0, 0)

    assert sc('l -90') == 1
    assert heading() == 270

    assert sc('r -90') == 1
    assert heading() == 0

    assert sc('r 0') == 1
    assert heading() == 0

    assert sc('r 360') == 1
    assert heading() == 0

    assert sc('r 720') == 1
    assert heading() == 0

    assert sc('r -360') == 1
    assert heading() == 0

    assert sc('r -720') == 1
    assert heading() == 0

    assert sc('l 0') == 1
    assert heading() == 0
    
    assert sc('l 360') == 1
    assert heading() == 0

    assert sc('l 720') == 1
    assert heading() == 0

    assert sc('l -360') == 1
    assert heading() == 0

    assert sc('l -720') == 1
    assert heading() == 0

    assert sc('c') == 1
    assert sc('clear') == 1

    # Test g and goto:
    assert sc('g 10 20') == 1
    assert (int(pos()[0]), int(pos()[1])) == (10, 20)

    assert sc('goto -30 -40') == 1
    assert (int(pos()[0]), int(pos()[1])) == (-30, -40)

    with pytest.raises(TurtleShortcutException):
        sc('goto 10')

    with pytest.raises(TurtleShortcutException):
        sc('goto 10 invalid')
    
    with pytest.raises(TurtleShortcutException):
        sc('goto invalid 20')
    
    with pytest.raises(TurtleShortcutException):
        sc('goto invalid invalid')
    
    with pytest.raises(TurtleShortcutException):
        sc('g')

    assert sc('x 100') == 1
    assert (int(pos()[0]), int(pos()[1])) == (100, -40)

    assert sc('y 200') == 1
    assert (int(pos()[0]), int(pos()[1])) == (100, 200)

    assert sc('setx 300') == 1
    assert (int(pos()[0]), int(pos()[1])) == (300, 200)

    assert sc('sety 400') == 1
    assert (int(pos()[0]), int(pos()[1])) == (300, 400)

    with pytest.raises(TurtleShortcutException):
        sc('setx invalid')
    
    with pytest.raises(TurtleShortcutException):
        sc('sety invalid')
    
    with pytest.raises(TurtleShortcutException):
        sc('x invalid')

    with pytest.raises(TurtleShortcutException):
        sc('y invalid')

def test_cardinal_directions_nsew():
    # Test calling a function while in radians mode:
    reset()
    radians()
    assert sc(f'n 100') == 1
    assert (int(pos()[0]), int(pos()[1])) == (0, 100)
    degrees()

    for n, s, e, w, nw, ne, sw, se in ('n s e w nw ne sw se'.split(), 
                                       'north south east west northwest northeast southwest southeast'.split(),
                                       'N S E W NW NE SW SE'.split(),
                                       'NORTH SOUTH EAST WEST NORTHWEST NORTHEAST SOUTHWEST SOUTHEAST'.split()):
        reset()
        assert sc(f'{n} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 100)
        assert sc(f'{n} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{s} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, -100)
        assert sc(f'{s} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{e} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (100, 0)
        assert sc(f'{e} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{w} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (-100, 0)
        assert sc(f'{w} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{nw} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (-70, 70)
        assert sc(f'{nw} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{ne} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (70, 70)
        assert sc(f'{ne} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{sw} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (-70, -70)
        assert sc(f'{sw} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)

        reset()
        assert sc(f'{se} 100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (70, -70)
        assert sc(f'{se} -100') == 1
        assert (int(pos()[0]), int(pos()[1])) == (0, 0)


def test_sleep():
    with pytest.raises(TurtleShortcutException):
        sc('sleep')  # Missing argument
    with pytest.raises(TurtleShortcutException):
        sc('sleep 1 2')  # Too many arguments
    with pytest.raises(TurtleShortcutException):
        sc('sleep invalid')  # Invalid argument

    assert sc('sleep 1') == 1
    assert sc('sleep 0.1') == 1

def test_tracer_update():
    orig_tracer = tracer()
    orig_delay = delay()

    for name in ('t', 'T', 'tracer', 'TRACER', 'tRaCeR'):
        with pytest.raises(TurtleShortcutException):
            sc('{name}') # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc('{name} 1 2 3') # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc('{name} invalid 0')
        with pytest.raises(TurtleShortcutException):
            sc('{name} 0 invalid')

        assert sc(f'{name} 123 1') == 1
        assert tracer() == 123
        assert delay() == 1

    for name in ('u', 'U', 'update', 'UPDATE', 'uPdAtE'):
        with pytest.raises(TurtleShortcutException):
            sc('{name} 1') # Too many arguments
        
        assert sc(f'{name}') == 1

    tracer(orig_tracer, orig_delay)


def test_show_hide():
    for name in ('show', 'SHOW', 'sHoW'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments
        
        assert sc(f'{name}') == 1
        assert isvisible()

    for name in ('hide', 'HIDE', 'hIdE'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1')  # Too many arguments
        
        assert sc(f'{name}') == 1
        assert not isvisible()


def test_dot():
    for name in ('dot', 'DOT', 'dOt'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} -1')  # Invalid argument
        

        assert sc(f'{name} 1') == 1
        assert sc(f'{name} 10') == 1
        assert sc(f'{name} 10.5') == 1
        assert sc(f'{name} 0') == 1


def test_clearstamp():
    for name in ('cs', 'clearstamp', 'CS', 'CLEARSTAMP', 'cLeArStAmP'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        stamp_id = stamp()
        assert sc(f'{name} {stamp_id}') == 1


def test_clearstamps():
    for name in ('css', 'clearstamps', 'CSS', 'CLEARSTAMPS', 'cLeArStAmPs'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        assert sc(f'{name} 0') == 1
        assert sc(f'{name} 2') == 1
        assert sc(f'{name} -2') == 1
        assert sc(f'{name}') == 1

def test_speed():
    for name in ('speed', 'SPEED', 'sPeEd'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Too many arguments
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid')  # Invalid argument
        
        # Test numeric settings 0 to 10:
        for speed_setting in tuple(range(11)):
            assert sc(f'{name} {speed_setting}') == 1
            assert speed() == speed_setting
        # Test string settings:
        for speed_setting, numeric_equivalent in {'fastest': 0, 'fast': 10, 'normal': 6, 'slow': 3, 'slowest': 1, 'FASTEST': 0, 'FAST': 10, 'NORMAL': 6, 'SLOW': 3, 'SLOWEST': 1}.items():
            assert sc(f'{name} {speed_setting}') == 1
            assert speed() == numeric_equivalent
        
        tracer(10000, 0)  # Restore the original tracer settings for other tests.

        
def test_scs():
    assert scs('f 100') == 'forward(100)\n'
    assert scs('b 100') == 'backward(100)\n'
    assert scs('l 90') == 'left(90)\n'
    assert scs('r 90') == 'right(90)\n'
    assert scs('g 100 200') == 'goto(100, 200)\n'
    assert scs('sh 90') == 'setheading(90)\n'
    assert scs('pu') == 'penup()\n'
    assert scs('pd') == 'pendown()\n'
    assert scs('ps 10') == 'pensize(10)\n'
    assert scs('bf') == 'begin_fill()\n'
    assert scs('ef') == 'end_fill()\n'
    assert scs('reset') == 'reset()\n'
    assert scs('sleep 1') == 'sleep(1)\n'
    assert scs('t 100 0') == 'tracer(100, 0)\n'
    assert scs('u') == 'update()\n'
    assert scs('show') == 'showturtle()\n'
    assert scs('hide') == 'hideturtle()\n'
    assert scs('dot 10') == 'dot(10)\n'
    assert scs('cs 1') == 'clearstamp(1)\n'
    assert scs('css') == 'clearstamps()\n'
    assert scs('css 1') == 'clearstamps(1)\n'
    assert scs('st') == 'stamp()\n'
    assert scs('speed 1') == 'speed(1)\n'
    assert scs('home') == 'home()\n'
    assert scs('x 100') == 'setx(100)\n'
    assert scs('y 100') == 'sety(100)\n'
    assert scs('setx 100') == 'setx(100)\n'
    assert scs('sety 100') == 'sety(100)\n'
    assert scs('c') == 'clear()\n'
    assert scs('undo') == 'undo()\n'
    assert scs('cir 100') == 'circle(100)\n'
    assert scs('g 100 200') == 'goto(100, 200)\n'
    assert scs('tele 100 200') == 'teleport(100, 200)\n'

    assert scs('pc red') == "pencolor('red')\n"
    assert scs('fc red') == "fillcolor('red')\n"
    assert scs('bc red') == "bgcolor('red')\n"

    colormode(255)
    assert scs('pc red') == "pencolor('red')\n"
    assert scs('pc 255 0 0') == 'pencolor((255, 0, 0))\n'
    assert scs('fc 255 0 0') == 'fillcolor((255, 0, 0))\n'
    assert scs('bc 255 0 0') == 'bgcolor((255, 0, 0))\n'
    
    colormode(1.0)
    assert scs('pc red') == "pencolor('red')\n"
    with pytest.raises(TurtleShortcutException):
        scs('pc 255 0 0')
    with pytest.raises(TurtleShortcutException):
        scs('fc 255 0 0')
    with pytest.raises(TurtleShortcutException):
        scs('bc 255 0 0')

    assert scs('pc 1.0 0.0 0.0') == 'pencolor((1.0, 0.0, 0.0))\n'
    assert scs('fc 1.0 0.0 0.0') == 'fillcolor((1.0, 0.0, 0.0))\n'
    assert scs('bc 1.0 0.0 0.0') == 'bgcolor((1.0, 0.0, 0.0))\n'
    
    degrees()
    assert scs('n 100') == 'setheading(90)\nforward(100)\n'
    assert scs('s 100') == 'setheading(270)\nforward(100)\n'
    assert scs('e 100') == 'setheading(0)\nforward(100)\n'
    assert scs('w 100') == 'setheading(180)\nforward(100)\n'
    assert scs('nw 100') == 'setheading(135)\nforward(100)\n'
    assert scs('ne 100') == 'setheading(45)\nforward(100)\n'
    assert scs('sw 100') == 'setheading(225)\nforward(100)\n'
    assert scs('se 100') == 'setheading(315)\nforward(100)\n'
    assert scs('north 100') == 'setheading(90)\nforward(100)\n'
    assert scs('south 100') == 'setheading(270)\nforward(100)\n'
    assert scs('east 100') == 'setheading(0)\nforward(100)\n'
    assert scs('west 100') == 'setheading(180)\nforward(100)\n'
    assert scs('northwest 100') == 'setheading(135)\nforward(100)\n'
    assert scs('northeast 100') == 'setheading(45)\nforward(100)\n'
    assert scs('southwest 100') == 'setheading(225)\nforward(100)\n'
    assert scs('southeast 100') == 'setheading(315)\nforward(100)\n'
    assert scs('N 100') == 'setheading(90)\nforward(100)\n'
    assert scs('S 100') == 'setheading(270)\nforward(100)\n'
    assert scs('E 100') == 'setheading(0)\nforward(100)\n'
    assert scs('W 100') == 'setheading(180)\nforward(100)\n'
    assert scs('NW 100') == 'setheading(135)\nforward(100)\n'
    assert scs('NE 100') == 'setheading(45)\nforward(100)\n'
    assert scs('SW 100') == 'setheading(225)\nforward(100)\n'
    assert scs('SE 100') == 'setheading(315)\nforward(100)\n'
    assert scs('NORTH 100') == 'setheading(90)\nforward(100)\n'
    assert scs('SOUTH 100') == 'setheading(270)\nforward(100)\n'
    assert scs('EAST 100') == 'setheading(0)\nforward(100)\n'
    assert scs('WEST 100') == 'setheading(180)\nforward(100)\n'
    assert scs('NORTHWEST 100') == 'setheading(135)\nforward(100)\n'
    assert scs('NORTHEAST 100') == 'setheading(45)\nforward(100)\n'
    assert scs('SOUTHWEST 100') == 'setheading(225)\nforward(100)\n'
    assert scs('SOUTHEAST 100') == 'setheading(315)\nforward(100)\n'
    assert scs('n 100, f 100') == 'setheading(90)\nforward(100)\nforward(100)\n'
    assert scs('n 100, f 100, f 100') == 'setheading(90)\nforward(100)\nforward(100)\nforward(100)\n'

    radians()
    assert scs('n 100') == 'degrees()\nsetheading(90)\nforward(100)\nradians()\n'
    assert scs('s 100') == 'degrees()\nsetheading(270)\nforward(100)\nradians()\n'
    assert scs('e 100') == 'degrees()\nsetheading(0)\nforward(100)\nradians()\n'
    assert scs('w 100') == 'degrees()\nsetheading(180)\nforward(100)\nradians()\n'
    assert scs('nw 100') == 'degrees()\nsetheading(135)\nforward(100)\nradians()\n'
    assert scs('ne 100') == 'degrees()\nsetheading(45)\nforward(100)\nradians()\n'
    assert scs('sw 100') == 'degrees()\nsetheading(225)\nforward(100)\nradians()\n'
    assert scs('se 100') == 'degrees()\nsetheading(315)\nforward(100)\nradians()\n'

    degrees()


def test_psc(capsys):
    psc('f 100')
    assert capsys.readouterr().out == 'forward(100)\n'
    psc('b 100')
    assert capsys.readouterr().out == 'backward(100)\n'
    psc('l 90')
    assert capsys.readouterr().out == 'left(90)\n'
    psc('r 90')
    assert capsys.readouterr().out == 'right(90)\n'
    psc('g 100 200')
    assert capsys.readouterr().out == 'goto(100, 200)\n'
    psc('sh 90')
    assert capsys.readouterr().out == 'setheading(90)\n'
    psc('pu')
    assert capsys.readouterr().out == 'penup()\n'
    psc('pd')
    assert capsys.readouterr().out == 'pendown()\n'
    psc('ps 10')
    assert capsys.readouterr().out == 'pensize(10)\n'
    psc('bf')
    assert capsys.readouterr().out == 'begin_fill()\n'
    psc('ef')
    assert capsys.readouterr().out == 'end_fill()\n'
    psc('reset')
    assert capsys.readouterr().out == 'reset()\n'
    psc('sleep 1')
    assert capsys.readouterr().out == 'sleep(1)\n'
    psc('t 100 0')
    assert capsys.readouterr().out == 'tracer(100, 0)\n'
    psc('u')
    assert capsys.readouterr().out == 'update()\n'
    psc('show')
    assert capsys.readouterr().out == 'showturtle()\n'
    psc('hide')
    assert capsys.readouterr().out == 'hideturtle()\n'
    psc('dot 10')
    assert capsys.readouterr().out == 'dot(10)\n'
    psc('cs 1')
    assert capsys.readouterr().out == 'clearstamp(1)\n'
    psc('css')
    assert capsys.readouterr().out == 'clearstamps()\n'
    psc('css 1')
    assert capsys.readouterr().out == 'clearstamps(1)\n'
    psc('st')
    assert capsys.readouterr().out == 'stamp()\n'
    psc('speed 1')
    assert capsys.readouterr().out == 'speed(1)\n'
    psc('home')
    assert capsys.readouterr().out == 'home()\n'
    psc('x 100')
    assert capsys.readouterr().out == 'setx(100)\n'
    psc('y 100')
    assert capsys.readouterr().out == 'sety(100)\n'
    psc('setx 100')
    assert capsys.readouterr().out == 'setx(100)\n'
    psc('sety 100')
    assert capsys.readouterr().out == 'sety(100)\n'
    psc('c')
    assert capsys.readouterr().out == 'clear()\n'
    psc('undo')
    assert capsys.readouterr().out == 'undo()\n'
    psc('cir 100')
    assert capsys.readouterr().out == 'circle(100)\n'
    psc('g 100 200')
    assert capsys.readouterr().out == 'goto(100, 200)\n'
    psc('tele 100 200')
    assert capsys.readouterr().out == 'teleport(100, 200)\n'

    psc('pc red')
    assert capsys.readouterr().out == "pencolor('red')\n"
    psc('fc red')
    assert capsys.readouterr().out == "fillcolor('red')\n"
    psc('bc red')
    assert capsys.readouterr().out == "bgcolor('red')\n"

    colormode(255)
    psc('pc red')
    assert capsys.readouterr().out == "pencolor('red')\n"
    psc('pc 255 0 0')
    assert capsys.readouterr().out == 'pencolor((255, 0, 0))\n'
    psc('fc 255 0 0')
    assert capsys.readouterr().out == 'fillcolor((255, 0, 0))\n'
    psc('bc 255 0 0')
    assert capsys.readouterr().out == 'bgcolor((255, 0, 0))\n'
    
    colormode(1.0)
    psc('pc red')
    assert capsys.readouterr().out == "pencolor('red')\n"
    with pytest.raises(TurtleShortcutException):
        psc('pc 255 0 0')
    with pytest.raises(TurtleShortcutException):
        psc('fc 255 0 0')
    with pytest.raises(TurtleShortcutException):
        psc('bc 255 0 0')

    psc('pc 1.0 0.0 0.0')
    assert capsys.readouterr().out == 'pencolor((1.0, 0.0, 0.0))\n'
    psc('fc 1.0 0.0 0.0')
    assert capsys.readouterr().out == 'fillcolor((1.0, 0.0, 0.0))\n'
    psc('bc 1.0 0.0 0.0')
    assert capsys.readouterr().out == 'bgcolor((1.0, 0.0, 0.0))\n'
    
    degrees()
    psc('n 100')
    assert capsys.readouterr().out == 'setheading(90)\nforward(100)\n'
    psc('s 100')
    assert capsys.readouterr().out == 'setheading(270)\nforward(100)\n'
    psc('e 100')
    assert capsys.readouterr().out == 'setheading(0)\nforward(100)\n'
    psc('w 100')
    assert capsys.readouterr().out == 'setheading(180)\nforward(100)\n'
    psc('nw 100')
    assert capsys.readouterr().out == 'setheading(135)\nforward(100)\n'
    psc('ne 100')
    assert capsys.readouterr().out == 'setheading(45)\nforward(100)\n'
    psc('sw 100')
    assert capsys.readouterr().out == 'setheading(225)\nforward(100)\n'
    psc('se 100')
    assert capsys.readouterr().out == 'setheading(315)\nforward(100)\n'
    psc('north 100')
    assert capsys.readouterr().out == 'setheading(90)\nforward(100)\n'
    psc('south 100')
    assert capsys.readouterr().out == 'setheading(270)\nforward(100)\n'
    psc('east 100')
    assert capsys.readouterr().out == 'setheading(0)\nforward(100)\n'
    psc('west 100')
    assert capsys.readouterr().out == 'setheading(180)\nforward(100)\n'
    psc('northwest 100')
    assert capsys.readouterr().out == 'setheading(135)\nforward(100)\n'
    psc('northeast 100')
    assert capsys.readouterr().out == 'setheading(45)\nforward(100)\n'
    psc('southwest 100')
    assert capsys.readouterr().out == 'setheading(225)\nforward(100)\n'
    psc('southeast 100')
    assert capsys.readouterr().out == 'setheading(315)\nforward(100)\n'
    psc('N 100')
    assert capsys.readouterr().out == 'setheading(90)\nforward(100)\n'
    psc('S 100')
    assert capsys.readouterr().out == 'setheading(270)\nforward(100)\n'
    psc('E 100')
    assert capsys.readouterr().out == 'setheading(0)\nforward(100)\n'
    psc('W 100')
    assert capsys.readouterr().out == 'setheading(180)\nforward(100)\n'
    psc('NW 100')
    assert capsys.readouterr().out == 'setheading(135)\nforward(100)\n'
    psc('NE 100')
    assert capsys.readouterr().out == 'setheading(45)\nforward(100)\n'
    psc('SW 100')
    assert capsys.readouterr().out == 'setheading(225)\nforward(100)\n'
    psc('SE 100')
    assert capsys.readouterr().out == 'setheading(315)\nforward(100)\n'
    psc('NORTH 100')
    assert capsys.readouterr().out == 'setheading(90)\nforward(100)\n'
    psc('SOUTH 100')
    assert capsys.readouterr().out == 'setheading(270)\nforward(100)\n'
    psc('EAST 100')
    assert capsys.readouterr().out == 'setheading(0)\nforward(100)\n'
    psc('WEST 100')
    assert capsys.readouterr().out == 'setheading(180)\nforward(100)\n'
    psc('NORTHWEST 100')
    assert capsys.readouterr().out == 'setheading(135)\nforward(100)\n'
    psc('NORTHEAST 100')
    assert capsys.readouterr().out == 'setheading(45)\nforward(100)\n'
    psc('SOUTHWEST 100')
    assert capsys.readouterr().out == 'setheading(225)\nforward(100)\n'
    psc('SOUTHEAST 100')
    assert capsys.readouterr().out == 'setheading(315)\nforward(100)\n'
    psc('n 100, f 100')
    assert capsys.readouterr().out == 'setheading(90)\nforward(100)\nforward(100)\n'
    psc('n 100, f 100, f 100')
    assert capsys.readouterr().out == 'setheading(90)\nforward(100)\nforward(100)\nforward(100)\n'

    radians()
    psc('n 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(90)\nforward(100)\nradians()\n'
    psc('s 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(270)\nforward(100)\nradians()\n'
    psc('e 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(0)\nforward(100)\nradians()\n'
    psc('w 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(180)\nforward(100)\nradians()\n'
    psc('nw 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(135)\nforward(100)\nradians()\n'
    psc('ne 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(45)\nforward(100)\nradians()\n'
    psc('sw 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(225)\nforward(100)\nradians()\n'
    psc('se 100')
    assert capsys.readouterr().out == 'degrees()\nsetheading(315)\nforward(100)\nradians()\n'

    degrees()


def test_skip(capsys):
    turtle.home()
    assert sc('f 100', skip=True) == 0
    assert turtle.pos() == (0, 0)
    assert sc('f 100', skip=True, _return_turtle_code=True) == ()
    

def test_comment():
    assert sc('# ignore 123 abc') == 0
    assert sc('f 100, # ignore this') == 1
    assert sc('f 100, # ignore this, b 100') == 2
    assert sc('f 100, # ignore this, b 100, # ignore this') == 2
    assert sc('f 100, # ignore this, b 100, # ignore this, f 100') == 3

    assert scs('# ignore this') == '# ignore this\n'
    assert scs('f 100, # ignore this') == 'forward(100)\n# ignore this\n'
    assert scs('f 100,          # ignore this') == 'forward(100)\n# ignore this\n'


def test_recording():
    begin_recording()
    assert RECORDED_SHORTCUTS == []
    assert sc('f 100, l 90, f 100, l 90, # foobar, f 100') == 5
    assert end_recording() == ['f 100', 'l 90', 'f 100', 'l 90', '# foobar', 'f 100']
    begin_recording()
    assert RECORDED_SHORTCUTS == []
    


# EXAMPLE PROGRAMS:

def test_colorful_squares():
    colormode(1.0)
    sc('t 1000 0, ps 4')

    for i in range(100):  # Draw 100 squares.
        # Move to a random place:
        sc(f'pu,g {randint(-400, 200)} {randint(-400, 200)},pd,fc {random()} {random()} {random()}, pc {random()} {random()} {random()}')
        line_length = randint(20, 200)

        # Draw the filled-in square:
        sc('bf')
        for j in range(4):
            sc(f'f {line_length}, l 90')
        sc('ef')

    sc('u,reset')


def test_draw_circles():
    sc('t 1000 0, ps 1')

    # Draw circle in the top half of the window:
    sc('sh 0')  # Face right.
    for i in range(20):
        sc(f'cir {i * 10}')

    # Draw circles in the bottom half of the window:
    sc('sh 180')  # Face left.
    for i in range(20):
        sc(f'cir {i * 10}')
    sc('u,reset')


def test_curve_path_filled():
    sc('t 1000 0, ps 1')
    colormode(1.0)
    for i in range(50):
        sc(f'fc {random()} {random()} {random()}')

        # Set a random heading and draw several short lines with changing direction:
        sc(f'sh {randint(0, 360)}, bf')

        for j in range(randint(200, 600)):
            sc(f'f 1,l {randint(-4, 4)}')
        sc(f'h, ef')
    sc('u,reset')


def test_merge_shortcuts():
    assert merge_shortcuts([]) == []

    assert merge_shortcuts(['f 100']) == ['f 100']
    assert merge_shortcuts(['f 100', 'f 100']) == ['f 200']
    assert merge_shortcuts(['f 100', 'f 100', 'f 100']) == ['f 300']
    assert merge_shortcuts(['f 100', 'b 25']) == ['f 100', 'b 25']
    assert merge_shortcuts(['pu', 'f 100', 'b 25']) == ['pu', 'f 75']
    assert merge_shortcuts(['pd', 'f 100', 'b 25']) == ['pd', 'f 100', 'b 25']

    assert merge_shortcuts(['b 100']) == ['b 100']
    assert merge_shortcuts(['b 100', 'b 100']) == ['b 200']
    assert merge_shortcuts(['b 100', 'b 100', 'b 100']) == ['b 300']
    assert merge_shortcuts(['b 100', 'f 25']) == ['b 100', 'f 25']
    assert merge_shortcuts(['pu', 'b 100', 'f 25']) == ['pu', 'b 75']
    assert merge_shortcuts(['pd', 'b 100', 'f 25']) == ['pd', 'b 100', 'f 25']
    
    assert merge_shortcuts(['l 100']) == ['l 100']
    assert merge_shortcuts(['l 100', 'l 100']) == ['l 200']
    assert merge_shortcuts(['l 100', 'l 100', 'l 100']) == ['l 300']
    assert merge_shortcuts(['l 100', 'r 25']) == ['l 75']
    assert merge_shortcuts(['pu', 'l 100', 'r 25']) == ['pu', 'l 75']
    assert merge_shortcuts(['pd', 'l 100', 'r 25']) == ['pd', 'l 75']
    
    assert merge_shortcuts(['r 100']) == ['r 100']
    assert merge_shortcuts(['r 100', 'r 100']) == ['r 200']
    assert merge_shortcuts(['r 100', 'r 100', 'r 100']) == ['r 300']
    assert merge_shortcuts(['r 100', 'l 25']) == ['r 75']
    assert merge_shortcuts(['pu', 'r 100', 'l 25']) == ['pu', 'r 75']
    assert merge_shortcuts(['pd', 'r 100', 'l 25']) == ['pd', 'r 75']

    

    assert merge_shortcuts(['f 1.5']) == ['f 1.5']
    assert merge_shortcuts(['f 1.5', 'f 1.5']) == ['f 3']
    assert merge_shortcuts(['f 1.5', 'f 1.5', 'f 1.5']) == ['f 4.5']

    assert merge_shortcuts(['b 1.5']) == ['b 1.5']
    assert merge_shortcuts(['b 1.5', 'b 1.5']) == ['b 3']
    assert merge_shortcuts(['b 1.5', 'b 1.5', 'b 1.5']) == ['b 4.5']

    assert merge_shortcuts(['l 1.5']) == ['l 1.5']
    assert merge_shortcuts(['l 1.5', 'l 1.5']) == ['l 3']
    assert merge_shortcuts(['l 1.5', 'l 1.5', 'l 1.5']) == ['l 4.5']

    assert merge_shortcuts(['r 1.5']) == ['r 1.5']
    assert merge_shortcuts(['r 1.5', 'r 1.5']) == ['r 3']
    assert merge_shortcuts(['r 1.5', 'r 1.5', 'r 1.5']) == ['r 4.5']

    assert merge_shortcuts(['n 1.5']) == ['n 1.5']
    assert merge_shortcuts(['n 1.5', 'n 1.5']) == ['n 3']
    assert merge_shortcuts(['n 1.5', 'n 1.5', 'n 1.5']) == ['n 4.5']

    assert merge_shortcuts(['s 1.5']) == ['s 1.5']
    assert merge_shortcuts(['s 1.5', 's 1.5']) == ['s 3']
    assert merge_shortcuts(['s 1.5', 's 1.5', 's 1.5']) == ['s 4.5']

    assert merge_shortcuts(['w 1.5']) == ['w 1.5']
    assert merge_shortcuts(['w 1.5', 'w 1.5']) == ['w 3']
    assert merge_shortcuts(['w 1.5', 'w 1.5', 'w 1.5']) == ['w 4.5']

    assert merge_shortcuts(['e 1.5']) == ['e 1.5']
    assert merge_shortcuts(['e 1.5', 'e 1.5']) == ['e 3']
    assert merge_shortcuts(['e 1.5', 'e 1.5', 'e 1.5']) == ['e 4.5']

    assert merge_shortcuts(['nw 1.5']) == ['nw 1.5']
    assert merge_shortcuts(['nw 1.5', 'nw 1.5']) == ['nw 3']
    assert merge_shortcuts(['nw 1.5', 'nw 1.5', 'nw 1.5']) == ['nw 4.5']

    assert merge_shortcuts(['ne 1.5']) == ['ne 1.5']
    assert merge_shortcuts(['ne 1.5', 'ne 1.5']) == ['ne 3']
    assert merge_shortcuts(['ne 1.5', 'ne 1.5', 'ne 1.5']) == ['ne 4.5']

    assert merge_shortcuts(['sw 1.5']) == ['sw 1.5']
    assert merge_shortcuts(['sw 1.5', 'sw 1.5']) == ['sw 3']
    assert merge_shortcuts(['sw 1.5', 'sw 1.5', 'sw 1.5']) == ['sw 4.5']

    assert merge_shortcuts(['se 1.5']) == ['se 1.5']
    assert merge_shortcuts(['se 1.5', 'se 1.5']) == ['se 3']
    assert merge_shortcuts(['se 1.5', 'se 1.5', 'se 1.5']) == ['se 4.5']

    assert merge_shortcuts(['h', 'h', 'h']) == ['h']
    assert merge_shortcuts(['pd', 'pd', 'pd']) == ['pd']
    assert merge_shortcuts(['pu', 'pu', 'pu']) == ['pu']
    


if __name__ == '__main__':
    pytest.main()











