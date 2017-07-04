
# Export functions
def exporting_answers():
    import reports
    with open("export_answers_2.txt", "w") as f:
        f.write(str(reports.get_most_played("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.sum_sold("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_selling_avg("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.count_longest_title("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_date_avg("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_game("game_stat.txt","World of Warcraft")))
        f.write("\n")
        f.write(str(reports.count_grouped_by_genre("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_date_ordered("game_stat.txt")))

exporting_answers()
