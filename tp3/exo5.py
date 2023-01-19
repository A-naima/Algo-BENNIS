def calculate_cost(start_time, end_time):
    if start_time < 0 or start_time > 24 or end_time < 0 or end_time > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return
    if start_time == end_time:
        print("Attention ! l'heure de fin est identique à l'heure de début.\n")
        return
    if start_time > end_time:
        print("Attention ! le début de la location est après la fin ...\n")
        return

    cost = 0
    if start_time >= 0 and start_time < 7:
        cost += (min(7, end_time) - start_time) * 1
        start_time = 7
    if start_time >= 7 and start_time < 17:
        cost += (min(17, end_time) - start_time) * 2
        start_time = 17
    if start_time >= 17 and start_time < 24:
        cost += (min(24, end_time) - start_time) * 1
        start_time = 24
    if start_time >= 0 and start_time < end_time:
        cost += (end_time - start_time) * 1
    return cost

start_time = int(input("Entrez l'heure de début (0-24): "))
end_time = int(input("Entrez l'heure de fin (0-24): "))
cost = calculate_cost(start_time, end_time)
if cost:
    print("Coût:", cost, "euros")
