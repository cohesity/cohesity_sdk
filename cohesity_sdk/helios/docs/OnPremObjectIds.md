# OnPremObjectIds

List of source ids for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[int]** | Specifies a list of object ids. Only files found in these objects will be returned. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.on_prem_object_ids import OnPremObjectIds

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremObjectIds from a JSON string
on_prem_object_ids_instance = OnPremObjectIds.from_json(json)
# print the JSON string representation of the object
print(OnPremObjectIds.to_json())

# convert the object into a dict
on_prem_object_ids_dict = on_prem_object_ids_instance.to_dict()
# create an instance of OnPremObjectIds from a dict
on_prem_object_ids_from_dict = OnPremObjectIds.from_dict(on_prem_object_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


