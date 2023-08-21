resource "aws_s3_bucket" "state_bucket" {
  bucket = var.bucket_name

  tags = {
    name        = var.bucket_name
    environment = var.environment
    owner       = var.owner
  }
}

resource "aws_s3_bucket_public_access_block" "state_bucket_public_access" {
  bucket = aws_s3_bucket.state_bucket.id

  block_public_acls       = var.block_public_acls
  block_public_policy     = var.block_public_policy
  ignore_public_acls      = var.ignore_public_acls
  restrict_public_buckets = var.restrict_public_buckets
}
