import requests, csv, subprocess

response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

rule = "netsh advfirewall firewall delete rule name='Malicious'"
subprocess.run(["Powershell", "-Command", rule])

mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.splitlines()))
for row in mycsv:
    ip = row[1]
    if(ip)!=("dst_ip"):
        print("Added Rule to block:", ip)
        rule = "netsh advfirewall firewall add rule name='Malicious' Dir=Out Action=Block RemoteIP=" + ip
        subprocess.run(["Powershell", "-Command", rule])
        rule = "netsh advfirewall firewall add rule name='Malicious' Dir=In Action=Block RemoteIP=" + ip
        subprocess.run(["Powershell", "-Command", rule])