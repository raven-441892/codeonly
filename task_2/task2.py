import sys
 
with open (sys.argv[1],"r") as file1 :
    #value initialization
    cat_count=0
    other_cat=0
    Total_time=0
    entry_time=[]
    exit_time=[]
    our_cat_enter=[]
    our_cat_exit=[]
    our_cat_time=0

#reads every line of file and counts how many times our cat entered and makes 2 list of our cat entry and exit time

    for line in file1:
        if "OURS" in line:
            cat_count=cat_count+1
            parts=line.split(',')
            our_cat_enter.append(int(parts[1]))
            our_cat_exit.append(int(parts[2]))
        
#counts the number of times the neighbour cat entered        
        if "THEIRS" in line:
            other_cat=other_cat+1


    file1.seek(0)   #take the pointer back to first line again
    

#cretes 2 list that adds entry and exit time of all cata         
    for line in file1:
        parts=line.split(',')
        if len(parts)>=3:
            entry_time.append(int(parts[1]))
            exit_time.append(int(parts[2]))

#calculates total time spend by all cats in the house
    for i in range(len(entry_time)):
        Total_time+=exit_time[i]-entry_time[i]
        hr=Total_time//60
        min=Total_time%60

#calculates time spend by our cat in the house           
    for i in range(len(our_cat_enter)):
        our_cat_time+=our_cat_exit[i]-our_cat_enter[i]
        hour=our_cat_time//60
        mins=our_cat_time%60
        
#calculates average time of visit by our cats
    avg_visit=int(our_cat_time/cat_count)

#calculates the longest and shortest time spend by our cats   
    longest=0       #value initialize as longest time must be sth above 0 mins or hours
    shortest=our_cat_exit[0]-our_cat_enter[0]      #value initialization as first time interval, as shortest could be as low as 1 min which could be selected through value swapping
    for i in range(len(our_cat_enter)):
        interval=our_cat_exit[i]-our_cat_enter[i]
        if interval>longest:
            longest=interval
        if interval<shortest:
            shortest=interval
            
#converts into hour and minutes 
    longest_hr=longest//60
    longest_min=longest%60
    shortest_hr=shortest//60
    shortest_min=shortest%60

        
    file1.close()   #file closing
    
#Output display
    print("Log File Analyasis")
    print("=====================")    
    print(f"Cat Visits: {cat_count}")
    print(f"Other Cats: {other_cat} ")   
    print(f"Total time in House by our cats and neighbours as well: {hr} hours,{min} minutes")
    print(f"Total time in House by our cats: {hour} hours,{mins} minutes")
    print(f"Average visit length of our cats: {avg_visit} minutes")
    if longest_hr>0:
        print(f"Longest visit: {longest_hr} hours, {longest_min} minutes")
    else:
        print(f"Longest visit: {longest_min} minutes")
    
    print(f"Shortest visit: {shortest_min} minutes")
