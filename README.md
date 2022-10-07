# USER GUIDE
## :memo: Where do I start?
### 此專案主要含 
1. read_TAF.py (main)
2. crawler.py (for crawling data)
3. preprocess.py (rearrange the raw data to the readable form)
### Step: Follow the steps below:
💡
- [X] Run the read_TAF.py at first
- [X] Choose whether crawl the data from website or not
- [X] Type in your CAA Account & Password
- [X] Result will only show the airport with WX
- NOTE: MAKE SURE YOU INSTALL THE google chrome webdriver
- NOTE: The path in preprocess.py is the location of your webdriver
- Please refer the following link for webdriver resource
- Crawling data is in crawler.py
[webdriver resource](https://www.youtube.com/watch?v=ximjGyZ93YQ&t=2935s)

- Contact *r07229013@ntu.edu.tw* if you have any problems
### Process :
```mermaid
graph LR
  id1[read_TAF.py]--crawl data-->id2[taf.txt]--rearrange form-->id3[out2.txt]--Logic flow-->id4(RESULTS)
```
:rocket::rocket:
## TAF Logic flow
#This is the brief flow chart of the for loop inside the code
```mermaid
graph TD
id1[LOOP_start]-->id2[TAF]
id1[LOOP_start]-->id3[BECMG]
id1[LOOP_start]-->id4[TEMPO]
id2-->id5[AMD/COR]
id2-->id6[TAFonly]
id5-->id7[WX]
id5-->id8[NoWX]
id7-->id9[end]
id9-->id10
id8-->id10[next line]
id6-->id7
id6-->id8
id3-->id11[intime]
id3-->id12[outtime]
id11-->id7
id12-->id8
id4-->id11
id4-->id12
id10-->id13[LOOP_next]
```
>Done on 15, Spetember, 2022 [name=peterpan]# This Readme is for User guide
