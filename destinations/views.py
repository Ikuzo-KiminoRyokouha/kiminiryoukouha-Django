import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import pandas
import pymysql
import environ
from destinations.utils.dataToCSV import dataToCSV
from destinations.utils.personalization import personalizationDestination


class IndexView(View):
    # data to csv
    def get(self, request):
        print('reset rating data and ')
        dataToCSV()
        return JsonResponse({'clear': True})
   
    # 
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)['data']
        print(body)
        userId = body['userId']
        tag = body['tag']
        start = body['start']
        end = body['end']
        areacode = body['areacode']
        sigungucode = body['sigungucode']
        
        personalizationItem = personalizationDestination(userId, start,end,tag,areacode,sigungucode)
        print(personalizationItem)
        return HttpResponse(personalizationItem )

    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")