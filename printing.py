
# Printing functions
import reports
print(reports.count_games("game_stat.txt"))
print(reports.decide("game_stat.txt", "2012"))
print(reports.get_latest("game_stat.txt"))
print(reports.count_by_genre("game_stat.txt", "Real-time strategy"))
print(reports.get_line_number_by_title("game_stat.txt", "Counter-Strike: Condition Zero"))
print(reports.sort_abc("game_stat.txt"))
print(reports.get_genres("game_stat.txt"))
print(reports.when_was_top_sold_fps("game_stat.txt"))
