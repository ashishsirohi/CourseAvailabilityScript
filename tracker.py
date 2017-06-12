import re
import urllib2
import urllib
import json
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup


headers = { 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language" : "en-US,en;q=0.5",
	"Connection" : "keep-alive",
	"Content-Length" : "6198",
	"Content-Type" : "text/plain",
	"Host" : "col.eum-appdynamics.com",
	"Origin" : "https://webapp4.asu.edu",
	"Referer" :	"https://webapp4.asu.edu/catalog/classlist?s=CSE&t=2177&e=all&hon=F&promod=F",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
}


payload = {"vr":"4.3.1.0","dt":"R","rg":"0","es":[{"eg":"0","et":0,"eu":"0://1/2/3?4","ts":1495579895702,"mc":
{"FET":4011,"DRT":3709,"PRT":302,"ts":1495579910297,"PLC":1},"mx":{"PLT":18598,"FBT":13634,"SCT":101
,"DLT":65,"TCP":0,"RAT":13533,"FET":4964,"DRT":2456,"DDT":923,"DPT":1533,"PRT":2508,"DOM":16090,"ts"
:1495579895702,"PLC":1},"pl":"Class Search / Course Catalog","sm":{"cg":"0","btgan":"ArizonaStateUniv_e5538580-29e9-45ee-80f7-b04d155220e6"
,"bt":[{"id":"5163","dn":-1,"ert":629}]},"rt":{"v":2,"ic":{"other":1,"link":15,"script":26,"css":1,"img"
:1},"it":{"other":1,"link":2,"script":3,"css":4,"img":5},"rc":{"other":2,"css":15,"script":26,"img":1
},"rt":{"other":1,"css":2,"script":3,"img":4},"f":{"1":["startTime","redirectStart","redirectEnd","fetchStart"
,"dnsLookupStart","dnsLookupEnd","connectStart","connectEnd","requestStart","responseStart","responseEnd"
],"2":["startTime","fetchStart","responseEnd"]},"t":1495579895702,"r":[{"u":"0://1/2/3?4","i":1,"r":1
,"f":1,"o":1,"m":[0,-1,-1,12,29,94,94,94,101,13634,14557]},{"u":"0://5/6?7","i":2,"r":1,"f":1,"o":13883
,"m":[0,-1,-1,0,0,0,0,0,0,82,191]},{"u":"0://1/2/6/8","i":2,"r":2,"f":1,"o":13885,"m":[0,-1,-1,0,0,0
,0,0,0,81,194]},{"u":"0://1/2/6/9","i":2,"r":2,"f":1,"o":13887,"m":[0,-1,-1,0,0,0,0,0,0,82,217]},{"u"
:"0://1/2/6/10?11","i":2,"r":2,"f":1,"o":13888,"m":[0,-1,-1,0,0,0,0,0,0,83,222]},{"u":"0://1/2/12/13/14/15","i":2,"r":2,"f":1,"o":13889,"m":[0,-1,-1,0,0,0,0,0,0,84,231]},{"u":"0://1/2/6/16","i":2,"r":2
,"f":1,"o":13889,"m":[0,-1,-1,0,0,0,0,0,0,85,234]},{"u":"0://1/2/6/17/6/18","i":2,"r":2,"f":1,"o":13891
,"m":[0,-1,-1,0,0,0,0,0,0,85,237]},{"u":"0://1/2/12/19","i":3,"r":3,"f":1,"o":13892,"m":[0,-1,-1,0,0
,0,0,0,0,86,244]},{"u":"0://1/2/12/13/20/21","i":3,"r":3,"f":1,"o":13893,"m":[0,-1,-1,0,0,0,0,0,0,87
,252]},{"u":"0://1/2/12/13/22/23","i":3,"r":3,"f":1,"o":13894,"m":[0,-1,-1,0,0,0,0,0,0,86,262]},{"u"
:"0://1/2/12/13/22/24","i":3,"r":3,"f":1,"o":13895,"m":[0,-1,-1,0,0,0,0,0,0,88,264]},{"u":"0://1/2/12/13/14/25","i":3,"r":3,"f":1,"o":13896,"m":[0,-1,-1,0,0,0,0,0,0,90,267]},{"u":"0://1/2/12/13/14/26","i"
:3,"r":3,"f":1,"o":13897,"m":[0,-1,-1,0,0,0,0,0,0,91,272]},{"u":"0://1/2/12/13/27/28","i":3,"r":3,"f"
:1,"o":13897,"m":[0,-1,-1,0,0,0,0,0,0,92,275]},{"u":"0://1/2/12/13/27/29","i":3,"r":3,"f":1,"o":13898
,"m":[0,-1,-1,0,0,0,0,0,0,93,278]},{"u":"0://1/2/12/13/27/30","i":3,"r":3,"f":1,"o":13899,"m":[0,-1,-1
,0,0,0,0,0,0,94,280]},{"u":"0://1/2/12/13/27/31","i":3,"r":3,"f":1,"o":13901,"m":[0,-1,-1,0,0,0,0,0,0
,93,282]},{"u":"0://1/2/12/13/27/32?33","i":3,"r":3,"f":1,"o":13903,"m":[0,-1,-1,0,0,0,0,0,0,93,283]
},{"u":"0://1/2/12/13/34/35","i":3,"r":3,"f":1,"o":13904,"m":[0,-1,-1,0,0,0,0,0,0,93,286]},{"u":"0://1/2/12/13/36/37","i":3,"r":3,"f":1,"o":13905,"m":[0,-1,-1,0,0,0,0,0,0,97,289]},{"u":"0://1/2/12/13/38/39","i":3,"r":3,"f":1,"o":13906,"m":[0,-1,-1,0,0,0,0,0,0,99,320]},{"u":"0://1/2/12/13/40/41/42","i":3,"r":3,"f":1,"o":13906,"m":[0,-1,-1,0,0,0,0,0,0,100,324]},{"u":"0://1/2/12/43","i":3,"r":3,"f":1,"o"
:13907,"m":[0,-1,-1,0,0,0,0,0,0,102,326]},{"u":"0://1/2/12/2/44?45","i":3,"r":3,"f":1,"o":13908,"m":
[0,-1,-1,0,0,0,0,0,0,103,331]},{"u":"0://1/2/12/13/46/47","i":3,"r":3,"f":1,"o":13909,"m":[0,-1,-1,0
,0,0,0,0,0,103,333]},{"u":"0://1/2/12/13/22/48","i":2,"r":2,"f":1,"o":13911,"m":[0,-1,-1,0,0,0,0,0,0
,103,335]},{"u":"0://1/2/12/13/49/50","i":2,"r":2,"f":1,"o":13911,"m":[0,-1,-1,0,0,0,0,0,0,104,341]}
,{"u":"0://1/2/12/13/36/51","i":2,"r":2,"f":1,"o":13912,"m":[0,-1,-1,0,0,0,0,0,0,105,351]},{"u":"0://1/2/12/13/40/41/52","i":2,"r":2,"f":1,"o":13913,"m":[0,-1,-1,0,0,0,0,0,0,108,356]},{"u":"0://1/2/12/13/53/6/54","i":2,"r":2,"f":1,"o":13914,"m":[0,-1,-1,0,0,0,0,0,0,109,366]},{"u":"0://1/2/12/13/53/12/55","i":3,"r":3,"f":1,"o":13915,"m":[0,-1,-1,0,0,0,0,0,0,109,372]},{"u":"0://1/2/12/13/53/12/56","i":3,"r":3,"f":1,"o":13916,"m":[0,-1,-1,0,0,0,0,0,0,109,374]},{"u":"0://1/2/12/13/53/12/57","i":3,"r":3,"f":1,"o":13917,"m":[0,-1,-1,0,0,0,0,0,0,109,375]},{"u":"0://1/2/6/58","i":2,"r":2,"f":1,"o":13919,"m"
:[0,-1,-1,0,0,0,0,0,0,110,378]},{"u":"0://1/2/59/60/6/61","i":2,"r":2,"f":1,"o":13920,"m":[0,-1,-1,0
,0,0,0,0,0,110,385]},{"u":"0://62/63/64","i":3,"r":3,"f":1,"o":13920,"m":[0,-1,-1,0,0,0,0,0,0,113,389
]},{"u":"0://1/2/59/60/12/65?66","i":3,"r":3,"f":1,"o":13921,"m":[0,-1,-1,0,0,0,0,0,0,114,392]},{"u"
:"0://1/2/6/67?33","i":2,"r":2,"f":1,"o":13922,"m":[0,-1,-1,0,0,0,0,0,0,114,402]},{"u":"0://1/2/12/2/68","i":3,"r":3,"f":1,"o":13922,"m":[0,-1,-1,0,0,0,0,0,0,115,421]},{"u":"0://1/2/12/13/69/70","i":3
,"r":3,"f":1,"o":13923,"m":[0,-1,-1,0,0,0,0,0,0,116,424]},{"u":"0://1/2/6/71","i":4,"r":2,"f":1,"o":14093
,"m":[0,-1,-1,0,0,0,0,0,0,281,300]},{"u":"0://72/73","i":3,"r":3,"f":1,"o":14894,"m":[0,-1,-1,0,0,0,0
,0,0,1095,1149]},{"u":"0://72/74?75","i":5,"r":4,"f":2,"o":16073,"m":[0,0,41]}]},"si":5}],"ai":"037e7c11_1859_e92d_c651_00350ff38b72"
,"gs":["8cf6f6dd-e8c3-476b-ac53-37fa0d0d9dd5"],"up":["https","webapp4.asu.edu","catalog","classlist"
,"s=CSE&t=2177&e=all&hon=F&promod=F","fonts.googleapis.com","css","family=Roboto:100,500,700,regular&subset=latin","global.css","asu_print.css","courseCatalog.css","version=2.0.6","js","jquery","cluetip"
,"jquery.cluetip.css","jquery.autocomplete.css","font-awesome-4.6.1","font-awesome.min.css","jquery-1.11.1.js","ui","jquery-ui.min.js","jqModal","jqModal.js","jqDrag.js","jquery.hoverIntent.js","jquery.cluetip.js","autocomplete","jquery.bgiframe.min.js","jquery.ajaxQueue.js","thickbox-compressed.js","jquery.autocomplete.js","localdata.js","version=2.0.4","selectbox","jquery.selectboxes.js","popup","jquery.popup.js","hintText","hints.js","timeSelector","src","jquery.ptTimeSelect.js","dateTimeValidation.js","catalog.js","version=2.13.0","cookie","jquery.cookie.js","jqModal.css","calendar","calendar.css","jquery.popup.css","jquery.ptTimeSelect.css","dataTable","jquery.dataTables.css","jquery.dataTables.min.js","time.js","natural.js","ps_tab.css","asuthemes-catalog","4.3","asu_header.css","cdn.appdynamics.com","adrum","adrum-latest.js","asu_header.js","version=4.3.1","main.css","asu-bootstrap.js","dropdown","jquery.ie-select-width.js","ie.css","ssl.google-analytics.com","ga.js","__utm.gif","utmwv=5.6.7&utms=7&utmn=798054465&utmhn=webapp4.asu.edu&utmc..."]}

url = 'https://col.eum-appdynamics.com/eumcollector/beacons/browser/v1/AD-AAB-AAC-HZV/adrum'

#url = 'https://webapp4.asu.edu/catalog/Home.ext'

"""opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
html = opener.open(url)"""

html = requests.post(url, headers=headers, data=json.dumps(payload))

print html.content

