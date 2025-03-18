# HostMappings

Specifies the list of host mappings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[HostEntry]**](HostEntry.md) | Specifies the list of host entries | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.host_mappings import HostMappings

# TODO update the JSON string below
json = "{}"
# create an instance of HostMappings from a JSON string
host_mappings_instance = HostMappings.from_json(json)
# print the JSON string representation of the object
print(HostMappings.to_json())

# convert the object into a dict
host_mappings_dict = host_mappings_instance.to_dict()
# create an instance of HostMappings from a dict
host_mappings_from_dict = HostMappings.from_dict(host_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


