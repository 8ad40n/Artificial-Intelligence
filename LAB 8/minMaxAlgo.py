import math

def minimax (depthCur, indexNode,
			tuenMax, results, 
			depthTarget):

	if (depthCur == depthTarget): 
		return results[indexNode]
	
	if (tuenMax):
		return max(minimax(depthCur + 1, indexNode * 2, 
					False, results, depthTarget), 
				minimax(depthCur + 1, indexNode * 2 + 1, 
					False, results, depthTarget))
	
	else:
		return min(minimax(depthCur + 1, indexNode * 2, 
					True, results, depthTarget), 
				minimax(depthCur + 1, indexNode * 2 + 1, 
					True, results, depthTarget))
	
results = [3, 5, 2, 9]

treeDepth = math.log(len(results), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, results, treeDepth))



