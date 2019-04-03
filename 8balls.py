import random
magicball = {}
counter = 0

##Read and import config file. Build dictionary containing possible answers
file = open("8ball.config")
for line in file:
magicball.update({counter:line.split("\n")[0]})
counter = counter+1

print "Seeing into " + str(counter) + " possible futures."

raw_input("Ask the Magic 8 Ball a question:")
answerkey = random.randrange(counter)
print ''
print ''
print magicball[answerkey]
