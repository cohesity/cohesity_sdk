# AuroraConfig

Specifies the parameters to recover AWS Aurora.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_instance_id** | **str** | Specifies the DB instance identifier to use for the restored DB. | 
**db_option_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**db_parameter_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**db_port** | **int** | Specifies the port to use for the DB in the restored Aurora instance. | 
**enable_auto_minor_version_upgrade** | **bool** | Specifies whether to enable auto minor version upgrade in the restored DB. | 
**enable_copy_tags_to_snapshots** | **bool** | Specifies whether to enable copying of tags to snapshots of the DB. | 
**enable_iam_db_authentication** | **bool** | Specifies whether to enable IAM authentication for the DB. | 
**enable_public_accessibility** | **bool** | Specifies whether this DB will be publicly accessible or not. | [optional] 
**is_multi_az_deployment** | **bool** | Specifies whether this is a multi-az deployment or not. | 
**point_in_time_usecs** | **int** | Specifies a point in time for recovery in microseconds. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aurora_config import AuroraConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuroraConfig from a JSON string
aurora_config_instance = AuroraConfig.from_json(json)
# print the JSON string representation of the object
print(AuroraConfig.to_json())

# convert the object into a dict
aurora_config_dict = aurora_config_instance.to_dict()
# create an instance of AuroraConfig from a dict
aurora_config_from_dict = AuroraConfig.from_dict(aurora_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


