# Оқытушылар тізімі

## Сипаттамасы

Бұл жоба 12-нұсқа бойынша әзірленген қарапайым Python оқу қосымшасы.
Қосымша оқытушылар тізімін алуға, аты бойынша іздеуге және жаңа оқытушы
қосуға мүмкіндік береді.

## Қолданылатын технологиялар

- Python 3.12+
- pytest
- Git
- GitHub
- GitHub Actions

## Орнату

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Тестілеу

```bash
pytest -v
```

## CI/CD

GitHub Actions көмегімен әрбір `push` және `pull request` кезінде:

1. Репозиторий checkout жасалады;
2. Python 3.12 орнатылады;
3. Тәуелділіктер орнатылады;
4. pytest арқылы автоматты тестілеу орындалады.

Pipeline нәтижесі GitHub-та **Actions** бөлімінде көрсетіледі.

## Coursework

Variant 12 - Teachers list with automated testing.