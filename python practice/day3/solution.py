n = int(input())
###########################################################
#  The input should be in the range of 1 to 100           #  
#  according to the constraints defined                   #
#  in the problem description                             #
#  but test file generates greater numbers in some cases  #
#  due to max is 100000 instead of 100                    #
###########################################################
#if( 1 <= n <= 100) :
if(n % 2 == 1) :
	print("Weird")
elif(2 <= n <= 5) :
	print("Not Weird")
elif(6 <= n <= 20) : 
	print("Weird")
elif(20 < n) : 
	print("Not Weird") 		
#else :
#	print("Your input is invalid!")