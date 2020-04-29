class RomanNumeral:
    def __init__(self, number):
        self.number = number
        self.int_num = 0
        self.rom_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def isroman(self):
        if self.IXC_triple_rules():
            return False
        for i in self.number:
            if i not in self.rom_dict.keys():
                return False
        return True

    def roman_or_int(self):
        if self.isroman():
            print(self.roman_to_int())
        elif self.number.isdigit():
            print("number")
        else:
            print("Entry is neither roman numerals or integers.")
    
    def IXC_triple_rules(self):
        if "IIII" in self.number or "XXXX" in self.number or "CCCC" in self.number:
            print("You cannot have more than three I, X, or Cs in a row")

    def roman_to_int(self):
        rom_values = list(self.rom_dict.items())
        for i in range(len(self.number) - 1):
            for j in range(len(rom_values)):
                if self.number[i] == rom_values[j][0]:
                    self.int_num += rom_values[j][1] 
                    for k in range(j+1, len(rom_values)):
                        if self.number[i+1] == rom_values[k][0]:
                            self.int_num -= 2*rom_values[j][1]
                            break
        for l in range(len(rom_values)):
            if self.number[-1] == rom_values[l][0]:
                self.int_num += rom_values[l][1]
        return self.int_num

while True:
    user_input = input("Enter a number in roman numerals(ENTER to exit): ")
    if user_input == "":
        exit()
    x = RomanNumeral(user_input)
    x.roman_or_int()
