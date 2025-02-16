from tasks.task_1 import task_1
from tasks.task_2 import task_2
from tasks.task_3 import task_3
from tasks.task_4 import task_4
from tasks.task_5 import task_5
from tasks.task_6 import task_6
from tasks.task_7 import task_7
from utils.helpers import Colors

def main_menu():
    print("\n",f"{Colors.CYAN}Виберіть завдання:{Colors.RESET}")
    print(f"{Colors.CYAN}1. Реверсування та сортування однозв'язного списку{Colors.RESET}")
    print(f"{Colors.CYAN}2. Дерево Піфагора{Colors.RESET}")
    print(f"{Colors.CYAN}3. Алгоритм Дейкстри{Colors.RESET}")
    print(f"{Colors.CYAN}4. Візуалізація бінарної купи{Colors.RESET}")
    print(f"{Colors.CYAN}5. Обхід бінарного дерева (DFS та BFS){Colors.RESET}")
    print(f"{Colors.CYAN}6. Жадібний алгоритм та динамічне програмування{Colors.RESET}")
    print(f"{Colors.CYAN}7. Метод Монте-Карло для кидання кубиків{Colors.RESET}")
    print(f"{Colors.CYAN}0. Вийти{Colors.RESET}", "\n")

    choice = input(f"{Colors.BLUE}Ваш вибір: {Colors.RESET}")
    return choice

# Головний цикл програми
while True:
    choice = main_menu()
    if choice == "1":
        task_1()
    elif choice == "2":
        task_2()
    elif choice == "3":
        task_3()
    elif choice == "4":
        task_4()
    elif choice == "5":
        task_5()
    elif choice == "6":
        task_6()
    elif choice == "7":
        task_7()
    elif choice == "0":
        print(f"{Colors.GREEN}Вихід з програми.{Colors.RESET}")
        break
    else:
        print(f"{Colors.RED}Невірний вибір. Спробуйте ще раз.{Colors.RESET}")