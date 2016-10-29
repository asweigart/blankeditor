

def transform(oldData):
	result = {}

	for oldKey, oldValueList in oldData.items():
		for oldValue in oldValueList:
			result[oldValue.lower()] = oldKey

	return result