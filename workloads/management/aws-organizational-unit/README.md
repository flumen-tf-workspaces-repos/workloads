<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.78.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_organizations_account.dev](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/organizations_account) | resource |
| [aws_organizations_account.prod](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/organizations_account) | resource |
| [aws_organizations_account.stage](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/organizations_account) | resource |
| [aws_organizations_organizational_unit.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/organizations_organizational_unit) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_close_on_deletion"></a> [close\_on\_deletion](#input\_close\_on\_deletion) | If true, a deletion event will close the account. Otherwise, it will only remove from the organization. This is not supported for GovCloud accounts | `bool` | `true` | no |
| <a name="input_master_email"></a> [master\_email](#input\_master\_email) | Master email address for account creation | `string` | n/a | yes |
| <a name="input_organization_parent_id"></a> [organization\_parent\_id](#input\_organization\_parent\_id) | Parent organizational unit ID | `string` | n/a | yes |
| <a name="input_organizational_unit_name"></a> [organizational\_unit\_name](#input\_organizational\_unit\_name) | Name of the organizational unit. Will be forced to be all lowercase | `string` | n/a | yes |
| <a name="input_role_name"></a> [role\_name](#input\_role\_name) | The name of an IAM role that Organizations automatically preconfigures in the new member account | `string` | n/a | yes |
| <a name="input_tags"></a> [tags](#input\_tags) | Resource tags | `map(string)` | `{}` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_account_ids"></a> [account\_ids](#output\_account\_ids) | Map of environment names to AWS account IDs |
| <a name="output_accounts"></a> [accounts](#output\_accounts) | Map of created AWS accounts with their details |
| <a name="output_organizational_unit"></a> [organizational\_unit](#output\_organizational\_unit) | The created AWS Organizations Organizational Unit |
<!-- END_TF_DOCS -->