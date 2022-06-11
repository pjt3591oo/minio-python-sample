import boto3

HOST = 'http://localhost:9000'
ACCESS_KEY = 'admin'
SECRET_KEY = 'password'

BUCKET_NAME = 'test-bucket'


s3r = boto3.resource(
  's3', 
  endpoint_url=HOST,
  aws_access_key_id=ACCESS_KEY,
  aws_secret_access_key=SECRET_KEY
)

# 버킷목록 조회
for i in s3r.buckets.all():
  print(i)

# 버킷 생성
try:
  s3r.create_bucket(Bucket=BUCKET_NAME, ACL='public-read')
except: 
  pass

# 업로드
bucket = s3r.Bucket(BUCKET_NAME)
bucket.upload_file(Filename="./test.txt", Key="test.txt", ExtraArgs={'ACL': 'public-read'})

bucket = s3r.Bucket(BUCKET_NAME)
bucket.download_file(Key="test.txt", Filename="./test.hoho")