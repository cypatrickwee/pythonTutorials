#Pig Latin simple python program
#a word Python become ythonpay
def PigLatin(input):
    print "Kindly enter an English word. Thank you.";
    try:
        val = int(input);
    except ValueError:
        #continue;
        print "Lets make some changes to the english word";
        strLength = len(input); #len is the number of character
        
        #first index start from 0
        convString = input[1:strLength-1] + input[0] + "ay";
        return convString.lower(); #convert to lower case
            
            

print PigLatin("English")