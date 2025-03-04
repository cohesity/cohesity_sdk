# ConstructMetaInfoSfdcParams

Params to fetch meta info for a salesforce object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_info_type** | **str** | Specifies the type of meta info to fetch for salesforce object. | 
**object_name** | **str** | Specifies the name of the object. | [optional] 

## Example

```python
from cohesity_sdk.models.construct_meta_info_sfdc_params import ConstructMetaInfoSfdcParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructMetaInfoSfdcParams from a JSON string
construct_meta_info_sfdc_params_instance = ConstructMetaInfoSfdcParams.from_json(json)
# print the JSON string representation of the object
print(ConstructMetaInfoSfdcParams.to_json())

# convert the object into a dict
construct_meta_info_sfdc_params_dict = construct_meta_info_sfdc_params_instance.to_dict()
# create an instance of ConstructMetaInfoSfdcParams from a dict
construct_meta_info_sfdc_params_from_dict = ConstructMetaInfoSfdcParams.from_dict(construct_meta_info_sfdc_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


