# RecoverGmailParams

Specifies the parameters to recover Gmail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other Gmail if one of Gmail failed to recover. Default value is false. | [optional] 
**download_as_zip** | **bool** | Specifies whether download the object as a ZIP file. If false and &#39;targetGmail&#39; is not specified, the objects will be recovered to original location. Default value is false. | [optional] 
**objects** | [**List[GmailParams]**](GmailParams.md) | Specifies a list of Gmail params associated with the objects to recover. | 
**target_gmail** | [**TargetGmailParams**](TargetGmailParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_gmail_params import RecoverGmailParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGmailParams from a JSON string
recover_gmail_params_instance = RecoverGmailParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGmailParams.to_json())

# convert the object into a dict
recover_gmail_params_dict = recover_gmail_params_instance.to_dict()
# create an instance of RecoverGmailParams from a dict
recover_gmail_params_from_dict = RecoverGmailParams.from_dict(recover_gmail_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


