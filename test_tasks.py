from tasks import *
import pytest

# TASK 1

# @pytest.mark.parametrize('x, exp_res', [
#     (3, "Positive"),
#     (-3, "Negative"),
#     (0, "Zero")
# ])
# def test_num(x, exp_res):
#     assert num(x) == exp_res




# TASK 2

# @pytest.mark.parametrize('x, exp_res', [
#     (4, "Even"),
#     (3, "Odd")
# ])
# def test_even_or_odd(x, exp_res):
#     assert even_or_odd(x) == exp_res





# TASK 3

# digit = 151235
# @pytest.mark.parametrize('x, exp_res', [
#     (digit, len(str(digit)))
# ])
# def test_digit_count(x, exp_res):
#     assert digit_count(x) == exp_res





# TASK 4

# array = [1,2,3,4,5]
# @pytest.mark.parametrize('x, exp_res', [
#     (array, array_sum(array))
# ])
# def test_array_sum(x, exp_res):
#     assert array_sum(x) == exp_res






# TASK 5

# st = '12,2431,3'
# @pytest.mark.parametrize('x, exp_res', [
#     (st, str_numbers_sum(st))
# ])
# def test_str_numbers_sum(x, exp_res):
#     assert str_numbers_sum(x) == exp_res






# Задание 1

# userDate = '2020-10-10'

# @pytest.mark.parametrize('x, exp_res', [
#     (userDate, user_date(userDate))
# ])
# def test_user_date(x, exp_res):
#     assert user_date(x) == exp_res





# Задание 2

# array = ['1','2','3','4','5']

# @pytest.mark.parametrize('x, exp_res', [
#     (array, str_array_sum(array))
# ])
# def test_str_array_sum(x, exp_res):
#     assert str_array_sum(x) == exp_res






# Задание 3

# array = [1,2,3,4,5,6]

# @pytest.mark.parametrize('x, exp_res', [
#     (array, half_array_sum(array))
# ])
# def test_shalf_array_sum(x, exp_res):
#     assert half_array_sum(x) == exp_res







# Задание 5

# arrayOfNumbers = [1,2,3,4,5,6,7,8,9,0]

# @pytest.mark.parametrize('x, exp_res', [
#     (arrayOfNumbers, min_max_dict(arrayOfNumbers))
# ])
# def test_min_max_dict(x, exp_res):
#     assert min_max_dict(x) == exp_res