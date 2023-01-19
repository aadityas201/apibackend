from django.shortcuts import render
from apibackend.session import *
from rest_framework.views import APIView
from django.http import JsonResponse, response
import requests
import json
from rest_framework.response import Response

# Create your views here.

class repInfo(APIView) : 
    #getting all the repo info
    def get(self,request):
        # print(request.GET)
        data = request.GET
        username = data['username']
        page_no = data['page_number']
        per_page = 10
        session = mysession()
        res = session.get(f"https://api.github.com/users/{username}/repos?per_page={per_page}&page={page_no}")
        # print("Hello = ", res.json())
        # print("https://api.github.com/users/aadityas201/repos?per_page=10&page=2")
        # print(session.headers)
        # response = json.loads(res.json)
        return Response(res.json())

#getting the languages info such as HTML, CSS for each repo
class langauges(APIView):
    def get(self, request):
        data  = request.GET
        username = data['username']
        reponame = data['name']
        session  = mysession()
        res = session.get(f"https://api.github.com/repos/{username}/{reponame}/languages")

        return JsonResponse( res.json())

