from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)
    
    assert x[:10] == [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629), 
    ("Cambridge Byron's Pool", 'Grantchester', 4.07204948005424), ('Cambridge Baits Bite', 'Milton', 5.115596582531859), 
    ('Girton', 'Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 'Haslingfield', 7.0443978959918025), 
    ('Oakington', 'Oakington', 7.12825901765745), ('Stapleford', 'Stapleford', 7.265704342799649), ('Comberton', 'Comberton', 7.735085060177142), 
    ('Dernford', 'Great Shelford', 7.993872393303291)]

    assert x[-10:] == [('Boscadjack', 'Wendron', 440.00325604140033), ('Gwithian', 'Gwithian', 442.0555261735786), 
    ('Helston County Bridge', 'Helston', 443.3788620846717), ('Loe Pool', 'Helston', 445.0724593420217), 
    ('Relubbus', 'Relubbus', 448.6500629265487), ('St Erth', 'St Erth', 449.0347773512542), 
    ('St Ives Consols Farm', 'St Ives', 450.07409071624505), ('Penzance Tesco', 'Penzance', 456.38638836619003), 
    ('Penzance Alverton', 'Penzance', 458.57727568406375), ('Penberth', 'Penberth', 467.53431870130544)]

test_stations_by_distance()