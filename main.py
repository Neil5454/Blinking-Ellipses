# # Print 2 sets of 3 blinking ellipses, then clear the console
# # New Version
import time, os
def blinking_ellipses(text, delay=0.5):
  print(end=text)
  n_dots = 0
  n_sets_ellipses = 0
  while n_sets_ellipses < 2:
    while n_dots < 3:
      print(end='.', flush=True)
      n_dots += 1
      time.sleep(delay)
    else:
      print(end='\b\b\b', flush=True)
      print(end='   ', flush=True)
      print(end='\b\b\b', flush=True)
      n_dots = 0
      n_sets_ellipses += 1
  else:
    os.system('clear')
    
blinking_ellipses("Shuffling")


# Old Version - printed 1 extra "." after second set of ellipses b/c after "n" reached zero upon printing the third "." at the end of the second set of ellipses, the code logic results in the program looping thru the inner while loop (while n_dots == 3:), which then proceeds to the inner else code (print(end='.', flush=True)), before looping thru the outer while loop (n_sets_ellipses < 2) which ends the program

# def blinking_ellipses(text, delay=0.5):
#   print(end=text)
#   n_dots = 0
#   n_sets_ellipses = 0
#   while n_sets_ellipses < 2:
#     while n_dots == 3:
#       print(end='\b\b\b', flush=True)
#       print(end='   ', flush=True)
#       print(end='\b\b\b', flush=True)
#       n_dots = 0
#       n_sets_ellipses += 1
#     else:
#       print(end='.', flush=True)
#       n_dots += 1
#     time.sleep(delay)
#   else:
#     os.system('clear')

# blinking_ellipses()