import pytest
from django.utils import timezone  # Correção na importação
from blog.factories import PosFactory

@pytest.fixture
def post_published():
    return PosFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

@pytest.mark.django_db
def test_post_created_on():
    post = PosFactory(title='Test Post')

    # Verifica se a data de criação não é nula
    assert post.created_on is not None

    # Verifica se a data de criação está no passado (assumindo que é um post recente)
    assert post.created_on <= timezone.now()  # Correção na chamada para timezone.now()
