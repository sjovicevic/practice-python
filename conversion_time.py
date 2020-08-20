def timeConversion(s):
    #
    # Write your code here.
    #

    ls = s.split(':')
    part = ls[2]
    result = ""
    am_pm = part[2:4]
    if am_pm == 'AM':
        result = f"{ls[0]}:{ls[1]}:{part[0:2]}"
    elif am_pm == "PM":
        result = f"{int(ls[0])+12}:{ls[1]}:{part[0:2]}"
    return result


print(timeConversion('01:40:30PM'))