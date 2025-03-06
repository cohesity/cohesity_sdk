# DMaaSInfo

Specifies the DMaaS info about the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dmaas** | **bool** | Specifies whether the cluster is a DMaaS cluster. | 

## Example

```python
from cohesity_sdk.cluster.models.d_maa_s_info import DMaaSInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DMaaSInfo from a JSON string
d_maa_s_info_instance = DMaaSInfo.from_json(json)
# print the JSON string representation of the object
print(DMaaSInfo.to_json())

# convert the object into a dict
d_maa_s_info_dict = d_maa_s_info_instance.to_dict()
# create an instance of DMaaSInfo from a dict
d_maa_s_info_from_dict = DMaaSInfo.from_dict(d_maa_s_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


