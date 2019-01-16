q = "what's your favorite song?"

with open("exfolder\\answer.txt","a") as f:
	ans = input(q) +"\n"
	f.write(ans)