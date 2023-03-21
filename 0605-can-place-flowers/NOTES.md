class Solution:
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
j=1
c=0
if n==0:
return True
if len(flowerbed)==1 and flowerbed[0]== 0 and n==1:
return True
for i in range(len(flowerbed)):
if j < len(flowerbed):
if flowerbed[i] == 1 and flowerbed[j] == 0:
j += 1
elif flowerbed[i] == 0 and flowerbed[j] == 0:
if j+1 == len(flowerbed):
flowerbed[j] = 1
c += 1
elif i == 0 :
flowerbed[i] = 1
j += 1
c += 1
elif flowerbed[j+1]==0:
flowerbed[j] = 1
c += 1
j += 1
else:
j += 1
else:
j += 1
if n == c:
return True
return False