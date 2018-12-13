import forecastio
import time
import subprocess


api_key="blep, don't take my key :("
lat=40.014984
lng=-105.270546
startTime=time.time()
#def main():
while True:
	currentTime=time.time()
	if abs((currentTime-startTime)%3599-0) >=0.1:
		forecast=forecastio.load_forecast(api_key, lat, lng)
		print "call was made"
		print "======Hourly Data======"
		#by_hour=forecast.hourly()
		#for hourly_data in by_hourly.data:
			#print hourly_data.temperature
		#print "Hourly summary: %s" % (by_hour.summary)
		now=forecast.currently()
		print "temperature is {}".format(now.temperature)
		print "precipitation is {}".format(now.precipProbability)
		print "wind speed is {}".format(now.windSpeed)
		print "cloud cover is {}".format(now.cloudCover)
		#for hourly_data_point in by_hour.data:
			#print hourly_data_point
		if now.temperature >= 35 and now.precipProbability >= 0.5:
			bashCommand="sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 1200 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/rainFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
			time.sleep(1)
			process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error=process.communicate()
		elif now.temperature < 35 and now.precipProbability >=0.5:
			bashCommand="sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 1200 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/snowFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
			time.sleep(1)
			process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error=process.communicate()	
		elif now.windSpeed>=15:
			bashCommand="sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 1200 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/windFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
			time.sleep(1)
			process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error=process.communicate()
		elif now.cloudCover >=0.3:
			bashCommand="sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 1200 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/cloudsFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
			time.sleep(1)
			process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error=process.communicate()
		else:
			bashCommand="sudo ./rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/utils/led-image-viewer -t 1200 rpi-rgb-led-matrix-814b79b5696d32dd1140304b41a1ec0068bb271a/img/sunFull.gif --led-no-hardware-pulse --led-gpio-mapping=adafruit-hat"
			time.sleep(1)
			process=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error=process.communicate()
		time.sleep(1)
	

