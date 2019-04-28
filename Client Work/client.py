def seedAlgo1(seed):
	KEY_CONSTANT_1 = 0xDDDDDDDD
	KEY_CONSTANT_2 = 0xAAAAAAAA
	AND_CONSTANT = 0xFFFFFFFF
	seedBigInt = seed
	tempSeed = (((seedBigInt>> 16)& 0xFF) << 24)
	tempSeed = tempSeed + (((seedBigInt >> 24) & 0xFF) << 16)
	tempSeed = tempSeed + ((seedBigInt >> 8) & 0xFF)
	tempSeed = tempSeed + (seedBigInt & 0xFF) << 8
	shiftSeed = (((tempSeed << 11) + (tempSeed >> 22)) & AND_CONSTANT)
	key = ((shiftSeed ^(KEY_CONSTANT_1 ^ (KEY_CONSTANT_2 & seedBigInt))) & AND_CONSTANT);
	return key

seedAlgo1(12345678)
