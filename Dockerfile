FROM --platform=linux/amd64 python:3.8-rc-slim-buster as baseimage

RUN apt update

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv \
 && PIPENV_VENV_IN_PROJECT=1 PIPENV_SITE_PACKAGES=1 pipenv install --dev --system --deploy


FROM baseimage
COPY --from=baseimage /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home user_a && mkdir app
USER user_a
WORKDIR /home/user_a/app

RUN mkdir -p /home/user_a/output

COPY --chown=user_a:user_a Pipfile* ./
COPY --chown=user_a:user_a test_cases.py ./
# COPY --chown=user_a:user_a allure-results ./
# COPY --chown=user_a:user_a docs ./