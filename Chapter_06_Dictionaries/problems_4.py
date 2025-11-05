'''
 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print 
statements with a loop that runs through the dictionary’s keys and values . 
When you’re sure that your loop works, add five more Python terms to your 
glossary . When you run your program again, these new words and meanings 
should automatically be included in the output
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

# I don't want to make any change just try by yourself 