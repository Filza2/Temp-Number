from requests import get
from time import sleep
import re,os,random
def main():
    os.system("cls" if os.name=='nt' else "clear")
    print("""
████████╗███████╗███╗   ███╗██████╗       ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗      ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
   ██║   █████╗  ██╔████╔██║██████╔╝█████╗██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ╚════╝██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
   ██║   ███████╗██║ ╚═╝ ██║██║           ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝           ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                        
                                By @TweakPY - @vv1ck                                                            
""")
def Temp_number():
    r=get('https://receive-smss.com/',headers={'Host': 'receive-smss.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Te': 'trailers'})
    num=re.findall('''<div class="row">
<div class="col-12">
<h4 class="number-boxes-itemm-number">(.*?)</h4>
<h5 class="number-boxes-item-country number-boxess-item-country">(.*?)</h5>
</div>
</div>''',r.text)
    data=random.choice(num)
    country=data[1]
    number=data[0]
    print(f"\n- Your Number : {number}\n- Number Country : {country}\n");sleep(2)
    while True:sleep(7);main();print(f"\n- Your Number : {number}\n- Number Country : {country}\n");get_message(number)
def get_message(number):
    r=get(f'https://receive-smss.com/sms/{str(number).replace("+","")}/',headers={'Host': 'receive-smss.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Te': 'trailers'})
    message=re.findall("""<td class="wr3pc333el1878">(.*?)</td>
<td class="wr3pc333el1878"><p>
(.*?)
</p></td>
<td class="wr3pc333el1878"><span>(.*?) seconds ago</span> </td>
</tr><tr>""",r.text)
    if message!=[]:
        for f,m,t in message:
            if 'data-clipboard-text' in str(m):
                code=re.findall('<span class="btn22cp1" data-clipboard-text="(.*?)"><b>(.*?)</b></span>',str(m))[0][0]
                try:
                    code0=re.findall('<span class="btn22cp1" data-clipboard-text="(.*?)"><b>(.*?)</b></span>',str(m))[1][0]
                    m=str(m).replace(f'<span class="btn22cp1" data-clipboard-text="{code}"><b>{code}</b></span>',f"{code}").replace(f'<span class="btn22cp1" data-clipboard-text="{code0}"><b>{code0}</b></span>',f'{code0}')
                except:code0=''
                m=str(m).replace(f'<span class="btn22cp1" data-clipboard-text="{code}"><b>{code}</b></span>',f"{code}")
                print(f"- From : {f}\n- Message : {m}\n- Time : {t} seconds ago\n- Codes : ( {code} , {code0} )\n")
            else:
                print(f"- From : {f}\n- Message : {m}\n- Time : {t} seconds ago\n")
    else:
        message=re.findall("""<td class="wr3pc333el1878">(.*?)</td>
<td class="wr3pc333el1878"><p>
(.*?)
</p></td>
<td class="wr3pc333el1878"><span>(.*?) minute ago</span> </td>
</tr><tr>""",r.text)
        for f,m,t in message:
            if 'data-clipboard-text' in str(m):
                code=re.findall('<span class="btn22cp1" data-clipboard-text="(.*?)"><b>(.*?)</b></span>',str(m))[0][0]
                try:
                    code0=re.findall('<span class="btn22cp1" data-clipboard-text="(.*?)"><b>(.*?)</b></span>',str(m))[1][0]
                    m=str(m).replace(f'<span class="btn22cp1" data-clipboard-text="{code}"><b>{code}</b></span>',f"{code}").replace(f'<span class="btn22cp1" data-clipboard-text="{code0}"><b>{code0}</b></span>',f'{code0}')
                except:code0=''
                m=str(m).replace(f'<span class="btn22cp1" data-clipboard-text="{code}"><b>{code}</b></span>',f"{code}")
                print(f"- From : {f}\n- Message : {m}\n- Time : {t} minute ago\n- Codes : ( {code} , {code0} )\n")
            else:
                print(f"- From : {f}\n- Message : {m}\n- Time : {t} minute ago\n")
        if message==[]:
            message=re.findall("""<td class="wr3pc333el1878">(.*?)</td>
<td class="wr3pc333el1878"><p>
(.*?)
</p></td>
<td class="wr3pc333el1878"><span>(.*?) minutes ago</span> </td>
</tr><tr>""",r.text)
            for f,m,t in message:
                if 'data-clipboard-text' in str(m):
                    code=re.findall('<span class="btn22cp1" data-clipboard-text="(.*?)"><b>(.*?)</b></span>',str(m))[0][0]
                    try:
                        code0=re.findall('<span class="btn22cp1" data-clipboard-text="(.*?)"><b>(.*?)</b></span>',str(m))[1][0]
                        m=str(m).replace(f'<span class="btn22cp1" data-clipboard-text="{code}"><b>{code}</b></span>',f"{code}").replace(f'<span class="btn22cp1" data-clipboard-text="{code0}"><b>{code0}</b></span>',f'{code0}')
                    except:code0=''
                    m=str(m).replace(f'<span class="btn22cp1" data-clipboard-text="{code}"><b>{code}</b></span>',f"{code}")
                    print(f"- From : {f}\n- Message : {m}\n- Time : {t} minutes ago\n- Codes : ( {code} , {code0} )\n")
                else:
                    print(f"- From : {f}\n- Message : {m}\n- Time : {t} minutes ago\n")
main();Temp_number()