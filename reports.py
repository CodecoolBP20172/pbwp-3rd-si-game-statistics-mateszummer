
# Report functions
def count_games(file_name):
    count=0
    with open(file_name) as f:
        for line in f:
            count += 1
    return count

def decide(file_name, year):
    year = str(year)
    with open(file_name) as f:
        for line in f:
            if year in line:
                return True

def get_latest(file_name):
    list_by_items = []
    latest = {}
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        latest[list_by_items[i][2]] = list_by_items[i][0]
    return latest[max(latest.keys())]

def count_by_genre(file_name, genre):
    count = 0
    with open(file_name) as f:
        for line in f:
            if genre in line:
                count += 1
    return count

def get_line_number_by_title(file_name, title):
    try:
        gotcha = False
        count = 0
        with open(file_name) as f:
            for line in f:
                count += 1
                if title in line:
                    return count
                    gotcha = True
        if gotcha is False:
            raise ValueError
    except ValueError:
        return "BEEP BOOP, The time of man has come to an end."

def sort_abc(file_name):
    list_by_items = []
    titles = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        titles.append(list_by_items[i][0])
    return sorted(titles)

def get_genres(file_name):
    list_by_items = []
    genres = []
    with open(file_name) as f:
        for line in f:
            list_by_items.append(line.split("	"))
    for i in range(len(list_by_items)):
        if list_by_items[i][3] not in genres:
            genres.append(list_by_items[i][3])
    iterations = 1
    N = len(genres)
    while iterations < N:
        j = 0
        while j <= N - 2:
            if genres[j][0].lower() > genres[j+1][0].lower():
                temp = genres[j+1]
                genres[j+1] = genres[j]
                genres[j] = temp
            if genres[j][0].lower() == genres[j+1][0].lower():
                if genres[j][1].lower() > genres[j+1][1].lower():
                    temp = genres[j+1]
                    genres[j+1] = genres[j]
                    genres[j] = temp
            j = j +1
        iterations = iterations + 1
    iterations = 1
    return(genres)

def when_was_top_sold_fps(file_name):
    try:
        list_by_items = []
        top_sold = {}
        with open(file_name) as f:
            for line in f:
                if "First-person shooter" in line:
                    list_by_items.append(line.split("	"))
        if len(list_by_items) == 0:
            raise ValueError
        for i in range(len(list_by_items)):
            top_sold[list_by_items[i][1]] = list_by_items[i][2]
        return int(top_sold[max(top_sold.keys() , key=float)])
    except ValueError:
        return "Exterminate. Exterminate"
