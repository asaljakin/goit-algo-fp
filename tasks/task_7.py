import random
import matplotlib.pyplot as plt
from utils.helpers import Colors

def monte_carlo_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}
    return probabilities

def analytical_probabilities():
    return {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }

def task_7():
    num_rolls = int(input(f"{Colors.BLUE}Введіть кількість кидків: {Colors.RESET}"))
    probabilities = monte_carlo_dice_rolls(num_rolls)
    
    print(f"{Colors.CYAN}Ймовірності сум (Метод Монте-Карло):{Colors.RESET}")
    for k, v in probabilities.items():
        print(f"{Colors.YELLOW}{k}{Colors.RESET}: {v:.4f}")

    analytical_probs = analytical_probabilities()
    
    print(f"\n{Colors.CYAN}Аналітичні ймовірності:{Colors.RESET}")
    for k, v in analytical_probs.items():
        print(f"{Colors.YELLOW}{k}{Colors.RESET}: {v:.4f}")
    
    x = list(probabilities.keys())
    y_mc = list(probabilities.values())
    y_analytical = [analytical_probs[k] for k in x]

    plt.bar(x, y_mc, alpha=0.5, label='Метод Монте-Карло', color='blue')
    plt.bar(x, y_analytical, alpha=0.5, label='Аналітичні', color='red')
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.legend()
    plt.show()

