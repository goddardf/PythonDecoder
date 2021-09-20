import sys
import os
import string

'''file = sys.argv[1]
outfile = sys.argv[2]
filenam = open(file, "rb")
#filename =file.readlines()
f = open(outfile, "w")
'''
reg = [0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0]
instructions = []
temp = []
opcodeStr = [] # <type list> ; [invalid, add, sw]
instrSpaced = []
arg1 = []
arg2 = []
arg3 = []
arg1Str = []
arg2Str = []
arg3Str = []
mem = []
binMem = []
opcode = []
memdata = []


opstr = []
rmstr = []
shamtstr = []
rnstr = []
rdstr = []
space = ' '
memnum = 92
x =32
j = 1
for i in range(len(sys.argv)): #could not get this to work
    if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
        inputFileName = sys.argv[i + 1]
        #print inputFileName
    elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
        outputFileName = sys.argv[i + 1]


filenam = open(inputFileName, "rb")
#filename =file.readlines()
f = open(outputFileName + ".txt", "w")
#fileS = open(outputFileName2, "w")

class Dissemble:
    def run(self):
        global instructions
        global temp
        global opcodeStr  # <type list> ; [invalid, add, sw]
        global instrSpaced
        global arg1
        global arg2
        global arg3
        global arg1Str
        global arg2Str
        global arg3Str
        global mem
        global binMem
        global opcode
        global opstr
        global rmstr
        global shamtstr
        global rnstr
        global rdstr
        global space
        global memnum
        global x
        global memdata

        specialmask = 0x1FFFFF #B mask

        rnMask = 0x3E0 #1st arg     ARM Rn
        rmMask = 0x1F0000 #2nd arg  ARM rm
        rdMask = 0x1F #destination  ARM rd
        imMask = 0x3FFC00 #ARM I Immediat
        shmtMask = 0xFC00 #ARM ShAMT
        addrMask = 0x1FF000 #ARM address for ld and st
        addr2Mask = 0xFFFFE0 #addr for CB format
        imsftMask = 0x600000 #shift for IM format
        imdataMask = 0x1FFFE0 #data for IM type
        last5mask = 0x7c0
        negBitMask =0x800
        negchange = 0b1111111111111111111
        negchangeb = 0b111111111111111111111


        #doesnt work
        #def encrypt(string, length):
            #return '\t'.join(string[length])

        #def immBitTo32BitConverter(num, bitsize):
            #if bitsize == 12:
                #negBitMask = 0x800
               # extendMask = 0xFFFFF000

        def bin2StringSpaced(s):  # changed num to s
            spacedStr = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
            return spacedStr

        #opcode.append((int(instruct, base=2)) >> 21)
        def bin2StringSpacedR(s):  # convert bin to string spaced out
            #example output
            #10001011000 00010 000000 00001 00011
            spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
            return spacedStr

        def bin2StringSpacedI(s):  # convert bin to string spaced out
            #example output
            #1001000100 000110010000 00010 00001
            spacedStr = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
            return spacedStr

        def bin2StringSpacedD(s):  # convert bin to string spaced out
            #example output
            #11111000000 001100100 00 00010 00001
            spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
            return spacedStr


        def bin2StringSpacedB(s):  # convert bin to string spaced out
            #example output
            #000101 00000000000010011100010000
            spacedStr = s[0:6] + " " + s[6:32]
            return spacedStr


        def bin2StringSpacedCB(s):  # convert bin to string spaced out
            #example output
            #10110100 0000000000000000011 10011
            spacedStr = s[0:8] + " " + s[8:27] + " " + s[27:32]
            return spacedStr


        def bin2StringSpacedIM(s):  # convert bin to string spaced out
            #example output
            #110100101 00 0000000011111111 00001
            spacedStr = s[0:9] + " " + s[9:11] + " " + s[11:27] + " " + s[27:32]
            return spacedStr

        def bin2StringSpacedNOP(s):
            #example output
            #11111111111111111111111111111111
            spacedStr = s[0:32]
            return spacedStr
        #instructions = [line.rstrip() for line in open(inputFileName, 'rb')]
        for instruct in filenam.readlines():
                # print(instructions)
                # opcode.append()
                # b = instructions.read
                # instructions >> b'21'
            #temp.append(str(instructions))
            instructions.append(instruct)
            opcode.append((int(instruct, base=2)) >> 21)
        #print(opcode)
        #print(instructions)
        k = 0

        #with open('pythonteam7_output1.txt', 'w')as f:
            #print('Filename:', filename, file=f)
        for i in range(len(opcode)):
            #if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):len(sys.argv)
            #opcode.append((int(instructions[i], base=2)) >> 21)
            #print(opcode[i])
            memnum = memnum + 4
            mem.append(memnum)

            if opcode[i] == 1112:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("ADD")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", R" + str(arg2[i]))
                #print(arg1, arg2, arg3, arg1Str, arg2Str, arg3Str)

            elif opcode[i] == 1624:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("SUB")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", R" + str(arg2[i]))

            elif opcode[i] == 1104:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("AND")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", R" + str(arg2[i]))

            elif opcode[i] == 1360:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("ORR")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", R" + str(arg2[i]))

            elif opcode[i] == 160 or opcode[i] == 191: #needs neg
                instrSpaced.append(bin2StringSpacedB(instructions[i]))
                opcodeStr.append("B")
                if (int(instructions[i], base=2) & negBitMask) !=0:
                    #arg1.append(~((int(instructions[i], base=2) & negBitMask) >> 7)+1)
                    arg1.append(~(((int(instructions[i], base=2) & specialmask) >> 0) ^ negchangeb))
                    #print arg1[i]
                else:
                    arg1.append((int(instructions[i], base=2) & specialmask) >> 0)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\t#" + str(arg1[i]))
                arg2Str.append(" ")
                arg3Str.append(" ")

            elif opcode[i] == 1160 or opcode[i] == 1161:
                instrSpaced.append(bin2StringSpacedI(instructions[i]))
                opcodeStr.append("ADDI")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & imMask) >> 10)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", #" + str(arg2[i]))

            elif opcode[i] == 1672 or opcode[i] == 1673:
                instrSpaced.append(bin2StringSpacedI(instructions[i]))
                opcodeStr.append("SUBI")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & imMask) >> 10)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", #" + str(arg2[i]))

            elif opcode[i] == 1986:
                instrSpaced.append(bin2StringSpacedD(instructions[i]))
                opcodeStr.append("LDUR")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & addrMask) >> 12)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", [R" + str(arg1[i]))
                arg3Str.append(", #" + str(arg2[i]) + "]")

            elif opcode[i] == 1984:
                instrSpaced.append(bin2StringSpacedD(instructions[i]))
                opcodeStr.append("STUR")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & addrMask) >> 12)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", [R" + str(arg1[i]))
                arg3Str.append(", #" + str(arg2[i]) + "]")

            elif opcode[i] == 1440 or opcode[i] == 1441 or opcode[i] == 1442 or opcode[i] == 1443 or opcode[i] == 1444 \
                    or opcode[i] == 1445 or opcode[i] == 1446 or opcode[i] == 1447: #neg
                instrSpaced.append(bin2StringSpacedCB(instructions[i]))
                opcodeStr.append("CBZ")
                if (int(instructions[i], base=2) & negBitMask) !=0:
                    arg1.append(~(((int(instructions[i], base=2) & addr2Mask) >> 5) ^ negchange))
                    #print arg1[i]
                else:
                    arg1.append((int(instructions[i], base=2) & addr2Mask) >> 5)
                arg2.append((int(instructions[i], base=2) & addr2Mask) >> 32)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", #" + str(arg1[i]))
                arg3Str.append(" ")#needs to be removed not printed

            elif opcode[i] == 1448 or opcode[i] == 1449 or opcode[i] == 1450 or opcode[i] == 1451 or opcode[i] == 1452 \
                    or opcode[i] == 1453 or opcode[i] == 1454 or opcode[i] == 1455: #neg
                instrSpaced.append(bin2StringSpacedCB(instructions[i]))
                opcodeStr.append("CBNZ")
                if (int(instructions[i], base=2) & negBitMask) != 0:
                    arg1.append(~(((int(instructions[i], base=2) & addr2Mask) >> 5) ^ negchange))
                    #print arg1[i]
                else:
                    arg1.append((int(instructions[i], base=2) & addr2Mask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 32)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", #" + str(arg1[i]))
                arg3Str.append(" ")

            elif opcode[i] == 1684 or opcode[i] == 1685 or opcode[i] == 1686 or opcode[i] == 1687:
                instrSpaced.append(bin2StringSpacedIM(instructions[i]))
                opcodeStr.append("MOVZ")
                arg1.append((int(instructions[i], base=2) & imdataMask) >> 5)
                arg2.append((int(instructions[i], base=2) & imsftMask) >> 17)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", " + str(arg1[i]))
                arg3Str.append(", LSL " + str(arg2[i]))

            elif opcode[i] == 1940 or opcode[i] == 1941 or opcode[i] == 1942 or opcode[i] == 1943:
                instrSpaced.append(bin2StringSpacedIM(instructions[i]))
                opcodeStr.append("MOVK")
                arg1.append((int(instructions[i], base=2) & imdataMask) >> 5)
                arg2.append((int(instructions[i], base=2) & imsftMask) >> 17)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(",  " + str(arg1[i]))
                arg3Str.append(", LSL " + str(arg2[i]))

            elif opcode[i] == 1690:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("LSR")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & shmtMask) >> 10)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", # " + str(arg2[i]))

            elif opcode[i] == 1691:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("LSL")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & shmtMask) >> 10)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", # " + str(arg2[i]))

            elif opcode[i] == 1692:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("ASR")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & shmtMask) >> 10)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", # " + str(arg2[i]))

            elif opcode[i] == 2038 and (int(instructions[i], base=2) & specialmask) == 2031591:
                instrSpaced.append(bin2StringSpaced(instructions[i]))
                opcodeStr.append("BREAK")
                arg1.append(0)
                arg2.append(0)
                arg3.append(0)
                arg1Str.append("")
                arg2Str.append("")
                arg3Str.append("")
                #print "breaking"
                break

            elif opcode[i] == 1872:
                instrSpaced.append(bin2StringSpacedR(instructions[i]))
                opcodeStr.append("EOR")
                arg1.append((int(instructions[i], base=2) & rnMask) >> 5)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 16)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 0)
                arg1Str.append("\tR" + str(arg3[i]))
                arg2Str.append(", R" + str(arg1[i]))
                arg3Str.append(", R" + str(arg2[i]))

            # elif
            elif opcode[i] == 2047:
                instrSpaced.append(bin2StringSpacedNOP(instructions[i]))
                opcodeStr.append(int(instructions[i], base=2) - 4294967296)  # not right
                arg1.append((int(instructions[i], base=2) & rnMask) >> 32)
                arg2.append((int(instructions[i], base=2) & rmMask) >> 32)
                arg3.append((int(instructions[i], base=2) & rdMask) >> 32)
                arg1Str.append(" ")
                arg2Str.append(" ")
                arg3Str.append(" ")
            else:
                #instructions[i] == 0:  # this might still be wrong need to test more
                instrSpaced.append(bin2StringSpaced(instructions[i]))
                opcodeStr.append("NOP")
                arg1.append(0)
                arg2.append(0)
                arg3.append(0)
                arg1Str.append("")
                arg2Str.append("")
                arg3Str.append("")




        for i in range(len(opcode)):
            f.write(str(instrSpaced[i]))
            f.write('\t')
            f.write(str(mem[i]))
            f.write('\t')
            f.write(str(opcodeStr[i]))
            f.write('\t')
            f.write(str(arg1Str[i]))
            f.write(str(arg2Str[i]))
            f.write(str(arg3Str[i]))
            f.write('\n')
        #print mem

class Simulator:
    def run(self):
        global instructions
        global temp
        global opcodeStr  # <type list> ; [invalid, add, sw]
        global instrSpaced
        global arg1
        global arg2
        global arg3
        global arg1Str
        global arg2Str
        global arg3Str
        global mem
        global binMem
        global opcode
        global opstr
        global rmstr
        global shamtstr
        global rnstr
        global rdstr
        global space
        global memnum
        global x
        global reg
        global memdata
        k = 0
        p = 0
        cyclecount = 0
        opcounter = []
        doBranch = 0
        testreg = 0
        currentlenght = 0
        printdata = 0

        storedin = 0
        reglabel = 212

        with open(outputFileName + "_sim.txt", 'w') as fileS:

            while (opcodeStr[k] != 'BREAK'):
                #print int(arg1[k])
                #print int(arg2[k])
                #print int(arg3[k])
                #print opcodeStr[k]
                opcounter.append(k)
                if p == 1:
                    if doBranch != 0:
                        k = doBranch + k
                        doBranch = 0
                    else:
                        k = k + 1

                if str(opcodeStr[k]) == "B":
                    doBranch = arg1[k]
                    #print "b"

                elif str(opcodeStr[k]) == "CBZ":
                    #print "cbz"
                    j = 0
                    testreg = arg3[k]
                    if testreg == j:
                        doBranch = arg1[k]

                elif str(opcodeStr[k]) == "CBNZ":
                    #print "cbnz" R3 1 _
                    #cbnz R0, #-1
                    #cbnz arg3, #arg1
                    j = 0
                    testreg = arg3[k]
                    if reg[testreg] != j:
                        doBranch = arg1[k]


                elif opcodeStr[k] == "ADDI":
                    #print "yo"
                    j = int(arg1[k])
                    m = int(arg2[k])
                    returnreg = int(arg3[k])
                    #print j
                    #print m
                    reg[returnreg] = m + reg[j]

                elif str(opcodeStr[k]) == "SUBI":
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]
                    # print j
                    # print m
                    reg[returnreg] = reg[j] - m


                elif str(opcodeStr[k]) == "MOVZ":
                    #MOVZ: 16 bit pattern in arg3 register shifted left by either 0,16,32,48
                    # positions determined by 2 bit arg1 value and written into zeroed arg2 register
                    j = arg2[k] #shift
                    m = arg1[k] #imm
                    returnreg = arg3[k]
                    reg[returnreg] = m << j

                elif str(opcodeStr[k]) == "MOVK":
                    #MOVK: 16 bit pattern in arg3 register shifted left by either 0,16,32,48 positions determined
                    #by 2 bit arg1 value and written into  arg2 register leaving all other bits intact.  3, 1, 2
                    j = arg2[k]  # shift
                    m = arg1[k]  # imm
                    returnreg = arg3[k]
                    finalincrease = m << j
                    reg[returnreg] = finalincrease + reg[returnreg]


                elif str(opcodeStr[k]) == "LSR":
                    #LSR: This is a pattern shift. Whatever is in register is shifted right with zero fill. 3 1 2
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]
                    reg[returnreg] = reg[j] >> m

                elif str(opcodeStr[k]) == "STUR":
                    printdata = 1
                    returnreg = arg3[k] #first R
                    j = arg1[k] #second R
                    m = arg2[k] * 4 #immm
                    result = reg[j] + m #currently has 360
                    result = result - memnum #360 - final memory spot
                    result = result / 4 #how many data should be created 38
                    #print result
                    if currentlenght < result:
                        resultfix = result
                        for loop in range(result):
                            memdata.append(0)
                        tester = result % 8
                        while tester != 0 and tester < 8:
                            tester = tester + 1
                            resultfix = resultfix + 1
                            memdata.append(0)
                    memdata[result - 1] = reg[j]
                    currentlenght = resultfix




                elif str(opcodeStr[k]) == "LDUR":
                    returnreg = arg3[k]  # first R
                    j = arg1[k]  # second R
                    m = arg2[k] * 4  # immm
                    result = reg[j] + m  # currently has 360
                    result = result - memnum  # 360 - final memory spot
                    result = result / 4  # how many data should be created 38
                    reg[returnreg] = memdata[result - 1]


                elif str(opcodeStr[k]) == "LSL":
                    #LSL: Shift left arg2 positions adding zeros on the right. 3 1 2
                    j = arg1[k] #second r
                    m = arg2[k] #imm
                    returnreg = arg3[k] #return reg
                    reg[returnreg] = reg[j] << m

                elif str(opcodeStr[k]) == "ASR":
                    #ASR: This is  ">>" will divide by 2.
                    #ASR R4,R4, #2
                    #ars arg3, arg1, #arg2
                    j = arg1[k]
                    m = arg2[k] #imm
                    returnreg = arg3[k]
                    reg[returnreg] = reg[j] >> m

                elif str(opcodeStr[k]) == "ASL":
                    #ASR: This is  ">>" will divide by 2.
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]
                    reg[returnreg] = reg[j] << m

                elif str(opcodeStr[k]) == "NOP":
                    j = 0 #do nothin

                elif str(opcodeStr[k]) == "ADD":
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]
                    reg[returnreg] = reg[m] + reg[j]


                elif str(opcodeStr[k]) == "SUB":
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]

                    reg[returnreg] = reg[j] - reg[m]

                elif str(opcodeStr[k]) == "AND":
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]

                    reg[returnreg] = reg[m] & reg[j]

                elif str(opcodeStr[k]) == "ORR":
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]
                    reg[returnreg] = reg[m] | reg[j]

                elif str(opcodeStr[k]) == "EOR":
                    j = arg1[k]
                    m = arg2[k]
                    returnreg = arg3[k]
                    reg[returnreg] = reg[m] ^ reg[j]

                p = 1
                #print opcounter
                cyclecount = cyclecount + 1
            #for counter in range(len(opcounter)):
                fileS.write('=====================')
                fileS.write('\n')
                fileS.write('cycle: ')
                fileS.write(str(cyclecount))
                fileS.write(' ')
                fileS.write(str(mem[k]))
                fileS.write('\t')
                fileS.write(str(opcodeStr[k]))
                fileS.write('\t')
                fileS.write(str(arg1Str[k]))
                fileS.write(str(arg2Str[k]))
                fileS.write(str(arg3Str[k]))
                fileS.write('\n \n')
                fileS.write('registers: \n')
                fileS.write('r00: \t')
                # needs for loop that runs  0-7 regs
                for count in range(8):
                    fileS.write(str(reg[count]))
                    fileS.write('\t')
                fileS.write('\n')
                fileS.write('r08: \t')
                    # needs for loop that runs 8-15
                for count in range(8):
                    fileS.write(str(reg[count + 8]))
                    fileS.write('\t')
                fileS.write('\n')
                fileS.write('r16: \t')
                # runs 16-23
                for count in range(8):
                    fileS.write(str(reg[count + 16]))
                    fileS.write('\t')
                fileS.write('\n')
                fileS.write('r24: \t')
                # runs 24-31
                for count in range(8):
                    fileS.write(str(reg[count + 24]))
                    fileS.write('\t')
                fileS.write('\n')
                fileS.write('\n')
                fileS.write('data: ')
                incrementer = 4
                if printdata == 1:
                    for printer in range(len(memdata)):
                        if printer == 0:
                            fileS.write('\n')
                            fileS.write(str(memnum + incrementer) +": ")
                            incrementer = incrementer + 32
                            fileS.write(str(memdata[printer]))
                            fileS.write('\t')
                        elif printer % 8 == 0:
                            fileS.write('\n')
                            fileS.write(str(memnum + incrementer) + ": ")
                            incrementer = incrementer + 32
                            fileS.write(str(memdata[printer]))
                            fileS.write('\t')
                        else:
                            fileS.write(str(memdata[printer]))
                            fileS.write('\t')



                fileS.write('\n \n')
        fileS.close()

                #print doBranch
               # k = k + 1
                #k = k + doBranch
                #doBranch = 0





    #if (str(opcodeStr[k]) == 'B'):
                #k = k + int(arg1Str[k])
D = Dissemble()
D.run()
S = Simulator()
S.run()

filenam.close()
f.close()
#fileS.close()


            #f.write(opstr[i])
           # f.write(opcodeStr[i])
            #f.write(arg1Str[i])
           # f.write(arg2Str[i])
            #f.write(arg3Str[i])
            #f.write('\n')
            #print( opstr[i], opcodeStr[i], arg1Str[i], arg2Str[i], arg3Str[i], file=f )

                #arg1[i], arg2[i], arg3[i],




        #def imm32BitUnsignedTo32BitSignedConverter(num):


        #for i in range(numInstructs, len(instructions)):
           # mem.append(imm32BitUnsignedTo32BitSignedConverter(int(instructions[i], base=2)))
            #binMem.append(instructions[i])

        #outfile =open(outputFileName + "_dis.txt", 'w')
