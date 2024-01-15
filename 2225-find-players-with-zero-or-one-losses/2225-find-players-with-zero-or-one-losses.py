class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = [], []
        d = {}
        for i in matches:
            if i[1] not in d:
                d[i[1]] = 1
            else:
                d[i[1]]+=1

            if i[0] not in d:
                d[i[0]] = 0
            

        for player, freq in d.items():
            if freq == 0:
                winners.append(player)
            if freq == 1:
                losers.append(player)

        return [sorted(winners), sorted(losers)]