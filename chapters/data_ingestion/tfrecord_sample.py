import tensorflow as tf

filename = "test.tfrecord"
with tf.io.TFRecordWriter(filename) as w:
    w.write(b"First record")
    w.write(b"Second record")

for record in tf.data.TFRecordDataset(filename):
    print(record)
