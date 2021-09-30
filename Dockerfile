# STEP #1 -> BUILD
FROM python:3.9-slim-bullseye AS build

RUN apt-get update \
    && apt-get install gcc -y

# Create and use virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Build and install our package, install dependencies
WORKDIR /app
ADD . /app

# Install the app
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --upgrade wheel \
    && python3 setup.py bdist_wheel \
    && python3 -m pip install .

# Remove the files that fail in Aquasec
# RUN rm -fR /opt/venv/lib/python3.7/site-packages/future/backports/test/*

# STEP #2 -> RUNTIME
FROM python:3.9-slim-bullseye
RUN apt-get update \
    && apt-get install -y libgl1-mesa-dev

# Create application user
RUN groupadd --gid 1001 application-group \
    && useradd --uid 1001 --gid 1001 --create-home --shell /sbin/nologin application-user

# Copy virtualenv from build image
ENV VIRTUAL_ENV=/opt/venv
COPY --from=build $VIRTUAL_ENV $VIRTUAL_ENV

WORKDIR /app

# Add code with unprivileged application-user ownership
ADD --chown=1001:1001 stortings-generator /app/stortings-generator
RUN chown application-user /app

# Use unprivileged application user and use virtualenv
USER application-user
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8080
CMD ["python3", "-m", "stortings-generator"]