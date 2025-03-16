# OverwriteViewParams

Specifies the parameters to overwrite a View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_view_id** | **int** | Specifies the source View id. Target View will be overwritten by the source View. | 

## Example

```python
from cohesity_sdk.helios.models.overwrite_view_params import OverwriteViewParams

# TODO update the JSON string below
json = "{}"
# create an instance of OverwriteViewParams from a JSON string
overwrite_view_params_instance = OverwriteViewParams.from_json(json)
# print the JSON string representation of the object
print(OverwriteViewParams.to_json())

# convert the object into a dict
overwrite_view_params_dict = overwrite_view_params_instance.to_dict()
# create an instance of OverwriteViewParams from a dict
overwrite_view_params_from_dict = OverwriteViewParams.from_dict(overwrite_view_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


