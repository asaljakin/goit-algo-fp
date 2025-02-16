import turtle
from utils.helpers import Colors

def draw_pythagoras_tree(t, branch_length, angle, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, level - 1)
    t.right(2 * angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, level - 1)
    t.left(angle)
    t.backward(branch_length)

def task_2():
    level = int(input(f"{Colors.BLUE}Введіть рівень рекурсії: {Colors.RESET}"))
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    def on_close():
        print(f"{Colors.BLUE}Шкода, що недочекалися візуалізації дерева... {Colors.RESET}")
        window.bye()

    window._root.protocol("WM_DELETE_WINDOW", on_close)

    try:
        draw_pythagoras_tree(t, 100, 45, level)
    except Exception as e:
        pass
  
    window.mainloop()

    