import optparse
import requests
import json
import xml2json
import xml2json2
import ast
from time import time


def recurse(d, k):
  if type(d)==type({}):
    for key in d:
        recurse(d[key], key)
  else:
    print (k,":", d)



querytrack = "http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&typename=track&maxfeatures=50" \
        "&filter=<PropertyIsEqualTo><PropertyName>TrackUUID</PropertyName><Literal>00539ddb-20d0-4e85-ab2b-5bff1d845a10</Literal></PropertyIsEqualTo>"
querym ="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&" \
"typename=motion_point&maxfeatures=50&filter=<PropertyIsEqualTo>" \
 "<PropertyName>TrackItemUUID</PropertyName><Literal>a7ce6fec-f064-4bf1-9ed1-fbf30b606487</Literal></PropertyIsEqualTo>"



query1="http://172.16.2.101:8080/geoserver/ows?service=wfs&version=2.0.0&request=getfeature&" \
      "typename=ne_50m_populated_places" \
      "&filter=<Filter><PropertyIsEqualTo>" \
     "<PropertyName>NAME</PropertyName><Literal>Sydney</Literal></PropertyIsEqualTo></Filter>"


query2="http://172.16.2.101:8080/geoserver/ows?service=wfs&version=1.1.0&request=getfeature" \
       "&typename=ne_50m_populated_places" \
       "&filter=<Filter><PropertyIsLike wildCard='*' singleChar='.' escape='!'>" \
       "<PropertyName>NAME</PropertyName><Literal>*lo*</Literal></PropertyIsLike></Filter>"


bboxquery = "http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&typename=track&maxfeatures=10&" \
            "BBOX=-80.95699,37.89799,-77.17946,52.04493&srsname=EPSG:4326" \

bboxquery2 = "http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&typename=track&maxfeatures=10&" \
             "filter=<ogc:Filter><ogc:BBOX><ogc:PropertyName>geometry</ogc:PropertyName><gml:Envelope srsDimension=\"2\" srsName=\"urn:x-ogc:def:crs:EPSG:4326\">" \
            "<gml:lowerCorner> -80.84640445134 37.84662451297</gml:lowerCorner><gml:upperCorner> -76.84318297811 58.84882187291</gml:upperCorner>" \
            "</gml:Envelope></ogc:BBOX></ogc:Filter>"

query="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=describefeaturetype&typename=motion_point"

q="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature" \
      "&typename=track&maxfeatures=50&filter=<And><PropertyIsGreaterThan><PropertyName>AvgSpeed</PropertyName>" \
      "<Literal>23</Literal></PropertyIsGreaterThan><PropertyIsLessThan><PropertyName>AvgSpeed</PropertyName><Literal>30</Literal>" \
      "</PropertyIsLessThan>" \
      "<PropertyIsEqualTo><PropertyName>TrackNumber</PropertyName><Literal>123123</Literal></PropertyIsEqualTo>" \
      "<PropertyIsEqualTo><PropertyName>TurnCount</PropertyName><Literal>3</Literal></PropertyIsEqualTo>" \
      "<PropertyIsEqualTo><PropertyName>MinSpeed</PropertyName><Literal>0</Literal></PropertyIsEqualTo></And>"

bbox2="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature" \
      "&typename=track&maxfeatures=14000&resultType=hits&filter=<And>" \
      "<PropertyIsGreaterThan><PropertyName>StartLatitude</PropertyName><Literal>38.8</Literal></PropertyIsGreaterThan>" \
      "<PropertyIsGreaterThan><PropertyName>StartLongitude</PropertyName><Literal>-104.9</Literal></PropertyIsGreaterThan>" \
      "<PropertyIsLessThan><PropertyName>EndLatitude</PropertyName><Literal>38.9</Literal></PropertyIsLessThan>" \
      "<PropertyIsLessThan><PropertyName>EndLongitude</PropertyName><Literal>-104.83</Literal></PropertyIsLessThan>" \
      "</And>"

query="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature" \
      "&typename=track&maxfeatures=10&filter=<And><PropertyIsGreaterThan><PropertyName>AvgSpeed</PropertyName>" \
      "<Literal>23</Literal></PropertyIsGreaterThan><PropertyIsLessThan><PropertyName>AvgSpeed</PropertyName><Literal>30</Literal>" \
      "</PropertyIsLessThan>" \
      "<PropertyIsEqualTo><PropertyName>MinSpeed</PropertyName><Literal>0</Literal></PropertyIsEqualTo></And>"

#query="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&typename=track&BBOX=-30.95699,50.89799,-30.17946,52.04493&srsname=EPSG:4326"

querydate="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&" \
          "request=getfeature&typename=track&maxfeatures=1&filter=<Filter><And>" \
          "<PropertyIsGreaterThan><PropertyName>StartTime</PropertyName><Function name='dateParse'><Literal>yyyy-MM-dd HH:mm:ss</Literal><Literal>2013-08-04 11:00:40</Literal></Function></PropertyIsGreaterThan>" \
          "<PropertyIsLessThan><PropertyName>EndTime</PropertyName><Function name='dateParse'><Literal>yyyy-MM-dd HH:mm:ss</Literal><Literal>2013-08-04 11:00:49</Literal></Function></PropertyIsLessThan>" \
          "</And></Filter>"

query3 ="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&" \
"typename=motion_point&maxfeatures=10&&" \
"filter=<Filter><PropertyIsLike wildCard='%' singleChar='.' escape='!'>" \
 "<PropertyName>MotionEvent</PropertyName><Literal>%RIG%TURN%</Literal>" \
 "</PropertyIsLike></Filter>"

queryMike="http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&" \
          "typename=motion_point&maxfeatures=100&filter=<Filter><PropertyIsLike wildCard='%' singleChar='.' escape='!' >" \
          "<PropertyName>MotionEvent</PropertyName><Literal>%RIG%</Literal></PropertyIsLike></Filter>"

bboxquery3 = "http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&typename=track&maxfeatures=10&" \
             "filter=<ogc:Filter><ogc:BBOX><ogc:PropertyName>geometry</ogc:PropertyName><gml:Box xmlns=\"http://www.opengis.net/cite/spatialTestSuite\" srsName=\"EPSG:4326\">" \
             "<gml:lowerCorner>-80.95699 37.89799</gml:lowerCorner><gml:upperCorner>-77.17946 52.04493</gml:upperCorner>" \
            "</gml:Box></ogc:BBOX></ogc:Filter>"

t0=time()
#httpurl = "http://172.16.2.10"
#print (querym)
#res= requests.get(querym)

postquery = "http://10.1.52.202:8282/geoserver/ows?service=wfs&version=1.1.0&request=getfeature&typename=track&maxfeatures=20&"
postdata= "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature maxFeatures=\"2\" xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" xmlns:ogc=\"http://www.opengis.net/ogc\" " \
         "xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" " \
         "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" outputFormat=\"text/xml; subtype=gml/3.1.1\" " \
         "resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query   srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\"><ogc:Filter>" \
         "<ogc:BBOX><ogc:PropertyName>geometry</ogc:PropertyName><gml:Envelope srsDimension=\"2\" srsName=\"urn:x-ogc:def:crs:EPSG:4326\"> " \
         "<gml:lowerCorner>-104.81446266174316 38.85271759192799</gml:lowerCorner><gml:upperCorner>-103.81120109558105 38.95555000464772</gml:upperCorner>" \
         "</gml:Envelope></ogc:BBOX></ogc:Filter></wfs:Query></wfs:GetFeature>"



p2 =  "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature maxFeatures=\"1\" xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" xmlns:ogc=\"http://www.opengis.net/ogc\" " \
         "xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" " \
         "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" outputFormat=\"text/xml; subtype=gml/3.1.1\" " \
         "resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query   srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\">" \
        "<ogc:Filter><ogc:PropertyIsGreaterThan matchCase=\"false\"><ogc:PropertyName>MaxSpeed</ogc:PropertyName><ogc:Literal>110.0</ogc:Literal></ogc:PropertyIsGreaterThan>" \
         "</ogc:Filter></wfs:Query></wfs:GetFeature>"

p3=  "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" "\
     "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" "\
     "xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" "\
     "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" "\
     "outputFormat=\"text/xml; subtype=gml/3.1.1\" resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query "\
     "srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\"><ogc:Filter><ogc:PropertyIsGreaterThan matchCase=\"false\"> "\
     "<ogc:PropertyName>MaxSpeed</ogc:PropertyName><ogc:Literal>60.0</ogc:Literal></ogc:PropertyIsGreaterThan></ogc:Filter></wfs:Query></wfs:GetFeature>"




p4=  "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" "\
     "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" "\
     "xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" "\
     "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" "\
     "outputFormat=\"text/xml; subtype=gml/3.1.1\" resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query "\
     "srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\"><ogc:Filter><ogc:PropertyIsLike wildCard='%' singleChar='.' escape='!' matchCase='false'> "\
     "<ogc:PropertyName>TrackNumber</ogc:PropertyName><ogc:Literal>%439%804%651%454%1%</ogc:Literal></ogc:PropertyIsLike></ogc:Filter></wfs:Query></wfs:GetFeature>"

p5=  "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" "\
     "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" "\
     "xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" "\
     "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" "\
     "outputFormat=\"text/xml; subtype=gml/3.1.1\" resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query "\
     "srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\"><ogc:Filter><ogc:PropertyIsLike wildCard='%' singleChar='.' escape='!' matchCase='false'> "\
     "<ogc:PropertyName>TrackNumber</ogc:PropertyName><ogc:Literal>13194139541321</ogc:Literal></ogc:PropertyIsLike></ogc:Filter></wfs:Query></wfs:GetFeature>"

p6=  "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" "\
     "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" "\
     "xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" "\
     "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" "\
     "outputFormat=\"text/xml; subtype=gml/3.1.1\" resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query "\
     "srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\">" \
     "<ogc:Filter><ogc:PropertyIsLike matchCase=\"false\"><ogc:PropertyName>TrackNumber</ogc:PropertyName><ogc:Literal>13194139541321</ogc:Literal>" \
       "</ogc:PropertyIsLike></ogc:Filter></wfs:Query></wfs:GetFeature>"

p7= "<?xml version=\"1.0\" encoding=\"UTF-8\"?><wfs:GetFeature xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" "\
     "xmlns:ogc=\"http://www.opengis.net/ogc\" xmlns:wfs=\"http://www.opengis.net/wfs\" xmlns:ows=\"http://www.opengis.net/ows\" "\
     "xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:gml=\"http://www.opengis.net/gml\" "\
     "handle=\"GeoTools 13-beta(d6d99849ba213258d20aa18e543d58c751040c2c) WFS 1.1.0 DataStore @EldoradoRHEL6-5Hydra#14\" "\
     "outputFormat=\"text/xml; subtype=gml/3.1.1\" resultType=\"results\" service=\"WFS\" version=\"1.1.0\"><wfs:Query "\
     "srsName=\"urn:x-ogc:def:crs:EPSG:4326\" typeName=\"geowave:track\">" \
     "<ogc:Filter><ogc:And><ogc:PropertyIsGreaterThan matchCase=\"false\"><ogc:PropertyName>StartTime</ogc:PropertyName><ogc:Function name='dateParse'><ogc:Literal>yyyy-MM-dd HH:mm:ss</ogc:Literal>" \
     "<ogc:Literal>2013-08-04 00:00:00</ogc:Literal></ogc:Function></ogc:PropertyIsGreaterThan><ogc:PropertyIsLessThan matchCase=\"false\"><ogc:PropertyName>StartTime</ogc:PropertyName>" \
     "<ogc:Function name='dateParse'><ogc:Literal>yyyy-MM-dd HH:mm:ss</ogc:Literal><ogc:Literal>2013-08-04 23:59:59</ogc:Literal></ogc:Function></ogc:PropertyIsLessThan></ogc:And></ogc:Filter></wfs:Query></wfs:GetFeature>"


res = requests.post(postquery,data=p2)
#res=requests.get(querydate);
t1=time()
#print(json2xml(res.content))
print ("query status", res.status_code)

#print(res.content)
#options= optparse.Values({"pretty": False}

jj = xml2json2.xml2json(res.content, options="-t")
#jj = xml2json.xml2json(res.content, options, 0)

print(jj)



"""
for key in jj.keys():
   print (key, "pari")
if res.text:
    results =  ast.literal_eval(xml2json2.xml2json(res.content, options = '-t'))
else:
    results = None




if 'ExceptionReport' not in results.keys():
    print ("successsssss")
else:
    print("EEEOEOEOEOEOEOEO ")

#print (jj)

print ("time is ", t1-t0)

js = json.loads(jj)

recurse(js, 1)

print("debug pari ", type(js), " _ ", js["{http://www.opengis.net/wfs}FeatureCollection"])



tree=ElementTree.parse(res.content)

root=tree.getroot()


try:
    for child in root:
        print child.tag, child.attrib

except:
    print "error parsing"

"""