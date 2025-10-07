#Task: Weather Advisor
Weather=float(input("Weather"))
if Weather >= 30:
  print ("It's a hot day. Stay hydrated!")
elif 20 <= Weather <= 29:
  print ("It's a warm day. Enjoy the weather!")
elif 10 <= Weather <=19:
  print ("It's a cool day. Wear a jacket!")
else:
  print ("It's a cold day. Stay warm!")

  
#Filter and Transform a List
for x in range (20):
  if x % 3 == 0:
    print (x)