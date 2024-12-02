variable "close_on_deletion" {
  type        = bool
  description = "If true, a deletion event will close the account. Otherwise, it will only remove from the organization. This is not supported for GovCloud accounts"
  default     = true
}
variable "master_email" {
  type        = string
  description = "Master email address for account creation"
}

variable "organizational_unit_name" {
  type        = string
  description = "Name of the organizational unit. Will be forced to be all lowercase"
}

variable "organization_parent_id" {
  type        = string
  description = "Parent organizational unit ID"
}
variable "role_name" {
  type        = string
  description = "The name of an IAM role that Organizations automatically preconfigures in the new member account"
}
variable "tags" {
  type        = map(string)
  description = "Resource tags"
  default     = {}
}