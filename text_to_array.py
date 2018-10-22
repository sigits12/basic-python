import re

txt = '''When I was a young boy my father took me into the city to see a marching band. He said, "Son when you grow up would you be the savior of the broken?". My father sat beside me, hugging my shoulders with both of his arms. I said "I Would.". My father replied "That is my boy!". When I was a young boy my father took me into the city to see a marching band. He said, "Son when you grow up would you be the savior of the broken?". My father sat beside me, hugging my shoulders with both of his arms. I said "I Would.". My father replied "That is my boy!".'''

pttrn = re.compile(r'(\.|\?|\!)(\'|\")?\s')

new = re.sub(pttrn, r'\1\2\n\n', txt)

splited = new.split("\n")
dengan_petik = list(filter(lambda x: '"' in x, splited))


print("List Kalimat Langsung :", dengan_petik)
print ('--------------------------------------------------------------------------------------')
for l in dengan_petik:
    print ("Kalimat :", l)
