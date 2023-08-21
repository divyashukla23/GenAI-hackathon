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

variable "block_public_acls" {
  description = "Whether to block public ACLs for the S3 bucket."
  type        = bool
  default     = true
}

variable "block_public_policy" {
  description = "Whether to block public bucket policies for the S3 bucket."
  type        = bool
  default     = true
}

variable "ignore_public_acls" {
  description = "Whether to ignore public ACLs for the S3 bucket."
  type        = bool
  default     = true
}

variable "restrict_public_buckets" {
  description = "Whether to restrict public access to buckets for the S3 bucket."
  type        = bool
  default     = true
}
