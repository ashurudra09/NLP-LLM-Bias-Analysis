def in_list(output, ex_list):
    for item in ex_list:
        if item in output:
            return True
    return False


def get_bias_sq(num_list):
    ans = 0
    for num in num_list:
        # print(num)
        ans += round(num**2,8)
    ans = round(ans**0.5,8)
    return ans
