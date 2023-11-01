from datetime import datetime
from datetime import timedelta
import ast

def print_schedule(output):
    # write output to file
    with open("output.txt", 'a') as file:
        file.writelines(output)
        file.close()


def schedule(person1_busy_Schedule, person1_work_hours, person2_busy_Schedule, person2_work_hours, duration):
    # convert inputs to datetime objects
    format = "%H:%M"
    res = eval(person1_work_hours)
    #print(person1_busy_Schedule)
    #print(person1_work_hours)
    workInput1 = [datetime.strptime(x, format) for x in res]
    res1 = person1_busy_Schedule.replace("[", "")
    res1 = res1.replace(']', "")
    res1 = res1.replace(',', "")
    res1 = res1.replace('\n', "")
    res1 = res1.replace('\'', "")
    res1 = res1.replace('\ufeff', "")
    li = list(res1.split(" "))
    t1 = True
    busyInput1 = []
    while t1:
        li1 = []
        if len(li) == 0:
            t1 = False
            break
        li1.append(datetime.strptime(li[0], format))
        li1.append(datetime.strptime(li[1], format))
        li.remove(li[0])
        li.remove(li[0])
        busyInput1.append(li1)
    #busyInput1 = [[datetime.strptime(x, format)
                   #for x in y] for y in res2]
    res = eval(person2_work_hours)
    workInput2 = [datetime.strptime(x, format) for x in res]
    
    res1 = person2_busy_Schedule.replace("[", "")
    res1 = res1.replace(']', "")
    res1 = res1.replace(',', "")
    res1 = res1.replace('\n', "")
    res1 = res1.replace('\'', "")
    res1 = res1.replace('\ufeff', "")
    li = list(res1.split(" "))
    t1 = True
    busyInput2 = []
    while t1:
        li2 = []
        if len(li) == 0:
            t1 = False
            break
        li2.append(datetime.strptime(li[0], format))
        li2.append(datetime.strptime(li[1], format))
        li.remove(li[0])
        li.remove(li[0])
        busyInput2.append(li2)
    #busyInput2 = [[datetime.strptime(x, format)
                   #for x in y] for y in person2_busy_Schedule]

    # find min time for work hours
    start_time = max(workInput1[0], workInput2[0])
    end_time = min(workInput1[1], workInput2[1])

    # create an array of unavailable time from the two inputs and sort it
    unavailable_time = busyInput1 + busyInput2
    unavailable_time.sort()
    available_time = []
    duration1 = int(duration)
    # find the time intervals when all members are available
    if (unavailable_time[0][0] - start_time >= timedelta(minutes=duration1)):
        available_time.append((start_time, unavailable_time[0][0]))

    for i in range(1, len(unavailable_time)):
        time_difference = unavailable_time[i][0] - unavailable_time[i-1][1]
        if (time_difference >= timedelta(minutes=duration1)):
            available_time.append(
                (unavailable_time[i-1][1], unavailable_time[i][0]))

    if (end_time - unavailable_time[len(unavailable_time) - 1][1] >= timedelta(minutes=duration1)):
        available_time.append(
            (unavailable_time[len(unavailable_time) - 1][1], end_time))

    # convert datetime objects back into time strings to display
    output = [[i.strftime(format) for i in l] for l in available_time]

    # send to print_schedule function to print out onto an output file
    print(output)
    output1 = str(output) + '\n'
    return output1
    #print_schedule(output1)
    #print(output)


def main():
    # Read input from file
    with open("input.txt", 'r') as file:
        content = file.readlines()
        file.close()
    result =[]
    compareTime = True
    while compareTime:
        if len(content) == 0:
            compareTime = False
            break
        elif len(content) == 1:
            compareTime = False
            content.remove(content[0])
            break
        else:
            person1_busy_Schedule = content[0]
            person1_work_hours = content[1]
            person2_busy_Schedule = content[2]
            person2_work_hours = content[3]
            duration = content[4]
            # prepare the next input
            content.remove(content[5])
            output = schedule(person1_busy_Schedule, person1_work_hours,
                     person2_busy_Schedule, person2_work_hours, duration)
            result.append(output)
            content.remove(content[0])
            content.remove(content[0])
            content.remove(content[0])
            content.remove(content[0])
            content.remove(content[0])
    print_schedule(result)

if __name__ == "__main__":
    main()
