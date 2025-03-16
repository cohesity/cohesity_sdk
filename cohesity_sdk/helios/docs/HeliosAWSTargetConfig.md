# HeliosAWSTargetConfig

Specifies the configuration for adding AWS as repilcation target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the AWS Replication target. | [optional] [readonly] 
**region** | **int** | Specifies id of the AWS region in which to replicate the Snapshot to. Applicable if replication target is AWS target. | 
**region_name** | **str** | Specifies name of the AWS region in which to replicate the Snapshot to. Applicable if replication target is AWS target. | [optional] [readonly] 
**source_id** | **int** | Specifies the source id of the AWS protection source registered on Cohesity cluster. | 

## Example

```python
from cohesity_sdk.helios.models.helios_aws_target_config import HeliosAWSTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAWSTargetConfig from a JSON string
helios_aws_target_config_instance = HeliosAWSTargetConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosAWSTargetConfig.to_json())

# convert the object into a dict
helios_aws_target_config_dict = helios_aws_target_config_instance.to_dict()
# create an instance of HeliosAWSTargetConfig from a dict
helios_aws_target_config_from_dict = HeliosAWSTargetConfig.from_dict(helios_aws_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


