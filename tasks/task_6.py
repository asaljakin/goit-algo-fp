from utils.helpers import Colors

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        for w in range(1, budget + 1):
            if details['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - details['cost']] + details['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, details = item_list[i - 1]
            selected_items.append(item)
            w -= details['cost']
            total_cost += details['cost']

    return selected_items, total_cost, total_calories

def task_6():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = int(input(f"{Colors.BLUE}Введіть бюджет: {Colors.RESET}"))
    
    selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print(f"{Colors.CYAN}Жадібний алгоритм:{Colors.RESET}")
    print(f"{Colors.YELLOW}Обрані страви: {Colors.RESET}{selected_items_greedy}")
    print(f"{Colors.YELLOW}Загальна вартість: {Colors.RESET}{total_cost_greedy}")
    print(f"{Colors.YELLOW}Загальна калорійність: {Colors.RESET}{total_calories_greedy}\n")

    selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
    print(f"{Colors.CYAN}Динамічне програмування:{Colors.RESET}")
    print(f"{Colors.YELLOW}Обрані страви: {Colors.RESET}{selected_items_dp}")
    print(f"{Colors.YELLOW}Загальна вартість: {Colors.RESET}{total_cost_dp}")
    print(f"{Colors.YELLOW}Загальна калорійність: {Colors.RESET}{total_calories_dp}")

