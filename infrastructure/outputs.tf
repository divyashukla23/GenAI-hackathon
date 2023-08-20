output "bucket_arn" {
  description = "The ARN of the created S3 bucket."
  value       = aws_s3_bucket.state_bucket.arn
}

output "bucket_id" {
  description = "The ID of the created S3 bucket."
  value       = aws_s3_bucket.state_bucket.id
}

output "bucket_region" {
  description = "The region where the S3 bucket resides."
  value       = var.region
}

output "environment" {
  description = "The environment where the infrastructure is deployed."
  value       = var.environment
}

output "owner" {
  description = "The owner of the infrastructure."
  value       = var.owner
}
