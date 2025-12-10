# TargetGmailParams

Specifies the target Gmail to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the GoogleWorkspace source. | [optional] 
**label_prefix** | **str** | Specifies the prefix to be added to restored labels. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**object_id** | **int** | Specifies the id of the target Gmail user. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.target_gmail_params import TargetGmailParams

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGmailParams from a JSON string
target_gmail_params_instance = TargetGmailParams.from_json(json)
# print the JSON string representation of the object
print(TargetGmailParams.to_json())

# convert the object into a dict
target_gmail_params_dict = target_gmail_params_instance.to_dict()
# create an instance of TargetGmailParams from a dict
target_gmail_params_from_dict = TargetGmailParams.from_dict(target_gmail_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


