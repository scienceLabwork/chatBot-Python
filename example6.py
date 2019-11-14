#1st nov

import random

userResponse = '\t\nWelcome to chatBot\n\n let\'s start chatting \n' 
print(userResponse)

#initial cost per person:
kidsCost = 4500
adultCost = 6000


#dictonary:

welcomeMessage = ['hello','hi','hey','grettings']
byeMessage = ['bye','see you soon','tata','bye bye','bye-bye','gn','bye-tata']
ticketMessage = ['book ticket','book ticket for me','tickets','ticket','book tickets','book tickets for me','book','book my ticket','book my tickets']


while userResponse:
    r = ['Hello!! ','Hi!! ','Greetings!! ','Hey!! ']
    z = random.randint(0,3)

    userResponse = input('              >>')
    y = userResponse.lower()
    if y in welcomeMessage:
        print('\n>> ',r[z],' Welcome to DisneyLand Bot powered by Rudra shah\nSo how can I help you? \n')
    elif y in byeMessage:
        print('\n>> See you soon','\n')
        break
    elif(y=='what can you do for me' or y=='what can you do'):
        print('\n>> I\'m a DisneyLand Bot and I can help you in booking tickets for you\nSo how can i help you','\n')
    elif():
        print('')
    elif y in ticketMessage:
        print('\n>>Great!! Let\'s go.......So how many people are travelling in total to DisneyLand? \n')
        newResponse = input('              >>')
        if newResponse.isdigit()==True:
            print('\n>>Hurray!! How many of then are Adults and Children,\n(for-eg, if 3 childrem and 2 adult write like 3,2)So how many?')
            kids,adult = [int(kids) for kids in input('              >>').split(',')]
            finalKidsCost = (kids * kidsCost)
            finalAdultCost = (adult * adultCost)
            finalCost = (finalAdultCost + finalKidsCost)
            TotalPeople = (kids + adult)
            print('\n>>So your final cost for',kids,'kids and',adult,'adults is',finalCost,'rupees\n')
            print('>>want to final this booking for',TotalPeople,'people?\n')
            yesno = input('              >>')
            yesNo = yesno.lower()
            if(yesNo=='yes'):
                print('Congratulation!! you booking is done......Thanks for talking with Disneyland Bot powered by Rudra Shah')
                break
            else:
                print('Okay, Terminating you booking........Thanks for talking with Disneyland Bot powered by Rudra Shah')
                break
        else:
            print('\n>>Invalid input back to main chat \n')
    else:
        print('\n>>Sorry i have not learn\'t that yet.......Try something like\n"HELLO"\n"What can you do"\n"Book ticket"\n')

print('Thank\'s for using DisneyLand Bot powered by Rudra Shah\n')