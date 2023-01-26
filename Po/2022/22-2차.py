Math = [70, 65, 90, 80, 50]
English = [40, 20, 30, 60, 50]

Math_scores = []
Eng_socres = []
result = 0
for i in range(len(Math)):
    Math_scores.append([i,Math[i]])
    Eng_socres.append([i,English[i]])

Math_scores.sort(key = lambda x:(x[1]))
Eng_socres.sort(key = lambda x:(x[1]))
print(Math_scores)
print(Eng_socres)

for j in range(len(Math_scores)-1):
    if Math_scores[i][0]
print(result)
