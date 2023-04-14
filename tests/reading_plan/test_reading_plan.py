from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def mock_mongo_DB():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title":  """Não deixe para depois: Python é a linguagem mais
                          quente do momento""",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana-2",
            "title": """Selenium, BeautifulSoup ou Parsel?
                          Entenda as diferenças""",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 3,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana-3",
            "title": "Pytest + Faker: a combinação poderosa dos testes!",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 10,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana-4",
            "title": "FastAPI e Flask: frameworks para APIs em Python",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 15,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana-5",
            "title": "A biblioteca Pandas e o sucesso da linguagem Python",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 12,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
    ]


@pytest.fixture
def mock_return_DB():
    return {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        """Não deixe para depois: Python é a linguagem mais
                          quente do momento""",
                        4,
                    ),
                    (
                        """Selenium, BeautifulSoup ou Parsel?
                          Entenda as diferenças""",
                        3,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Pytest + Faker: a combinação poderosa dos testes!",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("FastAPI e Flask: frameworks para APIs em Python", 15),
            ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
        ],
    }


def test_reading_plan_group_news(mock_mongo_DB, mock_return_DB):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    reading_plan_service = ReadingPlanService
    reading_plan_service._db_news_proxy = MagicMock(
        return_value=mock_mongo_DB)
    return_group = reading_plan_service.group_news_for_available_time(10)

    assert return_group == mock_return_DB
