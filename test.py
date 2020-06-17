import sys, getopt

def main(argv):
   station1 = ''
   station2 = ''
   try:
      opts, args = getopt.getopt(argv,"hs:f:",["sfile=","ffile="])
   except getopt.GetoptError:
      print ('test.py -s <station1> -f <station2>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -s <station1> -f <station2>')
         sys.exit()
      elif opt in ("-s", "--sfile"):
         station1 = arg
      elif opt in ("-f", "--ffile"):
         station2 = arg
   print ('Station 1 is "', station1)
   print ('Station 2 is "', station2)

if __name__ == "__main__":
   main(sys.argv[1:])