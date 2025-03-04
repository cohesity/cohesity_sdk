# Attachment

Specifies the attachment information of a firewall profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action. | [optional] 
**description** | **str** | Specifies a description for the attachment. | [optional] 
**interface_groups** | **List[str]** | Specifies the network interface groups. | [optional] 
**interfaces** | **List[str]** | Specifies the network interfaces | [optional] 
**ipset_names** | **List[str]** | Specifies the ip sets. | [optional] 
**is_implicit** | **bool** |  | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


