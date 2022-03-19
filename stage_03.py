
text="added files"

with open("artifacts01.txt","r") as f:
    text = f.read()

with open("artifacts02.txt","w") as f:
    f.write(text)


print("end of stage02")

    
