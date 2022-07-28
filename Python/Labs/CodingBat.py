def count_code(str):
  count = 0
  
  for i in range(0, len(str)):
    if i <= len(str)-4 and str[i:i+2] == "co" and str[i+3:i+4] == "e":
      count += 1
      i += 4
      
  return count

def regex():
    import re
    s = 'cozexxcope'
    match = re.search(r'co.e', s)
    print('Start Index:', match.start())
    print('End Index:', match.end())

if __name__ == "__main__":
    #print(count_code('codecode'))
    regex()