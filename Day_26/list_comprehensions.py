# newlist = [i*i for i in range(1,5) ]
# print(newlist)


sentence = "What is the density of Water when frozen?"
sentence = list(map(str,sentence.split()))
result = {key:len(key) for key in sentence}
print(sentence)
print(result)

weather_c = {
    "Mon":12,
    "Tue":14,
    'Wed':15,
    "Thu":14,
    "Fri":21,
    "Sat":22,
    "Sun":24
}
weather_f = {key:(value*9/5)+32 for (key,value) in weather_c.items()}
print(weather_f)