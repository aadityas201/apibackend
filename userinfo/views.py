from django.shortcuts import render
from apibackend.session import *
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
import requests
import json
from rest_framework.response import Response

# Create your views here.

#getting the USER info
class userInfo(APIView) : 
    def get(self,request):
        # print(request.GET)
        data = request.GET
        username = data['username']
        print(username)
        session = mysession()
        res = session.get(f"https://api.github.com/users/{username}")
        # print("HI" , res.url)
        # print(session.headers)
        # print(res.json())
        response  = (res.json())
        # print(response)
        # print(response["bio"])
        send_res = {}
        if(status.is_client_error(res.status_code)):
            return Response({'error': "Invalid Username"}, status=status.HTTP_400_BAD_REQUEST)
        send_res["username"] = response["login"]
        send_res["total_repos"] = response["public_repos"]
        if response["bio"] is not None : 
            send_res["bio"] = response["bio"]
        if response["location"] is not None : 
            send_res["location"] = response["location"]
        if response["twitter_username"] is not None : 
            send_res["twitter_username"] = response["twitter_username"]
        if response["avatar_url"] is not None : 
            send_res["avatar_url"] = response["avatar_url"]

        # print(send_res)
        # send_res_json = send_res
        # print(send_res_json)
        return JsonResponse(send_res)

