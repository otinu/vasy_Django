from django.urls import path
# 同ディレクトリからview.pyをインポート
from . import views

urlpatterns = [
    # path(アクセスするアドレス, 呼び出す処理, name=パス名)
    # 第一引数を''にすると、アプリが読み込まれたとき、最初に実行する
    path('', views.index, name='index'),
]