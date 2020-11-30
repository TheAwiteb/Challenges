#Create a function that takes a string (IPv4 address in standard dot-decimal format) and returns True if the IP is valid or False
#if it's not. For information on IPv4 formatting, please refer to the resources in the Resources tab.

#Examples
'''is_valid("1.2.3.4") ➞ True

is_valid("1.2.3") ➞ False

is_valid("1.2.3.4.5") ➞ False

is_valid("123.45.67.89") ➞ True

is_valid("123.456.78.90") ➞ False

is_valid("123.045.067.089") ➞ False'''

##Notes
#IPv6 addresses are not valid.
#Leading zeros are not valid ("123.045.067.089" should return False).
#You can expect a single string for every test case.
#Numbers may only be between 1 and 255.
#The last digit may not be zero, but any other might.

import numpy as np

def is_valid(ipv4 = ''):
    listIp = ipv4.split('.')
    if len(listIp) == 4:
        for i in listIp:
            try:
                num = int(i)
            except:
                return False
        for i in listIp:
            num = int(i)
            old = i
            new = np.uint8(old)
            if str(old) == str(new):
                if num >= 0 and num <= 255:
                    pass
                else:
                    return False
            else:return False

        return True
    else:
        return False
