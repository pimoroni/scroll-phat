import math, time, scrollphat, sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip = s.getsockname()[0]
s.close()

print ip
i = 0
scrollphat.set_brightness(20)

#scrollphat.write_string("This is a test, hurrah! The quick brown fox jumps over the lazy dog. y2 = (math.sin(((i/2.0)+(x*10.0))/10.0) + 1) * 2.5", 0)


while True:	
	scrollphat.clear()
	scrollphat.write_string("IP: " + ip + "    ", 11)
	for i in range(0, scrollphat.buffer_len() - 11):
		scrollphat.scroll()
		time.sleep(0.05)

	scrollphat.clear()
	scrollphat.write_string("Have a nice day! :-D    ", 11)
	for i in range(0, scrollphat.buffer_len() - 11):
		scrollphat.scroll()
		time.sleep(0.05)

	smileys = [":-D", ":-(", ":-O", "}:-(", ";-)", ":-S"]
	for smiley in smileys:
		scrollphat.clear()
		scrollphat.write_string(smiley, 2)
		time.sleep(0.5)

sys.exit()
#scrollphat.update()
buf = [0] * 11
while True:
	for x in range(0, 11):
		y = (math.sin(((i)+(x*10.0))/10.0) + 1) * 2.5
		y = int(y)
		y2 = (math.sin(((i/2.0)+(x*10.0))/10.0) + 1) * 2.5
		y2 = int(y2)
		buf[x] = 1 << y
		#buf[x] |= 1 << y2

	scrollphat.update(buf)

	time.sleep(0.005)

 	i += 1
#     # buf = [0] * 11
#     # t = millis()/50
#     # for o_x in range(11):
#     #     x = t + (o_x/3.0)
#     #     y = int((math.sin(x) + 1) * 2.5)
#     #     buf[o_x] |= (1 << y)
    
#     