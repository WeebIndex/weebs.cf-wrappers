import requests

def coin():
  return requests.get('https://weebs.cf/random/coin').text

def hug():
  return requests.get('https://weebs.cf/random/hug').text

def kiss():
  return requests.get('https://weebs.cf/random/kiss').text

def laugh():
  return requests.get('https://weebs.cf/random/laugh').text

def pat():
  return requests.get('https://weebs.cf/random/pat').text

def poke():
  return requests.get('https://weebs.cf/random/poke').text

def punch():
  return requests.get('https://weebs.cf/random/punch').text

def slap():
  return requests.get('https://weebs.cf/random/slap').text

def bite():
  return requests.get('https://weebs.cf/random/bite').text
  
def love():
  return requests.get('https://weebs.cf/random/love').text

def think():
  return requests.get('https://weebs.cf/random/think').text