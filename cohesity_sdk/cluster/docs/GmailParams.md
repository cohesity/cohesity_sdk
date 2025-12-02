# GmailParams

Specifies parameters to recover Gmail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_entire_mailbox** | **bool** | Specifies whether to recover the whole Gmail. | [optional] 
**recover_labels** | [**List[GmailRestoreLabel]**](GmailRestoreLabel.md) | Specifies a list of Gmail labels to recover. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gmail_params import GmailParams

# TODO update the JSON string below
json = "{}"
# create an instance of GmailParams from a JSON string
gmail_params_instance = GmailParams.from_json(json)
# print the JSON string representation of the object
print(GmailParams.to_json())

# convert the object into a dict
gmail_params_dict = gmail_params_instance.to_dict()
# create an instance of GmailParams from a dict
gmail_params_from_dict = GmailParams.from_dict(gmail_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


