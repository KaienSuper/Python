text = input("Text: ").upper().split()
morse = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", 
         "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..",
         "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", 
         "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", 
         "Y":"-.--", "Z":"--..", "1":".----", "2":"..---", "3":"...--",
         "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..",
         "9":"----.", "0":"-----"}
new_text = []
word_2 = ""
for word in text:
    for char in word:
        word_2 += morse[char]
    new_text.append(word_2)
    word_2 = ""
for i in new_text:
    print(i)
