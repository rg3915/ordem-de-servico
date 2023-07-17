# Ordem de Serviço

## Este projeto foi feito com:

* [Django 4.2.3](https://www.djangoproject.com/)
* [Django-ninja](https://django-ninja.rest-framework.com/)
* [AlpineJS](https://alpinejs.dev/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://gitlab.com/rg3915/ordem-de-servico.git
cd ordem-de-servico

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser
```

## Links

https://alpinejs.dev

https://django-ninja.rest-framework.com

## Videos

[A Essência do Django parte 1](https://youtu.be/mlaCLGItR7Q)

[A Essência do Django parte 2](https://youtu.be/Qu2QTxdYfZ4)

[FBV vs CBV](https://www.youtube.com/live/2qZcPb8ZWQA?feature=share)

[Class Based Views](https://www.youtube.com/live/C7Ecugxa7ic?feature=share) tem Login simples também.

[Django-ninja](https://youtu.be/4RdTltDCfl0)

[AlpineJS](https://www.youtube.com/watch?v=rqH70WZhKcc&list=PLsGCdfxkV9urAmKLmU5j_gshYXeEwzFpu)

