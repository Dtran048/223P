import json


class Flights:
    def __init__(self, filename):
        self.fn = filename
        self.flli = []
        try:
            with open(filename, 'r') as f:
                self.flli = json.load(f)
        except FileNotFoundError:
            return

    def add_flight(self, orgin, destination, flight_number, departure, next_day, arrival):
        if (departure.isnumeric() == False) or (len(departure) != 4) or (len(arrival) != 4) or (arrival.isnumeric() == False):
            return False
        self.flli.append([orgin, destination, flight_number, departure, next_day, arrival])
        with open(self.fn, "w") as outfile:
            json.dump(self.flli, outfile)
        return True

    def get_flights(self):
        templist = self.flli
        for i in templist:
            if i[4] == "Y":
                i[4] = ((int(i[5][:2]) * 60) + int(i[5][2:]) + 1440) - ((int(i[3][:2]) * 60) + int(i[3][2:]))                
                next_day = True
            else:
                i[4] = ((int(i[5][:2]) * 60) + int(i[5][2:])) - ((int(i[3][:2]) * 60) + int(i[3][2:]))
                next_day = False

            temp_num = divmod(i[4], 60)
            if len(str(temp_num[1])) == 1:
                i[4] = str(temp_num[0]) + ":0" + str(temp_num[1])
            else:
                i[4] = str(temp_num[0]) + ":" + str(temp_num[1])

            if int(i[3]) >= 1300:
                i[3] = str(int(i[3]) - 1200)
                if int(i[3]) < 1000:
                    i[3] =  str(int(i[3][:1])) + ":" + i[3][1:] + "pm"
                else:
                    i[3] = str(int(i[3][:2])) + ":" + i[3][2:] + "pm"
            else:
                if int(i[3]) >=1200:
                    i[3] = str(int(i[3][:2])) + ":" + i[3][2:] + "pm"
                else:
                    i[3] = str(int(i[3][:2])) + ":" + i[3][2:] + "am"

            if int(i[5]) > 1300:
                i[5] = str(int(i[5]) - 1200)
                if int(i[5]) < 1000:
                    if next_day == True:
                        i[5] =  "+" + str(int(i[5][:1])) + ":" + i[5][1:] + "pm"
                    else:
                        i[5] =  str(int(i[5][:1])) + ":" + i[5][1:] + "pm"
                else:
                    if next_day == True:
                        i[5] =  "+" + str(int(i[5][:2])) + ":" + i[5][2:] + "pm"
                    else:
                        i[5] =  str(int(i[5][:1])) + ":" + i[5][1:] + "pm"
            else:
                if int(i[5]) >=1200:
                    if next_day == True:
                        i[5] =  "+" + str(int(i[5][:1])) + ":" + i[5][1:] + "pm"
                    else:
                        i[5] =  str(int(i[5][:1])) + ":" + i[5][1:] + "pm"
                else:
                    if next_day == True:
                        i[5] =  "+" + str(int(i[5][:2])) + ":" + i[5][2:] + "am"
                    else:
                        i[5] =  str(int(i[5][:1])) + ":" + i[5][1:] + "am"
            

        return templist