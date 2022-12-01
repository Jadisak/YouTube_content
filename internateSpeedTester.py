from speedtest import Speedtest
test = Speedtest(secure = True)
print('\n\tPlease Wait !!\n\t')
download = str(test.download()/1024/1024)
upload = str(test.upload()/1024/1024)

download_speed = download[0:4]
upload_speed = upload[0:4]

print(f'Your download speed is: {download_speed} mbps\nYour upload speed is: {upload_speed} mbps')