class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} #id -> (startStation, time)
        self.totalMap = {} # (start, end) -> [totalTime, count]         

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkInMap[id]
        if (start, stationName) not in self.totalMap:
            self.totalMap[(start, stationName)] = [0, 0]        
        self.totalMap[(start, stationName)][0] += t - time
        self.totalMap[(start, stationName)][1] += 1        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)