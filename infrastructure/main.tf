resource "aws_s3_bucket" "state_bucket" {
  bucket = var.bucket_name
  tags = {
    name        = var.bucket_name
    environment = var.environment
    owner       = var.owner
  }
}

resource "aws_s3_bucket_public_access_block" "s3_bucket_access_block" {
  bucket                  = aws_s3_bucket.state_bucket.bucket
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}