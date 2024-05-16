from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Poll
from .serializers import PollSerializer

@api_view(['GET', 'POST'])
def poll_list(request):
    if request.method == 'GET':
        # polls = Poll.objects.all()
        order  = request.query_params.get('order')

        if order == 'oldest':
            polls = Poll.objects.all().order_by('createdAt')
        elif order == 'latest':
            polls = Poll.objects.all().order_by('-createdAt')

        elif order == 'agree':
            polls = Poll.objects.all().order_by('-agree')
        elif order == 'disagree':
            polls = Poll.objects.all().order_by('-disagree')    

        else:
            polls = Poll.objects.all().order_by('createdAt')    

        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])    
def poll_detail(request, id):
    poll = Poll.objects.get(id=id)
    
    if request.method == 'GET':
        serializer = PollSerializer(poll)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])    
def poll_agree(request, id):
    poll = Poll.objects.get(id=id)

    poll.agree += 1
    poll.save()
    return Response({'status': 'agreed'})

@api_view(['POST'])
def poll_disagree(request, id):
    poll = Poll.objects.get(id=id)

    poll.disagree += 1
    poll.save()
    return Response({'status': 'disagreed'})