import sys, random, string, httplib, requests, getopt, re

def usage():
    print "goXSS.py -u <attackurl> -o <outputfile>"

#simple payloadgenerator
def generatePayload():
    global varRandomString
    varRandomString = "".join(random.sample(string.ascii_uppercase, 8))
    print "-" * 65
    print "Random string generated for XSS attack is:", varRandomString

"""
def breakChars():
    global tryToBreak
    tryToBreak = ['<','>','"','\\','/','(',')']
    for character in tryToBreak:
        print "Trying to break:", tryToBreak
"""

def attackUrl():
    generatePayload()
    tryToBreak = ['<','>','"','script','/','(',')']
    for Char in tryToBreak:
        global inject
        inject = str(Char)
        print "Trying... " + inject
        #breakChars()
        urlRequest = urlSet + "/" + varRandomString + inject
        r = requests.get(url=urlRequest)
        print "Url to attack is:", urlRequest
        print r
        print "-" * 65
        #print 'Output file is =>', outFile
        # comment or uncomment next line to debug
        #print(r.content)
        global response
        response =  r.content
        searchReflection()

def searchReflection():
    #searchPayload = varRandomString + tryToBreak
    searchPayload = varRandomString + inject
    if re.search(searchPayload, response):
        print "Found", searchPayload, "on Response !"
        print "=" * 65
    else:
        print "REFLECTION NOT FOUND"


def main(argv):
    if len(argv)<2:
        usage()
    try:
        opts, args = getopt.getopt(argv,"hu:o:",["urlSet=","outFile="])
    except getopt.GetoptError:
        print "goXSS.py -u <attackurl> -o <outputfile>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'goXSS.py -u <attackurl> -o <outputfile>'
            sys.exit()
        elif opt in ("-u", "--url"):
            global urlSet
            urlSet = arg
        elif opt in ("-o", "--ofile"):
            global outFile
            outFile = arg
        attackUrl()

if __name__ == "__main__":
    main(sys.argv[1:])

##### TODO

# should also "fuzz" http methods
# try all methods, like requests.put, request.head, etc

#def encodeChars():
    # should encode *breakChars in unicode, hex, url, double encode

# Search reflection function should be created in a manner
# to search for literal "chars" reflected (raw hex value)
