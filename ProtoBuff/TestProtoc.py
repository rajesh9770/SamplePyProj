from google.protobuf import text_format
from google.protobuf.message import DecodeError
import ProtoBuff.host_pb2 as host_pb2
import google.protobuf.json_format as json_format

def Parse2Protobuf(file_contents_string, protobuf, ascii_text=None):
    """Parse a string containing a protobuf.
         set ascii_text=True if ASCII representation is used
         Returns:
             True if the protobuf was read correctly.
         """

    if file_contents_string is None:
        print('Unable to read string %s while trying to parse it as protobuf '
              'message %s.', file_contents_string, type(protobuf))
        return False

    try:
        if ascii_text:
            text_format.Merge(file_contents_string, protobuf)
        else:
            protobuf.MergeFromString(file_contents_string)
        return True
    except (DecodeError, text_format.ParseError) as err:
        print('Error while parsing file %s to protobuf message %s: %s',
              file_contents_string, type(protobuf), err)
        return False


def create_host_data():
    my_hostdata = host_pb2.hostData()
    my_hostdata.snapshotId = "RTART"
    my_hostdata.snapshotTime = 7878787
    my_hostdata.operation = "Delete"


    host = my_hostdata.hosts.add()
    host.source = "test.com"
    host.accessVLANId = "LAN ID"
    #my_hostdata.hosts.append(host)

    print(my_hostdata)
    with open("sample_hosyt_data.bin", "wb") as f:
        bytesAsString = my_hostdata.SerializeToString()
        f.write(bytesAsString)

    with open("sample_hosyt_data.bin", "rb") as f:
        print("read values")
        sample_host = host_pb2.hostData().FromString(f.read())
        print(sample_host)
        print(json_format.MessageToJson(sample_host))


def read_sample_date_to_create_binary_date(file):
    # Reads host data in json format and creates proto hostData msg
    with open(file, "r") as f:
        # print("read values")
        sample_host = host_pb2.hostData()
        json_format.Parse(f.read(), sample_host)
        # sample_host = host_pb2.hostData().FromString(f.read())
        # print(sample_host)
        # print(json_format.MessageToJson(sample_host))

    # write hostData msg to proto format
    with open("sample.bin", "wb") as f:
        bytes_as_string = sample_host.SerializeToString()
        f.write(bytes_as_string)

    # read proto data into json
    with open("sample.bin", "rb") as f:
        sample_host = host_pb2.hostData().FromString(f.read())
        # print(sample_host)
        print(json_format.MessageToJson(sample_host))


if __name__ == "__main__":
    #create_host_data()
    read_sample_date_to_create_binary_date(
        "/Users/></Documents/project-notes/sample-data/mock/backup/3502a064-ef5b-466e-a6c8-16b1342cb63b-delete")