import matplotlib.pyplot as plt 
def find_substring_position(s,t):
    positions=[]
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            positions.append(i+1)
    return positions 


#EXAMPLE DNA STRING 
s = input("ENTER THE DNA SEQUENCE:").upper()
t = input("ENTER THE SUBSTRING YOU WANT TO FIND IN DNA STRING:").upper()

positions=find_substring_position(s,t)
print(positions)

