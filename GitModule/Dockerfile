FROM python:3.7
RUN mkdir -p /metrics
WORKDIR /bin
COPY Code/ /app
WORKDIR /app
RUN git clone https://github.com/AlDanial/cloc
ENV PATH="/app/cloc:${PATH}"
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./SSLMetrics.py"]
