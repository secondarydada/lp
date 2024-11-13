from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight

    def __lt__(self, other):
        return other.weight < self.weight

def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    if j < n:
        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)

    return profit_bound

def knapsack(W, arr, n):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0)
    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():
        u = priority_queue.get()

        if u.level == -1:
            v = Node(0, 0, 0)
        elif u.level == n - 1:
            continue
        else:
            v = Node(u.level + 1, u.profit, u.weight)

        v.weight += arr[v.level].weight
        v.profit += arr[v.level].value

        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v_bound = bound(v, n, W, arr)
        if v_bound > max_profit:
            priority_queue.put(v)

        v = Node(u.level + 1, u.profit, u.weight)
        v_bound = bound(v, n, W, arr)
        if v_bound > max_profit:
            priority_queue.put(v)

    return max_profit

# Taking user input
n = int(input("Enter the number of items: "))
arr = []
for i in range(n):
    value = int(input(f"Enter value of item {i + 1}: "))
    weight = float(input(f"Enter weight of item {i + 1}: "))
    arr.append(Item(weight, value))

W = int(input("Enter maximum weight capacity of the knapsack: "))
max_profit = knapsack(W, arr, n)
print("Maximum possible profit =", max_profit)
