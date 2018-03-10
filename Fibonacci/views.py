from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
#Return list of Fibonacci result
def get_Fibonacci_list(request,n):
    if request.method == 'GET':#validate request method
        integer_n = int(n)
        if integer_n==0:
            return HttpResponse('[]')
        if integer_n < 0:#negative number not acceptable
            return HttpResponse(status=400)
        result = list()
        for i in range(0,integer_n):
            result.append(Fibonacci(i))
        return HttpResponse('[' +','.join(str(x) for x in result)+']')
    else:#bad method
        return HttpResponse(status=405)
# Fibonacci function
# if input is less or equal to 1 return input
# else Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
# using cache in order to avoid duplicate computing
def Fibonacci(n):
    if n <= 1:
        return n
    local_result = cache.get(n)
    if local_result:
        return local_result
    else:
        local_result = Fibonacci(n-1) + Fibonacci(n-2)
        cache.set(n,local_result)
        return local_result
