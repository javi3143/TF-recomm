FROM gcr.io/tensorflow/tensorflow
RUN apt-get update && apt-get install -y \
   git \
   wget \
   emacs \
   nano
RUN pip install Numpy
RUN pip install Pandas
RUN git clone https://github.com/javi3143/tfrecomm.git #recom57
RUN ./tfrecomm/download_data.sh
EXPOSE 81
