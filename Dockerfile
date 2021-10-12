	FROM alpine:latest
    RUN mkdir Downloads
	WORKDIR /Downloads
    RUN apk add git python3 py3-pip
    RUN pip install Flask
    RUN pip install flask_restful
    RUN git clone https://github.com/MihirSahu/Date-API.git
    WORKDIR /Downloads/Date-API
