FROM 31z4/tox:4.21-5.0.0

WORKDIR /tests

COPY requirements.txt requirements-dev.txt tox.ini setup.* README.md LICENSE MANIFEST.in ./
COPY tests tests
COPY netvisor_api_client netvisor_api_client

CMD [ "run-parallel" ]