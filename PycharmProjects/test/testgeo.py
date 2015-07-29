


    #building the schema statically for now. In future, we will load this from postgres.
field_list_motion_point = ["geometry", "Mission", "TrackNumber", "TrackUUID", "TrackItemUUID", "MotionEvent", "StartTime",
                         "EndTime", "Classification", "Latitude", "Longitude", "Elevation", "FrameNumber", "PixelRow",
                         "PixelColumn"]
set_motion_points = set(field_list_motion_point)
field_list_track =  ["geometry", "Mission", "TrackNumber", "TrackUUID", "TrackItemUUID", "StartTime", "EndTime",
                 "Duration", "MinSpeed", "MaxSpeed", "AvgSpeed", "Distance", "StartLatitude", "EndLatitude", "StartLongitude",
                 "EndLongitude", "PointCount",  "EventCount", "TrackStatus", "TurnCount", "UTurnCount", "StopCount", "StopDuration",
                 "AvgStopDuration", "Classification", "PointTimeStamp" ]
set_track = set(field_list_track)

set_unique_to_motion_point = set_motion_points - set_track


points = [{'category': 'AvgSpeed', 'weight': 0.5, 'value': '23<>80'},
          {'category': 'StopDuration', 'weight': 0.4, 'value': '0.0'},
          {'category': 'TurnCount', 'weight': 0.25, 'value': '<3'},
          {'category': 'UTurnCount', 'weight': 0.25, 'value': '0'},
          {'category': 'MotionEvent', 'weight': 0.25, 'value': 'STOP'},
          ]
points1=[]
points2=[]

for p in points:
    #print (p['category'], "val ", p['value'])
    if p['category'] in set_unique_to_motion_point:
        #print (p['category'], "val ", p['value'])
        points2.append(p)
    else:
        #print ("p2 ", p['category'], "val ", p['value'])
        points1.append(p)


for p in points2:
    print ("point2 ", p['category'], "val ", p['value'])


    #.intersection(set_motion_points)
#s2 = set_motion_points.symmetric_difference(set_track)
#s3= set_motion_points - set_track
print (set_unique_to_motion_point)

