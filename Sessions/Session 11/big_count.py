
handle = ["Writing programs (or programming) is a very creative and rewarding activity.  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem.  This book assumes that everyone needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills."]

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
