def data_preprocess(title):
        #TO  REARRANGE THE TAF LIST
        #Ex:
        #TAF.....
        #TEMPO...
        #BECMG...
        with open("taf.txt") as f:
            lines = [line.strip() for line in f if line.strip()]
        idx = []
        count = 0
        for i in range(len(lines)):
            line_new = lines[i].split()
            if (line_new[0]) not in title:       
                idx.append(i)
                if len(idx)==1:
                    count = 1
                    lines[i-count] =lines[i-count]+' '+lines[i]
                elif idx[-1] - idx[-2] == 1:
                
                    count = count + 1      
                    lines[i-count] =lines[i-count]+' '+lines[i]       
                else :
                    count = 1
                    lines[i-count] =lines[i-count]+' '+lines[i]
                lines[i]=''            
        lines = [value for value in lines if value != '']
        with open('out.text','w') as f1:
            for i in range(len(lines)):
                f1.write(str(lines[i])+'\n') 
        #Above is to rearrange the "lines" into (which means initials is inly TAF/TEMPO/BECMG) 
        #TAF-------------
        #TEMPO-----------
        #BECMG-----------
        count=0
        i=0
        while int(i) < len(lines):
            i+=1
        #for i in range(len(lines)+int(count)): #Here a little bit DRY...(dont repeat yourself principle)
            line_new = lines[i-1].split()
            idx= [bug for bug, x in enumerate(line_new[1:]) if x=='TEMPO' or x == 'BECMG']
            #print(line_new)
            #print(idx) #idx = [7,12,15,18,23]
            if len(idx)!=0:
                info=[]
                for j in range(len(idx)):  
                    if j == len(idx)-1:
                        #只處理一個tempo becmg..
                        s = ' '.join(str(x) for x in line_new[idx[j]+1:])   
                        info.append(s)  
                    else:# 處理兩個以上tempo becmg
                        s = ' '.join(str(x) for x in line_new[idx[j]+1 : idx[j+1]+1])
                        info.append(s)
                for v in range(len(idx)):
                    lines.insert(i+v, info[v])
                    count+=1
                    #print(count)
                line_new = line_new[:idx[0]+1]
                lines[i-1] = ' '.join(str(x) for x in line_new) 

        with open('out2.text','w') as f1:
            for i in range(len(lines)):
                f1.write(str(lines[i])+'\n')
                if str(lines[i][-1])=='=':
                    f1.write(' '+'\n')   
        #TO DEDERMINE THE VALID TIME FROM LIST
        if lines[0][4:7]=='COR' or lines[0][4:7]=='AMD':
            taf_time = lines[0][15:17]
            day = lines[0][13:15]
        else :
            taf_time = lines[0][11:13]
            day = lines[0][9:11]
        if taf_time == '05':
            sig_time = day+'18'
        elif taf_time == '11':
            sig_time = str(int(day)+1)+'00'
        elif taf_time == '17':
            sig_time = str(int(day)+1)+'06'
        elif taf_time == '23':
            sig_time = str(int(day)+1)+'12'

        taf_time = day + taf_time
        
        #print((taf_time), sig_time) #still str
        sig_time = int(sig_time)
        return(lines, taf_time, sig_time)