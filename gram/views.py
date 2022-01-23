from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView , ListAPIView , DestroyAPIView , RetrieveAPIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from . import serializers



class Login(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ObtainPairSerializer


class Register(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSerializer

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def Create_Album(request):
    if request.user.id is not None:
        user_id = request.user.id
        request.data['user'] = request.user.id
        serializer = serializers.AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if serializer.data['publish']==True:
                return Response({"message":'Your album is published',
                                'data':serializer.data},status=status.HTTP_201_CREATED)
            else:
                album_obj = Albums.objects.all().reverse()
                album_obj = album_obj[0]
                request_data = {'album':album_obj.id,
                                'user':user_id}
                draft_serializer = serializers.DraftSerializer(data=request_data)
                if draft_serializer.is_valid(raise_exception=True):
                    draft_serializer.save()
                    return Response({"message":'Your album is saved as draft',
                                    'album_data':serializer.data},status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def Publish_Album(request,id):
    hashtags = request.data['hashtags']
    album_obj = Albums.objects.get(id=id)
    print(album_obj.publish)
    if album_obj.user.id == request.user.id:
        if album_obj.publish == False:
            album_obj.publish = True
            album_obj.font_color = request.data['font_color']
            album_obj.caption = request.data['caption']
            album_obj.position_coordinates_top = request.data['position_coordinates_top']
            album_obj.position_coordinates_down = request.data['position_coordinates_down']
            album_obj.position_coordinates_left = request.data['position_coordinates_left']
            album_obj.position_coordinates_right = request.data['position_coordinates_right']
            album_obj.save()
            hashtags_request_data = {'hashtag':str(request.data['hashtags']),'album':id}
            hashtag_serializer  = serializers.HashtagSerializer(data=hashtags_request_data)
            del request.data['hashtags']
            album_related_data = request.data
            if hashtag_serializer.is_valid(raise_exception=True):
                hashtag_serializer.save()
                return Response({'message':"Your album is published now",'hashtags':hashtag_serializer.data,'album_data':album_related_data},status=status.HTTP_200_OK)
        else:
            return Response({'message':"Album is already published"},status=status.HTTP_400_BAD_REQUEST)
    else:
       return Response({"message":"You can not access this album"},status=status.HTTP_400_BAD_REQUEST)
        

   
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def GetALLDrafts(request):
    if request.user.id is not None:
        queryset = Albums.objects.filter(publish=False).filter(user=request.user.id)
        serializer = serializers.AlbumSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
     
  
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def AddHashtags(request,id):
    if request.user.id is not None:
        request.data['album'] = id
        hashtag_serializer = serializers.HashtagSerializer(data=request.data)
        if hashtag_serializer.is_valid(raise_exception=True):
            return Response({"message":"Hasgtag is added for the album","data":hashtag_serializer.data},status=status.HTTP_200_OK)
