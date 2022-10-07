from urllib.parse import quote
import uuid

def build_URI(gid):
    gid = quote(gid)
    return "inst:%s" % (gid)

def uuid_from_string(str):
    return uuid.uuid5(uuid.NAMESPACE_DNS, str)