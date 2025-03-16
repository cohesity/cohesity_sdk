# McmSources

Specifies the list of Protection Sources on Helios MCM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[McmSource]**](McmSource.md) | Specifies the list of Protection Sources. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_sources import McmSources

# TODO update the JSON string below
json = "{}"
# create an instance of McmSources from a JSON string
mcm_sources_instance = McmSources.from_json(json)
# print the JSON string representation of the object
print(McmSources.to_json())

# convert the object into a dict
mcm_sources_dict = mcm_sources_instance.to_dict()
# create an instance of McmSources from a dict
mcm_sources_from_dict = McmSources.from_dict(mcm_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


