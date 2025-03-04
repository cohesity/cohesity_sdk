# SfdcObjectParams

Specifies the Salesforce objects mutation parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_added** | **int** | Specifies the number of records added for the Object. | [optional] 
**records_modified** | **int** | Specifies the number of records updated for the Object. | [optional] 
**records_removed** | **int** | Specifies the number of records removed from the Object. | [optional] 

## Example

```python
from cohesity_sdk.models.sfdc_object_params import SfdcObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcObjectParams from a JSON string
sfdc_object_params_instance = SfdcObjectParams.from_json(json)
# print the JSON string representation of the object
print(SfdcObjectParams.to_json())

# convert the object into a dict
sfdc_object_params_dict = sfdc_object_params_instance.to_dict()
# create an instance of SfdcObjectParams from a dict
sfdc_object_params_from_dict = SfdcObjectParams.from_dict(sfdc_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


