# ViewObjectParams

Specifies the details of a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the view. | [optional] 
**uid** | **str** | Specifies a distinct value that&#39;s unique to a source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_object_params import ViewObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ViewObjectParams from a JSON string
view_object_params_instance = ViewObjectParams.from_json(json)
# print the JSON string representation of the object
print(ViewObjectParams.to_json())

# convert the object into a dict
view_object_params_dict = view_object_params_instance.to_dict()
# create an instance of ViewObjectParams from a dict
view_object_params_from_dict = ViewObjectParams.from_dict(view_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


