
import time
import subprocess

#def main():
while True:
	bashCommand = "sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 15 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/rainFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	print "rain"
	time.sleep(0.25)
	bashCommand = "sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 15 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/snowFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	print "snow"
	time.sleep(0.25)
	
	bashCommand = "sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 15 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/windFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
	#output, error = process.communicate()
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	time.sleep(0.25)
	bashCommand = "sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 15 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/cloudsFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	time.sleep(0.25)
	bashCommand = "sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 15 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/sunFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	time.sleep(0.25)
	time.sleep(1)
#if __name__ == "__main__":
#	main()
