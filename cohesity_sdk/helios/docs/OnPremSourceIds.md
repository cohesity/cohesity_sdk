# OnPremSourceIds

List of source ids for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.on_prem_source_ids import OnPremSourceIds

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremSourceIds from a JSON string
on_prem_source_ids_instance = OnPremSourceIds.from_json(json)
# print the JSON string representation of the object
print(OnPremSourceIds.to_json())

# convert the object into a dict
on_prem_source_ids_dict = on_prem_source_ids_instance.to_dict()
# create an instance of OnPremSourceIds from a dict
on_prem_source_ids_from_dict = OnPremSourceIds.from_dict(on_prem_source_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


