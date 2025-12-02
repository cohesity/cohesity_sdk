# S3RestoreConfig

Specifies the S3 config of the restore config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Specifies the access key of the S3 config. | [optional] 
**bucket** | **str** | Specifies the bucket of the S3 config. | [optional] 
**host** | **str** | Specifies the host of the S3 config. | [optional] 
**region** | **str** | Specifies the region of the s3 config. | [optional] 
**secret_key** | **str** | Specifies the secret key of the S3 config. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.s3_restore_config import S3RestoreConfig

# TODO update the JSON string below
json = "{}"
# create an instance of S3RestoreConfig from a JSON string
s3_restore_config_instance = S3RestoreConfig.from_json(json)
# print the JSON string representation of the object
print(S3RestoreConfig.to_json())

# convert the object into a dict
s3_restore_config_dict = s3_restore_config_instance.to_dict()
# create an instance of S3RestoreConfig from a dict
s3_restore_config_from_dict = S3RestoreConfig.from_dict(s3_restore_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


