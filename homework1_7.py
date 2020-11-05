#1
def answer_queries(k, *query_counts):
    count = 0
    number = 0
    for i in range(len(query_counts)):
        if query_counts[i] + count >= k:
            count = query_counts[i] + count - k
            number += 1
        else:
            return number+1
    if count > 0:
        number += count // k 
    return number+1


print(answer_queries(5, 10, 5, 5, 3, 2, 1))
