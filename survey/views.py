from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Survey
from .serializers import SurveySerializer
from django.views.generic import ListView
from .forms import AnswerForm


class SurveyViewApi(APIView):
    model = Survey
    queryset = Survey.objects.all()


    def get(self, request):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response({"surveys": serializer.data})

    def post(self, request):
        survey_saved = 0
        survey = request.data.get('survey')
        serializer = SurveySerializer(data=survey)
        if serializer.is_valid(raise_exception=True):
            survey_saved = serializer.save()
        return Response({"success": "Survey '{}' created successfully".format(survey_saved.name)})


class SurveyView(View):
    model = Survey
    queryset = Survey.objects.all()
    template_name = 'surveys/surveys_list.html'


class SurveyListView(ListView):
    model = Survey
    queryset = Survey.objects.all()
    template_name = 'surveys/surveys_list.html'

    def post_answer(self, request, pk):
        submit_button = request.POST.get("submit")

        text = ''

        form = AnswerForm(request.POST or None)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            print(text)
            form = form.save(commit=False)
            form.survey_id = pk
            form.save()

        return HttpResponse("OK")
