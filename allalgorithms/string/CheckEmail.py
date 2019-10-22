# -*- coding: UTF-8 -*-
#
# Check email
# The All ▲lgorithms library for python
#
# Contributed by: Natan Lucena
# Github: @NatanLucena
#

import re 
  
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
 
def check(email):  
  
    if(re.search(regex,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")
