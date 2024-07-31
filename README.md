# s3_aws

### Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ENV Vars
Create a .env file in your root directory with the following contents. Update the values to match your config.

```
AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME
AWS_DEFAULT_REGION=YOUR_REGION_NAME
AWS_ACCESS_KEY_ID=YOUR_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET
```

### AWS Setup
- name bucket
- enabled ACLs
- set object writer
- disable block public access
- enable transfer acceleration (optional and not used in example)


#### AWS Permissions

Bucket Policy
```
{"Version": "2012-10-17",
"Statement": [
    {
        "Sid": "myPolicy",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "*",
        "Resource": [
            "arn:aws:s3:::YOUR_BUCKET_NAME/*",
            "arn:aws:s3:::YOUR_BUCKET_NAME"
        ]
    }
]}

```


CORS Settings
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "ETag"
        ],
        "MaxAgeSeconds": 3000
    }
]
```


### Docker and run Server:
docker build -t s3-aws-project .
docker run -d -p 8000:8000 --memory=512m --name s3-upload-app s3-aws-project