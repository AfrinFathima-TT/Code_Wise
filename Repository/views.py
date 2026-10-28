from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDb,SubmissionsDb
from Repository.serializers import QuestionSerializer,SubmissionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs = QuestionsDb.objects.all()    #query the QuestionDb  model to retrive all questions

        seriallizer_instance = QuestionSerializer(qs,many=True)  #Serialize the queryset using QuestionSerializer

        return Response(data=seriallizer_instance.data)

    # post method for adding questions
    def post(self,request):
        form_data = request.data   # get the data from the request body , pythob native type

        serializer_instance = QuestionSerializer(data=form_data)

        if  serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            #create a new questiondb instance with the form data
            QuestionsDb.objects.create(**actual_data)

            return Response(data={"message" : "Question added successfully"})
        else:
            return Response(data={"errors" : serializer_instance.errors})

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs = QuestionsDb.objects.get(id = pk)

        serializer_instance = QuestionSerializer(qs)

        return Response(data = serializer_instance.data)

    def put(self,request,pk):
        form_data = request.data     #get data from client

        serializer_instance = QuestionSerializer(data = form_data)
        if serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            QuestionsDb.objects.filter(id = pk).update(**actual_data)

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):

        QuestionsDb.objects.filter(id = pk).delete()

        return Response({
            "Message" : "Question deleted successfully...!"
        })

class SubmissionsListCreateView(APIView):
    def get(self,request):
        qs = SubmissionsDb.objects.all()
        submission_instance = SubmissionSerializer(qs,many=True)
        return Response(data=submission_instance.data)


    def post(self,request):
        form_data = request.data
        submission_instance = SubmissionSerializer(data = form_data)
        if submission_instance.is_valid():
            actual_data = submission_instance.validated_data

            SubmissionsDb.objects.create(**actual_data)

            return Response(data ={"Message" : "Answer added successfully...!"})
        else:
            return Response(data = {"eroors":submission_instance.errors})



class SubmissionsRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        # qs = SubmissionsDb.objects.get(id = pk)

        qs = get_object_or_404(SubmissionsDb,id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):

        form_data = request.data
        serializer_instance = SubmissionSerializer(data = form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            SubmissionsDb.objects.filter(id = pk).update(**actual_data)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        SubmissionsDb.objects.filter(id = pk).delete()

        return Response({"Message" : "Answer deleted successfully"})


class EvaluateSubmissionView(APIView):
    def put(self,request,pk):

        form_data =request.data

        SubmissionsDb.objects.filter(id = pk).update(**form_data)

        return Response(data={
            "Message" : "Updated....!"
        })