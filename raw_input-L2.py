print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if (len(original) <= 0):
    print "empty";
    
elif (original.isalpha() and len(original) > 0):
    print original;

else: 
    print False;
