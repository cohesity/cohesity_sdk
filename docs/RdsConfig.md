# RdsConfig

Specifies the parameters to recover AWS RDS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_instance_id** | **str** | Specifies the DB instance identifier to use for the restored DB. | 
**db_option_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**db_parameter_group** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**db_port** | **int** | Specifies the port to use for the DB in the restored RDS instance. | 
**enable_auto_minor_version_upgrade** | **bool** | Specifies whether to enable auto minor version upgrade in the restored DB. | 
**enable_copy_tags_to_snapshots** | **bool** | Specifies whether to enable copying of tags to snapshots of the DB. | 
**enable_iam_db_authentication** | **bool** | Specifies whether to enable IAM authentication for the DB. | 
**enable_public_accessibility** | **bool** | Specifies whether this DB will be publicly accessible or not. | [optional] 
**is_multi_az_deployment** | **bool** | Specifies whether this is a multi-az deployment or not. | 
**point_in_time_usecs** | **int** | Specifies a point in time for recovery in microseconds. | [optional] 

## Example

```python
from cohesity_sdk.models.rds_config import RdsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RdsConfig from a JSON string
rds_config_instance = RdsConfig.from_json(json)
# print the JSON string representation of the object
print(RdsConfig.to_json())

# convert the object into a dict
rds_config_dict = rds_config_instance.to_dict()
# create an instance of RdsConfig from a dict
rds_config_from_dict = RdsConfig.from_dict(rds_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


