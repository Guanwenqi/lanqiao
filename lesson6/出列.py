n=int(input())
bin_n=bin(n)[2:]
print(1<<(len(bin_n)-1))#找规律且不能比n大