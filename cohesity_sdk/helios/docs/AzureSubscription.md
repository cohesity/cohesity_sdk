# AzureSubscription

Specifies the details of an Azure subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Specifies the id of Azure subscription. | 

## Example

```python
from cohesity_sdk.helios.models.azure_subscription import AzureSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSubscription from a JSON string
azure_subscription_instance = AzureSubscription.from_json(json)
# print the JSON string representation of the object
print(AzureSubscription.to_json())

# convert the object into a dict
azure_subscription_dict = azure_subscription_instance.to_dict()
# create an instance of AzureSubscription from a dict
azure_subscription_from_dict = AzureSubscription.from_dict(azure_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


