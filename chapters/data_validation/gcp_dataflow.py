import tensorflow_data_validation as tfdv
from apache_beam.options.pipeline_options import (
    GoogleCloudOptions,
    PipelineOptions,
    SetupOptions,
    StandardOptions,
)

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
bucket_name = "YOUR BUCKET NAME"
google_cloud_options.project = "YOUR PROJECT NAME"
google_cloud_options.job_name = "dataflow-example"
google_cloud_options.staging_location = f"gs://{bucket_name}/staging"
google_cloud_options.temp_location = f"gs://{bucket_name}/tmp"
options.view_as(StandardOptions).runner = "DataflowRunner"

setup_options = options.view_as(SetupOptions)
setup_options.extra_packages = [
    # 'tensorflow_data_validation-0.27.0-cp37-cp37m-manylinux2010_x86_64.whl'
    "tensorflow_data_validation-0.27.0-cp38-cp38-manylinux2010_x86_64.whl"
]

data_set_path = f"gs://{bucket_name}/consumer-complaints.tfrecord"
output_path = f"gs://{bucket_name}/output"
tfdv.generate_statistics_from_tfrecord(
    data_set_path, output_path=output_path, pipeline_options=options
)
