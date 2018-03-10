from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
#Return list of Fibonacci result
def get_Fibonacci_list(request,n):
    if request.method == 'GET':
        integer_n = int(n)
        if n==0:
            return '0'
        if integer_n < 0:
            return HttpResponse("invalud input")
        result = list()
        for i in range(0,integer_n):
            local_result = cache.get(i)
            if local_result:
                result.append(local_result)
            else:
                local_result = Fibonacci(i)
                cache.set(i,local_result)
                result.append(local_result)
        return HttpResponse(', '.join(str(x) for x in result))
    else:
        return HttpResponse("invalud method")
# Fibonacci function
# if input is less or equal to 1 return input
# else Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
# using cache in order to avoid duplicate computing
def Fibonacci(n):
    if n <= 1:
      return n

    local_result1 = cache.get(n-1)
    if local_result1:
       pass
    else:
        local_result1 = Fibonacci(n-1)
        cache.set(n-1,local_result1)

    local_result2 = cache.get(n-2)
    if local_result2:
        pass
    else:
        local_result2 = Fibonacci(n-2)
        cache.set(n-2,local_result2)

    return local_result1 + local_result2
