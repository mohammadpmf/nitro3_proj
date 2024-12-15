from django.shortcuts import HttpResponse
import ghasedakpack


def get_sms(request):
    sms = ghasedakpack.Ghasedak(
        "f889f4f2754a67771b17e6bed88477d582b594f844ff6b4c7b62db2679d98f5d"
    )
    my_number = "09xxxxxxxxx"
    answer = sms.send(
        {
            "message": f"اس ام اس به شماره {my_number} ارسال شد",
            "receptor": my_number,
            "linenumber": "30005006009956",
        }
    )
    if answer == True:
        return HttpResponse(f"اس ام اس با موفقیت به شماره {my_number} ارسال شد")
    else:
        return HttpResponse("در ارسال اس ام اس مشکلی پیش آمد")
