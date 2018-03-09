from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, exceptions


def get_Fibonacci_list(request,n):
    if request.method == 'GET':
        result = list()
        print int(n)
        if int(n) < 0:
            return HttpResponse("invalud input")
        for i in range(0,int(n)):
            result.append(Fibonacci(i))
        return HttpResponse(', '.join(str(x) for x in result))
    else:
        return HttpResponse("invalud method")

def Fibonacci(n):
    if n <= 1:
      return n;
    return Fibonacci(n-1) + Fibonacci(n-2)
