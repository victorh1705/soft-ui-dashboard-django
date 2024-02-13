FROM python:3.11.5-slim as base

# RUN useradd -ms /bin/bash python

#USER python

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /home/python/app

COPY requirements.txt .

ENV PATH=/home/python/.local/bin:$PATH
# install python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM base as development

COPY --chown=python:python init.sh init.sh
RUN chmod +x init.sh
CMD ["./init.sh"]
#CMD ["tail", "-f", "/dev/null"]

FROM base as production

ENV PATH=$PATH:~/.local/bin/
#CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
COPY . .

#COPY --chown=python:python build.sh build.sh
RUN chmod +x build.sh

#CMD ["./build.sh"]
CMD ["tail","-f","/dev/null"]