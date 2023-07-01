from rest_framework.response import Response
import os, openai
from solo_project.settings import OPENAI_API_KEY,BASE_DIR,SECRET_KEY
from rest_framework.views import APIView
from rest_framework import status


openai.api_key = OPENAI_API_KEY
def using_gpt(prompts):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "You:" + prompts,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
        )
    return response.choices[0].text


class FortuneTeller(APIView):
    def post(self, request):
        try:
            type = request.data["type"]
            gender = request.data["gender"]
            year_of_birth = request.data["year_of_birth"]
            month_of_birth = request.data["month_of_birth"]
            day_of_birth = request.data["day_of_birth"]
            time_of_birth = request.data["time_of_birth"]
            min_of_birth = request.data["min_of_birth"]
            prompts = f"{year_of_birth}년 {month_of_birth}월 {day_of_birth}일 {time_of_birth}시 {min_of_birth}분생 {gender}의 올해 {type} 알려줘"
            result = using_gpt(prompts=prompts)
            return Response({"message":f"{result}"}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"잘못 입력하셨습니다."}, status=status.HTTP_400_BAD_REQUEST)

class Tarot(APIView):
    def post(self, request):
        try:
            tarot_type = request.data["type"]
            prompts = f"{tarot_type} 타로를 봐줘."
            result = using_gpt(prompts=prompts)
            return Response({"massage":f"{result}"}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"잘못 입력하셨습니다."}, status=status.HTTP_400_BAD_REQUEST)

class RecommendName(APIView):
    def post(self, request):
        try:
            type = request.data["type"]
            gender = request.data["gender"]
            prompts = f"{gender} {type} 이름을 3가지만 추천해 줘."
            result = using_gpt(prompts=prompts)
            return Response({"message":f"{result}"})
        except:
            return Response({"error":"잘못 입력하셨습니다."}, status=status.HTTP_400_BAD_REQUEST)