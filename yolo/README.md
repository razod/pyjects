# Yolo
Using a Python API for interacting with the YOLO app by [Merkie](https://github.com/Merkie/yolo-api).

# Security risks
While making this I discovered that all YOLO messages are sent with the sender's IP address being logged. On top of that, you can view all of your recieved messages along with the senders' ips. This opens the floodgates for people with malitious intent to track down people's locations that respond to their YOLOs. Also, you can view anyone's phone number with only their YOLO code; this is also dangerous. I would encourage the YOLO team to fix these issues.

# [Documentation](https://github.com/Merkie/yolo-api#documentation)