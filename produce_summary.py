

def melon_report(day, info):
    """ Function which accesses a list of delivery information and prints out the details"""

    print(f"Day {day}")
    the_file = open(info)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()
melon_report(1, "um-deliveries-20140519.txt")
melon_report(2, "um-deliveries-20140520.txt")
melon_report(3, "um-deliveries-20140521.txt")


