import random
JSCII = {
    '0' : '000000',
    '1' : '000001',
    '2' : '000010',
    '3' : '000011',
    '4' : '000100',
    '5' : '000101',
    '6' : '000110',
    '7' : '000111',
    '8' : '001000',
    '9' : '001001',
    ' ' : '001010',
    'a' : '010010',
    'b' : '010011',
    'c' : '010100',
    'd' : '010101',
    'e' : '010110',
    'f' : '010111',
    'g' : '011000',
    'h' : '011001',
    'i' : '011010',
    'j' : '011011',
    'k' : '011100',
    'l' : '011101',
    'm' : '011110',
    'n' : '011111',
    'o' : '100000',
    'p' : '100001',
    'q' : '100010',
    'r' : '100011',
    's' : '100100',
    't' : '100101',
    'u' : '100110',
    'v' : '100111',
    'w' : '101000',
    'x' : '101001',
    'y' : '101010',
    'z' : '101011',
    'yes' : '111111'
}

def Encode(text):
    text = text.lower()
    jsc = ""
    for i in text:
        jsc += JSCII[i]
    jsc = jsc + '111111'
    chunks = [jsc[i:i+6] for i in range(0,len(jsc),6)]
    chunks = [chunk + str(random.randint(0,1)) for chunk in chunks]
    jsc = ''.join(chunks)
    return jsc

def Decode(jsc):
    yours = False
    if jsc[-7:-1] == '111111':
        yours = True
        jsc = jsc[:-7]

    chunks = [jsc[i:i+7] for i in range(0,len(jsc),7)]
    o_chunks = [chunk[:-1] for chunk in chunks]
    text = ""
    for i in o_chunks:
        for key,value in JSCII.items():
            if i == value:
                text += key
    return text, yours

# text = input("Enter your text here: ")
# jsc = Encode(text)
# print("The JSCII code is:\n", jsc)

# while True:
#     print("This is JSCII")
#     choice = int(input("Enter 1 to JSCII to Text and 2 to Text to JSCII: "))
#     if choice == 1:
#         jsc = input("Enter JSCII code: ")
#         if jsc[-7:-1] == '111111':
#             print("Yes this is our secret code")
#             jsc = jsc[:-7]

#         chunks = [jsc[i:i+7] for i in range(0,len(jsc),7)]
#         o_chunks = [chunk[:-1] for chunk in chunks]
#         text = ""
#         for i in o_chunks:
#             for key,value in JSCII.items():
#                 if i == value:
#                     text += key
#         print("The text is:\n ", text)
#     elif choice == 2:
#         text = input("Enter text: ")
#         text = text.lower()
#         jsc = ""
#         for i in text:
#             jsc += JSCII[i]
#         jsc = jsc + '111111'
#         chunks = [jsc[i:i+6] for i in range(0,len(jsc),6)]
#         chunks = [chunk + str(random.randint(0,1)) for chunk in chunks]
#         jsc = ''.join(chunks)
#         print("The JSCII code is:\n", jsc)
