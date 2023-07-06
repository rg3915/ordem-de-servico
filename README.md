# Ordem de Serviço

## Este projeto foi feito com:

* [Python 3.10.6](https://www.python.org/)
* [Django 4.1.5](https://www.djangoproject.com/)
* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
* [Bootstrap 4.0](https://getbootstrap.com/)
* [VueJS 3.2.13](https://vuejs.org/)
* [jQuery 3.4.1](https://jquery.com/)
* [htmx](https://htmx.org)

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

