# Default Django imports
from django.shortcuts import render

# Custom imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

# Create your views here
class HealthCheckView(APIView):
    def get(self, request=None, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = 'ok'
        except Exception:
            db_status = 'failed'

        response_data = {
            'status': 'ok' if db_status == 'ok' else 'failed',
            'database': db_status,
        }
        return Response(response_data, status=status.HTTP_200_OK if db_status == 'ok' else status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductsView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({"message": "ok"}, status.HTTP_200_OK)