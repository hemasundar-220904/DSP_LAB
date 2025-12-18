def knapsack_greedy(weights, values, capacity):
    n = len(values)
    
    ratios = [value / weight for value, weight in zip(values, weights)]

    sorted_items = sorted(zip(ratios, weights, values), reverse=True)
    total_value = 0
    selected_items = []
    for ratio, weight, value in sorted_items:
        if weight <= capacity:
            capacity -= weight
            total_value += value
            selected_items.append((weight, value))
        else:
            fraction = capacity / weight
            total_value += value * fraction
            selected_items.append((weight * fraction, value * fraction))
            break
    return total_value, selected_items


weights = [20,30,10,30]
values = [200,150,100,180]
capacity = 50
total_value, selected_items = knapsack_greedy(weights, values, capacity)
print("Total value:", total_value)
print("Selected items:", selected_items)