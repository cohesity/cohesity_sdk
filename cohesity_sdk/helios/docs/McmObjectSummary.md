# McmObjectSummary

Specifies the object summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment. | [optional] 
**view_summary** | [**ViewObjectSummary**](ViewObjectSummary.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_summary import McmObjectSummary

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectSummary from a JSON string
mcm_object_summary_instance = McmObjectSummary.from_json(json)
# print the JSON string representation of the object
print(McmObjectSummary.to_json())

# convert the object into a dict
mcm_object_summary_dict = mcm_object_summary_instance.to_dict()
# create an instance of McmObjectSummary from a dict
mcm_object_summary_from_dict = McmObjectSummary.from_dict(mcm_object_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


