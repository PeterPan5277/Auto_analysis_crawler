from ast import Lambda
from msilib.schema import Class
import numpy as np
from crawler import crawl
from preprocess import data_preprocess
class Taf_read():
    def __init__(self, weather, title):
        self.weather = weather
        self.title = title
    def logic_decision(self,i,lines, sigtime,amd, airport):
        #AMD 8:12
        #TAF 4:8
        if amd:
            s=8
            e=12
        else:
            s=4
            e=8
        for j in range(i+1, len(lines)):
            text2 = lines[j].split()
            if lines[j][:3] == 'TAF':
                break
            elif (list(set(text2) & set(self.weather))):
                if sigtime >= int(lines[j][6:10]) and sigtime <= int(lines[j][11:15]):
                    airport[(lines[i][s:e])]=(list(set(text2) & set(self.weather))[:])
                #解決1324 1400問題
                elif str(sigtime)[2:]=='00':#只解決00的時候
                    if lines[j][11:15] == str(int(str(sigtime)[:2])-1)+'24':
                        if (list(set(text2) & set(self.weather))):
                            airport[(lines[i][s:e])]=(list(set(text2) & set(self.weather))[:])
                    elif text2[0]=='BECMG' and int(lines[j][11:15])<=int(sigtime):
                        airport[(lines[i][s:e])]=(list(set(text2) & set(self.weather))[:])
                elif text2[0]=='BECMG' and int(lines[j][11:15])<=int(sigtime):
                    airport[(lines[i][s:e])]=(list(set(text2) & set(self.weather))[:])

    def airport_weather(self, lines, taftime, sigtime):
        airport={}
        for i in range(len(lines)):
            if lines[i][:3] == 'TAF':
                if lines[i][4:7] =='AMD' or lines[i][4:7]=='COR':
                    amd=True
                    #此處處理AMD/COR情況
                    airport[(lines[i][8:12])]='X'
                    text = lines[i].split()
                    if (list(set(text) & set(self.weather))):
                        airport[(lines[i][8:12])]=(list(set(text) & set(self.weather))[:])
                        self.logic_decision(i,lines,sigtime, amd, airport)                            
                    else:
                        self.logic_decision(i,lines,sigtime, amd, airport)
                else:
                    amd=False
                    airport[(lines[i][4:8])]='X'      
                    #以下判斷此行有無wx
                    text = lines[i].split()
                    if (list(set(text) & set(self.weather))):
                        airport[(lines[i][4:8])]=(list(set(text) & set(self.weather))[:])
                        self.logic_decision(i,lines,sigtime, amd, airport)
                    else:
                        for j in range(i+1, len(lines)):
                            text2 = lines[j].split()
                            self.logic_decision(i,lines,sigtime, amd, airport)
        
        print('Total airport:', len(airport))
        assert len(airport)==46, '機場數量不符合，請檢察程式碼'
        # try:
        #     len(airport)==4
        # except:
        #     print('機場數量不符合，請檢察程式碼')
        
        for k, v in list(airport.items()):
            if v=='X' or v[0]=='NSW':
                del airport[k]
        return(airport)

    def main(self):
        crawl_yes = input('Wanna crawl ? (自動爬蟲?) (y or n): ')
        PATH = "C:/Users/peteprpan/Desktop/CAA_TAF/chrome/chromedriver.exe"
        taf_list = ('VTCC VLLB VVNB ZGNN ZJHK ZPPP ZGKL ZGGG VHHH RPLI ZSAM ZSFZ ZSWZ ZSPD ZSOF ZSCN\
        ZHHH ZGHA ZUCK ZUUU ZLLL ZLXY ZHCC ZSJN ZBTJ ZBAA ZSQD ZSYT ZYTL ZYTX ZKPY RKSI\
        RKPK RKPC ROAH RJFK RJFF RJOK RJOB RJBB RJGG RJNT\
        RCQC RCYU RCMQ RCNN')
        if crawl_yes == 'y':
            crawl(PATH, taf_list)
        lines, taftime, sigtime = data_preprocess(title)

        print('Make sure the taftime and valid time is what you want as follow:')
        print('TAFtime is:', taftime,'Z')
        print('Validtime is:', sigtime,'Z')
        airport = self.airport_weather(lines, taftime, sigtime)
        for k,v in airport.items():
            print(f'At {sigtime}(day/hour(Z)),', k,':',v)
            
if __name__ == '__main__':
    #23Z TAF is for 12Z SIGX
    #05Z TAF is for 18Z SIGX  ->可以試看看找出 一大一小的情況!(8-9 和13-14)
    #11Z TAF is for 00Z SIGX
    #17Z TAF is for 06Z SIGX
    #期待最後輸出->機場的天氣現象在某個時段應為何
    weather = ['SHRA', '+SHRA', '-SHRA', 
            '+TSRA','-TSRA','TSRA','TS',
            '+RA','-RA','RA','DZ','-DZ','+DZ',
            'BR','HZ','FG','BCFG',
            'SN',
            'NSW','NSC','SA']
    for i in range(len(weather)):
        weather.append(weather[i]+'=')  #加上尾端有#的
    title = ['TAF','BECMG','TEMPO']
    read_taf = Taf_read(weather, title)
    read_taf.main()

    



