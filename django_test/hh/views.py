from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader,RequestContext
# Create your views here.
# from stock.models import PhoneInfo


def index(request):
    # template = loader.get_template('stock/index.html')
    # heros = PhoneInfo.objects.all().order_by('-favcount')[:30]
    # print(heros)
    # for i in heros:
    #     print(i.title+'\t'+str(i.favcount))
    # jsondata = {
    #     "key": [i.title for i in heros],
    #     "value": [i.favcount for i in heros]
    # }
    jsondata = {
    "by_field": "",
    "has_first_day": True,
    "rows": [
        {
            "by_value": "2017-06-07",
            "total_people": 4510,
            "cells": [
                {
                    "people": 4294,
                    "percent": 95.21
                },
                {
                    "people": 453,
                    "percent": 10.04
                },
                {
                    "people": 435,
                    "percent": 9.65
                },
                {
                    "people": 420,
                    "percent": 9.31
                },
                {
                    "people": 399,
                    "percent": 8.85
                },
                {
                    "people": 422,
                    "percent": 9.36
                },
                {
                    "people": 376,
                    "percent": 8.34
                },
                {
                    "people": 360,
                    "percent": 7.98
                }
            ]
        },
        {
            "by_value": "2017-06-08",
            "total_people": 4781,
            "cells": [
                {
                    "people": 4564,
                    "percent": 95.46
                },
                {
                    "people": 537,
                    "percent": 11.23
                },
                {
                    "people": 420,
                    "percent": 8.78
                },
                {
                    "people": 443,
                    "percent": 9.27
                },
                {
                    "people": 447,
                    "percent": 9.35
                },
                {
                    "people": 421,
                    "percent": 8.81
                },
                {
                    "people": 385,
                    "percent": 8.05
                }
            ]
        },
        {
            "by_value": "2017-06-09",
            "total_people": 4809,
            "cells": [
                {
                    "people": 4601,
                    "percent": 95.67
                },
                {
                    "people": 487,
                    "percent": 10.13
                },
                {
                    "people": 445,
                    "percent": 9.25
                },
                {
                    "people": 450,
                    "percent": 9.36
                },
                {
                    "people": 420,
                    "percent": 8.73
                },
                {
                    "people": 384,
                    "percent": 7.99
                }
            ]
        },
        {
            "by_value": "2017-06-10",
            "total_people": 4587,
            "cells": [
                {
                    "people": 4373,
                    "percent": 95.33
                },
                {
                    "people": 519,
                    "percent": 11.31
                },
                {
                    "people": 431,
                    "percent": 9.4
                },
                {
                    "people": 350,
                    "percent": 7.63
                },
                {
                    "people": 345,
                    "percent": 7.52
                }
            ]
        },
        {
            "by_value": "2017-06-11",
            "total_people": 4627,
            "cells": [
                {
                    "people": 4419,
                    "percent": 95.5
                },
                {
                    "people": 523,
                    "percent": 11.3
                },
                {
                    "people": 438,
                    "percent": 9.47
                },
                {
                    "people": 375,
                    "percent": 8.1
                }
            ]
        },
        {
            "by_value": "2017-06-12",
            "total_people": 4760,
            "cells": [
                {
                    "people": 4539,
                    "percent": 95.36
                },
                {
                    "people": 558,
                    "percent": 11.72
                },
                {
                    "people": 359,
                    "percent": 7.54
                }
            ]
        },
        {
            "by_value": "2017-06-13",
            "total_people": 4711,
            "cells": [
                {
                    "people": 4477,
                    "percent": 95.03
                },
                {
                    "people": 472,
                    "percent": 10.02
                }
            ]
        }
    ],
    "report_update_time": "2017-06-14 21:27:04.161",
    "data_update_time": "2017-06-14 21:26:19.000",
    "data_sufficient_update_time": "2017-06-14 21:26:19.000",
    "truncated": False
}
    return JsonResponse(jsondata)
    # print(heros)
    # context = RequestContext(request,{'title':'英雄','heros':heros})
    # return HttpResponse(template.render(context))