import numpy as np
ip = np.array([1,0,0,0,1])
print('Input: ',ip)
data_len = len(ip)

for i in range(0,data_len):
	lhs = 2**i
	rhs = i + data_len +1
	if(lhs>=rhs):
		break

mod_data_len = data_len+i
mod_data = np.zeros(mod_data_len, dtype=int)

parity_indices = np.zeros(i, dtype=int)
for j in range(0, i):
	parity_indices[j] = mod_data_len - 2**j

cx = data_len-1;
flag = True
for g in range(mod_data_len-1, -1,-1):
	for tx in range(0, len(parity_indices)):
		if g == parity_indices[tx]:
			flag = False
			break
		else:
			flag = True	
	if flag == True:
		mod_data[g] = ip[cx]
		cx = cx - 1

for itr1 in range(0,i):
	read_flag = True
	ones_count = 0 
	ref_count = 2**itr1
	True_count = 1
	False_count = 1
	k = parity_indices[itr1]
	for itr2 in range(k,-1,-1):
		if read_flag == True:
			if mod_data[itr2]==1:
				ones_count=ones_count+1
			True_count = True_count + 1
			if True_count>ref_count:
				read_flag = False
		else:
		 	False_count = False_count + 1
		 	if False_count>ref_count:
		 		read_flag = True
	if ones_count%2 == 0:
		bitToBeEntered = 0
	else:
		bitToBeEntered = 1
	mod_data[parity_indices[itr1]] = bitToBeEntered

print('CodeWord: ',mod_data)