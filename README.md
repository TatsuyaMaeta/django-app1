![https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/](aaa)

https://qiita.com/nokonoko_1203/items/242367a83c313a5e46bf

```
mkdir django-on-docker && cd django-on-docker

// アプリケーション用ディレクトリを作成、そのappに移動
mkdir app && cd app

// venvという仮想環境を構築
python3.11 -m venv venv

// venvの環境を立ち上げ
source venv/bin/activate
```


### venvにダウンロード

pip install django==3.0.7
pip install djangorestframework==3.11

user: super
pass: qwerty123

<https://qiita.com/Ryo-0131/items/522c4e9c0cb4c539eb37>

<https://github.com/GomaGoma676/react-drf-integration-basic>
<https://github.com/GomaGoma676/drf-rest-api>

Databaseのdefaultの設定を文字列化してエラーを防ぐ
<https://qiita.com/t_a_k_a_/items/d213e34a53d38076a48e>
