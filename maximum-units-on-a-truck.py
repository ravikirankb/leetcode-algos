
class Solution:
	def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
            sorted_box_types = sorted(boxTypes,key=lambda x: x[1],reverse=True)
            total = 0
            
            for boxes, units in sorted_box_types:
                if boxes <= truckSize:
                    truckSize = truckSize - boxes
                    total = total + boxes*units
                else:
                    total = total + truckSize*units
                    break
                
            return total
