dump = False
import fileinput
def applyDoubleAndAddMethod(x0, y0, k, a, b, mod):
	
	x_temp = x0
	y_temp = y0
	
	kAsBinary = bin(k) #0b1111111001
	kAsBinary = kAsBinary[2:len(kAsBinary)] #1111111001
	#print(kAsBinary)
	
	for i in range(1, len(kAsBinary)):
		currentBit = kAsBinary[i: i+1]
		#always apply doubling
		x_temp, y_temp = pointAddition(x_temp, y_temp, x_temp, y_temp, a, b, mod)
		
		if currentBit == '1':
			#add base point
			x_temp, y_temp = pointAddition(x_temp, y_temp, x0, y0, a, b, mod)
	
	return x_temp, y_temp

def pointAddition(x1, y1, x2, y2, a, b, mod):
	
	if x1 == x2 and y1 == y2:
		#doubling
		beta = (3*x1*x1 + a) * (findModularInverse(2*y1, mod))
	
	else:
		#point addition
		beta = (y2 - y1)*(findModularInverse((x2 - x1), mod))
	
	x3 = beta*beta - x1 - x2
	y3 = beta*(x1 - x3) - y1
	
	x3 = x3 % mod
	y3 = y3 % mod
	
	while(x3 < 0):
		x3 = x3 + mod
	
	while(y3 < 0):
		y3 = y3 + mod
	
	return x3, y3

def findModularInverse(a, mod):
			
	while(a < 0):
		a = a + mod
	
	#a = a % mod
	
	x1 = 1; x2 = 0; x3 = mod
	y1 = 0; y2 = 1; y3 = a
	
	q = int(x3 / y3)
	t1 = x1 - q*y1
	t2 = x2 - q*y2
	t3 = x3 - (q*y3)
	
	if dump == True:
		print("q\tx1\tx2\tx3\ty1\ty2\ty3\tt1\tt2\tt3")
		print("----------------------------------------------------------------------------")
		print(q,"\t",x1,"\t",x2,"\t",x3,"\t",y1,"\t",y2,"\t",y3,"\t",t1,"\t",t2,"\t",t3)
	
	while(y3 != 1):
		x1 = y1; x2 = y2; x3 = y3
		
		y1 = t1; y2 = t2; y3 = t3
		
		q = int(x3 / y3)
		t1 = x1 - q*y1
		t2 = x2 - q*y2
		t3 = x3 - (q*y3)
		
		if dump == True:
			print(q,"\t",x1,"\t",x2,"\t",x3,"\t",y1,"\t",y2,"\t",y3,"\t",t1,"\t",t2,"\t",t3)
			print("----------------------------------------------------------------------------")
			print("")
	
	while(y2 < 0):
		y2 = y2 + mod
	
	return y2

def main():
    with open(r"C:\Users\bklee\Documents\School\Senior Year\Crypto\HW3+HW4\a4.cipher.txt", "r") as file:
        for _,line in enumerate(file):
            tokens = line.split(" ")

            cipher = [int(tokens[0]),int(tokens[1])]

            halfmask = [int(tokens[2]),int(tokens[3])]

            #random prime
            p = 73482936276013145955565144225861612903052378488799025581459884388790895646531

            #Curve Parameters
            A = 106232669604492000952101983011424051981376980857635143588066911520770063114189    
            B = 76587977420977035044598204053610304596633008638205335306823124689977025819271

            #random point (Gx, Gy)
            G = [10653634968474602131259680612117761410240294893518819057928307519545438935105,53590057826264431726814016302376375223987987950117371742659725930948430562791]

            #Public Point = N*G
            P = [28532308240163403308957388634927833383486854937647900059668124240434058298343,69104332354999776650513976089584444069941586735957501584816228392545085961665]

            #secret key 
            N = 3

            fullmask = applyDoubleAndAddMethod(halfmask[0], halfmask[1], N, A, B, p)

            neg_fullmask = (fullmask[0], -fullmask[1])

            plainttext_point = pointAddition(cipher[0], cipher[1], neg_fullmask[0], neg_fullmask[1], A, B, p)

            print(chr(plainttext_point[0]), end='')

if __name__ == "__main__":
    main()