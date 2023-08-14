resource "aws_s3_bucket" "state_bucket" {
  bucket = local.bucket_name

  tags = {
    name        = local.bucket_name
    environment = local.environment
    owner       = local.owner
  }
}
