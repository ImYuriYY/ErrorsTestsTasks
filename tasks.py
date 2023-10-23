# TASK 1
def num(digit):
    try:
        digit = float(digit)
        if (digit > 0):
            return ("Positive")
        elif(digit < 0):
            return ("Negative")
        else:
            return ("Zero")
    except TypeError:
        return("Error! TypeError!")
    except ValueError:
        return("Error! ValueError")
    except BaseException:
        return("Unknown Error!")



# TASK 2

def even_or_odd(digit):
    try:
        digit = float(digit)
        if(digit % 2 == 0):
            return "Even"
        else:
            return "Odd"
    except TypeError:
        return("Error! TypeError!")
    except ValueError:
        return("Error! ValueError!")
    except BaseException:
        return("Unknown Error!")




# TASK 3

def digit_count(digit):
    try:
        digit = int(digit)
        digit = str(digit)
        result = len(digit)
        return result
    except ValueError:
        return "Error! ValueError!"
    except TypeError:
        return "Error! TypeError!"
    except BaseException:
        return "Unknown Error!"





# TASK 4
def array_sum(arr):
    try:
        result = 0
        for i in range(len(arr)):
            arr[i] = int(arr[i])
            result += arr[i]
        return result

    except ValueError:
        return "Error! ValueError!"
    except TypeError:
        return "Error! TypeError!"
    except BaseException:
        return "Unknown Error!"






# TASK 5

def str_numbers_sum(st):
    try:
        sum = 0
        st = st.split(",")
        for i in range(len(st)):
            st[i] = int(st[i])
            sum += st[i]
        return sum
    except ValueError:
        return "Error! ValueError!"
    except TypeError:
        return "Error! TypeError!"
    except BaseException:
        return "Unknown Error!"
    








# Задание 1

def user_date(date):
    try:
        date = date.split("-")
        for i in range(len(date)):
            date[i] = int(date[i])
        year = str(date[0])
        month = str(date[1])
        day = str(date[2])
        resultTurp = (day, month, year)
        return resultTurp
    except ValueError:
        return "Error! ValueError!"
    except TypeError:
        return "Error! TypeError!"
    except BaseException:
        return "Unknown Error!"





# Задание 2


def str_array_sum(arr):
    try:
        result = 0
        for i in range(len(arr)):
            arr[i] = float(arr[i])
            result += arr[i]
        return result 

    except ValueError:
        return "Error! ValueError!"
    except TypeError:
        return "Error! TypeError!"
    except BaseException:
        return "Unknown Error!"





# Задание 3

def half_array_sum(arr):
    if(len(arr) % 2 == 0 ):
        try:
            for i in range(len(arr)):
                arr[i] = int(arr[i])
            dividor = int(len(arr) / 2)
            sum_1 = 0
            sum_2 = 0
            for i in range(0, dividor):
                sum_1 += arr[i]
            for i in range(dividor, len(arr)):
                sum_2 += arr[i]
            return(f'result = {sum_1 / sum_2}')
        except ValueError:
            return "Error! ValueError!"
        except TypeError:
            return "Error! TypeError!"
        except BaseException:
            return "Unknown Error!"
    else:
        return "Ошибка! Количество элементов в списке должно быть чётным!"





# Задание 4
# dct1 = {
#      'a': 1,
#      'b': 2,
# }
# dct2 = {
#      'c': 3,
#      'd': 4,
# }
# result = {}
#
# print(dct1)

# for i in range(len(dct1)):
#      result[dct1[i]] = "A"
# print(result)









# Задание 5 (min/max)

def min_max_dict(arr):
    try:
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        maxDigit = max(arr)
        minDigit = min(arr)
        result = {
            'max': maxDigit,
            'min': minDigit
        }
        return result
    except ValueError:
        return "Error! ValueError!"
    except TypeError:
        return "Error! TypeError!"
    except BaseException:
        return "Unknown Error!"