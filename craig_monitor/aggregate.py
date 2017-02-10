import json
from settings import archive_path, update_path




def main_aggregate():
    with open (archive_path) as archive_file:
        archive_data = json.load(archive_file)


    with open(update_path) as update_file:
        update_data = json.load(update_file)



    combined = archive_data+update_data

    with open(archive_path, 'wb') as outfile:
        json.dump(combined,outfile)

    print len(archive_data), 'items in current archive'
    print len(update_data), 'items to update archive with'
    print len(combined), 'final count of items'
    with open(update_path, 'wb') as outpath:
        json.dump([],outpath)
    print 'update archive erased'



