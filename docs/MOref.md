# MOref

Specifies the MoRef for a VMware object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **str** | Unique identifier for the object type. | [optional] 
**type** | **str** | Specifies the type of VMware object | [optional] 

## Example

```python
from cohesity_sdk.models.m_oref import MOref

# TODO update the JSON string below
json = "{}"
# create an instance of MOref from a JSON string
m_oref_instance = MOref.from_json(json)
# print the JSON string representation of the object
print(MOref.to_json())

# convert the object into a dict
m_oref_dict = m_oref_instance.to_dict()
# create an instance of MOref from a dict
m_oref_from_dict = MOref.from_dict(m_oref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


