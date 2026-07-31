terraform {
  required_version = ">= 1.7.0"
}

variable "provider_name" {
  type        = string
  description = "aws, azure or gcp; this local module creates no paid resources"
  validation {
    condition     = contains(["aws", "azure", "gcp"], var.provider_name)
    error_message = "provider_name must be aws, azure or gcp"
  }
}

locals {
  tags = { program = "multi-cloud-engineering", owner = "student", expires = "24h" }
}

output "deployment_contract" {
  value = { provider = var.provider_name, tags = local.tags, creates_resources = false }
}
