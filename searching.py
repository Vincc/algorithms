#strings
##########naive string search##############
def naiveStringSearch(sub,string):
    for i in range(len(string)):
        if string[i:i+len(sub)] == sub:
            print("String found! index: "+str(i))
#naiveStringSearch("aa","aabbaawsaba")
#answer: 0,4


#intergers
##########naive interger search##############
def naiveIntergerSearch(sub,interger):

    for i in range(len(interger)):
        if interger[i:i+len(sub)] == sub:
            print("Interger found! index: "+str(i))
#naiveIntergerSearch("123","12123211231235123")
#answer: 2,7,10,14

###########binary search##################
