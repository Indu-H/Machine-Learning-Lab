import csv
num_attributes=6 
a=[]
print("\n The given training data set \n") 
csvfile=open('1a.csv','r') 
reader=csv.reader(csvfile)
for row in reader: 
    a.append(row) 
    print(row)
print("The initial values of hypothesis ") 
hypothesis=['0']*num_attributes
print(hypothesis)

for j in range(0,num_attributes): 
    hypothesis[j]=a[0][j]

for i in range(0,len(a)): 
    if(a[i][num_attributes]=='Yes'):
        for j in range(0,num_attributes): 
            if(a[i][j]!=hypothesis[j]):
                hypothesis[j]='?' 
            else:
                hypothesis[j]=a[i][j]
    print("For training instance no:",i," the hypothesis is ",hypothesis) 
print("The maximally specific hypothesis is ",hypothesis)



# The given training data set 

# ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
# ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']
# ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No']
# ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
# The initial values of hypothesis 
# ['0', '0', '0', '0', '0', '0']
# For training instance no: 0  the hypothesis is  ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
# For training instance no: 1  the hypothesis is  ['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
# For training instance no: 2  the hypothesis is  ['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
# For training instance no: 3  the hypothesis is  ['Sunny', 'Warm', '?', 'Strong', '?', '?']
# The maximally specific hypothesis is  ['Sunny', 'Warm', '?', 'Strong', '?', '?']
