import pytest
from turtle import *
from turtlesc import *
from random import *

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


def test_pencolor():
    for name in ('pc', 'pencolor', 'PC', 'PENCOLOR', 'pEnCoLoR'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid 0 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 invalid 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 0 invalid')  # Invalid argument


        colormode(1.0)  # Set to 1.0 for testing

        pencolor('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert pencolor() == 'red'

        pencolor('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert pencolor() == 'red'

        pencolor('black')  # Reset to black
        assert sc(f'{name} 1 0 0') == 1
        assert pencolor() == (1.0, 0.0, 0.0)

        pencolor('black')  # Reset to black
        assert sc(f'{name} 1.0 0.0 0.0') == 1
        assert pencolor() == (1.0, 0.0, 0.0)

        pencolor('black')  # Reset to black
        assert sc(f'{name} 255 0 0') == 1  # Test that temporarily setting colormode to 255 works.
        assert pencolor() == (1.0, 0.0, 0.0)

        colormode(255) # Test that temporarily setting colormode to 1 works.
        assert sc(f'{name} 0 1.0 0') == 1
        colormode(1.0)
        assert pencolor() == (0, 1, 0)

        for color_name in 'black blue brown orange gray grey green purple violet pink yellow white red magenta cyan'.split():
            assert sc(f'{name} {color_name}') == 1
            assert pencolor() == color_name
        
        colormode(255)
        assert sc(f'{name} FF0000') == 1
        assert pencolor() == (255, 0, 0.0)

        colormode(1)
        assert sc(f'{name} FF0000') == 1
        assert pencolor() == (1, 0, 0.0)

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} xxyyzz')  # Invalid color name


def test_fillcolor():
    for name in ('fc', 'fillcolor', 'FC', 'FILLCOLOR', 'fIlLcOlOr'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid 0 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 invalid 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 0 invalid')  # Invalid argument


        colormode(1.0)  # Set to 1.0 for testing

        fillcolor('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert fillcolor() == 'red'

        fillcolor('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert fillcolor() == 'red'

        fillcolor('black')  # Reset to black
        assert sc(f'{name} 1 0 0') == 1
        assert fillcolor() == (1.0, 0.0, 0.0)

        fillcolor('black')  # Reset to black
        assert sc(f'{name} 1.0 0.0 0.0') == 1
        assert fillcolor() == (1.0, 0.0, 0.0)

        pencolor('black')  # Reset to black
        assert sc(f'{name} 255 0 0') == 1  # Test that temporarily setting colormode to 255 works.
        assert fillcolor() == (1.0, 0.0, 0.0)

        colormode(255) # Test that temporarily setting colormode to 1 works.
        assert sc(f'{name} 0 1.0 0') == 1
        colormode(1.0)
        assert fillcolor() == (0, 1, 0)

        for color_name in 'black blue brown orange gray grey green purple violet pink yellow white red magenta cyan'.split():
            assert sc(f'{name} {color_name}') == 1
            assert fillcolor() == color_name

        colormode(255)
        assert sc(f'{name} FF0000') == 1
        assert fillcolor() == (255, 0, 0.0)

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} xxyyzz')  # Invalid color name


def test_bgcolor():
    for name in ('bc', 'bgcolor', 'BC', 'BGCOLOR', 'bGcOlOr'):
        with pytest.raises(TurtleShortcutException):
            sc(f'{name}')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 1 2')  # Missing argument

        with pytest.raises(TurtleShortcutException):
            sc(f'{name} invalid 0 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 invalid 0')  # Invalid argument
        with pytest.raises(TurtleShortcutException):
            sc(f'{name} 0 0 invalid')  # Invalid argument


        colormode(1.0)  # Set to 1.0 for testing

        bgcolor('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert bgcolor() == 'red'

        bgcolor('black')  # Reset to black
        assert sc(f'{name} red') == 1
        assert bgcolor() == 'red'

        bgcolor('black')  # Reset to black
        assert sc(f'{name} 1 0 0') == 1
        assert bgcolor() == (1.0, 0.0, 0.0)

        bgcolor('black')  # Reset to black
        assert sc(f'{name} 1.0 0.0 0.0') == 1
        assert bgcolor() == (1.0, 0.0, 0.0)

        bgcolor('black')  # Reset to black
        assert sc(f'{name} 255 0 0') == 1  # Test that temporarily setting colormode to 255 works.
        assert bgcolor() == (1.0, 0.0, 0.0)

        colormode(255) # Test that temporarily setting colormode to 1 works.
        assert sc(f'{name} 0 1.0 0') == 1
        colormode(1.0)
        assert bgcolor() == (0, 1, 0)

        for color_name in 'black blue brown orange gray grey green purple violet pink yellow white red magenta cyan'.split():
            assert sc(f'{name} {color_name}') == 1
            assert bgcolor() == color_name

        colormode(255)
        assert sc(f'{name} FF0000') == 1
        assert bgcolor() == (255, 0, 0.0)

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

        



def test_colorful_squares():
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

    sc('u')
    sc('reset')


def test_draw_circles():
    # Draw circle in the top half of the window:
    sc('sh 0')  # Face right.
    for i in range(20):
        sc(f'cir {i * 10}')

    # Draw circles in the bottom half of the window:
    sc('sh 180')  # Face left.
    for i in range(20):
        sc(f'cir {i * 10}')
    sc('u')
    sc('reset')


def test_curve_path_filled():
    for i in range(50):
        sc(f'fc {random()} {random()} {random()}')

        # Set a random heading and draw several short lines with changing direction:
        sc(f'sh {randint(0, 360)}, bf')

        for j in range(randint(200, 600)):
            sc(f'f 1,l {randint(-4, 4)}')
        sc(f'h, ef')
    sc('u')
    sc('reset')


if __name__ == '__main__':
    pytest.main()