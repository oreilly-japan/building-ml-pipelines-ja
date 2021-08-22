FROM tensorflow/tfx:0.27.0

LABEL maintainer="hannes.hapke@gmail.com"

RUN CFLAGS=$(/usr/bin/python3.7-config --cflags) python3.7 -m pip install \
  "tensorflow-hub" "slackclient"

ENTRYPOINT ["python3.7", "/tfx-src/tfx/scripts/run_executor.py"]
