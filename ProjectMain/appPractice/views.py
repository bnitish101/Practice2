from django.shortcuts import render
from .models import Room

# Create your views here.

home = [
    {'id':1, 'name':'Home One'},
    {'id':2, 'name':'Home Two'},
    {'id':3, 'name':'Home Three'},
]

roomData_niu = [
    {'id':1, 'name':'Frontend Developer'},
    {'id':2, 'name':'Backend Developer'},
    {'id':3, 'name':'Full Stack Developer'},
]

def home(request):
    roomData = Room.objects.all()
    print('---------')
    print(roomData)
    print('---------')
    context = {'roomData':roomData}
    return render(request, 'appPractice/home.html', context)

roomDetails = [
    {'id': 1, 'name':'Room One'},
    {'id': 2, 'name':'Room Two'},
    {'id': 3, 'name':'Room Three'},
]
def room(request, pk):
    roomName = None
    # context = {'roomData':roomData}
    # print('---------------')
    # print(pk)
    # print(int(pk))
    # print('---------------')
    # for i in roomData:
    #     print('---------------')
    #     print(i)
    #     print('---------------')
    #     if i['id'] == int(pk):
    #         roomName = i['name']
    roomName = Room.objects.get(id=pk)

    context = {'roomName':roomName}
    return render(request, 'appPractice/room.html', context)