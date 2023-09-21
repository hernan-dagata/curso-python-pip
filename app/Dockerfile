FROM python:3.11.4

WORKDIR /app
RUN command pip install --upgrade pip
COPY requirements.txt /app/requirements.txt

RUN pip install --disable-pip-version-check --no-cache-dir --trusted-host pypi.org --trusted-host=files.pythonhosted.org --upgrade -r /app/requirements.txt

COPY . app/

CMD bash -c "while true; do sleep 1; done"