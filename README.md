<h1 align="center"><b>Stima Parser</b></h1>

[![Project Status: WIP – Initial development is in progress.](https://www.repostatus.org/badges/latest/wip.svg)]()

## <b>Description</b>
Stima parser extracts interruption data from  scheduled power interruptions pdf documents with regex pattern-matching for the following fields:

1. Region
2. County
3. Area
4. Date
5. Time
6. Mtaa

## <b>Prerequisites</b>
- Python3

## <b>Parser Current State</b>
This are randomly picked pattern match outputs from the parser. 
### Regions
```bash
***************************************************************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Power-20Interruption-20Notice-20--20Western-20&-20North-20Rift-20Regions-20--2025-20&-2026.05.2021.pdf
***************************************************************************************************************************************************

Region Match 1 at 39-60: AND NORTH RIFT REGION
Actual Region found at 46-53: TH RIFT
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2025.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Region Match 1 at 392-406: NAIROBI REGION
Actual Region found at 392-399: NAIROBI
Region Match 2 at 3097-3116: CENTRAL RIFT REGION
Actual Region found at 3097-3109: CENTRAL RIFT
Region Match 3 at 3650-3667: NORTH RIFT REGION
Actual Region found at 3650-3660: NORTH RIFT
Region Match 4 at 4317-4331: WESTERN REGION
Actual Region found at 4317-4324: WESTERN
Region Match 5 at 4789-4808: SOUTH NYANZA REGION
Actual Region found at 4789-4801: SOUTH NYANZA
Region Match 6 at 5433-5445: KENYA REGION
Actual Region found at 5433-5438: KENYA
Region Match 7 at 6769-6781: COAST REGION
Actual Region found at 6769-6774: COAST
*******************************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Power-20Interruptions-20Notice-20--20Kisumu-20CBD-20--2028.05.2021.pdf
*******************************************************************************************************************

Region Match 1 at 43-60: OF WESTERN REGION
Actual Region found at 43-53: OF WESTERN
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2001.07.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Region Match 1 at 392-406: NAIROBI REGION
Actual Region found at 392-399: NAIROBI
Region Match 2 at 1271-1288: NORTH RIFT REGION
Actual Region found at 1271-1281: NORTH RIFT
Region Match 3 at 1766-1785: SOUTH NYANZA REGION
Actual Region found at 1766-1778: SOUTH NYANZA
Region Match 4 at 2672-2684: KENYA REGION
Actual Region found at 2672-2677: KENYA
Region Match 5 at 3196-3216: NORTH EASTERN REGION
Actual Region found at 3196-3209: NORTH EASTERN
Region Match 6 at 4282-4294: COAST REGION
Actual Region found at 4282-4287: COAST
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Region Match 1 at 0-17: NORTH RIFT REGION
Actual Region found at 0-10: NORTH RIFT
Region Match 2 at 319-333: WESTERN REGION
Actual Region found at 319-326: WESTERN
Region Match 3 at 585-605: NORTH EASTERN REGION
Actual Region found at 585-598: NORTH EASTERN
Region Match 4 at 1753-1765: COAST REGION
Actual Region found at 1753-1758: COAST
Region Match 5 at 2422-2436: NAIROBI REGION
Actual Region found at 2422-2429: NAIROBI
Region Match 6 at 5801-5820: CENTRAL RIFT REGION
Actual Region found at 5801-5813: CENTRAL RIFT
```
### Counties
```
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2011.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

County Match 1 at 1555-1572: OF TURKANA COUNTY
Actual County found at 1558-1566: TURKANA 
County Match 2 at 2157-2172: OF NANDI COUNTY
Actual County found at 2160-2166: NANDI 
County Match 3 at 2410-2425: OF KISII COUNTY
Actual County found at 2413-2419: KISII 
County Match 4 at 2666-2683: OF NYAMIRA COUNTY
Actual County found at 2669-2677: NYAMIRA 
County Match 5 at 2984-3002: OF MACHAKOS COUNTY
Actual County found at 2987-2996: MACHAKOS 
County Match 6 at 3223-3237: OF EMBU COUNTY
Actual County found at 3226-3231: EMBU 
County Match 7 at 4554-4571: OF KAJIADO COUNTY
Actual County found at 4557-4565: KAJIADO 
County Match 8 at 4972-4988: OF NAKURU COUNTY
Actual County found at 4975-4982: NAKURU 
County Match 9 at 5228-5245: OF KERICHO COUNTY
Actual County found at 5231-5239: KERICHO 
County Match 10 at 5714-5735: OF UASIN GISHU COUNTY
Actual County found at 5717-5729: UASIN GISHU 
County Match 11 at 6008-6024: OF KIAMBU COUNTY
Actual County found at 6011-6018: KIAMBU 
County Match 12 at 7353-7369: OF KILIFI COUNTY
Actual County found at 7356-7363: KILIFI 
County Match 13 at 7869-7889: OF TANA RIVER COUNTY
Actual County found at 7872-7883: TANA RIVER 
***************************************************************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Power-20Interruption-20Notice-20--20Western-20&-20North-20Rift-20Regions-20--2025-20&-2026.05.2021.pdf
***************************************************************************************************************************************************

County Match 1 at 620-633: KISUMU COUNTY
Actual County found at 620-627: KISUMU 
County Match 2 at 1528-1546: UASIN GISHU COUNTY
Actual County found at 1528-1540: UASIN GISHU 
County Match 3 at 2477-2495: TRANS NZOIA COUNTY
Actual County found at 2477-2489: TRANS NZOIA 
County Match 4 at 2804-2826: ELGEYO MARAKWET COUNTY
Actual County found at 2804-2820: ELGEYO MARAKWET 
County Match 5 at 3206-3220: TURKANA COUNTY
Actual County found at 3206-3214: TURKANA 
County Match 6 at 3473-3490: WEST POKOT COUNTY
Actual County found at 3473-3484: WEST POKOT 
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2025.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

County Match 1 at 2862-2880: OF MACHAKOS COUNTY
Actual County found at 2865-2874: MACHAKOS 
County Match 2 at 3125-3141: OF NAKURU COUNTY
Actual County found at 3128-3135: NAKURU 
County Match 3 at 3676-3697: OF TRANS NZOIA COUNTY
Actual County found at 3679-3691: TRANS NZOIA 
County Match 4 at 4017-4038: OF UASIN GISHU COUNTY
Actual County found at 4020-4032: UASIN GISHU 
County Match 5 at 4340-4356: OF KISUMU COUNTY
Actual County found at 4343-4350: KISUMU 
County Match 6 at 4551-4569: OF KAKAMEGA COUNTY
Actual County found at 4554-4563: KAKAMEGA 
County Match 7 at 4817-4834: OF HOMABAY COUNTY
Actual County found at 4820-4828: HOMABAY 
County Match 8 at 5031-5047: OF MIGORI COUNTY
Actual County found at 5034-5041: MIGORI 
County Match 9 at 5454-5468: OF EMBU COUNTY
Actual County found at 5457-5462: EMBU 
County Match 10 at 6186-6200: OF MERU COUNTY
Actual County found at 6189-6194: MERU 
County Match 11 at 6790-6806: OF KILIFI COUNTY
Actual County found at 6793-6800: KILIFI 
*******************************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Power-20Interruptions-20Notice-20--20Kisumu-20CBD-20--2028.05.2021.pdf
*******************************************************************************************************************

County Match 1 at 589-602: KISUMU COUNTY
Actual County found at 589-596: KISUMU 
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2001.07.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

County Match 1 at 1012-1030: OF MACHAKOS COUNTY
Actual County found at 1015-1024: MACHAKOS 
County Match 2 at 1297-1318: OF UASIN GISHU COUNTY
Actual County found at 1300-1312: UASIN GISHU 
County Match 3 at 1794-1811: OF HOMABAY COUNTY
Actual County found at 1797-1805: HOMABAY 
County Match 4 at 2328-2343: OF KISII COUNTY
Actual County found at 2331-2337: KISII 
County Match 5 at 2693-2707: OF EMBU COUNTY
Actual County found at 2696-2701: EMBU 
County Match 6 at 3225-3241: OF KIAMBU COUNTY
Actual County found at 3228-3235: KIAMBU 
County Match 7 at 4303-4319: OF KILIFI COUNTY
Actual County found at 4306-4313: KILIFI 
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

County Match 1 at 26-47: OF TRANS NZOIA COUNTY
Actual County found at 29-41: TRANS NZOIA 
County Match 2 at 342-357: OF SIAYA COUNTY
Actual County found at 345-351: SIAYA 
County Match 3 at 614-630: OF KIAMBU COUNTY
Actual County found at 617-624: KIAMBU 
County Match 4 at 1774-1789: OF KWALE COUNTY
Actual County found at 1777-1783: KWALE 
County Match 5 at 4914-4932: OF MACHAKOS COUNTY
Actual County found at 4917-4926: MACHAKOS 
County Match 6 at 5829-5844: OF BOMET COUNTY
Actual County found at 5832-5838: BOMET 
```
### Areas
```text
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2025.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Area Match 1 at 409-438: AREA: PART OF MOMBASA ROAD
Actual Area found at 415-438: PART OF MOMBASA ROAD
Area Match 2 at 714-751: AREA: DANDORA, PART OF LUCKY SUMMER
Actual Area found at 720-751: DANDORA, PART OF LUCKY SUMMER
Area Match 3 at 968-982: AREA: SAIKA
Actual Area found at 974-982: SAIKA
Area Match 4 at 1202-1234: AREA: NYARI ESTATE
Actual Area found at 1208-1234: NYARI ESTATE
Area Match 5 at 1519-1546: AREA: PART OF NEW DONHOLM
Actual Area found at 1525-1546: PART OF NEW DONHOLM
Area Match 6 at 1746-1775: AREA: LANGATA, NAIROBI WEST
Actual Area found at 1752-1775: LANGATA, NAIROBI WEST
Area Match 7 at 2315-2342: AREA: PART OF WAIYAKI WAY
Actual Area found at 2321-2342: PART OF WAIYAKI WAY
Area Match 8 at 2882-2900: AREA: ATHI RIVER
Actual Area found at 2888-2900: ATHI RIVER
Area Match 9 at 3143-3170: AREA: PART OF RACE COURSE
Actual Area found at 3149-3170: PART OF RACE COURSE
Area Match 10 at 3433-3455: AREA: WHOLE OF LIKIA
Actual Area found at 3439-3455: WHOLE OF LIKIA
Area Match 11 at 3699-3730: AREA: CHISARE, KIBOMET, TWIGA
Actual Area found at 3705-3730: CHISARE, KIBOMET, TWIGA
Area Match 12 at 4040-4067: AREA: KERITA BURNT FOREST
Actual Area found at 4046-4067: KERITA BURNT FOREST
Area Match 13 at 4358-4395: AREA: NYANGOMA HOSPITAL
Actual Area found at 4364-4395: NYANGOMA HOSPITAL
Area Match 14 at 4571-4595: AREA: MATUNGU HOSPITAL
Actual Area found at 4577-4595: MATUNGU HOSPITAL
Area Match 15 at 4836-4859: AREA: MARIWA, LUGODHO
Actual Area found at 4842-4859: MARIWA, LUGODHO
Area Match 16 at 5049-5077: AREA: NYABOHANSE, ISIBANIA
Actual Area found at 5055-5077: NYABOHANSE, ISIBANIA
Area Match 17 at 5470-5517: AREA: MUTUNDURI, KIRIGI, MANYATTA, KIANJOKOMA
Actual Area found at 5476-5517: MUTUNDURI, KIRIGI, MANYATTA, KIANJOKOMA
Area Match 18 at 5875-5901: AREA: GACABARI, KIAMBERE
Actual Area found at 5881-5901: GACABARI, KIAMBERE
Area Match 19 at 6202-6236: AREA: KITHEO, ANKAMIA, MIKINDURI
Actual Area found at 6208-6236: KITHEO, ANKAMIA, MIKINDURI
Area Match 20 at 6808-6833: AREA: SHEERIJI CHEMICAL
Actual Area found at 6814-6833: SHEERIJI CHEMICAL
Area Match 21 at 7182-7198: AREA: KALOLENI
Actual Area found at 7188-7198: KALOLENI
*******************************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Power-20Interruptions-20Notice-20--20Kisumu-20CBD-20--2028.05.2021.pdf
*******************************************************************************************************************

Area Match 1 at 603-928: AREA: KISUMU CBD
Sea Food, Mombasa Millers, Pabari Enterprises, Sabuni Road, United Millers, 
Equator Bottlers Limited, Industrial Estate, Pipeline Estate, Bandani, Airport, 
Kenya Breweries Limited, Kisumu Concrete, Abyssinia Steel Mills, KIWASCO, 
Mambo  Leo,  Kanyakwar,  Highrise  Estate,  Kisumu  Specialist  Hospital,
Actual Area found at 609-928: KISUMU CBD
Sea Food, Mombasa Millers, Pabari Enterprises, Sabuni Road, United Millers, 
Equator Bottlers Limited, Industrial Estate, Pipeline Estate, Bandani, Airport, 
Kenya Breweries Limited, Kisumu Concrete, Abyssinia Steel Mills, KIWASCO, 
Mambo  Leo,  Kanyakwar,  Highrise  Estate,  Kisumu  Specialist  Hospital,
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2001.07.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Area Match 1 at 409-438: AREA: PART OF MOMBASA ROAD
Actual Area found at 415-438: PART OF MOMBASA ROAD
Area Match 2 at 598-612: AREA: SUNTON
Actual Area found at 604-612: SUNTON
Area Match 3 at 765-800: AREA: PART OF TRANSAMI, PIPELINE
Actual Area found at 771-800: PART OF TRANSAMI, PIPELINE
Area Match 4 at 1032-1045: AREA: ATHI
Actual Area found at 1038-1045: ATHI
Area Match 5 at 1320-1339: AREA: WEST INDIES
Actual Area found at 1326-1339: WEST INDIES
Area Match 6 at 1500-1528: AREA: MOTWOT MARKET, SIMAT
Actual Area found at 1506-1528: MOTWOT MARKET, SIMAT
Area Match 7 at 1813-1835: AREA: ORIANG, OYOMBE
Actual Area found at 1819-1835: ORIANG, OYOMBE
Area Match 8 at 2345-2372: AREA: NYAGUTA, NYANDEREMA
Actual Area found at 2351-2372: NYAGUTA, NYANDEREMA
Area Match 9 at 2527-2543: AREA: NYAMBOGA
Actual Area found at 2533-2543: NYAMBOGA
Area Match 10 at 2709-2744: AREA: MEDUSA INDUSTRIES, MWEMBENI
Actual Area found at 2715-2744: MEDUSA INDUSTRIES, MWEMBENI
Area Match 11 at 2986-3013: AREA: KATHANJURI, KITHERA
Actual Area found at 2992-3013: KATHANJURI, KITHERA
Area Match 12 at 3243-3274: AREA: LORETO, KABUKU, REDHILL,
Actual Area found at 3249-3274: LORETO, KABUKU, REDHILL,
Area Match 13 at 3969-3993: AREA: MATARA, GITUAMBA
Actual Area found at 3975-3993: MATARA, GITUAMBA
Area Match 14 at 4321-4338: AREA: MARIAKANI
Actual Area found at 4327-4338: MARIAKANI
Area Match 15 at 4696-4721: AREA: MARIAKANI, RABAI
Actual Area found at 4702-4721: MARIAKANI, RABAI
Area Match 16 at 5236-5251: AREA: KANAMAI
Actual Area found at 5242-5251: KANAMAI
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Area Match 1 at 49-82: AREA: KITALALE, SABOTI, KINYORO
Actual Area found at 55-82: KITALALE, SABOTI, KINYORO
Area Match 2 at 359-393: AREA: SIDINDI, SIMENYA, MUDHIERO
Actual Area found at 365-393: SIDINDI, SIMENYA, MUDHIERO
Area Match 3 at 632-671: AREA: KARANJEE, LIMURU SEWARAGE PLANT
Actual Area found at 638-671: KARANJEE, LIMURU SEWARAGE PLANT
Area Match 4 at 857-906: AREA: JUJA TOWN, JUJA INDUSTRIAL, KENYATTA ROAD
Actual Area found at 863-906: JUJA TOWN, JUJA INDUSTRIAL, KENYATTA ROAD
Area Match 5 at 1327-1369: AREA: CARBACID, RIVELCO, LARE ESCARPMENT
Actual Area found at 1333-1369: CARBACID, RIVELCO, LARE ESCARPMENT
Area Match 6 at 1791-1808: AREA: MWAMBUNGO
Actual Area found at 1797-1808: MWAMBUNGO
Area Match 7 at 2439-2478: AREA: PART OF PARKLANDS
Actual Area found at 2445-2478: PART OF PARKLANDS
Area Match 8 at 3228-3256: AREA: SHIMO LA TEWA, DUNGA
Actual Area found at 3234-3256: SHIMO LA TEWA, DUNGA
Area Match 9 at 3419-3461: AREA: LUSAKA ROAD, ADDIS ABABA, BAMBURI
Actual Area found at 3425-3461: LUSAKA ROAD, ADDIS ABABA, BAMBURI
Area Match 10 at 3681-3733: AREA: PART OF EASTLEIGH SECTION 3, PART OF MAJENGO
Actual Area found at 3687-3733: PART OF EASTLEIGH SECTION 3, PART OF MAJENGO
Area Match 11 at 3949-3975: AREA: BURUBURU PHASE 1, 2
Actual Area found at 3955-3975: BURUBURU PHASE 1, 2
Area Match 12 at 4307-4330: AREA: BURUBURU PHASE 4
Actual Area found at 4313-4330: BURUBURU PHASE 4
Area Match 13 at 4696-4726: AREA: GITHURAI 44, KIAMUMBI
Actual Area found at 4702-4726: GITHURAI 44, KIAMUMBI
Area Match 14 at 4934-5018: AREA: MOMBASA ROAD, KINANIE
Actual Area found at 4940-5018: MOMBASA ROAD, KINANIE
Area Match 15 at 5374-5389: AREA: VYULYA
Actual Area found at 5380-5389: VYULYA
Area Match 16 at 5595-5610: AREA: KALALA
Actual Area found at 5601-5610: KALALA
Area Match 17 at 5846-5882: AREA: SIONGIOROI, CHEBUNYO, EMARTI
Actual Area found at 5852-5882: SIONGIOROI, CHEBUNYO, EMARTI
```
### Dates
```bash
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2001.07.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Date Match 1 at 438-461: DATE: Sunday 04.07.2021
Actual Date found at 444-461: Sunday 04.07.2021
Date Match 2 at 612-636: DATE: Tuesday 06.07.2021
Actual Date found at 618-636: Tuesday 06.07.2021
Date Match 3 at 800-824: DATE: Tuesday 06.07.2021
Actual Date found at 806-824: Tuesday 06.07.2021
Date Match 4 at 1045-1068: DATE: Monday 05.07.2021
Actual Date found at 1051-1068: Monday 05.07.2021
Date Match 5 at 1339-1363: DATE: Tuesday 06.07.2021
Actual Date found at 1345-1363: Tuesday 06.07.2021
Date Match 6 at 1528-1554: DATE: Wednesday 07.07.2021
Actual Date found at 1534-1554: Wednesday 07.07.2021
Date Match 7 at 1835-1859: DATE: Tuesday 06.07.2021
Actual Date found at 1841-1859: Tuesday 06.07.2021
Date Match 8 at 2372-2395: DATE: Monday 05.07.2021
Actual Date found at 2378-2395: Monday 05.07.2021
Date Match 9 at 2543-2567: DATE: Tuesday 06.07.2021
Actual Date found at 2549-2567: Tuesday 06.07.2021
Date Match 10 at 2744-2767: DATE: Monday 05.07.2021
Actual Date found at 2750-2767: Monday 05.07.2021
Date Match 11 at 3013-3036: DATE: Monday 05.07.2021
Actual Date found at 3019-3036: Monday 05.07.2021
Date Match 12 at 3287-3312: DATE: Saturday 03.07.2012
Actual Date found at 3293-3312: Saturday 03.07.2012
Date Match 13 at 3993-4016: DATE: Monday 05.07.2021
Actual Date found at 3999-4016: Monday 05.07.2021
Date Match 14 at 4338-4361: DATE: Sunday 04.07.2021
Actual Date found at 4344-4361: Sunday 04.07.2021
Date Match 15 at 4721-4745: DATE: Tuesday 06.07.2021
Actual Date found at 4727-4745: Tuesday 06.07.2021
Date Match 16 at 5251-5275: DATE: Tuesday 06.07.2021
Actual Date found at 5257-5275: Tuesday 06.07.2021
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Date Match 1 at 82-105: DATE: Monday 07.06.2021
Actual Date found at 88-105: Monday 07.06.2021
Date Match 2 at 393-416: DATE: Sunday 06.06.2021
Actual Date found at 399-416: Sunday 06.06.2021
Date Match 3 at 671-696: DATE: Saturday 05.06.2021
Actual Date found at 677-696: Saturday 05.06.2021
Date Match 4 at 906-929: DATE: Sunday 06.06.2021
Actual Date found at 912-929: Sunday 06.06.2021
Date Match 5 at 1369-1392: DATE: Monday 07.06.2021
Actual Date found at 1375-1392: Monday 07.06.2021
Date Match 6 at 1808-1832: DATE: Tuesday 08.06.2021
Actual Date found at 1814-1832: Tuesday 08.06.2021
Date Match 7 at 2507-2530: DATE: Sunday 06.06.2021
Actual Date found at 2513-2530: Sunday 06.06.2021
Date Match 8 at 3256-3279: DATE: Sunday 06.06.2021
Actual Date found at 3262-3279: Sunday 06.06.2021
Date Match 9 at 3461-3484: DATE: Sunday 06.06.2021
Actual Date found at 3467-3484: Sunday 06.06.2021
Date Match 10 at 3733-3756: DATE: Monday 07.06.2021
Actual Date found at 3739-3756: Monday 07.06.2021
Date Match 11 at 3989-4013: DATE: Tuesday 08.06.2021
Actual Date found at 3995-4013: Tuesday 08.06.2021
Date Match 12 at 4354-4378: DATE: Tuesday 08.06.2021
Actual Date found at 4360-4378: Tuesday 08.06.2021
Date Match 13 at 4726-4750: DATE: Tuesday 08.06.2021
Actual Date found at 4732-4750: Tuesday 08.06.2021
Date Match 14 at 5018-5041: DATE: Sunday 06.06.2021
Actual Date found at 5024-5041: Sunday 06.06.2021
Date Match 15 at 5389-5412: DATE: Monday 07.06.2021
Actual Date found at 5395-5412: Monday 07.06.2021
Date Match 16 at 5610-5634: DATE: Tuesday 08.06.2021
Actual Date found at 5616-5634: Tuesday 08.06.2021
Date Match 17 at 5882-5908: DATE: Wednesday 09.06.2021
Actual Date found at 5888-5908: Wednesday 09.06.2021
```
### Time
```bash
*******************************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Power-20Interruptions-20Notice-20--20Kisumu-20CBD-20--2028.05.2021.pdf
*******************************************************************************************************************

Time Match 1 at 560-587: TIME: 7.00 A.M. – 5.00 P.M.
Actual Time found at 566-587: 7.00 A.M. – 5.00 P.M.
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2001.07.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Time Match 1 at 484-511: TIME: 9.00 A.M. - 5.00 P.M.
Actual Time found at 490-511: 9.00 A.M. - 5.00 P.M.
Time Match 2 at 669-696: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 675-696: 9.00 A.M. – 5.00 P.M.
Time Match 3 at 845-872: TIME: 9.00 A.M. - 1.00 P.M.
Actual Time found at 851-872: 9.00 A.M. - 1.00 P.M.
Time Match 4 at 1098-1127: TIME: 10.00 A.M. - 12.00 P.M.
Actual Time found at 1104-1127: 10.00 A.M. - 12.00 P.M.
Time Match 5 at 1397-1425: TIME: 10.00 A.M. – 2.00 P.M.
Actual Time found at 1403-1425: 10.00 A.M. – 2.00 P.M.
Time Match 6 at 1577-1606: TIME: 10.00 A.M. – 12.30 P.M.
Actual Time found at 1583-1606: 10.00 A.M. – 12.30 P.M.
Time Match 7 at 1892-1919: TIME: 9.00 A.M. - 4.00 P.M.
Actual Time found at 1898-1919: 9.00 A.M. - 4.00 P.M.
Time Match 8 at 2426-2454: TIME: 10.00 A.M. – 4.00 P.M.
Actual Time found at 2432-2454: 10.00 A.M. – 4.00 P.M.
Time Match 9 at 2597-2625: TIME: 10.00 A.M. – 4.00 P.M.
Actual Time found at 2603-2625: 10.00 A.M. – 4.00 P.M.
Time Match 10 at 2799-2826: TIME: 8.30 A.M. – 4.30 P.M.
Actual Time found at 2805-2826: 8.30 A.M. – 4.30 P.M.
Time Match 11 at 3066-3094: TIME: 8.30 A.M. – 11.30 A.M.
Actual Time found at 3072-3094: 8.30 A.M. – 11.30 A.M.
Time Match 12 at 3342-3369: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 3348-3369: 9.00 A.M. – 5.00 P.M.
Time Match 13 at 4049-4076: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 4055-4076: 9.00 A.M. – 5.00 P.M.
Time Match 14 at 4390-4417: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 4396-4417: 9.00 A.M. – 5.00 P.M.
Time Match 15 at 4777-4804: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 4783-4804: 9.00 A.M. – 5.00 P.M.
Time Match 16 at 5307-5334: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 5313-5334: 9.00 A.M. – 5.00 P.M.
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Time Match 1 at 139-166: TIME: 9.00 A.M. – 2.00 P.M.
Actual Time found at 145-166: 9.00 A.M. – 2.00 P.M.
Time Match 2 at 431-458: TIME: 8.30 A.M. – 5.00 P.M.
Actual Time found at 437-458: 8.30 A.M. – 5.00 P.M.
Time Match 3 at 726-754: TIME: 9.00 A.M. –  4.00 P.M.
Actual Time found at 732-754: 9.00 A.M. –  4.00 P.M.
Time Match 4 at 962-990: TIME: 9.00 A.M. –  5.00 P.M.
Actual Time found at 968-990: 9.00 A.M. –  5.00 P.M.
Time Match 5 at 1425-1452: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 1431-1452: 9.00 A.M. – 5.00 P.M.
Time Match 6 at 1864-1891: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 1870-1891: 9.00 A.M. – 5.00 P.M.
Time Match 7 at 2478-2505: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 2484-2505: 9.00 A.M. – 5.00 P.M.
Time Match 8 at 3314-3341: TIME: 9.00 A.M. - 5.00 P.M.
Actual Time found at 3320-3341: 9.00 A.M. - 5.00 P.M.
Time Match 9 at 3517-3544: TIME: 9.00 A.M. - 5.00 P.M.
Actual Time found at 3523-3544: 9.00 A.M. - 5.00 P.M.
Time Match 10 at 3789-3816: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 3795-3816: 9.00 A.M. – 5.00 P.M.
Time Match 11 at 4045-4072: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 4051-4072: 9.00 A.M. – 5.00 P.M.
Time Match 12 at 4410-4437: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 4416-4437: 9.00 A.M. – 5.00 P.M.
Time Match 13 at 4782-4809: TIME: 9.00 A.M. – 5.00 P.M.
Actual Time found at 4788-4809: 9.00 A.M. – 5.00 P.M.
Time Match 14 at 5076-5103: TIME: 9.00 A.M. - 5.00 P.M.
Actual Time found at 5082-5103: 9.00 A.M. - 5.00 P.M.
Time Match 15 at 5446-5473: TIME: 9.00 A.M. - 3.00 P.M.
Actual Time found at 5452-5473: 9.00 A.M. - 3.00 P.M.
Time Match 16 at 5667-5694: TIME: 9.00 A.M. - 3.00 P.M.
Actual Time found at 5673-5694: 9.00 A.M. - 3.00 P.M.
Time Match 17 at 5933-5960: TIME: 9.00 A.M. - 5.00 P.M.
Actual Time found at 5939-5960: 9.00 A.M. - 5.00 P.M.
```

### Mtaa
```bash
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2001.07.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Mtaa Match 1 was found at 525-589: \nOdds and Ends, Plaza 2000, Ellams, Subaru Kenya, Simba Corp & 
Actual Mtaa found at 525-589: \nOdds and Ends, Plaza 2000, Ellams, Subaru Kenya, Simba Corp &
Mtaa Match 2 was found at 715-762: \nSunton Business Center, Sunton Police Post & 
Actual Mtaa found at 715-762: \nSunton Business Center, Sunton Police Post &
Mtaa Match 3 was found at 895-1007: \nKenya Builders, Unique Est, Honey Suckle Est, Part of Pipeline Quarry, Parts \nof Transami, Part of Plot 10 & 
Actual Mtaa found at 895-1007: \nKenya Builders, Unique Est, Honey Suckle Est, Part of Pipeline Quarry, Parts \nof Transami, Part of Plot 10 &
Mtaa Match 4 was found at 1156-1279: \nKenya  Israel,  Kanaani,  Katheka  Kai,  Kathome,  Kithini,  Mua  Hills,  Kyumbi \nJunction, Leaders Academy, Maanzoni & 
Actual Mtaa found at 1156-1279: \nKenya  Israel,  Kanaani,  Katheka  Kai,  Kathome,  Kithini,  Mua  Hills,  Kyumbi \nJunction, Leaders Academy, Maanzoni &
Mtaa Match 5 was found at 1462-1515: \nPauls Bakery, West Indies, Kipkaren Est, Pioneer & 
Actual Mtaa found at 1462-1515: \nPauls Bakery, West Indies, Kipkaren Est, Pioneer &
Mtaa Match 6 was found at 1647-1785: \nSimat, Safaricom Booster, Kampi Ngombe, Soko Mujinga, Tuiyo Mkt, Tuioyo \nMilk  Cooler,  Motwot  Mkt,  Samutet  Mkt, Ndalat  Gaa Mkt &  
Actual Mtaa found at 1647-1785: \nSimat, Safaricom Booster, Kampi Ngombe, Soko Mujinga, Tuiyo Mkt, Tuioyo \nMilk  Cooler,  Motwot  Mkt,  Samutet  Mkt, Ndalat  Gaa Mkt &
Mtaa Match 7 was found at 1969-2354: \nAkwakra,  Mawego  W/Pump,  Mawego  Girls,  Mawego  Technical,  Ramula, \nRamba,  Lida  Youth,  Dani,  Kokwanyo,  Miyuga,  Got  Rateng,  Dago,  Njwelu, \nGweno  Kipodi,  Kauma,  Owiro,  Ogiro,  Kochora,  Mawego,  Akwakra,  Lida, \nRamba, Chut Ber, Kochora, Adhigo, Ogilo, Ramula, Ongoro, Apuko, Kauma, \nOwiro,  Dani,  Kanu,  Odino,  Got  Rateng,  Ruga,  Osuri,  Gweno,  Kipondi  & \n
Actual Mtaa found at 1969-2354: \nAkwakra,  Mawego  W/Pump,  Mawego  Girls,  Mawego  Technical,  Ramula, \nRamba,  Lida  Youth,  Dani,  Kokwanyo,  Miyuga,  Got  Rateng,  Dago,  Njwelu, \nGweno  Kipodi,  Kauma,  Owiro,  Ogiro,  Kochora,  Mawego,  Akwakra,  Lida, \nRamba, Chut Ber, Kochora, Adhigo, Ogilo, Ramula, Ongoro, Apuko, Kauma, \nOwiro,  Dani,  Kanu,  Odino,  Got  Rateng,  Ruga,  Osuri,  Gweno,  Kipondi  & \n
Mtaa Match 8 was found at 2514-2565: \nNyaguta Mkt, Nyanderema, Riangombenene Village & 
Actual Mtaa found at 2514-2565: \nNyaguta Mkt, Nyanderema, Riangombenene Village &
Mtaa Match 9 was found at 2689-2710: \nNyamboga Pri Sch & 
Actual Mtaa found at 2689-2710: \nNyamboga Pri Sch &
Mtaa Match 10 was found at 2897-3035: \nSt. Barnabas Sec Sch, Medusa Industries, Mwembeni, Karamani Boys Sec \nSch,  Kiaganari  Girls  Sec,  Kier  Houses,  Mukundu  C/Fact  &  
Actual Mtaa found at 2897-3035: \nSt. Barnabas Sec Sch, Medusa Industries, Mwembeni, Karamani Boys Sec \nSch,  Kiaganari  Girls  Sec,  Kier  Houses,  Mukundu  C/Fact  &
Mtaa Match 11 was found at 3454-4039: \nLoreto  Girls  Sch,  St.  Pauls  Univ,  Whole  of  Karanjee  Village,  Jumuia \nConference,  Kabuku S/Centre, Kabuku Water, Fairy  Flowers, Trophy Flora \nKabuki,  Flora  Delight,  Potato  Research,  International  School,  Terasol  Ltd, \nSara Rosen, Red Hill Villas, 2020 Est, Moo Lito, Zerenty, Tropical Heat Fact, \nMunyaka Karura, Sovereign Suits, Eva’s Garden, St. Julian’s, The Retreat, \nNgecha  S/Centre,  Part  of  Gatimu,  Thandes  Place,  Tigoni,  Tigoni  Police, \nBracken Hurst, Limuru County Club, Tigoni Farm, Ken Chick Ltd, Tigoni Hos, \nPart of Mabroukie Factory & 
Actual Mtaa found at 3454-4039: \nLoreto  Girls  Sch,  St.  Pauls  Univ,  Whole  of  Karanjee  Village,  Jumuia \nConference,  Kabuku S/Centre, Kabuku Water, Fairy  Flowers, Trophy Flora \nKabuki,  Flora  Delight,  Potato  Research,  International  School,  Terasol  Ltd, \nSara Rosen, Red Hill Villas, 2020 Est, Moo Lito, Zerenty, Tropical Heat Fact, \nMunyaka Karura, Sovereign Suits, Eva’s Garden, St. Julian’s, The Retreat, \nNgecha  S/Centre,  Part  of  Gatimu,  Thandes  Place,  Tigoni,  Tigoni  Police, \nBracken Hurst, Limuru County Club, Tigoni Farm, Ken Chick Ltd, Tigoni Hos, \nPart of Mabroukie Factory &
Mtaa Match 12 was found at 4172-4358: \nGituamba Village, Njathaini, Gatunguru Village, Matara T/Fact, Miugu Village, \nMatara  Dispensary,  Miugu  Tea  Buying  Center,  Mariaini  Sch,  Muchakai \nVillage, Matara S/Center & 
Actual Mtaa found at 4172-4358: \nGituamba Village, Njathaini, Gatunguru Village, Matara T/Fact, Miugu Village, \nMatara  Dispensary,  Miugu  Tea  Buying  Center,  Mariaini  Sch,  Muchakai \nVillage, Matara S/Center &
Mtaa Match 13 was found at 4523-4770: \nSheeriji  Chemical,  Part  of  Mariakani  Town,  Mwananchi  Maize  Millers, \nS/Centre,  Mariakani Stage, Shalma, \nKadzonzo Girls, \nMariakani Poly,  Mariakani  Sec,  Mwareni,  Mnyenzeni,  Tshangasini,  Bamba \nTown, Jila, Shangweni, Bandari & 
Actual Mtaa found at 4523-4770: \nSheeriji  Chemical,  Part  of  Mariakani  Town,  Mwananchi  Maize  Millers, \nS/Centre,  Mariakani Stage, Shalma, \nKadzonzo Girls, \nMariakani Poly,  Mariakani  Sec,  Mwareni,  Mnyenzeni,  Tshangasini,  Bamba \nTown, Jila, Shangweni, Bandari &
Mtaa Match 14 was found at 4920-5335: \nMariakani White House, Abba Shops, Luqman Petrol Stn, Crown Petroleum \nMCL,  Petro  City,  Kibanda  Hasara,  Elephant  Steel,  SS  Mehta  Kokotoni, \nKashan Ramji Quarry, Danjal Bro Quarry, Kokotoni Shopping, Kavee Quarry, \nKaydee Quarry, Shell P/Stn, Danka, PN Masru, Transeast, Kasemeni, Bofu \nMkt,  Mnyenzeni,  Matumbi,  Mazeras,  Rabai  H/Centre,  Dr.  Kraph,  Buni, \nKafuduni, Mwanda Disp, Mavirvirini & 
Actual Mtaa found at 4920-5335: \nMariakani White House, Abba Shops, Luqman Petrol Stn, Crown Petroleum \nMCL,  Petro  City,  Kibanda  Hasara,  Elephant  Steel,  SS  Mehta  Kokotoni, \nKashan Ramji Quarry, Danjal Bro Quarry, Kokotoni Shopping, Kavee Quarry, \nKaydee Quarry, Shell P/Stn, Danka, PN Masru, Transeast, Kasemeni, Bofu \nMkt,  Mnyenzeni,  Matumbi,  Mazeras,  Rabai  H/Centre,  Dr.  Kraph,  Buni, \nKafuduni, Mwanda Disp, Mavirvirini &
Mtaa Match 15 was found at 5459-5722: \nCoca  Cola  Bottlers,  North  Coast  Beach  Resort,  Whispering  Palms, \nGurudumu  Villas,  Royal  Reserve,  Jumuiya  Conference,  Salama  Beach \nResort,  Mwendo  wa  Panya,  St  Mathews,  Kwa  Mutua,  Kwa  Kariuki,  Boyani \nFarm, Kwa DO Majengo, Kwa Rogo & 
Actual Mtaa found at 5459-5722: \nCoca  Cola  Bottlers,  North  Coast  Beach  Resort,  Whispering  Palms, \nGurudumu  Villas,  Royal  Reserve,  Jumuiya  Conference,  Salama  Beach \nResort,  Mwendo  wa  Panya,  St  Mathews,  Kwa  Mutua,  Kwa  Kariuki,  Boyani \nFarm, Kwa DO Majengo, Kwa Rogo &
*****************************************************************************************************
/home/daniel/Desktop/learn/stima_parser/pdfs/Interruptions-20--2003.06.2021-20(Part-201-20of-202).pdf
*****************************************************************************************************

Mtaa Match 1 was found at 172-303: \nKitalale, Kinyoro, Mbio, Kotut Farm, Cheptumbelio, Manor House, Lavington, \nRafiki, Sango, Saboti, Muroki, Kapretwa, Gitwamba & 
Actual Mtaa found at 172-303: \nKitalale, Kinyoro, Mbio, Kotut Farm, Cheptumbelio, Manor House, Lavington, \nRafiki, Sango, Saboti, Muroki, Kapretwa, Gitwamba &
Mtaa Match 2 was found at 473-579: \nSimenya,  Sidindi,  Ruwe,  Uluthe,  Wang  Otong,  Mudhiero,  Sikalame,  Uhui \nDispensary, Luanda Pri & 
Actual Mtaa found at 473-579: \nSimenya,  Sidindi,  Ruwe,  Uluthe,  Wang  Otong,  Mudhiero,  Sikalame,  Uhui \nDispensary, Luanda Pri &
Mtaa Match 3 was found at 777-858: \nLimuru  Sewerage  Plant,  Limuru  Milk  Processor,  Ravenswood,  Karanjee  & \n
Actual Mtaa found at 777-858: \nLimuru  Sewerage  Plant,  Limuru  Milk  Processor,  Ravenswood,  Karanjee  & \n
Mtaa Match 4 was found at 1018-1336: \nKiaora, Bob Harris, Mungetho, Kariki, Azania, Gachororo, Njengo Evaflora, \nJuja JKUAT, Juja Industrial, Milimaini, Juja Town, Brister Girls, Kwa Woria, \nStar of Hope,  Superhighway  Est, Chai Est, Precious Blood, Newwood  Est, \nTheta  Hotel,  Mariapolis,  Kays  Est,  Joyland  Est,  Shalom  Est,  St.  Peter  & \n
Actual Mtaa found at 1018-1336: \nKiaora, Bob Harris, Mungetho, Kariki, Azania, Gachororo, Njengo Evaflora, \nJuja JKUAT, Juja Industrial, Milimaini, Juja Town, Brister Girls, Kwa Woria, \nStar of Hope,  Superhighway  Est, Chai Est, Precious Blood, Newwood  Est, \nTheta  Hotel,  Mariapolis,  Kays  Est,  Joyland  Est,  Shalom  Est,  St.  Peter  & \n
Mtaa Match 5 was found at 1488-1770: \nCarbacid  Ltd,  Rivelco,  Soko  Mjinga,  Afro  Dine  Ltd,  Kinale,  Kamae  Forest, \nSulmac,  Marira  Clinic,  Kimende  S/Centre,  Magina  S/Centre,  Maingi,  Bathi \nDam,  Gituamba  Borehole,  Mukeu,  Kiandutu  Shops,  Rukuma  Shops,  Kwa \nEdwards, Mbau-Ini, Mathore S/Centre & 
Actual Mtaa found at 1488-1770: \nCarbacid  Ltd,  Rivelco,  Soko  Mjinga,  Afro  Dine  Ltd,  Kinale,  Kamae  Forest, \nSulmac,  Marira  Clinic,  Kimende  S/Centre,  Magina  S/Centre,  Maingi,  Bathi \nDam,  Gituamba  Borehole,  Mukeu,  Kiandutu  Shops,  Rukuma  Shops,  Kwa \nEdwards, Mbau-Ini, Mathore S/Centre &
Mtaa Match 6 was found at 1937-2055: \n420 South, Mwisho wa  Lami, Colobus Conservancy, Blue Marlin, Neptune, \nKinondo Kwetu, Villa Kalista, Madago Sec & 
Actual Mtaa found at 1937-2055: \n420 South, Mwisho wa  Lami, Colobus Conservancy, Blue Marlin, Neptune, \nKinondo Kwetu, Villa Kalista, Madago Sec &
Mtaa Match 7 was found at 2567-3277: \nDATE: Sunday 06.06.2021                \nWhole of 1st Parklands Ave, Parts of Batubatu Rd, Swami Papa Rd, Ita Rd, \nBatu  Batu  Gardens,  Masari  Rd,  Pramukh  Swami  Ave,  Amani  Plaza,  High \nPark,  Avenue  Health  Care,  Oshwal  Complex  Swimming  Pool,  Citam \nParklands, Parts 2nd Parklands, Parts of Kusi Lane, Oshwal Academy Nairobi, \nJalaram Rd, Maratha Rd, Maya Apts, Aura Apts, Tigoni Apt, Kings Bury Court, \nNdovu  Ahmed  Lane,  Moran  Rd,  MCS  Fry’s  Highridge,  Parts  of  Mutati  Rd, \nChandarana  Food  Plus  S/Mkt,  Parts  of  4th  Parklands  Ave,  Parts  of  5th \nParklands  Ave,  Iregi  Rd,  Parts  of  Mwanzi  Rd,  Westgate  Shopping  Mall, \nAcculaser Institute, Parts of Ring Rd & 
Actual Mtaa found at 2567-3277: \nDATE: Sunday 06.06.2021                \nWhole of 1st Parklands Ave, Parts of Batubatu Rd, Swami Papa Rd, Ita Rd, \nBatu  Batu  Gardens,  Masari  Rd,  Pramukh  Swami  Ave,  Amani  Plaza,  High \nPark,  Avenue  Health  Care,  Oshwal  Complex  Swimming  Pool,  Citam \nParklands, Parts 2nd Parklands, Parts of Kusi Lane, Oshwal Academy Nairobi, \nJalaram Rd, Maratha Rd, Maya Apts, Aura Apts, Tigoni Apt, Kings Bury Court, \nNdovu  Ahmed  Lane,  Moran  Rd,  MCS  Fry’s  Highridge,  Parts  of  Mutati  Rd, \nChandarana  Food  Plus  S/Mkt,  Parts  of  4th  Parklands  Ave,  Parts  of  5th \nParklands  Ave,  Iregi  Rd,  Parts  of  Mwanzi  Rd,  Westgate  Shopping  Mall, \nAcculaser Institute, Parts of Ring Rd &
Mtaa Match 8 was found at 3416-3472: \nDavis & Shirtliff, Mater Hosp, Bondo Rd, Dundori Rd & 
Actual Mtaa found at 3416-3472: \nDavis & Shirtliff, Mater Hosp, Bondo Rd, Dundori Rd &
Mtaa Match 9 was found at 3623-3739: \nWire products, ASL, East Africa Cable, Impala Glass, Shanga Engineering, \nElite Tools, Kenya prisons, DT Dobie & 
Actual Mtaa found at 3623-3739: \nWire products, ASL, East Africa Cable, Impala Glass, Shanga Engineering, \nElite Tools, Kenya prisons, DT Dobie &
Mtaa Match 10 was found at 3900-4012: \nEastleigh  Section  3  Sewage,  California,  Pumwani  Maternity,  1st  Avenue \nEastleigh, Parts of Majengo & 
Actual Mtaa found at 3900-4012: \nEastleigh  Section  3  Sewage,  California,  Pumwani  Maternity,  1st  Avenue \nEastleigh, Parts of Majengo &
Mtaa Match 11 was found at 4161-4375: \nBuruburu  S/Centre,  Metropolitan  Hosp,  Buruburu  Flats,  Buruburu \nMaisonettes, Buruburu Girls High Sch, Huruma Girls High Sch, Ofafa Jericho \nHigh Sch, Buruburu Est, Phase 2 & 3, Jericho Est, Maringo Est & 
Actual Mtaa found at 4161-4375: \nBuruburu  S/Centre,  Metropolitan  Hosp,  Buruburu  Flats,  Buruburu \nMaisonettes, Buruburu Girls High Sch, Huruma Girls High Sch, Ofafa Jericho \nHigh Sch, Buruburu Est, Phase 2 & 3, Jericho Est, Maringo Est &
Mtaa Match 12 was found at 4533-4773: \nKCB  Complex,  Mbotela  S/Centre,  Makadara  Law  Court  &  DC’s  Office, \nBuruburu Phase 4 & 5, Part of Jogoo Rd, Part of Rabai Rd, Part of Mumias \nSouth Rd, Jogoo Rd Police Stn, Uchumi S/Mkt Jogoo Rd, Nyasa Rd, Nile Rd, \nUhuru Mkt & 
Actual Mtaa found at 4533-4773: \nKCB  Complex,  Mbotela  S/Centre,  Makadara  Law  Court  &  DC’s  Office, \nBuruburu Phase 4 & 5, Part of Jogoo Rd, Part of Rabai Rd, Part of Mumias \nSouth Rd, Jogoo Rd Police Stn, Uchumi S/Mkt Jogoo Rd, Nyasa Rd, Nile Rd, \nUhuru Mkt &
Mtaa Match 13 was found at 4912-4988: \nPart  of  Githurai  44,  Part  of  Kiamumbi,  Jacaranda  Est,  Maziwa  &  
Actual Mtaa found at 4912-4988: \nPart  of  Githurai  44,  Part  of  Kiamumbi,  Jacaranda  Est,  Maziwa  &
Mtaa Match 14 was found at 5212-5464: \nApex  TMD,  Ashapura  Business  Park,  Karibu  Homes,  Evergreen  State, \nKinanie Mkt, Kinanie, Shell Mto Mawe, Green Park Est, Lukenya Academy, \nGame  Ranch,  Kusyombungo  Hotel,  Amazing  Kenya,  Brava  Juices,  Gilbi \nBusiness Park, Top Tank & 
Actual Mtaa found at 5212-5464: \nApex  TMD,  Ashapura  Business  Park,  Karibu  Homes,  Evergreen  State, \nKinanie Mkt, Kinanie, Shell Mto Mawe, Green Park Est, Lukenya Academy, \nGame  Ranch,  Kusyombungo  Hotel,  Amazing  Kenya,  Brava  Juices,  Gilbi \nBusiness Park, Top Tank &
Mtaa Match 15 was found at 5589-5690: \nVyulya  Mkt,  Vyulya  Girls,  Muusini,  Katheka  Mkt  &  High  School,  Uuni \nSafaricom Booster & 
Actual Mtaa found at 5589-5690: \nVyulya  Mkt,  Vyulya  Girls,  Muusini,  Katheka  Mkt  &  High  School,  Uuni \nSafaricom Booster &
Mtaa Match 16 was found at 5815-5901: \nSt.  Catherine  Girls,  Kalala  Mkt,  Kalala  Pri,  Kalala  Safaricom  Booster  & \n
Actual Mtaa found at 5815-5901: \nSt.  Catherine  Girls,  Kalala  Mkt,  Kalala  Pri,  Kalala  Safaricom  Booster  & \n
Mtaa Match 17 was found at 6089-6255: \nSachora, Olbutyo, Sigor, Tumoi, Lugumek, Kabolwo, Lalela Farm, Kaboson, \nEmarti, Chebunyo, Kabolecho, Labotiet Mkt & Cooler, Siongiroi Mkt & Dairy, \nKapolesero & 
Actual Mtaa found at 6089-6255: \nSachora, Olbutyo, Sigor, Tumoi, Lugumek, Kabolwo, Lalela Farm, Kaboson, \nEmarti, Chebunyo, Kabolecho, Labotiet Mkt & Cooler, Siongiroi Mkt & Dairy, \nKapolesero &
```

## Built With
- [Regex](https://docs.python.org/3/library/re.html)
- [Stima-scraper](https://github.com/DanNduati/Stima_scraper)

## <b>License and Copyright</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)

Copyright 2022 Daniel Chege Nduati