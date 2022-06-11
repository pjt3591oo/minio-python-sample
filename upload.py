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

if minioClient.bucket_exists(BUCKET_NAME) == False:
  minioClient.make_bucket(BUCKET_NAME)

print(minioClient.get_bucket_policy(BUCKET_NAME))

# minioClient.fput_object(BUCKET_NAME, 'test.hoho', 'test.txt', {"x-amz-acl": "public-read"}) 