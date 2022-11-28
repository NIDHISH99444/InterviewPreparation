
res=[]
def letterCombination(digit,output,index,mapping):
    if index==len(digit):
        res.append(output)
        return
    key=int(digit[index])
    value=mapping[key]
    for char in value:
        output1=output
        output=output + char
        letterCombination(digit,output,index+1,mapping)
        output = output1


digit="22"
output=""

mapping=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
letterCombination(digit,output,0,mapping)
print(res)
