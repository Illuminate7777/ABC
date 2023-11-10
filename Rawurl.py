# your link goes here

link = "https://github.com/Illuminate7777/ABC/blob/main/STUDENT%20RESPONSIBILITY.txt"

# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
