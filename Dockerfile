FROM python:3.9-slim
COPY . /file
WORKDIR /file
RUN pip install nltk
RUN python -c "import nltk; nltk.download('stopwords')"
EXPOSE 80
ENV NAME dockerfile
CMD ["python", "cloud.py"]

