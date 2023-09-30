def main():
    print("Please choose your flight destination: ")
    print("1. Hawaii")
    print("2. Bahamas")
    print("3. Cancun")
    ch=int(input())
    
    if(ch==1):
        destination="Hawaii"
    elif(ch==2):
        destination="Bahamas"
    else:
        destination="Cancun"
    print("You have chosen",destination, "as your flight destination")
    carrier()
    
def carrier():
    print("Which airline would you like to fly with? ")
    print("1. US Air")
    print("2. Delta")
    print("3. United")
    ch=int(input())
    
    if ch==1:
        airline="US Air"
    elif ch==2:
        airline="Delta"
    else:
        airline="United"
    print("You have chosen ",airline,"airlines")
    fare=int(input("What is the airfare for a round trip? "))
    passenger(fare);
    
def passenger(fare):
    print("How many people will be flying? ")
    print("1. One person")
    print("2. Two people")
    print("3. Three people")
    print("4. Four people")
    ch=int(input())
    
    if ch==1:
        ppl="One person"
    elif ch==2:
        ppl="Two people"
    elif ch==3:
        ppl="Three people"
    else:
        ppl="Four people"
    print("There will be",ppl, "flying")
    age=int(input("How many of the passengers are under 18? "))
    calculation(ppl,age,fare)
    
def calculation(ppl,age,fare):
    if ppl=="One person":
        choice=1
    elif ppl=="Two people":
        choice=2
    elif ppl=="Three people":
        choice=3
    else:
        choice=4
    choice=choice-age
    adultFare=choice*fare
    underAge=age*(fare-(fare*25/100))
    totalCost=underAge+adultFare
    print("Total airfare for adult passengers: $",adultFare)
    print("Total airfare for passengers under 18: $",underAge)
    print("Total fare for all passengers: $",totalCost)
    
if __name__=="__main__":
    main()