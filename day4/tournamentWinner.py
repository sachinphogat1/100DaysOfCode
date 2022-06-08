"""MY SOLUTION1"""

#This is slow because return max(result, key=result.get) is also a for loop and hence we now are having two for loops  and hence slow. Solution 2 is fast because we are checking it consequently

# def tournamentWinner(competitions, results):
#     # Write your code here.
#     result = {}
#     resIdx = 0
#     for i in competitions:
#         resValue = results[resIdx]
#         if resValue == 0:
#             thisWinner = i[1]
#         else:
#             thisWinner = i[0]

#         resIdx+=1
        
#         if thisWinner not in result:
#             result[thisWinner]=3
#         else:
#             result[thisWinner]+=3

#     return max(result, key=result.get)
# competitions = [["HTML" ,"C#"],["C#", "Python"],["Python","HTML"]]
# results = [0,0,1]

# print(tournamentWinner(competitions, results))

"""Testing"""
# res = {"sachin":10, "sunny":10, "pratibha":32}
# print(max(res, key=res.get))
# print(competitions[0][1])
# print("Hello")

"""ACTUAL SOLUTION"""

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
        
    return currentBestTeam

def updateScores(team, points, scores):

    if team not in scores:
        scores[team] = 0

    scores[team]+=points


competitions = [["HTML" ,"C#"],["C#", "Python"],["Python","HTML"]]
results = [0,0,1]

print(tournamentWinner(competitions, results))
