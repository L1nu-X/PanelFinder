import requests,argparse,sys,socket,time


parser = argparse.ArgumentParser()

parser.add_argument('-d', '--domain', help="Domain to search. Example: -d google.com", action='store', dest='domain')
parser.add_argument('-p', '--panel', help="Admin panel finder", action='store_true', dest='panel')
parser.add_argument('-b', '--backdoors', help="Backdoor finder", action='store_true', dest='backdoor')
parser.add_argument('-f', '--files', help="Common files finder", action='store_true', dest='files')
parser.add_argument('-c', '--directories', help="Common directories finder", action='store_true', dest='directories')
parser.add_argument('-o', '--output', help="Output results to a file", action='store', dest='output')

args = parser.parse_args()

print "\n - Created by H4ck3rCame -\n"
print " If not you, who? If not now, when?"
print "  _   _            _      ____             _    _ "
print " | | | | __ _  ___| | __ | __ )  __ _  ___| | _| |"
print " | |_| |/ _` |/ __| |/ / |  _ \ / _` |/ __| |/ / |"
print " |  _  | (_| | (__|   <  | |_) | (_| | (__|   <|_|"
print " |_| |_|\__,_|\___|_|\_\ |____/ \__,_|\___|_|\_(_)"

domain = args.domain
if (type(domain) != str):
	print "\n[!] Domain not defined"
	sys.exit(1)

print "\n[*] Checking if domain exists..."
try:
	get = socket.gethostbyname(domain.strip())
	print '[%s] Domain %s is valid - %s' % (time.strftime("%H:%M:%S"),domain.strip(), get)
	r = True
except socket.gaierror, e:
	print "[%s] Unable to resolve: %s" % (time.strftime("%H:%M:%S"), domain.strip())
	print "[*] Retrying by adding www at the beginning..."
	rdomain = "www."+domain.strip()
	try:
		get = socket.gethostbyname(rdomain.strip())
		print '[%s] Domain %s is valid - %s' % (time.strftime("%H:%M:%S"), rdomain.strip(), get)
		r = True
	except socket.gaierror, e:
		print "[%s] Unable to resolve: %s" % (time.strftime("%H:%M:%S"), rdomain.strip())
		r = False

if (args.panel == False and args.backdoor == False and args.files == False and args.directories == False):
	print "\n[!] No parameters defined"
	sys.exit(1)

if (args.panel):
	print "\n[PANEL] Searching for administration panels in "+rdomain.strip()
	f = open('admin_panels.txt', 'r')
	for line in f:
		panel = line.strip('\n')
		url = 'http://'+str(rdomain)+'/'+str(panel)
		print "{0}\r".format(url),
		r = requests.get(url)
		if r.status_code == 200:
			print "[%s] Admin panel apparently found: %s" % (time.strftime("%H:%M:%S"), url)
		elif r.status_code == 404:
			pass
	print "\t\t\t\t\t\t\t\t\r"

if (args.backdoor):
	print "\n[BACKDOOR] Searching for backdoors in "+rdomain.strip()
	f = open('backdoors.txt', 'r')
	for line in f:
		backdoor = line.strip('\n')
		url = 'http://'+str(rdomain)+'/'+str(backdoor)
		print "{0}\r".format(url),
		r = requests.get(url)
		if r.status_code == 200:
			print "[%s] Backdoor apparently found: %s" % (time.strftime("%H:%M:%S"), url)
		elif r.status_code == 404:
			pass
	print "\t\t\t\t\t\t\t\t\r"

if (args.files):
	print "\n[FILES] Searching for common files in "+rdomain.strip()
	f = open('common_files.txt', 'r')
	for line in f:
		file = line.strip('\n')
		url = 'http://'+str(rdomain)+'/'+str(file)
		print "{0}\r".format(url),
		r = requests.get(url)
		if r.status_code == 200:
			print "[%s] File apparently found: %s" % (time.strftime("%H:%M:%S"), url)
		elif r.status_code == 404:
			pass
	print "\t\t\t\t\t\t\t\t\r"

if (args.directories):
	print "\n[DIRECTORIES] Searching for common directories in "+rdomain.strip()
	f = open('common_directories.txt', 'r')
	for line in f:
		directory = line.strip('\n')
		url = 'http://'+str(rdomain)+'/'+str(directory)
		print "{0}\r".format(url),
		r = requests.get(url)
		if r.status_code == 200:
			print "[%s] Directory apparently found: %s" % (time.strftime("%H:%M:%S"), url)
		elif r.status_code == 404:
			pass
	print "\t\t\t\t\t\t\t\t\r"

print "[*] Finished!"