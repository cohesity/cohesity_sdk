# RecoverGCPBigQueryNewSourceConfig

Specifies the configuration for recovering GCP BigQuery dataset to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**target_region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_big_query_new_source_config import RecoverGCPBigQueryNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPBigQueryNewSourceConfig from a JSON string
recover_gcp_big_query_new_source_config_instance = RecoverGCPBigQueryNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPBigQueryNewSourceConfig.to_json())

# convert the object into a dict
recover_gcp_big_query_new_source_config_dict = recover_gcp_big_query_new_source_config_instance.to_dict()
# create an instance of RecoverGCPBigQueryNewSourceConfig from a dict
recover_gcp_big_query_new_source_config_from_dict = RecoverGCPBigQueryNewSourceConfig.from_dict(recover_gcp_big_query_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


