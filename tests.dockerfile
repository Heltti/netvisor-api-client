FROM 31z4/tox:4.21-5.0.0

USER root

RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    python3.7; \
    rm -rf /var/lib/apt/lists/*

USER tox

WORKDIR /tests

COPY --chown=tox:tox requirements.txt requirements-dev.txt tox.ini setup.* README.md LICENSE MANIFEST.in ./
COPY --chown=tox:tox tests tests
COPY --chown=tox:tox netvisor_api_client netvisor_api_client

CMD [ "-v", "run-parallel" ]