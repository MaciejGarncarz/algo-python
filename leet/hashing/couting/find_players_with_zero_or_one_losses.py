# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4606/

from typing import List

input = [[2,3],[1,3],[5,4],[6,4]]


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    players_ledger = dict()
    

    for match in matches:
        winner = match[0]
        loser = match[1]

        winners_value = players_ledger.get(winner, None)
        if winners_value is None:
            players_ledger[winner] = [1, 0]
        else:
            winners_value[0] += 1
            players_ledger[winner] = winners_value

        losers_value = players_ledger.get(loser, None)
        if losers_value is None:
            players_ledger[loser] = [0, 1]
        else:
            losers_value[1] += 1
            players_ledger[loser] = losers_value

        
    never_lost = []
    lost_one = []

    for player in players_ledger:
        value = players_ledger[player]
        if value[1] == 0:
            never_lost.append(player)
        elif value[1] == 1:
            lost_one.append(player) 


    return [sorted(never_lost), sorted(lost_one)]




print(findWinners(input))