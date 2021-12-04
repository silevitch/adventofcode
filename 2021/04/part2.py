file = open("input.txt", "r")

numbers = []
data = []
boards = []

def make_board(data, count):
    board = { "name" : count, "numbers" : {}, "checks" : {}, "winner" : 0 }
    row = 1

    for datum in data:
        numbers = datum.split()
        col = 1
        for number in numbers:
            board["numbers"][ number ] = 1

            if (col * 10) not in board["checks"]:
                board["checks"][col * 10] = {}
            if (row) not in board["checks"]:
                board["checks"][row] = {}

            board["checks"][col * 10][ number ] = 1
            board["checks"][row][ number ] = 1
            col += 1
        row += 1
    
    return board

for line in file:
    if len(numbers) == 0:
        numbers = line.strip().split(',')
        continue

    if line == "\n":
        continue

    data.append(line.strip())

    if len(data) == 5:
        boards.append(make_board(data, len(boards)))
        data = []

def find_score(board, played_nums):
    last_num = played_nums[len(played_nums) - 1 ]
    unmarked_sum = 0

    for num in board["numbers"]:
        if num not in played_nums:
            unmarked_sum += int(num)

    return(int(last_num) * unmarked_sum)

def check_winner(boards, played_nums):
    for board in boards:
        if board["winner"] == 1:
            continue

        for check in board["checks"]:
            winner = 0
            for num in played_nums:
                if num in board["checks"][check]:
                    winner += 1

            if winner == 5:
                print("Winner!")
                print(board)
                print(find_score(board, played_nums))
                board["winner"] = 1
                break

played_nums = []

def play():
    for number in numbers:
        played_nums.append(number)
        check_winner(boards, played_nums)

play()
