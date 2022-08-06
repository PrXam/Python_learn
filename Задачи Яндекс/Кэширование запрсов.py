def delete(dict_requests, num):
    a = list(sorted(dict_requests.items(), key = lambda x: int(x[1])))
    print(num, "DELETE", (a.pop(0)[0]))
    dict_requests.clear()
    return dict(a)


def update(dict_requests, list_req, limit, num):
    if len(dict_requests) < limit:
        dict_requests[list_req[0]] = list_req[1]
    elif (int(min(dict_requests.values())) < int(list_req[1])):
        dict_requests = delete(dict_requests, num)
        dict_requests[list_req[0]] = list_req[1]
    return dict_requests


list1 = input().split()
request = int(list1[0])
limit = int(list1[1])
dict_requests = {}
for numreq in range(request):
    num = numreq + 1
    list_req = input().split()
    if list_req[0] in dict_requests.keys() and int(list_req[1]) > int(dict_requests.get(list_req[0])):
        dict_requests = update(dict_requests, list_req, limit, num)
        print(num, "UPDATE", list_req[0])
    elif not (list_req[0] in dict_requests.keys()):
        dict_requests = update(dict_requests, list_req, limit, num)
        print(num, "PUT", list_req[0])
