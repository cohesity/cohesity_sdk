# SmbActiveOpen

Specifies an active open of an SMB file, its access and sharing information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_info_list** | **List[str]** | Specifies the File Access Type. Following documentation was taken from MSDN. https://msdn.microsoft.com/en-us/library/Cc246802.aspx  &#39;FileReadData&#39; indicates the right to read data from the file or named   pipe. &#39;FileWriteData&#39; indicates the right to write data into the file or named   pipe beyond the end of the file. &#39;FileAppendData&#39; indicates the right to append data into the file or named   pipe. &#39;FileReadEa&#39; indicates the right to read the extended attributes of the   file or named pipe. &#39;FileWriteEa&#39; indicates the right to write or change the extended   attributes to the file or named pipe. &#39;FileExecute&#39; indicates the right to delete entries within a directory. &#39;FileDeleteChild&#39; indicates the right to execute the file. &#39;FileReadAttributes&#39; indicates the right to read the attributes of the   file. &#39;FileWriteAttributes&#39; indicates the right to change the attributes of the   file. &#39;Delete&#39; indicates the right to delete the file. &#39;ReadControl&#39; indicates the right to read the security descriptor for the   file or named pipe. &#39;WriteDac&#39; indicates the right to change the discretionary access control   list (DACL) in the security descriptor for the file or named pipe. For   the DACL data structure, see ACL in [MS-DTYP]. &#39;WriteOwner&#39; indicates the right to change the owner in the security   descriptor for the file or named pipe. &#39;Synchronize&#39; is used only by SMB2 clients. &#39;AccessSystemSecurity&#39; indicates the right to read or change the system   access control list (SACL) in the security descriptor for the file or   named pipe. For the SACL data structure, see ACL in [MS-DTYP].&lt;42&gt; &#39;MaximumAllowed&#39; indicates that the client is requesting an open to the   file with the highest level of access the client has on this file.   If no access is granted for the client on this file, the server MUST   fail the open with STATUS_ACCESS_DENIED. &#39;GenericAll&#39; indicates a request for all the access flags that are   previously listed except MaximumAllowed and AccessSystemSecurity. &#39;GenericExecute&#39; indicates a request for the following combination of   access flags listed above:   FileReadAttributes| FileExecute| Synchronize| ReadControl. &#39;GenericWrite&#39; indicates a request for the following combination of   access flags listed above:   FileWriteData| FileAppendData| FileWriteAttributes| FileWriteEa|   Synchronize| ReadControl. &#39;GenericRead&#39; indicates a request for the following combination of   access flags listed above:   FileReadData| FileReadAttributes| FileReadEa| Synchronize|   ReadControl. | [optional] 
**access_privilege** | **List[str]** | Specifies whether access privilege of others if they&#39;re allowed to read/write/delete. | [optional] 
**open_id** | **int** | Specifies the id of the active open. | [optional] 

## Example

```python
from cohesity_sdk.models.smb_active_open import SmbActiveOpen

# TODO update the JSON string below
json = "{}"
# create an instance of SmbActiveOpen from a JSON string
smb_active_open_instance = SmbActiveOpen.from_json(json)
# print the JSON string representation of the object
print(SmbActiveOpen.to_json())

# convert the object into a dict
smb_active_open_dict = smb_active_open_instance.to_dict()
# create an instance of SmbActiveOpen from a dict
smb_active_open_from_dict = SmbActiveOpen.from_dict(smb_active_open_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


