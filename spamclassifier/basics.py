emails=["free offers", "project discussions", "win cash"]

for msg in emails:
    if "free" in msg or "win" in msg:
        print(msg,"-->Spam")
    else:
        print(msg,"-->Not Spam")