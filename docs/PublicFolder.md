# PublicFolder

Specifies an PublicFolder item to recover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | Specifies the Unique ID of the folder. | 
**item_ids** | **List[str]** | Specifies a list of item ids to recover. This field is applicable only if &#39;recoverEntireFolder&#39; is false. | [optional] 
**recover_entire_folder** | **bool** | Specifies whether to recover the whole PublicFolder. | [optional] 

## Example

```python
from cohesity_sdk.models.public_folder import PublicFolder

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFolder from a JSON string
public_folder_instance = PublicFolder.from_json(json)
# print the JSON string representation of the object
print(PublicFolder.to_json())

# convert the object into a dict
public_folder_dict = public_folder_instance.to_dict()
# create an instance of PublicFolder from a dict
public_folder_from_dict = PublicFolder.from_dict(public_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


