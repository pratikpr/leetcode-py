from typing import List


class CanPlantFlowers:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		count = 0
		
		for i in range(len(flowerbed)):
			if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
					i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
				flowerbed[i] = 1
				count += 1
			
			if count >= n:
				return True
		
		return False

obj = CanPlantFlowers()
flowers = [0,0,1,0,1]
n = 1
print(obj.canPlaceFlowers(flowers, n))