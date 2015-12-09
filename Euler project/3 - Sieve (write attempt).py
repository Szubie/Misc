import tempfile
import os
import sys

def createSieve(outputFile, maxp, logging=0):
    """Creates a sieve and stores one prime per line in file outputFile."""
    # Write a list of all numbers to check to a file
    myNumFile = createBeginNumberList(maxp, outputFile)

    # Do the looping
    rfh = open(myNumFile, "r")
    try:
        totalRead = 0
        for i in range(maxp+1):
            # log if necessary
            if logging > 0 and i % logging == 0:
                print("Checking number", i, "(" + str(int(i/(maxp+1)*100)) + "%)")

            # do thingy
            bytesRead, myNum = readNumber(rfh)
            if bytesRead == 0:
                break

            totalRead += bytesRead

            if myNum != 0:
                rfh.close()
                rfh = None

                rewriteFileWithoutMultiples(myNumFile, myNum, totalRead)

                rfh = open(myNumFile, "r")
                rfh.seek(totalRead)

    finally:
        if rfh != None:
            rfh.close()

    # Remove zeros
    removeZerosInFile(outputFile)

    return myNumFile


def createBeginNumberList(maxn, fileName):
    """@return value: the file path"""

    tfh = open(fileName, "w")
    try:
        writeLineToFile(tfh, "0")
        writeLineToFile(tfh, "0")
        for i in range(2, maxn+1):
            writeLineToFile(tfh, str(i))
    finally:
        tfh.close()

    return fileName

def rewriteFileWithoutMultiples(inputFilename, multiple, startPos):
    rfh = open(inputFilename, "r")
    try:
        writeFile = tempfile.mkstemp()
        os.close(writeFile[0])
        wfh = open(writeFile[1], "w")
    except:
        rfh.close()
        raise

    # Rewrite file
    try:
        readBytes = 0
        while readBytes < startPos:
            b, aNum = readNumber(rfh)
            readBytes += b
            writeLineToFile(wfh, str(aNum))

        while True:
            b, aNum = readNumber(rfh)
            if aNum == None:
                break

            if aNum % multiple == 0:
                writeLineToFile(wfh, "0")
            else:
                writeLineToFile(wfh, str(aNum))
    finally:
        rfh.close()
        wfh.close()

    # Copy
    copyFile(writeFile[1], inputFilename)

def copyFile(source, dest):
    rfh = open(source, "r")
    try:
        wfh = open(dest, "w")
    except:
        rfh.close()
        raise

    try:
        aLine = rfh.readline()
        while len(aLine) != 0:
            wfh.write(aLine)
            aLine = rfh.readline()
    finally:
        rfh.close()
        wfh.close()

def removeZerosInFile(inputFile):
    rfh = open(inputFile, "r")
    try:
        writeFile = tempfile.mkstemp()
        os.close(writeFile[0])
        wfh = open(writeFile[1], "w")
    except:
        rfh.close()
        raise

    # Rewrite file
    try:
        while True:
            b, aNum = readNumber(rfh)
            if aNum == None:
                break

            if aNum != 0:
                writeLineToFile(wfh, str(aNum))

    finally:
        rfh.close()
        wfh.close()

    # Copy
    copyFile(writeFile[1], inputFile)



def writeLineToFile(fh, l):
    try:
        fh.write(l)
        fh.write('\n')
    except:
        fh.close()
        raise

def readNumber(fh):
    mynum = fh.readline()
    numb = len(mynum)
    mynum = mynum.strip('\n')

    if len(mynum) == 0:
        return (0, None)

    return (numb, int(mynum))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "MAX_PRIME [LOG_INTERVAL]")
        sys.exit(1)

    maxp = int(sys.argv[1])
    logging = int(maxp / 100)
    try:
        logging = int(sys.argv[2])
    except:
        pass

    print("Creating seive until number", maxp, "with logging interval", logging)
    createSieve(os.path.expanduser("~/Desktop/Sieve-" + str(maxp) + ".txt"),
                maxp, logging)