# CloudArchivalDirectConfig

Specifies the properties of vaults used to perform Cloud Archive Direct (CAD)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_namespace** | **str** | Specifies a namespace under the bucket used for archival. | [optional] 
**physical_quota** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cloud_archival_direct_config import CloudArchivalDirectConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CloudArchivalDirectConfig from a JSON string
cloud_archival_direct_config_instance = CloudArchivalDirectConfig.from_json(json)
# print the JSON string representation of the object
print(CloudArchivalDirectConfig.to_json())

# convert the object into a dict
cloud_archival_direct_config_dict = cloud_archival_direct_config_instance.to_dict()
# create an instance of CloudArchivalDirectConfig from a dict
cloud_archival_direct_config_from_dict = CloudArchivalDirectConfig.from_dict(cloud_archival_direct_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


