# goXSS
Very simple XSS reflection tester

This is just a very simple XSS reflection tester

Stage: Alfa

Just send's a HTTP Get request with a random generated payload + some "breaking" chars

Then trys to search the payload + breakingChar on the response

If the payload + breakingChar are found this can mean that a Reflected XSS vuln is found

TODO: Lot's of stuff =)

  + Search reflection function should be changed:
    - searching for literal "chars" reflected (raw hex value)
    
  + Should also "fuzz" http methods
    - try all methods, like requests.put, requests.head, etc
    
  + create a function #def encodeChars():
    - should encode "breakingChars" in unicode, hex, url, double encode
  
