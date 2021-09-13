#https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/

#Makes circle
circles = [
	[1, 1, 2],
	[2, 2, 0.5],
	[-1, -3, 2],
	[5, 2, 1]
	]

#Makes box
box = [
	circles[0][0] - circles[0][2],
	circles[0][1] - circles[0][2],
	circles[0][0] + circles[0][2],
	circles[0][1] + circles[0][2]
	]

#C for Circles
for c in circles[1:]:
    box[0] = min(box[0], c[0] - c[2])
    box[1] = min(box[1], c[1] - c[2])
    box[2] = max(box[2], c[0] + c[2])
    box[3] = max(box[3], c[1] + c[2])

#Gets the four corners for our box
low_x_low_y = (box[0], box[2])
high_x_low_y = (box[1], box[2])
high_x_high_y = (box[1], box[3])
low_x_high_y = (box[0], box[3])

#Format
formatted = "{} {} {} {}".format(low_x_low_y, high_x_low_y, high_x_high_y, low_x_high_y)

#Print
print(formatted)