def tournamentWinner(competitions, results):
    scores = {best_team: 0}
    best_team = ""
    for idx, comp in enumerate(competitions):
        result = results[idx]
        home, away = comp

        winner = home if result == 1 else away

        update_scores(winner, 3, scores)

        if scores[winner] > scores[best_team]:
            best_team = winner
    
    return best_team

def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points



    

# competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
# print(list(enumerate(competitions)))
# [(0, ['HTML', 'C#']), (1, ['C#', 'Python']), (2, ['Python', 'HTML'])]