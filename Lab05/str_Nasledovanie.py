class str_Nasledovanie(str):
    def repeats(self, s):
        count = {}
        for data in s:
            if count.__contains__(data):
                count[data] += 1
            else:
                count[data] = 1

        for key in count:
            if count[key] >= 3:
                print(True)
                break
            else:
                print(False)
                break
    
    def if_palidrom(self, s):
        return s.lower() == s[::-1].lower()