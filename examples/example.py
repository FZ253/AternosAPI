from aternosapi import AternosAPI

headers_cookie = "Tzw7MqHp67lXU8oE82Sv3Sg3CpI7j9ZRAVBuYkQlLX8VUmV1kq6UL1vZ7MfC5ka7OYcWHDLOpZSgPaNY0Pv6r73lqZm24QVWuwOW"
TOKEN = "rjVwJaN2pfdrwMpWDCp5"
server = AternosAPI(headers_cookie, TOKEN, timeout = 10)

def cmd(cmd):
	if cmd == "start":
		print(server.StartServer())
	if cmd == "stop":
		print(server.StopServer())
	if cmd == "status":
		print(server.GetStatus())
	if cmd == "info":
		print(server.GetServerInfo())

while True:
	icmd = input("[*] > ")
	cmd(icmd)
