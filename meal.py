def main():

    checkTime = input("What time is it?  ")

    if checkTime == "":
        return

    else:

        time = convert(checkTime)
        time = round(time, 2)
        # print(time)

        if time >= 7.00 and time  <= 8.00:
            print("breakfast time")

        elif time >= 12.00 and time <= 13.00:
            print("lunch time")

        elif time >= 18.00 and time <= 19.00:
            print("dinner time")

        else:
            print("")


def convert(time):
    # if time == "":
    #     print("")
    # else:
        time = time.split(":")
        hours = int(time[0])
        minutes = float(time[1])
        minutes = minutes * 1.66
        minutes = round(minutes / 100, 2)
        # print(minutes)

        return hours + minutes

if __name__ == "__main__":
    main()