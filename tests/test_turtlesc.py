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
                assert sc(f'{name} {color_name}') == 1
                assert function_to_test() == color_name
        
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

        
def test_get_turtle_code():
    assert get_turtle_code('f 100') == ('forward(100)',)
    assert get_turtle_code('b 100') == ('backward(100)',)
    assert get_turtle_code('l 90') == ('left(90)',)
    assert get_turtle_code('r 90') == ('right(90)',)
    assert get_turtle_code('g 100 200') == ('goto(100, 200)',)
    assert get_turtle_code('sh 90') == ('setheading(90)',)
    assert get_turtle_code('pu') == ('penup()',)
    assert get_turtle_code('pd') == ('pendown()',)
    assert get_turtle_code('ps 10') == ('pensize(10)',)
    assert get_turtle_code('bf') == ('begin_fill()',)
    assert get_turtle_code('ef') == ('end_fill()',)
    assert get_turtle_code('reset') == ('reset()',)
    assert get_turtle_code('sleep 1') == ('sleep(1)',)
    assert get_turtle_code('t 100 0') == ('tracer(100, 0)',)
    assert get_turtle_code('u') == ('update()',)
    assert get_turtle_code('show') == ('showturtle()',)
    assert get_turtle_code('hide') == ('hideturtle()',)
    assert get_turtle_code('dot 10') == ('dot(10)',)
    assert get_turtle_code('cs 1') == ('clearstamp(1)',)
    assert get_turtle_code('css') == ('clearstamps()',)
    assert get_turtle_code('css 1') == ('clearstamps(1)',)
    assert get_turtle_code('st') == ('stamp()',)
    assert get_turtle_code('speed 1') == ('speed(1)',)
    assert get_turtle_code('home') == ('home()',)
    assert get_turtle_code('x 100') == ('setx(100)',)
    assert get_turtle_code('y 100') == ('sety(100)',)
    assert get_turtle_code('setx 100') == ('setx(100)',)
    assert get_turtle_code('sety 100') == ('sety(100)',)
    assert get_turtle_code('c') == ('clear()',)
    assert get_turtle_code('undo') == ('undo()',)
    assert get_turtle_code('cir 100') == ('circle(100)',)
    assert get_turtle_code('g 100 200') == ('goto(100, 200)',)
    assert get_turtle_code('tele 100 200') == ('teleport(100, 200)',)

    assert get_turtle_code('pc red') == ("pencolor('red')",)
    assert get_turtle_code('fc red') == ("fillcolor('red')",)
    assert get_turtle_code('bc red') == ("bgcolor('red')",)

    colormode(255)
    assert get_turtle_code('pc red') == ("pencolor('red')",)
    assert get_turtle_code('pc 255 0 0') == ('pencolor((255, 0, 0))',)
    assert get_turtle_code('fc 255 0 0') == ('fillcolor((255, 0, 0))',)
    assert get_turtle_code('bc 255 0 0') == ('bgcolor((255, 0, 0))',)
    
    colormode(1.0)
    assert get_turtle_code('pc red') == ("pencolor('red')",)
    with pytest.raises(TurtleShortcutException):
        get_turtle_code('pc 255 0 0')
    with pytest.raises(TurtleShortcutException):
        get_turtle_code('fc 255 0 0')
    with pytest.raises(TurtleShortcutException):
        get_turtle_code('bc 255 0 0')

    assert get_turtle_code('pc 1.0 0.0 0.0') == ('pencolor((1.0, 0.0, 0.0))',)
    assert get_turtle_code('fc 1.0 0.0 0.0') == ('fillcolor((1.0, 0.0, 0.0))',)
    assert get_turtle_code('bc 1.0 0.0 0.0') == ('bgcolor((1.0, 0.0, 0.0))',)
    
    
    
    degrees()
    assert get_turtle_code('n 100') == ('setheading(90)', 'forward(100)')
    assert get_turtle_code('s 100') == ('setheading(270)', 'forward(100)')
    assert get_turtle_code('e 100') == ('setheading(0)', 'forward(100)')
    assert get_turtle_code('w 100') == ('setheading(180)', 'forward(100)')
    assert get_turtle_code('nw 100') == ('setheading(135)', 'forward(100)')
    assert get_turtle_code('ne 100') == ('setheading(45)', 'forward(100)')
    assert get_turtle_code('sw 100') == ('setheading(225)', 'forward(100)')
    assert get_turtle_code('se 100') == ('setheading(315)', 'forward(100)')
    assert get_turtle_code('north 100') == ('setheading(90)', 'forward(100)')
    assert get_turtle_code('south 100') == ('setheading(270)', 'forward(100)')
    assert get_turtle_code('east 100') == ('setheading(0)', 'forward(100)')
    assert get_turtle_code('west 100') == ('setheading(180)', 'forward(100)')
    assert get_turtle_code('northwest 100') == ('setheading(135)', 'forward(100)')
    assert get_turtle_code('northeast 100') == ('setheading(45)', 'forward(100)')
    assert get_turtle_code('southwest 100') == ('setheading(225)', 'forward(100)')
    assert get_turtle_code('southeast 100') == ('setheading(315)', 'forward(100)')
    assert get_turtle_code('N 100') == ('setheading(90)', 'forward(100)')
    assert get_turtle_code('S 100') == ('setheading(270)', 'forward(100)')
    assert get_turtle_code('E 100') == ('setheading(0)', 'forward(100)')
    assert get_turtle_code('W 100') == ('setheading(180)', 'forward(100)')
    assert get_turtle_code('NW 100') == ('setheading(135)', 'forward(100)')
    assert get_turtle_code('NE 100') == ('setheading(45)', 'forward(100)')
    assert get_turtle_code('SW 100') == ('setheading(225)', 'forward(100)')
    assert get_turtle_code('SE 100') == ('setheading(315)', 'forward(100)')
    assert get_turtle_code('NORTH 100') == ('setheading(90)', 'forward(100)')
    assert get_turtle_code('SOUTH 100') == ('setheading(270)', 'forward(100)')
    assert get_turtle_code('EAST 100') == ('setheading(0)', 'forward(100)')
    assert get_turtle_code('WEST 100') == ('setheading(180)', 'forward(100)')
    assert get_turtle_code('NORTHWEST 100') == ('setheading(135)', 'forward(100)')
    assert get_turtle_code('NORTHEAST 100') == ('setheading(45)', 'forward(100)')
    assert get_turtle_code('SOUTHWEST 100') == ('setheading(225)', 'forward(100)')
    assert get_turtle_code('SOUTHEAST 100') == ('setheading(315)', 'forward(100)')
    assert get_turtle_code('n 100, f 100') == ('setheading(90)', 'forward(100)', 'forward(100)')
    assert get_turtle_code('n 100, f 100, f 100') == ('setheading(90)', 'forward(100)', 'forward(100)', 'forward(100)')

    radians()
    assert get_turtle_code('n 100') == ('degrees()', 'setheading(90)', 'forward(100)', 'radians()')
    assert get_turtle_code('s 100') == ('degrees()', 'setheading(270)', 'forward(100)', 'radians()')
    assert get_turtle_code('e 100') == ('degrees()', 'setheading(0)', 'forward(100)', 'radians()')
    assert get_turtle_code('w 100') == ('degrees()', 'setheading(180)', 'forward(100)', 'radians()')
    assert get_turtle_code('nw 100') == ('degrees()', 'setheading(135)', 'forward(100)', 'radians()')
    assert get_turtle_code('ne 100') == ('degrees()', 'setheading(45)', 'forward(100)', 'radians()')
    assert get_turtle_code('sw 100') == ('degrees()', 'setheading(225)', 'forward(100)', 'radians()')
    assert get_turtle_code('se 100') == ('degrees()', 'setheading(315)', 'forward(100)', 'radians()')

    degrees()







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


if __name__ == '__main__':
    pytest.main()