def aboved(notes):
    ttnotes = len(notes)
    ttnotessup = 0
    for number in range(len(notes)):
        if notes[number] > 10 :
            ttnotessup += 1
    percentage = (ttnotessup / ttnotes) * 100
    #print(percentage) 
    round(percentage)
    return percentage
    
marks = [7 , 15.5 , 5.5 , 11 , 14 , 9 , 10 , 11.5 , 14 , 7 , 19]
marks_above_avg_percentage = aboved(marks)
#marks_above_avg_percentage = 0
print(marks_above_avg_percentage)
print('hello')