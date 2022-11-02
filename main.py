
#!/usr/bin/python3
import csv
import requests

answers = []

with open('top-1m.csv', newline='') as csvfile:

    top1m = csv.reader(csvfile, delimiter=' ', quotechar='|')

    count = 0

    for row in top1m:
        target = row[0].split(',')[1]
        count += 1
        try:
            r = requests.get('https://' + target, timeout=2)
        except:
            print("ignored...", target)

        if "Cache-Control" in r.headers:
            header = str(r.headers["Cache-Control"]).replace(" ", "")
            header_list = sorted(header.split(','))
            delim = ","
            temp_header = list(map(str, header_list))
            final_header = delim.join(temp_header)
            answers.append(final_header)

        if count == 1000:
            break

    str=""
    stats = {}

    print("parsing answers")

    for i in answers:

        if i not in stats:
            stats[i] = 0

        else:
            for j in answers:
                if i == j:
                    stats[i] += 1

    sorted_stats = sorted(stats.items(), key=lambda x:x[1], reverse = True)

    converted_dict = dict(sorted_stats)

    for i in converted_dict:
        print(converted_dict[i], i)
