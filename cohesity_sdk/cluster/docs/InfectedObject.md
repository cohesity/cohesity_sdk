# InfectedObject

Specifies an infected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies the bucket name of the infected object. | 
**object_name** | **str** | Specifies the key name of the infected object. | 
**version_id** | **str** | Specifies the version id of the infected object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.infected_object import InfectedObject

# TODO update the JSON string below
json = "{}"
# create an instance of InfectedObject from a JSON string
infected_object_instance = InfectedObject.from_json(json)
# print the JSON string representation of the object
print(InfectedObject.to_json())

# convert the object into a dict
infected_object_dict = infected_object_instance.to_dict()
# create an instance of InfectedObject from a dict
infected_object_from_dict = InfectedObject.from_dict(infected_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


