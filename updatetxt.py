
def update(text):
# Open the file in read mode to read the existing content
    with open("./data/dictonary.txt", "r") as file:
        content = file.read()

    # Modify the content as desired
    updated_content = content +"\n"+text

    # Open the file in write mode to write the updated content
    with open("./data/dictonary.txt", "w") as file:
        file.write(updated_content)
    

