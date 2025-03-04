# SmbFileOpens

Specifies the response to SMB active file opens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_file_paths** | [**List[SmbActiveFilePath]**](SmbActiveFilePath.md) | Specifies the active opens for an SMB file in a view. | [optional] 
**cookie** | **str** | Specifies the pagination cookie | [optional] 

## Example

```python
from cohesity_sdk.models.smb_file_opens import SmbFileOpens

# TODO update the JSON string below
json = "{}"
# create an instance of SmbFileOpens from a JSON string
smb_file_opens_instance = SmbFileOpens.from_json(json)
# print the JSON string representation of the object
print(SmbFileOpens.to_json())

# convert the object into a dict
smb_file_opens_dict = smb_file_opens_instance.to_dict()
# create an instance of SmbFileOpens from a dict
smb_file_opens_from_dict = SmbFileOpens.from_dict(smb_file_opens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


