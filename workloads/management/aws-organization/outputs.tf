output "parent_root_id" {
  value       = aws_organizations_organization.this.roots[0].id
  description = "Parent identifier of the root"
}

output "parent_root_arn" {
  value       = aws_organizations_organization.this.roots[0].arn
  description = "Parent ARN of the root"
}