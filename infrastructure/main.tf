resource "aws_s3_bucket" "state_bucket" {
  bucket = var.bucket_name

  tags = {
    name        = var.bucket_name
    environment = var.environment
    owner       = var.owner
  }
}
