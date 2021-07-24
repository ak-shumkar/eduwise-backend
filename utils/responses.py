from rest_framework.response import Response
from rest_framework import status


def ok(data=None):
    return Response(data=data, status=status.HTTP_200_OK)


def bad_request(data=None):
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


def created(data=None):
    return Response(data=data, status=status.HTTP_201_CREATED)


def unauthorised(data=None):
    return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)


def forbidden(data=None):
    return Response(data=data, status=status.HTTP_403_FORBIDDEN)


def no_content(data=None):
    return Response(data=data, status=status.HTTP_204_NO_CONTENT)
