# GAME OF LIFE, Jeremy Kovalchuk 2022
import re

# input_string = input()


def next_generation_field(field: list, rules: list, field_size):
    temp_field = [[field[i][j] for j in range(field_size)] for i in range(field_size)]

    debug_neighbors_field = [[0 for j in range(field_size)] for i in range(field_size)]
    debug_neighbors_field2 = [[0 for j in range(field_size)] for i in range(field_size)]

    for i in range(field_size):
        for j in range(field_size):

            neighbors = 0

            for ii in range(max(0, i - 1), min(field_size - 1, i + 1) + 1):
                for jj in range(max(0, j - 1), min(field_size - 1, j + 1) + 1):
                    if field[ii][jj] == rules[2]:
                        # print(ii, jj, "for cell", i, j)
                        neighbors += 1

            if field[i][j] == rules[2]:
                neighbors -= 1

            debug_neighbors_field[i][j] = neighbors

            # if neighbors != 0:
            #     print(i, j, "has", neighbors, "neighbors")

            if field[i][j] == rules[2]:

                if neighbors in rules[0]:
                    temp_field[i][j] = rules[2]
                else:
                    temp_field[i][j] -= 1
            else:
                if neighbors in rules[1]:
                    # print(neighbors, "is in", rules[1])
                    temp_field[i][j] = rules[2]
                else:
                    temp_field[i][j] -= 1

            if temp_field[i][j] < 0:
                temp_field[i][j] = 0

            debug_neighbors_field[i][j] = neighbors

    field = [[temp_field[i][j] for j in range(field_size)] for i in range(field_size)]

    # print("NEIGHBORS MAP:")
    # for k in range(field_size):
    #     print(debug_neighbors_field[k])
    #
    # print()

    return field


def parse_input(inp_str):

    rules = [[], [], []]
    current_rule = 0
    for i in inp_str:
        if i=='/':
            current_rule+=1
            continue
        rules[current_rule
        ].append(i)

    rules[2] = ''.join(rules[2])
    rules[2] = int(rules[2])

    for i in range(len(rules[0])):
        rules[0][i] = int(rules[0][i])
    for i in range(len(rules[1])):
        rules[1][i] = int(rules[1][i])
    return rules

def example():
    print("main.py file executed, starting example program...")
    input_string = "2/2/25"
    rules = parse_input(input_string)
    field_size = 30

    field1 = [[int(0) for i in range(field_size)] for j in range(field_size)]

    field1[14][14] = rules[2]
    field1[14][15] = rules[2]
    field1[15][14] = rules[2]
    field1[15][15] = rules[2]

    while True:
        field1 = next_generation_field(field1, rules, field_size).copy()

        print('\n' * 10)  # clear for pycharm
        for k in range(field_size):
            print(field1[k])

        for i in range(field_size):
            for j in range(field_size):
                if field1[i][j] == rules[2]:
                    print("🟩", end=' ')
                elif field1[i][j] > rules[2] * 3 / 4:
                    print("🟨", end=' ')
                elif field1[i][j] > rules[2] * 2 / 4:
                    print("🟧", end=' ')
                elif field1[i][j] > 0:
                    print("🟥", end=' ')
                else:
                    print("🟫", end=' ')
            print()
        input()


def interface_input(cells_coordinates: list, inp_str: str, field_size: int):
    rules = parse_input(inp_str)
    field = [[int(0) for i in range(field_size)] for j in range(field_size)]
    for point in cells_coordinates:
        field[point[0]][point[1]] = rules[2]

    return


if __name__ == "__main__":
    example()


