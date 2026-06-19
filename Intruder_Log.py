import pyfiglet

logfile = open(input("Enter the path to the logfile: "))
loglines = logfile.readlines()

ip_list = {}
ip_totals = {}

count = 0

logfile.close()

def extract_from_line_in_file(line, start, end,):
      return line.split(start)[1].split(end)[0]


def extract_from_dictionary(ip_totals, ip_address,):
            if ip_address in ip_totals:
                 ip_totals[ip_address] += 1
            else:
                 ip_totals[ip_address] = 1

def ip_profile(data, ip, account):
      if ip not in data:
          data[ip] = {}
      if account in data[ip]:
            data[ip][account] += 1
      else:
            data[ip][account] = 1
  
for line in loglines:
    if "Failed password" in line:
            count += 1
            ip_address = extract_from_line_in_file(line, "from", "port")
            account = extract_from_line_in_file(line, "for", "from")
            extract_from_dictionary(ip_totals, ip_address)
            ip_profile(ip_list, ip_address, account)
                            


sorted_ips = sorted(ip_totals, key=ip_totals.get, reverse=True)
top_ips = sorted_ips[:5]

banner = pyfiglet.figlet_format("INTRUDER_LOG", font="slant")
                                                                                       
print("\033[94m" + banner + "\033[0m")                                
print(f"\033[91m              WARNING {count} SUSPICIOUS LOGIN ATTEMPTS FOUND! \033[0m")
print(" \033[91m IF YOU DON'T RECOGNIZE ONE OR MORE ADDRESSES BELOW, ACT IMIDIATELY! \033[0m")
print("                                                                                        ")
print("==============================================================================")
for ip in top_ips:

    percentage = ip_totals[ip] / count * 100
    accounts = ", ".join(f"{acct} ({n}x)" for acct, n in ip_list[ip].items())

    print(f"ip address:                  {ip}                                                     ")
    print(f"Attepts:                    {ip_totals[ip]} SSH login attempt(s)")
    print(f"Targeted:              {accounts}")
    print(f"contributing:           ({percentage:.2f}%) to total login attempts                     ")
    print("=" *78)
    print("==============================================================================")        
print( "           \033[1;94m  INTRUDER_LOG V1.0 BY NOTCRYPT_0X \033[0m")                                     

