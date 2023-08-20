variable "bucket_name" {
  description = "The name of the S3 bucket."
  type        = string
}

variable "region" {
  description = "The AWS region where resources will be created."
  type        = string
}

variable "environment" {
  description = "The environment where the infrastructure is deployed."
  type        = string
}

variable "owner" {
  description = "The owner of the infrastructure."
  type        = string
}
