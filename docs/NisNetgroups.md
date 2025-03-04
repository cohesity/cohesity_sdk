# NisNetgroups

Response of NIS Netgroups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nis_netgroups** | [**List[NisNetgroup]**](NisNetgroup.md) | A list of NIS Netgroups. | [optional] 

## Example

```python
from cohesity_sdk.models.nis_netgroups import NisNetgroups

# TODO update the JSON string below
json = "{}"
# create an instance of NisNetgroups from a JSON string
nis_netgroups_instance = NisNetgroups.from_json(json)
# print the JSON string representation of the object
print(NisNetgroups.to_json())

# convert the object into a dict
nis_netgroups_dict = nis_netgroups_instance.to_dict()
# create an instance of NisNetgroups from a dict
nis_netgroups_from_dict = NisNetgroups.from_dict(nis_netgroups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


