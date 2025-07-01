FROM 31z4/tox:4.21-5.0.0

WORKDIR /tests

USER tox

COPY --chown=tox:tox requirements.txt requirements-dev.txt tox.ini setup.* README.md LICENSE MANIFEST.in ./
COPY --chown=tox:tox tests tests
COPY --chown=tox:tox netvisor_api_client netvisor_api_client

CMD [ "run-parallel" ]