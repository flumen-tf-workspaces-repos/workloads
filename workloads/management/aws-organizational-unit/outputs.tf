output "organizational_unit" {
  description = "The created AWS Organizations Organizational Unit"
  value = {
    id   = aws_organizations_organizational_unit.this.id
    name = aws_organizations_organizational_unit.this.name
    arn  = aws_organizations_organizational_unit.this.arn
  }
}

output "accounts" {
  description = "Map of created AWS accounts with their details"
  value = {
    dev = {
      id    = aws_organizations_account.dev.id
      arn   = aws_organizations_account.dev.arn
      name  = aws_organizations_account.dev.name
      email = aws_organizations_account.dev.email
    }
    stage = {
      id    = aws_organizations_account.stage.id
      arn   = aws_organizations_account.stage.arn
      name  = aws_organizations_account.stage.name
      email = aws_organizations_account.stage.email
    }
    prod = {
      id    = aws_organizations_account.prod.id
      arn   = aws_organizations_account.prod.arn
      name  = aws_organizations_account.prod.name
      email = aws_organizations_account.prod.email
    }
  }
}

output "account_ids" {
  description = "Map of environment names to AWS account IDs"
  value = {
    dev   = aws_organizations_account.dev.id
    stage = aws_organizations_account.stage.id
    prod  = aws_organizations_account.prod.id
  }
}