#!/usr/bin/env python
# include standard modules
import argparse
import sys

__author__ = "Pranav Goel"
__copyright__ = "Copyright 2019"
__credits__ = ["Pranav Goel"]
__license__ = "Apache 2.0"
__version__ = "1.0.1"
__maintainer__ = "Pranav Goel"
__email__ = "pranavg4@illinois.edu"
__status__ = "Prototype"

def main():
  print("This is a program that helps convert to and from IEEE 754 floating point with binary.\n\nWhat makes this program different from others, is that it shows the work done as well.\n\nThis should make it easier for various homeworks where you have to show all the work.\n\nI hope this makes your life easier!\n\n-Pranav Goel\n\n")

  text = "This is a program that helps convert to and from IEEE 754 floating point with binary.\n\nWhat makes this program different from others, is that it shows the work done as well.\n\nThis should make it easier for various homeworks where you have to show all the work.\n\nI hope this makes your life easier!\n\n-Pranav Goel\n\n------------------------------------------------------------------------------\n\nUsage tips:\nWhen putting in a binary string that has spaces in it, make sure you put \"\" around it.\n\nFor example: 0100 0000 0100 1001 0000 1110 0101 0110 should be written as \"0100 0000 0100 1001 0000 1110 0101 0110\" instead.\n\nThis is because the program would otherwise read the string as multiple arguments."

  CLIUsed = False

  # initiate the parser
  parser = argparse.ArgumentParser(description = text)

  # add long and short argument
  parser.add_argument("--floatToBinary", "-ftb", help="Convert a Float to Binary")
  parser.add_argument("--binaryToFloat", "-btf", help="Convert a Binary String to a Float")

  # read arguments from the command line
  args = parser.parse_args()

  if args.floatToBinary:
    checkValid(True, args.floatToBinary)
    print("Converting %s from a Float to a Binary" % args.floatToBinary)
    floatToBinary(args.floatToBinary)
    CLIUsed = True
  if args.binaryToFloat:
    y = "".join(str(args.binaryToFloat).split(" "))
    print("Making sure there are no spaces:\n\n%s\n\n\n\n\n\n\n\n\n\n\n\nResult:\n\n" % y)
    checkValid(False, y)
    print("Converting %s from a Binary to a Float" % y[:32])
    binaryToFloat(y)
    CLIUsed = True

  if(not CLIUsed):
    choice = str(input("To convert from Binary to Float type \"0\".\n\nTo convert from Float to Binary type \"1\"\n\n"))
    if (choice == "0"):
      print("You are converting from Binary to Float")
      binary = "".join(str(input("Type your Binary String:\n")).split(" "))
      print("Making sure there are no spaces:\n\n%s\n\n\n\n\n\n\n\n\n\nResult:\n\n" % binary)
      checkValid(False, binary)
      binaryToFloat(binary)
    elif(choice == "1"):
      print("You are converting from Float to Binary")
      f = str(input("Type in your float:\n"))
      checkValid(True,f)
      zero = checkZero(f)
      if(zero[0]):
        if(zero[1]):
          print("Sign will be 1 which = - as it is -0. Since it is zero there is no need to do work as the result will always be 0. So your answer is:\n\n1 00000000 00000000000000000000000")
        else:
          print("Sign will be 0 which = + as it is 0. Since it is zero there is no need to do work as the result will always be 0. So your answer is:\n\n0 00000000 00000000000000000000000")
      else:
        floatToBinary(f)
    else:
      sys.exit("You did not choose a valid option. Please try again.")
def checkZero(n):
  checks = [False,False]
  if(float(n) == 0):
    checks[0] = True
    if("-" in n):
      checks[1] = True
  return checks
def checkValid(ftb, string):
  s = string
  valid = True
  if(ftb):
    try:
      float(s)
    except ValueError:
      valid = False
  else:
    bCheck = set(s)
    b = {'0', '1'}
    if b == bCheck or bCheck == {'0'} or bCheck == {'1'}:
      valid = True
    else:
      valid = False
    if(len(string)<32):
      sys.exit("Value is less than 32 bits, please try again")
    elif(len(string)>32):
      s = s[:32]
      print("Cutting out any bits after 32 bits so that string is 32 bits.\nYour new string is %s" % s)
  if(not valid):
    sys.exit("Value not a binary string or a float please try again")

def floatToBinary(num):
  test = float(num)
  if(int(test) == test and isinstance(test, float)):
    floatNum = float(num)
  else:
    if("0." not in num):
      floatNum = "0" + num
    else:
      floatNum = num
  floatString = (str)(floatNum)
  print(floatString)
  normNum = ""
  arrayFloat = floatString.split('.')
  sign = "+"
  for x in arrayFloat[0]:
    if (x == '-'):
      sign = "-"
    else:
      normNum += x
  binNormNum = bin(int(normNum))[2:]
  print("Sign: %s" % sign)
  print("Before decimal point: %s" % normNum)
  print("Before decimal point as binary: %s" % binNormNum)
  res = mantissa(str(arrayFloat[1]))
  print("Value after decimal point: %s" % res)
  decibin = str(binNormNum) + "." + res
  print("Results in: %s" % decibin)
  normalized = normalize(str(binNormNum),str(res))
  print("Normalized Value: %s\nPower: %s\nFinal Exponent: %s\nMantissa: %s" % (normalized[0],normalized[1],normalized[2],normalized[3]))
  exponentBin = str(bin(int(normalized[2])))[2:]
  if (len(exponentBin) < 8):
    exponentBin = "0"*(8-len(exponentBin)) + str(bin(int(normalized[2])))[2:]

  print("Exponent in Binary: %s" % exponentBin)
  numZeros = 23 - len(normalized[3])
  zeroString = ""
  for y in range(0,numZeros):
    zeroString += "0"
  if (sign == "+"):
    answer = "0" + exponentBin + normalized[3] + zeroString
  else:
    answer = "1" + exponentBin + normalized[3] + zeroString
  print("The answer is: %s %s %s" % (answer[:-31],answer[1:9],answer[9:32]))

def mantissa(numCon):
  stop = 1
  num = float("." + numCon)
  zoro = ""
  valstring = ""
  val = num*2
  count = 0
  countOn = False
  if(num == 0):
    print("Since the value after the decimal is 0, there is no need to do any work as it will always be 0.")
    zoro = "0"*25
  else:
    while ((val != stop) and (count != 27)):
      if("1" in zoro):
          countOn = True
      if(countOn):
          count += 1
      if(val > 1):
        zoro += "1"
        valstring = str(val).split(".")
        valNext = float("." + valstring[1])*2
      else:
        zoro += "0"
        valNext = val *2
      print("Work:\n%s * 2 = %s\nBuilding Binary: %s" % (val/2,val,zoro)
      )
      val = valNext
      #print("Building Binary: %s" % zoro)
    zoro += "1"
    if(len(zoro) < 25):
      print("0.5 * 2 = 1\nBuilding Binary: %s" % (zoro))
  return(zoro)

def normalize(binStart, binEnd):
  start = binStart
  end = binEnd
  count = 0
  startLen = len(binStart)
  endLen = len(binEnd)
  normalize = "1"
  normalize += "."
  if(start != "0"):
    power = startLen - 1
    normalize += start[1:]
    normalize += end
  else:
    for x in end:
      if (x == "0"):
        count += 1
      else:
        break
    normalize += end[(count+1):]
    power = (count + 1) * -1
  mantissaA = normalize.split(".")
  mantissa = mantissaA[1][:24]
  ct = 22
  if(endLen > 23 and mantissa[23] == "1"):
      one = True
  elif(mantissa[endLen - 1] == "1"):
      one = True
  else:
      one = False
  mantissa = mantissa[:23]
  for x in reversed(mantissa):
      if(one):
          if(x == "1"):
              mantissa = mantissa[:ct] + mantissa[ct:ct+1].replace("1","0")+ mantissa[ct+1:]
              one = True
          else:
              mantissa = mantissa[:ct] + mantissa[ct:ct+1].replace("0","1") + mantissa[ct+1:]
              one = False
              break
          ct = ct - 1
      else:
        break
  exponent = power + 127
  result = [normalize,power,exponent,mantissa[:23]]
  return result

def binaryToFloat(binary):
  binaryString = binary[:32]
  if (len(binaryString) < 32):
    print("You didn't put a 32 bit string")
  else:
    sign,exponent,mantissa = binaryString[:1], binaryString[1:9],binaryString[9:32]
  exponentFinal = int(exponent,2) - 127
  print("Exponent is %s in Binary\nIn Decimal it is %s\nTo get to final exponent do %s - 127 = %s.\nThe exponent is %s" % (exponent,int(exponent,2),int(exponent,2),exponentFinal,exponentFinal))
  work = ["0"]*23
  workM = 0
  finalWork = ""
  mantissaL = list(mantissa)
  for x in range(0,len(mantissa)):
    work[x] = "(" + mantissaL[x] + " x 2^" + str((x+1)*-1) +")"
    workM += int(mantissaL[x]) * (2**((x+1)*-1))
  finalWork = " + ".join(work)
  print ("In binary, the mantissa is: %s\n\nConverting to decimal:\n%s = %s\n\nSo the mantissa is: %s" % (mantissa,finalWork,workM,workM))
  if(sign == "0"):
    signChar = "+"
  else:
    signChar = "-"
  print("\nThe sign is %s => %s" % (sign,signChar))
  print("\nIn the formula you have:\n\n((-1)^%s) x 1.%s x (2^%s)" % (sign,str(workM)[2:],exponentFinal))
  center = float("1." + str(workM)[2:])
  FinalResult = ((-1)**int(sign))*center*(2**int(exponentFinal))
  print("\nThe answer is: %s" % FinalResult)

if __name__ == '__main__':
    main()
