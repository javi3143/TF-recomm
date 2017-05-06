FROM gcr.io/tensorflow/tensorflow
RUN apt-get update && apt-get install -y \
   git \
   wget \
   emacs
RUN pip install Numpy
RUN pip install Pandas
RUN git clone -b  ml-latest-small https://github.com/acobley/TF-recomm.git #recom-latest-small
RUN ./TF-recomm/download_data.sh
EXPOSE 81
