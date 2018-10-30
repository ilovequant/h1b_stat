import re

with open('./input/h1b_input.csv', 'r') as f:
    occupation = {}  # dictionary for occupation
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
             "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
             "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    state = {}  # dictionary for state
    for i in states:
        state[i] = [0, 0, 0]

    total_cert = 0  # total number of certified applications
    for line in f:
            items = line.split(';')

            # update occupation dictionary
            for idx in range(len(items)):
                if items[idx] == "CERTIFIED":
                    cert = True
                    total_cert += 1

                if re.match(r'^\d{2}[\-]\d{4}$',items[idx]):
                    items[idx+1] = items[idx+1].replace('"','')
                    if items[idx+1] not in occupation:
                        occupation[items[idx+1]] = [1, 0, 0]
                        if cert:
                            occupation[items[idx+1]][1] = 1

                    else:
                        occupation[items[idx+1]][0] += 1
                        if cert:
                            occupation[items[idx + 1]][1] += 1

            # update state dictionary
            if items[-3] in state:
                state[items[-3]][0] += 1
                if cert:
                    state[items[-3]][1] += 1

            cert = False  # flag

# compute percentage
for key in occupation:
    occupation[key][2] = occupation[key][1]/total_cert

for key in state:
    state[key][2] = state[key][1] / total_cert

# sort by value first then by the alphabetical order of the key
res_occu = sorted(occupation, key=lambda k: (-occupation[k][1], k))

if len(res_occu) > 10:
    res_occu = res_occu[0:10]

res_state = sorted(state, key=lambda k: (-state[k][1], k))

if len(res_state) > 10:
    res_state = res_state[0:10]

# write to txt
f_occu = open('./output/top_10_occupations.txt', 'w')
with open("./output/top_10_occupations.txt", "w") as f1:
    f1.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(len(res_occu)):
        if occupation[res_occu[i]][1] > 0:
           f1.write(res_occu[i] + ";" + str(occupation[res_occu[i]][1]) + ";" + "{0:.1f}%".format(occupation[res_occu[i]][2]*100) + "\n")

f_state = open('./output/top_10_states.txt', 'w')
with open("./output/top_10_states.txt", "w") as f2:
    f2.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(len(res_state)):
        if state[res_state[i]][1] > 0:
            f2.write(res_state[i] + ";" + str(state[res_state[i]][1]) + ";" + "{0:.1f}%".format(state[res_state[i]][2]*100) + "\n")






