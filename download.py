from minio import Minio

HOST = 'localhost:9000'
ACCESS_KEY = 'admin'
SECRET_KEY = 'password'

BUCKET_NAME = 'test-bucket'

minioClient = Minio(
  HOST,
  access_key=ACCESS_KEY,
  secret_key=SECRET_KEY,
  secure=False
)

minioClient.fget_object(BUCKET_NAME, 'test.txt', 'test.txt', request_headers=None)