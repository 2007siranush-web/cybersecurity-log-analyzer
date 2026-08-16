with open("logs.txt","r") as file:
 logs = file.readlines()
print(logs)
for log in logs:
 if "LOGIN_FAILED" in log:
  print(log)

failed_ips = {}
for log in logs:
 if "LOGIN_FAILED" in log:
  ip = log.split("ip=")[1].strip()
  failed_ips[ip] = failed_ips.get(ip, 0)+1
print(failed_ips)

for ip, count in failed_ips.items():
 if count>=3:
  print("SUSPICIOUS IP:", ip) 

failed_users={}
for log in logs:
 if "LOGIN_FAILED" in log:
  user=log.split("user=")[1].split(" ")[0]
  failed_users[user] = failed_users.get(user, 0) + 1
print(failed_users)


print("=== SECURITY REPORT ===")
print("Suspicious IPs:")
for ip, count in failed_ips.items():
 if count>=3:
  print(ip, "-", count, "failed attempts")
print("Targeted users:")
for user, count in failed_users.items():
 print(user, "-", count, "failed attempts")
