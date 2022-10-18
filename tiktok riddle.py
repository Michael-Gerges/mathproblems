## https://www.tiktok.com/@the.virtual.math.lab/video/7128047303373475114?is_copy_url=1&is_from_webapp=v1

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


mynumbers = list(range(1,21))

def get_connections_to_a_number(number):
    global mynumbers
    connections = []
    for i in mynumbers:
        if is_prime(abs(i-number)):
            connections.append(i)
    return connections



set_of_solutions = set()

for i in mynumbers:
    connections = get_connections_to_a_number(i)
    for j in connections:
        second_connections = get_connections_to_a_number(j)
        for k in second_connections:
            third_connections = get_connections_to_a_number(k)
            if i in third_connections:
                solution = str(sorted([i,j,k]))
                set_of_solutions.add(solution)


print(len(set_of_solutions))
