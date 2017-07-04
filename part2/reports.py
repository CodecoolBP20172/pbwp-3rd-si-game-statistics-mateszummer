
# Report functions
def get_most_played(file_name):
    list_by_items = []
    played_games = {}
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        if list_by_items[i][1] not in played_games:
            played_games[list_by_items[i][1]] = list_by_items[i][0]
    return str(played_games[max(played_games.keys() , key=float)])

print(get_most_played("game_stat.txt"))


def sum_sold(file_name):
    list_by_items = []
    sold = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        sold.append(float(list_by_items[i][1]))
    return sum(sold)

print(sum_sold("game_stat.txt"))


def get_selling_avg(file_name):
    list_by_items = []
    sold = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        sold.append(float(list_by_items[i][1]))
    return float(sum(sold)/len(sold))

print(get_selling_avg("game_stat.txt"))


def count_longest_title(file_name):
    list_by_items = []
    titles = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        titles.append(list_by_items[i][0])
    return len(max(titles, key=len))

print(count_longest_title("game_stat.txt"))


def get_date_avg(file_name):
    import math
    list_by_items = []
    dates = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        dates.append(int(list_by_items[i][2]))
    return math.ceil(sum(dates)/len(dates))

print(get_date_avg("game_stat.txt"))


def get_game(file_name,title):
    list_by_items = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        list_by_items[i][4] = list_by_items[i][4][:-1] 
        for n in range(len(list_by_items[i])):
            try:
                list_by_items[i][n] = int(list_by_items[i][n])
            except:
                try:
                    list_by_items[i][n] = float(list_by_items[i][n])
                except:
                    continue
    for i in range(len(list_by_items)):
        if title in list_by_items[i]:
            return list_by_items[i]

print(get_game("game_stat.txt","World of Warcraft"))

def count_grouped_by_genre(file_name):
    list_by_items = []
    genres = {}
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        if list_by_items[i][3] not in genres:
            genres[list_by_items[i][3]] = 1
        else:
            genres[list_by_items[i][3]] +=1
    return genres

print(count_grouped_by_genre("game_stat.txt"))

def get_date_ordered(file_name):
    list_by_items = []
    dates = []
    titles = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        dates.append(list_by_items[i][2])
    dates = sorted(set(dates), reverse=True)
    list_by_items = sorted(list_by_items)
    for date in dates:
        for i in range(len(list_by_items)):
            if date in list_by_items[i]:
                titles.append(list_by_items[i][0])
    return (titles)

print(get_date_ordered("game_stat.txt"))
