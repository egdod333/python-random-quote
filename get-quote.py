import random
def primary():
  #  print("Keep it logically awesome.")
  f = open("/home/ec2-user/environment/test/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
