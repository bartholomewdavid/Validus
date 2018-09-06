from django.http import HttpResponse
from django.template import loader

from validus.models import Currency
import validus.mathutils as mathutils

from datetime import datetime

def date_to_milliseconds(date):
    return datetime(date.year, date.month, date.day, 0, 0, 0, 0).timestamp() * 1000

def raw_data(request):
    template = loader.get_template('raw_data.html')

    EUR = Currency.objects.filter(underlying='GBPEUR')
    USD = Currency.objects.filter(underlying='GBPUSD')

    context = {
        'GBPEUR': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in EUR],
        'GBPUSD': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in USD]
    }

    return HttpResponse(template.render(context, request))

def question_1(request):
    template = loader.get_template('question_1.html')

    EUR = Currency.objects.filter(underlying='GBPEUR')
    USD = Currency.objects.filter(underlying='GBPUSD')

    EUR_Returns = []
    for i in range(len(EUR)):
        cur = EUR[i]
        prev = EUR[i - 1] if i > 0 else None

        EUR_Returns.append({
            'x': date_to_milliseconds(cur.valuation_date),
            'y': mathutils.daily_return(prev.mid, cur.mid) if prev is not None else 0
        })

    USD_Returns = []
    for i in range(len(USD)):
        cur = USD[i]
        prev = USD[i - 1] if i > 0 else None

        USD_Returns.append({
            'x': date_to_milliseconds(cur.valuation_date),
            'y': mathutils.daily_return(prev.mid, cur.mid) if prev is not None else 0
        })

    context = {
        'GBPEUR_Returns': EUR_Returns,
        'GBPUSD_Returns': USD_Returns,
    }

    return HttpResponse(template.render(context, request))

def question_2(request):
    template = loader.get_template('question_2.html')

    USD = Currency.objects.filter(underlying='GBPUSD')

    # This slice is a wild guess at how to determine how many records are in a "1 year" rolling average
    # I counted 260 rows for the year of 1990 and just assumed that would work for demo purposes
    USD_Rolling_1 = []
    USD_Rolling_2 = []
    USD_Rolling_3 = []

    for i in range(len(USD)):
        USD_Rolling_1.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.average([val.mid for val in USD[i-260:i]]) if i > 260 else ''
        })
        USD_Rolling_2.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.average([val.mid for val in USD[i-520:i]]) if i > 520 else ''
        })
        USD_Rolling_3.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.average([val.mid for val in USD[i-780:i]]) if i > 780 else ''
        })

    context = {
        'GBPUSD': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in USD],
        'USD_Rolling_1': USD_Rolling_1,
        'USD_Rolling_2': USD_Rolling_2,
        'USD_Rolling_3': USD_Rolling_3,
    }

    return HttpResponse(template.render(context, request))

def question_3(request):
    template = loader.get_template('question_3.html')

    USD = Currency.objects.filter(underlying='GBPUSD')

    # This slice is a wild guess at how to determine how many records are in a "1 year" rolling average
    # I counted 260 rows for the year of 1990 and just assumed that would work for demo purposes
    USD_Rolling_1 = []
    USD_Rolling_2 = []
    USD_Rolling_3 = []

    for i in range(len(USD)):
        USD_Rolling_1.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.std_deviation([val.mid for val in USD[i-260:i]]) if i > 260 else ''
        })
        USD_Rolling_2.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.std_deviation([val.mid for val in USD[i-520:i]]) if i > 520 else ''
        })
        USD_Rolling_3.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.std_deviation([val.mid for val in USD[i-780:i]]) if i > 780 else ''
        })

    context = {
        'GBPUSD': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in USD],
        'USD_Rolling_Std_1': USD_Rolling_1,
        'USD_Rolling_Std_2': USD_Rolling_2,
        'USD_Rolling_Std_3': USD_Rolling_3,
    }

    return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))

def question_4(request):
    template = loader.get_template('question_4.html')

    EUR = Currency.objects.filter(underlying='GBPEUR')
    USD = Currency.objects.filter(underlying='GBPUSD')

    # This slice is a wild guess at how to determine how many records are in a "1 year" rolling average
    # I counted 260 rows for the year of 1990 and just assumed that would work for demo purposes
    Cov_Rolling_1 = []
    Cov_Rolling_2 = []
    Cov_Rolling_3 = []

    for i in range(len(USD)):
        x_inputs_1_year = [val.mid for val in USD[i-260:i]] if i > 260 else None
        y_inputs_1_year = [val.mid for val in EUR[i-260:i]] if i > 260 else None

        x_inputs_2_year = [val.mid for val in USD[i-520:i]] if i > 520 else None
        y_inputs_2_year = [val.mid for val in EUR[i-520:i]] if i > 520 else None

        x_inputs_3_year = [val.mid for val in USD[i-780:i]] if i > 780 else None
        y_inputs_3_year = [val.mid for val in EUR[i-780:i]] if i > 780 else None

        Cov_Rolling_1.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.covariance(x_inputs_1_year, y_inputs_1_year) if x_inputs_1_year and y_inputs_1_year else 0
        })
        Cov_Rolling_2.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.covariance(x_inputs_2_year, y_inputs_2_year) if x_inputs_2_year and y_inputs_2_year else 0
        })
        Cov_Rolling_3.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.covariance(x_inputs_3_year, y_inputs_3_year) if x_inputs_3_year and y_inputs_3_year else 0
        })

    context = {
        'GBPUSD': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in USD],
        'GBPEUR': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in EUR],
        'Cov_Rolling_1': Cov_Rolling_1,
        'Cov_Rolling_2': Cov_Rolling_2,
        'Cov_Rolling_3': Cov_Rolling_3,
    }

    return HttpResponse(template.render(context, request))

def question_5(request):
    template = loader.get_template('question_5.html')

    EUR = Currency.objects.filter(underlying='GBPEUR')
    USD = Currency.objects.filter(underlying='GBPUSD')

    # This slice is a wild guess at how to determine how many records are in a "1 year" rolling average
    # I counted 260 rows for the year of 1990 and just assumed that would work for demo purposes
    Cor_Rolling_1 = []
    Cor_Rolling_2 = []
    Cor_Rolling_3 = []

    for i in range(len(USD)):
        x_inputs_1_year = [val.mid for val in USD[i-260:i]] if i > 260 else None
        y_inputs_1_year = [val.mid for val in EUR[i-260:i]] if i > 260 else None

        x_inputs_2_year = [val.mid for val in USD[i-520:i]] if i > 520 else None
        y_inputs_2_year = [val.mid for val in EUR[i-520:i]] if i > 520 else None

        x_inputs_3_year = [val.mid for val in USD[i-780:i]] if i > 780 else None
        y_inputs_3_year = [val.mid for val in EUR[i-780:i]] if i > 780 else None

        Cor_Rolling_1.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.correlation(x_inputs_1_year, y_inputs_1_year) if x_inputs_1_year and y_inputs_1_year else 0
        })
        Cor_Rolling_2.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.correlation(x_inputs_2_year, y_inputs_2_year) if x_inputs_2_year and y_inputs_2_year else 0
        })
        Cor_Rolling_3.append({
            'x': date_to_milliseconds(USD[i].valuation_date),
            'y': mathutils.correlation(x_inputs_3_year, y_inputs_3_year) if x_inputs_3_year and y_inputs_3_year else 0
        })

    context = {
        'GBPUSD': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in USD],
        'GBPEUR': [{'x': date_to_milliseconds(val.valuation_date), 'y': val.mid} for val in EUR],
        'Cor_Rolling_1': Cor_Rolling_1,
        'Cor_Rolling_2': Cor_Rolling_2,
        'Cor_Rolling_3': Cor_Rolling_3,
    }

    return HttpResponse(template.render(context, request))