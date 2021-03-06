def export_answers():
    import reports
    with open("export_answers.txt", "w") as f:
        f.write(str(reports.count_games("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.decide("game_stat.txt", "1999")))
        f.write("\n")
        f.write(str(reports.get_latest("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.count_by_genre("game_stat.txt", "Real-time strategy")))
        f.write("\n")
        f.write(str(reports.get_line_number_by_title("game_stat.txt", "Counter-Strike: Condition Zero")))
        f.write("\n")
        f.write(str(reports.sort_abc("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_genres("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.when_was_top_sold_fps("game_stat.txt")))

export_answers()
