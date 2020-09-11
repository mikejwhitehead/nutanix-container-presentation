FROM python

COPY . /presentation

WORKDIR /presentation

RUN pip install -r requirements.txt

CMD [ "present", "containers.md" ]