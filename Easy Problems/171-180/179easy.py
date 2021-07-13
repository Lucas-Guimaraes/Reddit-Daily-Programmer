#https://www.reddit.com/r/dailyprogrammer/comments/2ftcb8/9082014_challenge_179_easy_you_make_me_happy_when/

#This is just the formula with no actual image
#BUT can easily be modified with PIL to include image support

#simple method
def naive_method(pixel)
    avg = round(sum(pixel/3)
    return (avg, avg, avg)

#makes image lighter
def lightness(pixel):
    avg = round((max(pixel) + min(pixel))/2)
    return (avg, avg, avg)

#tries the weighted method 
def weighted_method(pixel):
    r, g, b = pixel
    r, g, b = .29 * r, .587 * g, .114 * b
    return (r, g, b)

#Uses the Luminosity method
def luminosity(pixel):
    r, g, b = pixel
    avg = round(0.21*R + 0.72*G + 0.07*B)
	return (avg, avg, avg)