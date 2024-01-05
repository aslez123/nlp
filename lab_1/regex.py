import re
import json
import matplotlib.pyplot as plt

data_pattern = r'\b\d{1,2}:\d{2}\b'
time_pattern = r'\b\d{1,2}\s+\w{3,20}'

l, k = [],[]
with open('corpus/corpus.jsonl', encoding='utf-8') as file_j:
    for num, line in enumerate(file_j):
        if num > 150:
            break
        try:
            data = json.loads(line)
            text_data = json.dumps(data)
            print("hejo")
            m = re.findall(data_pattern, text_data)
            # t = re.findall(time_pattern, text_data)
            print(m)
            l.extend(m)
            k.extend(t)
        except json.JSONDecodeError as e:
            print("Błąd")

print(l)
print(k)


# dict_d = {}
# dict_k = {}
# for i in l:
#     dict_d[i] = dict_d.get(i,0) + 1
#
# for i in k:
#     dict_k[i] = dict_k.get(i,0) + 1
#
# plt.figure(figsize=(9,3))
# plt.subplot(121)
# plt.bar(list(dict_d.keys()), list(dict_d.values()))
# plt.subplot(122)
# plt.pie(list(dict_k.keys()), list(dict_k.values()))
# plt.show()
#
#
# #3
# sty = r'\bstycz\w{2,5}\b'
# text = str(l)
# num = len(re.findall(sty,text))
#
# #4
# sty2 = r'\b\d{1,2}\s+stycz\w{2,5}'
# num2 = len(re.findall(sty2,text))