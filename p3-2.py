print('x={:},y={:}'.format('braintabs','pwlive'));

print('x={:>20},y={:>50}'.format('braintabs','pwlive'));
#right alligns the string 20 or 50 - Minimum field width (total number of characters)
#'braintabs' has 9 characters
#Field width is 20
#Right-aligned (>), so it adds 11 spaces on the left (20 - 9 = 11)
print('x={:<20},y={:<50}'.format('braintabs','pwlive'));
# same as above but left alligned 
print('x={:-20},y={:-50}'.format(-100,+90));
#The - in {:-20} is actually the sign option, not an alignment option. Here's what it means:
#Sign option (-): This means to always show the sign of the number, even if it's positive. In this case, it adds a + sign to the positive number.
# t creates a field width of 20 characters
#Right-aligns the number (default for numbers)
#Shows the sign only if the number is negative as you can see that if we put +90 it will not show + sign
print('x={:+20},y={:+50}'.format(-100,+90));
#Shows the sign for both positive and negative numbers
print('x={:,},y={:,}'.format(-1000000,-9000000))
# this will add comma in the numbers as in output for thousands
# this is only for ints and floats not for strings
print('x={:,.2f},y={:,}'.format(9.2434345465,6654545.6567547543))
#.2f tells to show only 2 decimal places after point
print('x={:b},y={:b}'.format(90,66))
# here b is for binary
print('x={:o},y={:o}'.format(90,66))
# here o is for octal
print('x={:x},y={:x}'.format(90,66))
# here x is for hexadecimal
print('x={:X},y={:X}'.format(90,66989))
# here X is for hexadecimal in uppercase
print('x={:e},y={:E}'.format(90,66))
# here e is for exponential
print('x={:f},y={:F}'.format(90.5453453,66.6567547543))
# here f is for float
print('x={:c},y={:c}'.format(90,66))
# here c is for character
print('x={:_^20},y={:_^20}'.format('idkwts','sybauas'))
# 'idkwts' has 6 characters
# Field width is 20
# Center-aligned (^), so it needs (20 - 6) = 14 padding characters
# 14 ÷ 2 = 7 underscores on each side
# Result: _______idkwts_______
print('x={:n},y={:n}'.format(1000000,9000000))
#:n = "Format this number according to my computer's language/region settings"
# In your case (English_India), it doesn't add thousand separators
# it will add thousand separators as per your locale settings
i=int(input())
j=int(input())
k=float(input())
print(f'GATE YEAR={i:5d},AIR={j:<4d},GATE SCORE={k:7.3f}')








