from django.http import JsonResponse
import json
import kociemba

def solve_cube(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode('utf-8'))
        cubeStr = post_data.get("cubeStr")
        try:
            solution = kociemba.solve(cubeStr)
            return JsonResponse({'message':solution})
        except:
            return JsonResponse({'message':'Entered configuration is invalid or out of limit!!'})
        
    return JsonResponse({'message':'not a POST request'})

