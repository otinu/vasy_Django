from django.shortcuts import render

 
def index(request):
    # Pythonのデータはディクショナリにして、テンプレートファイルに渡すことができる
    array = {"Morning": "Good,Morning", "Bye": "Good,Bye", "Night": "Good,Night"}

    # renderで指定するテンプレートファイルはtemplatesという名称のディレクトリ配下に設置する必要がある
    return render(request,'test.html', array)