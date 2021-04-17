# Ranges:
# A. 10k - 20k
# B.  1k - 5k
# C. 22k - 30k
# D. 15k - 25k
# E.  2k - 3k
# F. 40k - 50k


class Request():

    def __init__(self,start,end):
        self.start = start 
        self.end = end

    def is_overlap(self,request2):
        #print(self.start,self.end,request2)
        if self.start < request2.start < self.end \
            or self.start < request2.end < self.end:
            return True
        return False

    def __str__(self):
        return "Start : {} End: {}".format(self.start,self.end)

requestProcessed = []

# def does_processed_request_overlapwith(current_request):
#     for past_request in requestProcessed:
#         if current_request.is_overlap(past_request):
#             return past_request
#     return None


def get_nonoverlapping_part(current_request):
    q = [current_request]
    last_data = []
    while q:
        current_request = q.pop(0)
        new_requests = []
        for p_r in requestProcessed:
            if p_r.is_overlap(current_request):
                min_current,max_current = min(current_request.start,current_request.end) , max(current_request.start,current_request.end)
                if  p_r.start <= min_current and max_current <= p_r.end:
                    return [p_r]
                if  min_current < p_r.start:
                    new_requests.append(Request(min_current,p_r.start))
                if  max_current > p_r.end:
                    new_requests.append(Request(max_current,p_r.end))    
            if new_requests: 
                q.extend(new_requests)
                break 
        if new_requests:
            last_data = new_requests
    if last_data: return last_data

def dataToSend(current_request):
    non_overlapping_parts = get_nonoverlapping_part(current_request)
    if non_overlapping_parts:
        for n_p in non_overlapping_parts:
            if n_p not in requestProcessed:
                requestProcessed.append(n_p)
        return non_overlapping_parts
    requestProcessed.append(current_request)
    return [current_request]


requests = [(10,20),(1,5),(22,30),(15,25),(2,3),(40,50)]

for s,e in requests:
    print(" For request :")
    print(Request(s,e))
    res = dataToSend(Request(s,e))
    if res:
        print("Send range :")
        for t_r in res:
            print(t_r)
