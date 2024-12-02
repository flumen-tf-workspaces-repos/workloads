locals {
  email_parts              = split("@", var.master_email)
  domain                   = local.email_parts[1]
  username                 = local.email_parts[0]
  organizational_unit_name = lower(var.organizational_unit_name)
}

resource "aws_organizations_organizational_unit" "this" {
  name      = local.organizational_unit_name
  parent_id = var.organization_parent_id
}

resource "aws_organizations_account" "dev" {
  name              = "${local.organizational_unit_name}-dev"
  email             = "${local.username}+${local.organizational_unit_name}-dev@${local.domain}"
  close_on_deletion = var.close_on_deletion
  parent_id         = aws_organizations_organizational_unit.this.id
  role_name         = var.role_name
  tags              = var.tags
}

resource "aws_organizations_account" "stage" {
  name              = "${local.organizational_unit_name}-stage"
  email             = "${local.username}+${local.organizational_unit_name}-stage@${local.domain}"
  close_on_deletion = var.close_on_deletion
  parent_id         = aws_organizations_organizational_unit.this.id
  tags              = var.tags
}

resource "aws_organizations_account" "prod" {
  name              = "${local.organizational_unit_name}-prod"
  email             = "${local.username}+${var.organizational_unit_name}-prod@${local.domain}"
  close_on_deletion = var.close_on_deletion
  parent_id         = aws_organizations_organizational_unit.this.id
  tags              = var.tags
}