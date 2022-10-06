# USER GUIDE
## :memo: Where do I start?

### Step: Follow the steps below:
💡
- [X] Run the read_TAF.py at first
- [X] Choose whether crawl the data from website or not
- [X] Type in your CAA Account & Password
- [X] Result will only show the airport with WX
- NOTE: MAKE SURE YOU INSTALL THE google chrome webdriver
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
id1[LOOP]-->id2[TAF]
id1[LOOP]-->id3[BECMG]
id1[LOOP]-->id4[TEMPO]
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
```
![](https://i.imgur.com/4powZkZ.png)
>Done on 15, Spetember, 2022 [name=peterpan]# This Readme is for User guide
## :rocket: User guide

```shell=
Please run the read_TAF.py at first
Choose whether crawl the data from website or not
Type in your CAA Account & Password
Result will only show the airport with WX
*NOTE: MAKE SURE YOU INSTALL THE google chrome webdriver
*NOTE: Contain **r07229013@ntu.edu.tw** if you have any problems
```

## TAF Logic flow
```graphviz
digraph hierarchy {

                nodesep=0.5 // increases the separation between nodes
                
                node [color=Red,fontname=Courier,shape=box] //All nodes will this shape and colour
                edge [color=Blue, style=dashed] //All the lines look like this
                LOOP_start->{TAF TEMPO BECMG}
                TAF->{AMDorCOR TAFonly}
                AMDorCOR->{WX NoWX}
                WX->END->Nextline
                NoWX->Nextline
                Nextline->LOOP_start
                TAFonly->{WX NoWX}
                
                {TEMPO BECMG}->{INTIME OUTTIME}
                INTIME->WX
                OUTTIME->NoWX
                
                // Put them on the same level
}
