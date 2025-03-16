# GroupObjectEntityParams

Specifies the common parameters for Office365 Group objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_mail_enabled** | **bool** | Specifies whether the Group is mail enabled. Mail enabled groups are used within Microsoft to distribute messages. | [optional] 
**is_security_enabled** | **bool** | Specifies whether the Group is security enabled. Security enabled groups are used to grant access permissions to resources in Exchange and Active Directory. | [optional] 
**member_count** | **int** | Specifies the count of members within the Group. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.group_object_entity_params import GroupObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of GroupObjectEntityParams from a JSON string
group_object_entity_params_instance = GroupObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(GroupObjectEntityParams.to_json())

# convert the object into a dict
group_object_entity_params_dict = group_object_entity_params_instance.to_dict()
# create an instance of GroupObjectEntityParams from a dict
group_object_entity_params_from_dict = GroupObjectEntityParams.from_dict(group_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


