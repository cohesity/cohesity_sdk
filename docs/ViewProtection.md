# ViewProtection

Specifies information about the Protection Groups that are protecting the View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inactive** | **bool** | Specifies if this View is an inactive View that was created on this Remote Cluster to store the Snapshots created by replication. This inactive View cannot be NFS or SMB mounted. | [optional] 
**magneto_entity_id** | **int** | Specifies the id of the Protection Source that is using this View. | [optional] 
**protection_groups** | [**List[ProtectionGroupInfo]**](ProtectionGroupInfo.md) | Array of Protection Group. Specifies the Protection Group that are protecting the View. | [optional] 

## Example

```python
from cohesity_sdk.models.view_protection import ViewProtection

# TODO update the JSON string below
json = "{}"
# create an instance of ViewProtection from a JSON string
view_protection_instance = ViewProtection.from_json(json)
# print the JSON string representation of the object
print(ViewProtection.to_json())

# convert the object into a dict
view_protection_dict = view_protection_instance.to_dict()
# create an instance of ViewProtection from a dict
view_protection_from_dict = ViewProtection.from_dict(view_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


