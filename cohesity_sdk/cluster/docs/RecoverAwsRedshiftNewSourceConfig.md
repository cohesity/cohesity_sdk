# RecoverAwsRedshiftNewSourceConfig

Specifies the new destination Source configuration where the Redshift database will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_redshift_new_source_config import RecoverAwsRedshiftNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRedshiftNewSourceConfig from a JSON string
recover_aws_redshift_new_source_config_instance = RecoverAwsRedshiftNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRedshiftNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_redshift_new_source_config_dict = recover_aws_redshift_new_source_config_instance.to_dict()
# create an instance of RecoverAwsRedshiftNewSourceConfig from a dict
recover_aws_redshift_new_source_config_from_dict = RecoverAwsRedshiftNewSourceConfig.from_dict(recover_aws_redshift_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


