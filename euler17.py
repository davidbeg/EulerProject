ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

def strip_len(s):
    print(s.replace(" ", ""), end="")
    return len(s.replace(" ", ""))

sub_total = 0
sub_total += sum(map(strip_len, ones))
for i in range(2, 10):
    for j in range(10):
        sub_total += strip_len(twenties[i] + ones[j])
        # print(twenties[i] + ones[j])
print(sub_total)
total = sub_total
for i in range(1, 10):
    total += strip_len(ones[i] + "hundred")
    total += strip_len(ones[i] + "hundred and") * 99 + sub_total

total += strip_len("one thousand")

print(total)


