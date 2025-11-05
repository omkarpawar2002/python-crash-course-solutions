'''
 6-3. Glossary: A Python dictionary can be used to model an actual dictionary . 
However, to avoid confusion, let’s call it a glossary .
 •	Think of five programming words you’ve learned about in the previous 
chapters . Use these words as the keys in your glossary, and store their 
meanings as values .
 •	Print each word and its meaning as neatly formatted output . You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line . Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output 
'''

Glossary = {
    'print':'This function is used to display the output',
    'len':'This function is used to find the length',
    'for':'This is a control statement to execute certain code in repetative manner',
    'break':'This break statement will be used to immediatly exit from the loop',
    'continue':'This continue statement is used to skip the current iteration of loop',
}
for word,meaning in Glossary.items():
    print(word,':\n\t',meaning)